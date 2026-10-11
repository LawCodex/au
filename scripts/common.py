"""Shared helpers: polite HTTP client for the Federal Register of Legislation API, paths."""
import json
import os
import sys
import threading
import time

import requests

API = "https://api.prod.legislation.gov.au/v1"
SITE = "https://www.legislation.gov.au"
UA = "LawCodex/1.0 (+https://github.com/LawCodex)"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.environ.get("LAWCODEX_RAW", os.path.join(os.path.dirname(ROOT), "_raw", "au"))

# FRL collection -> (output directory, front-matter type)
COLLECTIONS = {
    "Constitution": ("constitution", "constitution"),
    "Act": ("acts", "act"),
    "LegislativeInstrument": ("instruments", "legislative_instrument"),
    "ContinuedLaw": ("continued-laws", "continued_law"),
    "PrerogativeInstrument": ("prerogative-instruments", "prerogative_instrument"),
    "AdministrativeArrangementsOrder": ("administrative-arrangements-orders", "administrative_arrangements_order"),
}

# Minimum seconds between the start of two requests (global, across threads).
MIN_INTERVAL = float(os.environ.get("LAWCODEX_MIN_INTERVAL", "0.3"))

_lock = threading.Lock()
_last = [0.0]
_local = threading.local()


def _session():
    s = getattr(_local, "s", None)
    if s is None:
        s = requests.Session()
        s.headers["User-Agent"] = UA
        _local.s = s
    return s


def _throttle():
    with _lock:
        now = time.monotonic()
        wait = _last[0] + MIN_INTERVAL - now
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.monotonic()


def get(url, params=None, timeout=120, tries=10):
    """GET with global rate limiting and exponential backoff. Returns Response, or None for 404."""
    delay = 5
    err = None
    for attempt in range(tries):
        _throttle()
        try:
            r = _session().get(url, params=params, timeout=timeout)
        except requests.RequestException as e:
            err = str(e)
        else:
            if r.status_code == 200:
                return r
            if r.status_code in (404, 410):
                return None
            err = f"HTTP {r.status_code}: {r.text[:200]}"
            if r.status_code in (429, 503):
                ra = r.headers.get("Retry-After")
                if ra and ra.isdigit():
                    delay = max(delay, int(ra))
        if attempt < tries - 1:
            print(f"  retry in {delay}s: {url} ({err[:120]})", file=sys.stderr, flush=True)
            time.sleep(delay)
            delay = min(delay * 2, 300)
    raise RuntimeError(f"GET {url} {params} failed: {err}")


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)
    os.replace(tmp, path)


def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
