---
title: Digital ID (AGDIS) Data Standards 2024
identifier: F2024L01443
register_id: F2024L01443
type: legislative_instrument
jurisdiction: au
language: en
date: "2024-11-07"
version_start: "2024-11-13"
status: in_force
source: "https://www.legislation.gov.au/F2024L01443/latest/text"
retrieved: "2026-10-11"
---

# Digital ID (AGDIS) Data Standards 2024

[image]

I, Katy Gallagher, Minister for Finance, acting as the Digital ID Data Standards Chair, make the following instrument.

Dated 7 November 2024

Katy Gallagher Minister for Finance

Digital ID Data Standards Chair

[image]

[image]

Contents

**Chapter 1—Preliminary 1**

Name 1

Commencement 1

Authority 1

Definitions 1

Meaning of *federation protocol* 7

Meaning of *technical relying party* 7

Abbreviations 7

Key words 8

Incorporated instruments 10

Application—transitioned participating relying parties 10

Schedules 12

**Schedule 1—AGDIS Onboarding Specifications** 13

**Schedule 2—AGDIS OpenID Connect Profile** 27

**Schedule 3—AGDIS Attribute Profile** 67

[image]

**Chapter 1—Preliminary**

**Name**

This instrument is the *Digital ID (AGDIS) Data Standards 2024*.

**Commencement**

This instrument commences at the same time as the *Digital ID Act 2024*

commences.

**Authority**

This instrument is made under section 99 of the *Digital ID Act 2024*.

**Definitions**

Note 1: A number of expressions used in this instrument are defined in the Act, including the following:

accredited attribute service provider;

accredited identity exchange provider;

accredited identity service provider;

attribute;

participating relying party;

restricted attribute.

Note 2: A number of expressions used in this instrument are defined in the Transitional Act, including the following:

ImmiCard;

marriage certificate;

medicare card;

passport.

Note 3: A number of expressions used in this instrument are defined in the Accreditation Rules, including the following:

authenticated session;

commencement of identity credential;

DI data environment;

identity proofing level;

IP level.

Note 4: A number of expressions used in this instrument are defined in the Digital ID Rules, including the following:

participating entity;

pairwise identifier.

Unless otherwise specified, expressions defined in the Transitional Act, the Accreditation Rules and the Digital ID Rules have the same meaning in this instrument.

Example: The expressions ‘ASP’, ‘ISP’ and ‘IXP’, which are used in the Accreditation Rules, have a different meaning in this instrument. Similarly, the expression ‘IXP’, which is used in the Digital ID Rules, has a different meaning in this instrument. See subsection (2) and section 1.7.

In this instrument:

***access channel*** has the meaning in section 4.1.2 of Schedule 1 (AGDIS Onboarding Specifications).

***Accreditation Data Standards*** means the *Digital ID (Accreditation) Data Standards 2024*.

***Accreditation Rules*** means the *Digital ID (Accreditation) Rules 2024*.

***Act*** means the *Digital ID Act 2024*.

***attribute set*** has the same meaning as in section 1.1 of Schedule 3 (AGDIS Attribute Profile).

Note: Attributes are not unique to a single attribute set. The same attribute may be used across multiple attribute sets. Further information can be found in Schedule 3 (AGDIS Attribute Profile).

***attribute sharing policy*** means any policy mentioned in Chapter 2 or Chapter 3 of Schedule 3 (AGDIS Attribute Profile) that describes rules to be applied when sharing attributes with a participating relying party.

***authentication context class reference*** is an identifier for an authentication context class supported by OpenID Connect 1.0 and used in the Australian Government Digital ID System for the levels of assurance.

***authentication level*** has the meaning given in the Accreditation Data Standards.

***computed attribute*** means an attribute that is dynamically derived from the attributes in an attribute set using an algorithm.

***consumer history***, in relation to an individual, means the history of all the individual’s interactions with a participating accredited identity exchange provider.

***Designated Identity Exchange Provider*** has the same meaning as in the Transitional Rules.

***digital ID identifier*** means a unique identifier specified in section 2.2.1.1 of Schedule 3 (AGDIS Attribute Profile).

***Digital ID Rules*** means the *Digital ID Rules 2024.*

***Document Verification Service*** has the same meaning as ‘DVS’ in section 15 of the *Identity Verification Services Act 2023*.

***evidence of identity*** has the same meaning as the National Identity Proofing Guidelines published by the Attorney-General’s Department.

Note: At the time this instrument was made, located at: https://www.ag.gov.au/national-security/publications/national-identity-proofing- guidelines.

***federation protocol***: see section 1.5.

***general purpose identifier***, in relation to an individual, means a unique identifier assigned by a participating accredited identity service provider:

to the individual; and

independently from a participating relying party or a participating accredited identity exchange provider.

***incorporated instrument*** has the meaning given in subsection 1.9(1).

***ITU E.164*** means the standard for international public telecommunication structures published by the International Telecommunication Union.

Note: At the time this instrument was made, located at: https://www.itu.int/rec/T-REC-E.164-201011-I/en.

***JSON Web Key Set*** has the same meaning as in RFC 7517.

***JSON Web Token*** has the same meaning as in RFC 7517.

***JavaScript Object Notation*** has the same meaning as in RFC 7517 and RFC 8259.

***levels of assurance*** has the meaning given in section 2.1.3 of Schedule 1 (AGDIS Onboarding Specifications).

***MAY***: see section 1.8.

***MUST*** and ***MUST NOT***: see section 1.8.

***OAuth 2.0*** has the same meaning as in RFC 6749.

***OpenID Connect Core 1.0*** means the standard published by the OpenID Foundation for an identity layer which operates on top of RFC 6749.

Note: At the time this instrument was made, located at: https://openid.net/specs/openid-connect-core-1_0.html.

***OpenID Connect Core 1.0 provider*** means an entity which incorporates OpenID Connect Core 1.0 into its operations.

***OpenID Connect Discovery 1.0*** means the specification titled *OpenID Connect Discovery 1.0 incorporating errata set 2* published by the OpenID Foundation.

Note: At the time this instrument was made, located at: https://openid.net/specs/openid-connect-discovery-1_0.html.

***OpenID Connect Extended Authentication Profile (EAP) ACR Values 1.0*** means the standard used to request specific authentication context classes, published by the OpenID Foundation.

Note: At the time this instrument was made, located at: https://openid.net/specs/openid-connect-eap-acr-values-1_0.html.

***OPTIONAL***: see section 1.8.

***proof key for code exchange*** has the same meaning as in RFC 7636. ***RECOMMENDED*** and ***NOT RECOMMENDED***: see section 1.8. ***REQUIRED***: see section 1.8.

***participating accredited attribute service provider*** means an accredited attribute service provider that is participating in the Australian Government Digital ID System.

***participating accredited identity exchange provider*** means an accredited identity exchange provider that is participating in the Australian Government Digital ID System.

***participating accredited identity service provider*** means an accredited identity service provider that is participating in the Australian Government Digital ID System.

***relying party audit ID*** means a transaction audit identifier for transactions between participating identity exchange providers and participating relying parties.

Note: The relying party audit ID is never shared with a participating identity service provider. A separate audit ID is shared between a participating identity exchange provider and a participating identity service provider.

***RFC*** means a document published by the Internet Engineering Task Force that contains technical specifications regarding the internet.

Note: RFCs are freely available. For more information, see: https://www.ietf.org/process/rfcs/.

***RFC 2119*** means the RFC numbered 2119 and titled *Key Words for use in RFCs to Indicate Requirement Levels*.

Note 1: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc2119.

Note 2: See also RFC 8174 (*Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*).

***RFC 3339*** means the RFC numbered 3339 and titled *Date and Time on the Internet: Timestamps.*

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc3339.

***RFC 3629*** means the RFC numbered 3629 and titled *UTF-8, a transformation format of Unicode and ISO 10646*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc3629.

***RFC 3696*** means the RFC numbered 3696 and titled *Application Techniques for Checking and Transformation of Names*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc3696.

***RFC 3986*** means the RFC numbered 3986 and titled *Uniform Resource Identifier (URI): Generic Syntax*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc3986.

***RFC 4122*** means the RFC numbered 4122 and titled *A Universally Unique IDentifier (UUID) URN Namespace*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc4122.

***RFC 5321*** means the RFC numbered 5321 and titled *Simple Mail Transfer Protocol*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc5321.

***RFC 5322*** means the RFC numbered 5322 and titled *Internet Message Format*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc5322.

***RFC 5646*** means the RFC numbered 5646 and titled *Tags for Identifying Languages*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc5646.

***RFC 6749*** means the RFC numbered 6749 and titled *The OAuth 2.0 Authorization Framework*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc6749.

***RFC 6750*** means the RFC numbered 6750 and titled *The OAuth 2.0 Authorization Framework: Bearer Token Usage*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc6750.

***RFC 6819*** means the RFC numbered 6819 and titled *OAuth 2.0 Threat Model and Security Considerations*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc6819.

***RFC 7009*** means the RFC numbered 7009 and titled *OAuth 2.0 Token Revocation*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc7009.

***RFC 7517*** means the RFC numbered 7517 and titled *JSON Web Key (JWK)*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc7517.

***RFC 7591*** means the RFC numbered 7591 and titled *OAuth 2.0 Dynamic Client Registration Protocol*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc7591.

***RFC 7636*** means the RFC numbered 7636 and titled *Proof Key for Code Exchange by OAuth Public Clients*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc7636.

***RFC 7662*** means the RFC numbered 7662 and titled *OAuth 2.0 Token Introspection*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc7662.

***RFC 8141*** means the RFC numbered 8141 and titled *Uniform Resource Names*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc8141.

***RFC 8174*** means the RFC numbered 8174 and titled *Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc8174.

***RFC 8259*** means the RFC numbered 8259 and titled *The JavaScript Object Notation (JSON) Data Interchange Format*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc8259.

***RFC 8446*** means the RFC numbered 8446 and titled *The Transport Layer Security (TLS) Protocol Version 1.3*.

Note: At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc8446.

***sector identifier*** has the same meaning as in OpenID Connect Core 1.0.

***SHALL*** and ***SHALL NOT***: see section 1.8.

***single logout*** means the ability for an individual to initiate a logout process for relying parties that relied on a single logon session for the individual at an exchange operated by a participating accredited identity exchange provider.

***single sign on*** means the ability for an individual to make use of their digital ID at multiple services in a short period of time, with a single user authentication.

***technical relying party***: see section 1.6.

***technical relying party profile*** means the profile in Schedule 2 (AGDIS Open ID Connect Profile).

***Transitional Act*** means the *Digital ID (Transitional and Consequential Provisions) Act 2024.*

***Transitional Rules*** means the *Digital ID (Transitional and Consequential Provisions) Rules 2024*.

***transitioned participating relying party*** means a relying party that is taken to be a participating relying party in accordance with subitem 4(2) of Schedule 1 to the Transitional Act.

Note: See also rules 2.3 and 2.4 of Part 2 of Chapter 2 of the Transitional Rules.

***transitioned participating relying party service***, in relation to a transitioned participating relying party, means the service that the entity is approved to provide, or provide access to, in accordance with subitem 4(2) of Schedule 1 to the Transitional Act.

Note: See also rules 2.3 and 2.4 of Part 2 of Chapter 2 of the Transitional Rules.

***transport layer security*** has the same meaning as in RFC 8446. ***uniform resource identifier*** has the same meaning as in RFC 3986. ***uniform resource name*** has the same meaning as in RFC 8141.

***UTF-8*** means the standard for encoding electronic communications published by the Unicode Consortium.

Note: At the time this instrument was made, located at: https://www.unicode.org/versions/Unicode15.1.0/.

***universally unique identifier*** has the same meaning as in RFC 4122.

**Meaning of** ***federation protocol***

A ***federation protocol*** means an open protocol that enables participating entities to communicate with each other and share attributes of individuals in a trusted manner.

Subject to section 1.10, Schedule 2 (AGDIS OpenID Connect Profile) is the only federation protocol for the Australian Government Digital ID System.

**Meaning of** ***technical relying party***

A ***technical relying party*** means:

a participating accredited identity exchange provider’s OpenID Connect Core 1.0 software used to co-ordinate the flow of data or information between entities participating in the Australian Government Digital ID System; or

a participating relying party’s OpenID Connect Core 1.0 software used to: authenticate the participating relying party with the participating accredited identity exchange; and request and receive information or data from the participating accredited identity exchange; or

a participating accredited attribute service provider’s OpenID Connect Core 1.0 software used to: authenticate the participating accredited attribute service provider with the participating accredited identity exchange; and request and receive information or data from the participating accredited identity exchange.

Note: To avoid doubt, a technical relying party is not a relying party as defined in section 9 of the Act.

**Abbreviations**

In this instrument, an abbreviation mentioned in column 1 of an item in the following table has the meaning set out in column 2 of that item.

<table>
<tr>
<td colspan="3"><b>Abbreviations</b></td>
</tr>
<tr>
<td><b>Item</b></td>
<td><b>Column 1</b></td>
<td><b>Column 2</b></td>
</tr>
<tr>
<td></td>
<td><b>Abbreviation</b></td>
<td><b>Meaning</b></td>
</tr>
<tr>
<td>1</td>
<td>ACR</td>
<td>authentication context class reference</td>
</tr>
<tr>
<td>2</td>
<td>AGDIS</td>
<td>Australian Government Digital ID System</td>
</tr>
<tr>
<td>3</td>
<td>AL</td>
<td>authentication level</td>
</tr>
<tr>
<td>4</td>
<td>ASP</td>
<td>participating accredited attribute service provider</td>
</tr>
<tr>
<td>5</td>
<td>BDM</td>
<td>State and/or Territory Registry of Births, Deaths and Marriages</td>
</tr>
<tr>
<td>6</td>
<td>CoI credential</td>
<td>commencement of identity credential</td>
</tr>
<tr>
<td>7</td>
<td>DVS</td>
<td>Document Verification Service</td>
</tr>
<tr>
<td>8</td>
<td>EoI</td>
<td>evidence of identity</td>
</tr>
<tr>
<td>9</td>
<td>GPI</td>
<td>general purpose identifier</td>
</tr>
<tr>
<td>10</td>
<td>IP level</td>
<td>identity proofing level</td>
</tr>
<tr>
<td>11</td>
<td>IP#</td>
<td>identity proofing level number (for example, IP1, IP1 Plus, IP2, IP2 Plus, IP3, IP4)</td>
</tr>
<tr>
<td>12</td>
<td>ISP</td>
<td>participating accredited identity service provider</td>
</tr>
<tr>
<td>13</td>
<td>IXP</td>
<td>participating accredited identity exchange provider</td>
</tr>
<tr>
<td>14</td>
<td>JSON</td>
<td>JavaScript Object Notation</td>
</tr>
<tr>
<td>15</td>
<td>JWKS</td>
<td>JSON Web Key Set</td>
</tr>
<tr>
<td>16</td>
<td>JWT</td>
<td>JSON Web Token</td>
</tr>
<tr>
<td>17</td>
<td>OIDC provider</td>
<td>OpenID Connect Core 1.0 provider</td>
</tr>
<tr>
<td>18</td>
<td>PKCE</td>
<td>proof key for code exchange</td>
</tr>
<tr>
<td>19</td>
<td>PRP</td>
<td>participating relying party</td>
</tr>
<tr>
<td>20</td>
<td>RP audit ID</td>
<td>relying party audit ID</td>
</tr>
<tr>
<td>21</td>
<td>SLO</td>
<td>single logout</td>
</tr>
<tr>
<td>22</td>
<td>SSO</td>
<td>single sign on</td>
</tr>
<tr>
<td>23</td>
<td>TLS</td>
<td>transport layer security</td>
</tr>
<tr>
<td>24</td>
<td>TRP</td>
<td>technical relying party</td>
</tr>
<tr>
<td>25</td>
<td>URI</td>
<td>uniform resource identifier</td>
</tr>
<tr>
<td>26</td>
<td>URN</td>
<td>uniform resource name</td>
</tr>
<tr>
<td>27</td>
<td>UUID</td>
<td>universally unique identifier</td>
</tr>
</table>

**Key words**

In this instrument, and in each incorporated instrument, a capitalised term mentioned in column 1 of an item in the following table (***key word***) has the meaning and effect, in relation to an entity, set out in column 2 of that item subject to any exception or requirement in column 3 of that item.

[image]\
Section 1.8

<table>
<tr>
<td colspan="4"><b>Key words</b></td>
</tr>
<tr>
<td><b>Item</b></td>
<td><b>Column 1</b></td>
<td><b>Column 2</b></td>
<td><b>Column 3</b></td>
</tr>
<tr>
<td></td>
<td><b>Key word</b></td>
<td><b>Meaning and effect</b></td>
<td><b>Exception/requirement</b></td>
</tr>
<tr>
<td>1</td>
<td><b>MAY</b></td>
<td>Optional—the entity has discretion in relation to the behaviour</td>
<td>Except where it is necessary to:<br>interoperate with another implementation which does or does not include the option, in which case the entity <b>MUST</b> or <b>MUST NOT</b> implement the behaviour, as the case requires, to interoperate with the other implementation; or<br>comply with a condition imposed on the entity’s approval to participate in the AGDIS under section 64 of the Act, in which case the entity <b>MUST</b> or <b>MUST NOT</b><br>implement the behaviour,<br>as the case requires, to comply with that condition.</td>
</tr>
<tr>
<td>2</td>
<td><b>MUST</b></td>
<td>Absolute requirement—the entity has no discretion in relation to the behaviour.</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td><b>MUST NOT</b></td>
<td>Absolute prohibition—the entity has no discretion in relation to the behaviour.</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td><b>NOT RECOMMENDED</b></td>
<td>There may exist valid reasons in particular circumstances when the particular behaviour is acceptable or even useful, but the full implications should be understood and the case carefully weighed before the entity implements any<br>behaviour to which this term applies</td>
<td>Same as item 1.</td>
</tr>
<tr>
<td>5</td>
<td><b>OPTIONAL</b></td>
<td>Same as item 1</td>
<td>Same as item 1.</td>
</tr>
<tr>
<td>6</td>
<td><b>RECOMMENDED</b></td>
<td>There may exist valid reasons in particular circumstances to ignore a particular item, but the full implications must be understood and carefully weighed before the entity implements a different<br>behaviour to which this term applies</td>
<td>Same as item 1.</td>
</tr>
</table>

<table>
<tr>
<td colspan="4"><b>Key words</b></td>
</tr>
<tr>
<td><b>Item</b></td>
<td><b>Column 1</b></td>
<td><b>Column 2</b></td>
<td><b>Column 3</b></td>
</tr>
<tr>
<td></td>
<td><b>Key word</b></td>
<td><b>Meaning and effect</b></td>
<td><b>Exception/requirement</b></td>
</tr>
<tr>
<td>7</td>
<td><b>REQUIRED</b></td>
<td>Same as item 2.</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td><b>SHALL</b></td>
<td>Same as item 2.</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td><b>SHALL NOT</b></td>
<td>Same as item 3.</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td><b>SHOULD</b></td>
<td>Same as item 6</td>
<td>Same as item 1.</td>
</tr>
<tr>
<td>11</td>
<td><b>SHOULD NOT</b></td>
<td>Same as item 4</td>
<td>Same as item 1.</td>
</tr>
</table>

RFC 2119 and RFC 8174 do not apply to the interpretation of a key word appearing in: this instrument; or an incorporated instrument to the extent that this instrument applies, adopts or incorporates, with or without modification, any matter contained in the incorporated instrument.

**Incorporated instruments**

If a provision of this instrument applies, adopts or incorporates, with or without modification, any matter contained in any other instrument or other writing (***incorporated instrument***), then, unless the contrary intention appears in the provision, the reference to the incorporated instrument is a reference to the incorporated instrument as in force at the commencement of this instrument.

For the avoidance of doubt, if an incorporated instrument expressly refers to or requires compliance with any other instrument or other writing, then, the reference to the other instrument or other writing is a reference to the other instrument or other writing as in force at the commencement of this instrument.

Example: Section 10.9 of RFC 6749 provides that the authorisation server MUST require the use of TLS with server authentication as defined by RFC 2818 for certain purposes.

RFC 2818 was obsoleted (superseded) by RFC 9110 in June 2022. RFC 9110, as published in June 2022, was in force at the commencement of this instrument.

Therefore, for the purposes of section 10.9 of RFC 6749, the reference to RFC 2818 is taken to be a reference to RFC 9110.

Note: RFC 9110 means the RFC numbered 9110 and titled *HTTP Semantics*. At the time this instrument was made, located at: https://datatracker.ietf.org/doc/html/rfc9110.

**Application—transitioned participating relying parties**

This section applies to: a transitioned participating relying party: specified in column 1 of an item in the following table; when participating in the Australian Government Digital ID System; and in relation to the transitioned participating relying party service specified in column 2 of that item; and the Designated Identity Exchange Provider.

Section 1.10

<table>
<tr>
<td colspan="3"></td>
</tr>
<tr>
<td colspan="3"><b>Transitioned participating relying parties and services</b></td>
</tr>
<tr>
<td><b>Item</b></td>
<td><b>Column 1</b></td>
<td><b>Column 2</b></td>
</tr>
<tr>
<td></td>
<td><b>Entity</b></td>
<td><b>Service</b></td>
</tr>
<tr>
<td>1</td>
<td>Australian Communications and Media Authority</td>
<td>ACMA Lodgement Facility.</td>
</tr>
<tr>
<td>2</td>
<td>Australian Prudential Regulation Authority</td>
<td>APRA Connect.</td>
</tr>
<tr>
<td>3</td>
<td>Australian Prudential Regulation Authority</td>
<td>APRA Connect (External Test).</td>
</tr>
<tr>
<td>4</td>
<td>Australian Prudential Regulation Authority</td>
<td>APRA Extranet.</td>
</tr>
<tr>
<td>5</td>
<td>Commissioner of State Revenue (Victoria)</td>
<td>PTX Express.</td>
</tr>
<tr>
<td>6</td>
<td>Commissioner of Taxation</td>
<td>Australian Business Register Explorer.</td>
</tr>
<tr>
<td>7</td>
<td>Commonwealth Department of Employment and Workplace Relations</td>
<td>SkillSelect.</td>
</tr>
<tr>
<td>8</td>
<td>Commonwealth Department of Social Services</td>
<td>Humanitarian Settlement Program.</td>
</tr>
<tr>
<td>9</td>
<td>Commonwealth Department of the Treasury</td>
<td>Franchise Disclosure Register.</td>
</tr>
<tr>
<td>10</td>
<td>Commonwealth Department of the Treasury</td>
<td>Payment Times Reporting Portal.</td>
</tr>
<tr>
<td>11</td>
<td>Commonwealth Department of the Treasury</td>
<td>Treasury Authentication Broker.</td>
</tr>
<tr>
<td>12</td>
<td>Northern Territory Department of Corporate and Digital Development</td>
<td>InvoiceNTG.</td>
</tr>
<tr>
<td>13</td>
<td>Northern Territory Department of Industry, Tourism and Trade</td>
<td>Vocational Education and Training Provider Portal.</td>
</tr>
<tr>
<td>14</td>
<td>Northern Territory Department of Infrastructure, Planning and Logistics</td>
<td>Motor Vehicle Registry for Business.</td>
</tr>
<tr>
<td>15</td>
<td>Tasmanian State Revenue Office</td>
<td>Tasmanian Revenue Online.</td>
</tr>
<tr>
<td>16</td>
<td>Workplace Gender Equality Agency</td>
<td>WGEA Employer Portal.</td>
</tr>
</table>

*Transitioned participating relying party*

(2) Unless subsection (3) or (4) applies:

a provision, or part of a provision, of this instrument that contains a requirement in relation to Schedule 2 (AGDIS OpenID Connect Profile) only applies to a transitioned participating relying party in relation to the entity’s transitioned participating relying party service on and from the specified day; and

every provision, or every part of a provision, of this instrument not specified in paragraph (a) applies to that entity in relation to that service in accordance with its terms and on and from the commencement of this instrument.

Example: If this instrument commences on 1 December 2024 and the specified day is 1 December 2029 (see subsection (6)), then a provision or part of a provision

mentioned in paragraph (b) applies on and from 1 December 2024, and a provision or part of a provision mentioned in paragraph (a) applies on and from 1 December 2029.

If a transitioned participating relying party is required by this instrument, or another instrument made under section 99 of the Act, to comply with Schedule 2 (AGDIS OpenID Connect Profile) in relation to the entity’s transitioned participating relying party service at a particular time after commencement of

this instrument and before the specified day, then Schedule 2 (AGDIS OpenID Connect Profile) applies to that entity in relation to that service at that time.

If a transitioned participating relying party is required by this instrument, or another instrument made under section 99 of the Act, to comply with an alternative federation protocol that supports Security Assertion Markup Language in relation to the entity’s transitioned participating relying party service at a particular time after commencement of this instrument and before the specified day, then the alternative federal protocol applies to that entity in relation to that service at that time.

*Designated Identity Exchange Provider*

If a provision, or part of a provision, of this instrument that contains a requirement in relation to Schedule 2 (AGDIS OpenID Connect Profile) does not apply to a particular transitioned participating relying party, then that provision, or that part of the provision, does not apply to the Designated Identity Exchange Provider to the extent that: the Designated Identity Exchange Provider conveys, manages or coordinates the flow of data or other information in Security Assertion Markup Language within the Australian Government Digital ID System; and the activity mentioned in paragraph (a) enables the transitioned participating relying party to participate in the Australian Government Digital ID System.

*Definition*

In this section:

***specified day*** means the day that is 5 years after the day on which this instrument commences.

**Schedules**

Each instrument that is specified in a Schedule to this instrument is amended or repealed as set out in the applicable items in the Schedule concerned, and any other provision (however described) in a Schedule to this instrument has effect according to its terms.

[image: Branding shape for Australia's Digital ID System]

Schedule 1 – AGDIS Onboarding Specifications

Contents

**Common requirements for participating accredited entities 1 Security considerations 1 Identity resolution 1 General purposes identifiers 1 Pairwise identifiers 1 Sector Identifiers 1 Data sharing 2 Request processing 2**

**Identity exchange provider 3 Technical integration requirements 3 Protocol requirements 3 Audit requirements 3 Levels of assurance 3 Identity resolution 5 Authenticated sessions 5 Single sign on 5 Single logout 5 Attribute service provider integration 5 Federation protocol brokering 6 Identity provider selection 6 Blinding 6 User dashboard 7 Data requirements 7 Attribute requirements 7 Computed attributes 7 Attribute sharing policy 7 Data representation 8**

**Identity service provider 8 Technical integration requirements 8 Protocol requirements 8 Identity resolution 8 Single sign on 8 Single logout 8**

Data requirements 9 Attribute requirements 9 Computed attributes 9

**Attribute service provider 9 Technical integration requirements 9 Protocol requirements 9 Access channels 9 Audit logging 10 Attribute schema 10**

List of Tables

Table 1 Level of assurance combinations used in the AGDIS 4

Table 2 Mapping of new authentication levels to legacy credential levels 4

## 1. Common requirements for participating accredited entities

This Chapter outlines the role requirements, where applicable, that MUST be met by ASPs, ISPs and IXPs.

### 1.1 Security considerations

ASPs, ISPs and IXPs:

MUST comply with the security considerations in section 10 (Security Considerations) of RFC 6749; and

SHOULD consider the additional security considerations in section 5 (Security Considerations) of RFC 6819.

### 1.2 Identity resolution

#### 1.2.1 General purposes identifiers

An IXP MUST NOT issue a GPI.

An ISP MAY issue a GPI. Where an ISP chooses to issue a GPI, the ISP MUST:

(a) bind the GPI to only a single digital ID account;

(b) only use the GPI within the AGDIS;

(c) only use the GPI to map the individual’s digital ID to a single IXP; and

(d) issue additional GPIs for each IXP an individual accesses.

A GPI MUST be unique within the DI data environment of the ISP that issues it.

#### 1.2.2 Pairwise identifiers

An IXP MUST issue a pairwise identifier.

An ISP SHOULD issue a pairwise identifier. If an ISP issues a pairwise identifier, the ISP MUST NOT issue a GPI.

IXPs or ISPs that issue digital ID identifiers as pairwise identifiers MUST generate the identifiers in accordance with the algorithm outlined in section 8.1 (Pairwise Identifier Algorithm) of OpenID Connect Core 1.0.

#### 1.2.3 Sector Identifiers

IXPs and ISPs SHOULD use sector identifiers.

The scope of a sector identifier MUST be limited as per the role specific role requirements outlined in the following specified sections of OpenID Connect Core 1.0.

If a sector identifier is used, it MUST conform to the definition outlined in the following specified sections of OpenID Connect Core 1.0.

For this standard, the following sections of OpenID Connect Core 1.0 are specified:

(a) section 1.2 (Terminology); and

(b) section 8.1 (Pairwise Identifier Algorithm).

### 1.3 Data sharing

Irrespective of the federation protocol used, ASPs, ISPs and IXPs MUST handle and transmit data in accordance with the data sharing policies outlined in Schedule 3 (AGDIS Attribute Profile).

#### 1.3.1 Request processing

ASPs, ISPs and IXPs MUST NOT attempt to fulfill requests for unknown attributes or attribute sets.

Requests for known attributes or attribute sets that cannot be fulfilled, regardless of the reason, MUST NOT be returned with empty values unless explicitly permitted by an attribute sharing policy as outlined in Schedule 3 (AGDIS Attribute Profile).

## 2. Identity exchange provider

This Chapter outlines the requirements that MUST be met by IXPs.

### 2.1 Technical integration requirements

#### 2.1.1 Protocol requirements

An IXP MUST implement Schedule 2 (AGDIS OpenID Connect Profile) for an:

(a) IXP acting as an OIDC provider; and

(b) IXP acting as TRP to an ISP.

#### 2.1.2 Audit requirements

An IXP MUST generate the RP Audit ID attribute as outlined in Schedule 3 (AGDIS Attribute Profile).

The IXP MUST provide the RP Audit ID attribute it generated in response to every logical transaction between itself (the IXP) and the PRP (including ASPs).

The IXP MUST include the RP Audit ID attribute it generated for the PRP’s authentication request in every logical transaction between itself and each of the ASPs required to fulfill the attribute requirements of a PRP’s authentication request.

The IXP MUST NOT send the RP Audit ID attribute it generated for the PRP’s authentication request to its ISP.

#### 2.1.3 Levels of assurance

Levels of assurance are used to define the IP level and AL of an individual’s authenticated session.

Levels of assurance are ranked from the lowest to the highest degree of confidence in the authentication process. The rankings of levels of assurance are specified in Table 1below.

Note the URNs in Table 1below MUST reference the legacy acronym cl (credential level) in their namespace to represent AL.

A mapping of the new ALs to the legacy credential levels, used in the URNs outlined in Table 1, is provided below in Table 2.

An IXP MUST allow a PRP to request a minimum level of assurance when making authentication requests.

**Table 1 Level of assurance combinations used in the AGDIS.**

| **Identity proofing level** | **Authentication level** | **URN** | **Ranking (low to high)** |
|---|---|---|---|
| IP1 | AL1 | urn:id.gov.au:tdif:acr:ip1:cl1 | 1 |
|  | AL2 | urn:id.gov.au:tdif:acr:ip1:cl2 | 2 |
|  | AL3 | urn:id.gov.au:tdif:acr:ip1:cl3 | 3 |
| IP1 Plus | AL1 | urn:id.gov.au:tdif:acr:ip1p:cl1 | 4 |
|  | AL2 | urn:id.gov.au:tdif:acr:ip1p:cl2 | 5 |
|  | AL3 | urn:id.gov.au:tdif:acr:ip1p:cl3 | 6 |
| IP2 | AL2 | urn:id.gov.au:tdif:acr:ip2:cl2 | 7 |
|  | AL3 | urn:id.gov.au:tdif:acr:ip2:cl3 | 8 |
| IP2 Plus | AL2 | urn:id.gov.au:tdif:acr:ip2p:cl2 | 9 |
|  | AL3 | urn:id.gov.au:tdif:acr:ip2p:cl3 | 10 |
| IP3 | AL2 | urn:id.gov.au:tdif:acr:ip3:cl2 | 11 |
|  | AL3 | urn:id.gov.au:tdif:acr:ip2p:cl2 | 12 |
| IP4 | AL3 | urn:id.gov.au:tdif:acr:ip4:cl3 | 13 |

**Table 2 Mapping of new authentication levels to legacy credential levels.**

| **Authentication level** | **Credential level** |
|---|---|
| AL1 | CL1 |
| AL2 | CL2 |
| AL3 | CL3 |

#### 2.1.4 Identity resolution

An IXP MUST generate pairwise identifiers as required in section 1.2.2 of this Schedule.

If an IXP does not use sector identifiers, the IXP MUST generate a pairwise identifier for every distinct service it connects, even if these services are operated by the same PRP.

If an IXP makes use of sector identifiers:

(a) the pairwise identifiers MUST only have a one-to-one mapping with a sector identifier; and

(b) a sector identifier MUST only map to a single PRP, regardless of the number of connected services.

Pairwise identifiers MUST be used when presenting individuals to PRPs irrespective of the federation protocols being brokered by the IXP in a transaction.

#### 2.1.5 Authenticated sessions

An authenticated session managed by the IXP MUST expire.

For each supported federation protocol, an IXP MUST provide PRPs with information regarding session expiration times.

An IXP MAY support features as specified in the relevant federation protocol to allow refreshing of an authenticated session before expiry.

#### 2.1.6 Single sign on

An IXP MAY support a SSO scheme.

If an IXP supports SSO, it MUST support the ability for a PRP to request authentication for a particular individual, using all the methods outlined in the profile of their supported federation protocols.

An IXP MUST permit a PRP to request an individual’s reauthentication even when a pre-existing session is active and valid, regardless of the PRP that created the session.

An IXP MUST ensure their implementation of SSO does not result in the disclosure of attributes including restricted attributes of an individual.

#### 2.1.7 Single logout

If an IXP supports SSO, the IXP MUST implement SLO.

The IXP MUST ensure their implementation of SLO does not result in the disclosure of attributes including restricted attributes of an individual.

#### 2.1.8 Attribute service provider integration

When an IXP receives an authentication request from a PRP that includes attributes supplied by an ASP, the IXP MUST facilitate gathering those attributes from the ASP.

An IXP MUST implement mechanisms to support the access channels it has agreed with an ASP as referenced in section 4.1.2 of this Schedule.

When accessing attributes directly from the ASP, an IXP MUST do so using the pairwise identifier it has issued to the ASP.

To facilitate direct communication between an ASP and a PRP, an IXP MAY share an individual’s encrypted pairwise identifier:

(a) for the ASP with the PRP requesting authentication; and

(b) for the PRP with the ASP that can fulfill the attribute requests.

If an IXP chooses to share an encrypted identifier, the identifier MUST be:

encrypted using a public key of the PRP or ASP it belongs to; and

be packaged with a timestamp and a nonce to limit the opportunity for replay and the creation of de facto pairwise identifiers.

#### 2.1.9 Federation protocol brokering

When accepting authentication requests from a PRP, an IXP MUST broker the federation protocol used by the PRP to the federation protocol of the ISP selected by the individual.

### 2.2 Identity provider selection

An IXP MUST provide a mechanism for the individual to choose an ISP.

The list of ISPs presented by an IXP MUST only display ISPs that satisfy the IP level and AL requested in the PRP’s authentication request.

An IXP MAY provide a mechanism for the individual to remember their choice of ISP for a given PRP.

If an individual has remembered their ISP choice for a given PRP, an IXP MAY redirect them to the remembered ISP.

If an IXP provides a mechanism to remember ISP selection, the IXP MUST provide:

a notice to ensure the individual understands the nature of the express consent they are providing;

a notice outlining the duration of the remembered ISP selection and the limitations on how it is remembered (for example, if it is limited to the device or web browser from which the express consent is given); and

a mechanism to revoke the remembered choice.

#### 2.2.1 Blinding

An IXP MUST NOT broker any information about the PRP requesting authentication to any of its ISPs.

An IXP MAY inform the PRP which ISP the individual used to authenticate.

If an IXP informs the PRP which ISP the individual used to authenticate, the IXP MUST do so in accordance with the requirements outlined for the federation protocol used by the PRP.

### 2.3 User dashboard

An IXP MUST provide a user dashboard that allows an individual, for the digital ID used to create the individual’s current authenticated session, to:

view their consumer history;

manage the express consent they have given; and

manage their ISP preferences.

The user dashboard MUST only display information for services at or below the level of assurance for the current authenticated session.

When a user dashboard is accessed, an IXP MAY re-authenticate the individual, even if the individual already has a current authenticated session.

### 2.4 Data requirements

#### 2.4.1 Attribute requirements

An IXP MUST support brokering all attributes as outlined in Schedule 3 (AGDIS Attribute Profile).

An IXP MUST support the disclosure of all IXP managed or generated attributes as outlined in Schedule 3 (AGDIS Attribute Profile).

An IXP MUST support requesting any ISP specific attributes outlined in Schedule 3 (AGDIS Attribute Profile) in an authentication request to an ISP.

#### 2.4.2 Computed attributes

For each of their supported federation protocols, an IXP MUST implement the following requirements in this section.

An IXP MUST support the disclosure of computed attributes as described in Schedule 3 (AGDIS Attribute Profile).

An IXP MAY source computed attributes from an ISP or an ASP.

An IXP MAY define support for additional computed attributes derived from attributes available from its ISPs and ASPs.

Any new computed attribute MUST NOT violate attribute sharing policies defined in Schedule 3 (AGDIS Attribute Profile).

#### 2.4.3 Attribute sharing policy

The IXP MUST only disclose an attribute or attribute set with PRPs in accordance with that attribute or attribute set’s attribute sharing policy as defined in Schedule 3 (AGDIS Attribute Profile).

#### 2.4.4 Data representation

When disclosing IXP specific attributes, an IXP MUST use the data representation as prescribed in Schedule 3 (AGDIS Attribute Profile).

An IXP MAY use the data representation, defined in Schedule 3 (AGDIS Attribute Profile), to validate attribute payloads received from ISPs and ASPs.

An IXP MUST NOT alter payloads received from an ISP or ASP unless the relevant attribute sharing polices explicitly permit alteration to occur.

## 3. Identity service provider

This Chapter outlines the requirements that MUST be met by ISPs.

### 3.1 Technical integration requirements

#### 3.1.1 Protocol requirements

An ISP MUST implement the ISP requirements in Schedule 2 (AGDIS OpenID Connect Profile).

#### 3.1.2 Identity resolution

An ISP MAY generate GPIs as prescribed in section 1.2.1 of this Schedule.

An ISP SHOULD generate pairwise identifiers as prescribed in section 1.2.2 of this Schedule.

An identifier linking a digital ID to an IXP MUST only be used to map that one-to-one relationship. The identifier MUST NOT be shared by the IXP with any other service connected to the ISP.

#### 3.1.3 Single sign on

An ISP MAY support an SSO scheme operated by one or more of its connected IXPs.

Where an ISP chooses to support an IXP’s SSO scheme, the ISP MAY choose to re-authenticate an individual at their discretion when servicing a SSO request.

If an ISP is unable to fulfill a request of SSO then it MUST re-authenticate the user.

#### 3.1.4 Single logout

The ISP MUST support the SLO scheme operated by its connected IXPs.

The ISP MUST support the SLO scheme (of its connected IXPs) regardless of whether the ISP has supported the SSO.

### 3.2 Data requirements

#### 3.2.1 Attribute requirements

An ISP MUST support the disclosure of attributes based on support and fulfilment requirements outlined in Schedule 3 (AGDIS Attribute Profile).

For each of their supported federation protocols, an ISP MUST implement the specific attribute profile and attribute mapping.

#### 3.2.2 Computed attributes

An ISP MUST support computed attributes as outlined in Schedule 3 (AGDIS Attribute Profile).

An ISP MAY define support for additional computed attributes. The new computed attribute MUST NOT violate attribute sharing policies defined in Schedule 3 (AGDIS Attribute Profile).

## 4. Attribute service provider

This Chapter outlines the requirements that MUST be met by ASPs.

### 4.1 Technical integration requirements

#### 4.1.1 Protocol requirements

An ASP, in addition to these requirements, is subject to TRP requirements as outlined in section 1.7 of Schedule 2 (AGDIS OpenID Connect Profile).

An ASP, in addition to these requirements, MAY also have a role as a PRP in another context, and in that context is subject to PRP requirements.

The ASP MUST implement the technical relying party profile for one of the federation protocols supported by the IXP it is connecting to.

At the time this instrument was made, the only technical relying party profile for the AGDIS is in Schedule 2 (AGDIS OpenID Connect Profile).

#### 4.1.2 Access channels

An access channel is any mechanism that allows ASP managed attributes to be provided either:

(a) directly to a PRP; or

(b) to a PRP via an IXP.

Examples include, but are not limited to, the use of OpenID Connect Core 1.0 distributed claims issued by IXP, authorisation methods (within the meaning of RFC 6749), event streaming services or application programming interfaces.

An ASP MAY make multiple access channels available for IXPs or PRPs to access the attributes they control.

For each access channel that an ASP makes available, the ASP MUST:

provide documentation outlining the technical integration requirements for the IXP and/or the PRP, as the case may be;

outline the attribute lifecycle features supported by the channel and how the IXP and/or PRP, as the case may be, can use them;

document and demonstrate how an individual’s consent is collected and managed;

document and demonstrate how an individual can manage their consent; and

document how the audit logging will be undertaken.

### 4.2 Audit logging

An ASP’s audit log MUST include any individual’s consent managed by the ASP that enables the sharing of attributes with PRPs.

An ASP’s audit log MUST include the value of the RP Audit ID supplied by the IXP:

when binding a digital ID brokered by the IXP to any of the attributes managed by the ASP;

if the IXP directly retrieves the attributes; and

if the ASP provides attributes indirectly and the RP Audit ID is available.

### 4.3 Attribute schema

An ASP MUST publish an attribute schema for any attributes it provides.

The attribute schema MAY support multiple data formats if required by the various access channels provided by the ASP to IXPs and PRPs to access the ASP’s attributes.

A published attribute schema MUST outline data types and constraints for the fields that comprise the attribute sets managed by the ASP.

The published attribute schema MUST support a data format compatible with the federation protocol the ASP uses to connect to the IXP.

An ASP MUST establish procedures to publish updates to their attribute schema in accordance with Schedule 3 (AGDIS Attribute Profile).

[image: Branding shape for Australia's Digital ID System]

Schedule 2 – AGDIS Open ID Connect Profile

Contents

**Identity exchange 1 Authorisation grant types 1 Client types 1 Full Client with User Delegation 1 Native Client with User Delegation 1 Direct Access Client 2 Client Registration 3 Redirect URI 3 Native Client Applications 3 Connection to the authorisation server 4 Client keys 4 Grant types 5 Technical Relying Party Profile 5 Requests to the Authorisation Endpoint 5 Requests to the Token Endpoint 7 Token response 9 ID Tokens 9 . Request to the UserInfo Endpoint 9 . Request Object 9 . Discovery 9 Identity Exchange OpenID Connect provider Profile 10 Connecting to clients 10 Grant types 10 Client authentication 10 Dynamic registration 11 Discovery 11 PKCE 14 . Response to Authorisation Requests 14 Authentication Error Response 14 Responding to Invalid Claims 15 . Token Response 15 ID Token 15 . UserInfo Endpoint 16**

. Request Objects 16

. Authentication Context 16

Entity information 16 Claims supported 16 Scope profiles 17 Valid ACR Claims 17

User consent 18

Privacy considerations 18

Security considerations 18

**Identity service provider 19 Client types 19 Full Client with User Delegation 19 Client registration 19 Redirect URI 20 Client keys 20 Grant types 20 Technical Relying Party Profile 20 Audit Logging 20 Request to the Authorisation Endpoint 21 Request to the Token Endpoint 22 Request to the UserInfo Endpoint 24 ID Tokens 24 Request Objects 24 Discovery 24 Identity Provider Profile 24 Audit Logging 25 Connecting to clients 25 Grant types 25 Client authentication 25 Dynamic registration 26 Discovery 26 . Requests to the Authorisation Endpoint (Authentication Request) 27 . User consent 27 . Response to Authorisation Requests 27 Authentication Error Response 27 . Token Response 28**

ID Token 28

. UserInfo Endpoint 29

. Request Object 29

. Authentication context 30

Entity information 30 Claims supported 30 Scope profiles 30 Valid ACR Claims 30

Privacy Requirements 31

Security Considerations 31

**Protocol brokering 32 OIDC to OIDC brokering 32 Mapping Claims and Scopes 32 Handling of Subject ID 32 Mapping assurance levels 32 Prompt Parameter 33 ID Token Hint Parameter 33**

**Attributes 34 Restricted attributes 34 OIDC Attribute Mapping 34**

List of Tables

Table 1 IXP prompt parameter brokering requirements 33

## List of Figures

Figure 1 JSON WEB Key Set example 4

Figure 2 Example authorisation request 7

Figure 3 Sample Token Endpoint HTTP POST request 8

Figure 4 Client authentication JWT example 11

Figure 5 Normative example of the well-known configuration 14

Figure 6 Requesting authentication assurance level with claims 17

Figure 7 Token Endpoint private JWT example 22

Figure 8 UserInfo endpoint example request 23

Figure 9 Sample ID Token signature 29

Figure 10 Claims used to the generate the prior signature 29

Figure 11 Sample assurance level requests using claims 31

## 1. Identity exchange

This Chapter outlines the requirements that an IXP MUST satisfy to facilitate brokering access to ISPs using OpenID Connect Core 1.0 as their federation protocol.

Interoperability between IXPs is not within scope for this release of the *Digital ID (AGDIS) Data Standards 2024*.

### 1.1 Authorisation grant types

An IXP MUST NOT use the resource owner password credentials grant type defined in RFC 6749.

### 1.2 Client types

#### 1.2.1 Full Client with User Delegation

An IXP MUST support the Full Client with User Delegation client type.

This client type applies to clients that act on behalf of a particular resource owner and require delegation of that user’s authority to access the protected resource. This client type can interact with a separate web browser application to facilitate the resource owner’s interaction with the authentication endpoint of the authorisation server.

All IXP clients of this type MUST use the authorisation code flow of RFC 6749 by sending the resource owner to the Authorisation Endpoint to obtain authorisation.

An IXP MUST ensure that the individual authenticates to the Authorisation Endpoint. The user’s web browser is then redirected back to a URI hosted by the client service, from which the client can obtain an authorisation code passed as a query parameter. The client then presents that authorisation code along with its own credentials (private_key_jwt) to the authorisation server’s Token Endpoint to obtain an access token.

An IXP MUST associate the clients with a unique public key as described in section 1.5.1 of this Schedule.

An IXP MAY issue this client type a refresh token if the security parameters of the access request allow for it.

#### 1.2.2 Native Client with User Delegation

A Native Client with User Delegations is a client that acts on behalf of a particular resource owner, such as an application on a mobile platform, and requires delegation of that individual’s authority to the protected resource. This client type can interact with a separate web browser application to facilitate the resource owner’s interaction with the authentication endpoint of the authorisation server. Specifically, this client type runs natively on the resource owner’s device, often leading to many identical instances of a piece of software operating in different environments and running simultaneously for different end users.

An IXP MAY support Native Clients with User Delegation.

If an IXP supports Native Clients with User Delegation, the IXP MUST implement the following requirements.

An IXP client MUST use the authorisation code flow of RFC 6749 by sending the resource owner to the Authorisation Endpoint to obtain authorisation.

An IXP MUST authenticate an individual to the Authorisation Endpoint.

The user’s web browser is then redirected back to a URI hosted by the client, from which the client can obtain an authorisation code passed as a query parameter. The client then presents that authorisation code along to the authorisation servers Token Endpoint to obtain an access token.

Native clients connecting to a IXP MUST either be:

dynamically registered to obtain a separate client identifier for each instance; or

act as Public Clients (as defined in section 2.1 (Client Types) of RFC 6749) by using a common client identifier and using PKCE (as per RFC 7636) to protect calls to the Token Endpoint.

An IXP supporting dynamic registration of native applications MUST support one of the following methods to register or exchange a unique public key value:

the native application generates unique public and private keys on the device and registers the public key value with the IXP; or

the IXP generates a unique public and private key pair, registering the public key with itself and securely transmitting the public and private key pair to the client. After transmission, the IXP MUST discard the private key.

An IXP MUST NOT permit sharing of client credentials among instances of client software.

All native applications registered with a IXP not registering a separate public key for each instance are considered Public Clients and MUST use PKCE with the S256 code challenge method (within the meaning of RFC 7636).

An IXP MUST NOT permit Public Clients to authenticate to the Token Endpoint in any other way.

If an IXP supports Native Clients with User Delegation, the IXP MAY implement the following requirements.

An IXP MAY permit dynamically registered native applications to use PKCE.

An IXP MAY issue a refresh token to a Native Client with User Delegation if the IXP is satisfied that there are no security issues.

#### 1.2.3 Direct Access Client

A Direct Access Client is a client that connects directly to protected resources and do not act on behalf of a particular resource owner, for example, machine to machine access.

An IXP MAY only implement this client type to support interactions between itself and other entities participating in the AGDIS.

If an IXP supports the Direct Access Client type, the IXP MUST support the confidential client type and the client_credentials grant types.

### 1.3 Client Registration

An IXP MUST support Client Registration by static configuration or dynamic configuration. An IXP MAY support both static and dynamic Client Registration.

All clients of an IXP MUST register with the authorisation server.

For client software that may be installed on multiple client instances, an IXP MUST issue each client instance a unique client identifier from the authorisation server.

An IXP MUST advise a PRP of the information that is required to be supplied when configuring its connection as a TRP of the IXP.

Where a TRP is seeking to register by dynamic configuration, an IXP MUST require the TRP provide an initial access token (as defined in RFC 7591).

If an IXP supports dynamic registration of clients, the IXP MUST implement support for bearer tokens in the manner prescribed in RFC 6750.

### 1.4 Redirect URI

An IXP’s clients that use the authorisation code grant type MUST register its full redirect URIs.

An IXP MUST as the authorisation server validate the redirect URI given by the client at the Authorisation Endpoint using strict string comparison.

An IXP MUST ensure that the redirect URI used by a client is one of the following:

hosted on a website with TLS protection (HTTPS);

hosted on a local domain of the client (for example: http://localhost/); or

hosted on a client specific non-remote protocol URI scheme (for example: myapp:// or au.gov.app://).

If a client’s redirect URI is either hosted on the local domain of the client or hosted on a client specific non-remote protocol URI schema, then a IXP MAY require that the TRP uses the PKCE extension to the authorisation code flow.

An IXP MUST NOT allow its ASPs to have URIs in more than one of the 3 categories outlined above. An IXP SHOULD NOT allow ASP clients to have multiple redirects URIs on different domains.

#### 1.4.1 Native Client Applications

The use of client specific non-remote protocol URI schemes SHOULD be phased out for native application.

An IXP MAY allow existing native application clients to continue using non-remote protocol URI schemes in their redirect URI.

When a new Native Client Application is running on a platform that supports Claimed HTTPs Scheme URI redirection, an IXP SHOULD require these native applications to use that scheme in their redirect URI.

### 1.5 Connection to the authorisation server

#### 1.5.1 Client keys

An IXP MUST require clients using the authorisation code grant type to have a public and private key pair type for use in authentication to the Token Endpoint.

An IXP MUST require each client to register its public keys in its client registration metadata by either sending the public key directly in the jwks field or by registering a jwks_uri.

If a client registers a jwks_uri, the IXP MUST require the URI to be reachable by the authorisation server.

An IXP SHOULD require the use of a jwks_uri as it allows for easier key rotation.

An IXP MUST reject a jwks field or the content available from a jwks_uri provided by the client if the content does not contain a public key in the format prescribed in RFC 7517.

As the authorisation server, a IXP MUST verify the content available from a client’s registered

jwks_uri contains a valid JSON Web Key Set. The example below is of a 2048-bit RSA key.

{

"keys": [{\
"alg": "RS256",

"e": "AQAB",

"n": "kAMYD62n_f2rUcR4awJX4uccDt0zcXRssq_mDch5aifcShx9aTtTVza23PTn3KaKrsBXwWcfioXR6zQn5eYdZQVGNBfOR4rxF5i7t3hfb4WkS50EK1gBYk2lO9NSrQzxG9QsUsAnN6RHksXqsdOqvnxjLexDfIJlgbcCN9h6TBC66ZXv7PVhl19gIYVifSU7liHkLe0l0fw7jUI6rHLHf4d96_neR1HrNIK_xssr99Xpv1EM_ubxpktX0T925qej9fMEpzzQ5HLmcNt1H2_VQ_Ww1JOLn9vRnH48FDj7TxlIT74XdTZgTv31w_GRPAOfyxEw_ZUmxhz5ZngTlQ",

"kty": "RSA",

"kid": "oauth-client"

}]

}

**Figure 1 JSON WEB Key Set example**

An IXP MAY allow native client applications to omit their key during registration if they are a Public Client using PKCE.

### 1.6 Grant types

The grant type of authorisation_code MUST be supported by an IXP.

The Authorisation Code authentication flow implemented by an IXP MUST follow the steps outlined in the section 3.1 (Authentication using the Authorization Code Flow) of OpenID Connect Core 1.0.

If an IXP supports a Direct Access Client type, it MUST also support the grant type of

client_credentials.

Implementation of the Client Credentials grant MUST conform to RFC 6749.

### 1.7 Technical Relying Party Profile

In this section the terms client and technical relying party (TRP) refer to the OpenID Connect Core 1.0 software operated by a PRP or an ASP.

#### 1.7.1 Requests to the Authorisation Endpoint

IXP’s clients making a request to the Authorisation Endpoint SHOULD use an unpredictable value for the state parameter with at least 128 bits of entropy.

IXP’s clients MUST validate the value of the state parameter upon return to the redirect URI and MUST ensure that the state value is securely tied to the individual’s current session, for example, by relating the state value to a session identifier issued by the client software to the browser.

IXP’s clients MUST include their full redirect URI in the authorisation request.

To prevent open redirection and other injection attacks, an IXP MUST match the entire redirect URI using a direct string comparison against registered values and MUST reject requests with invalid or missing redirect URIs.

The Authentication Request MUST contain the following REQUIRED parameters and MAY contain the following OPTIONAL parameter values:

client_idREQUIRED. Client Identifier (within the meaning of RFC 6749) valid at the authorisation server.

response_typeREQUIRED. Must be set to code.

scopeREQUIRED. Indicates the attributes being requested. The openid scope MUST always be present. Additional scopes are defined in Schedule 3 (AGDIS Attribute Profile).

redirect_uriREQUIRED. Indicates a valid endpoint where the client will receive the authentication response. The URI MUST match exactly one of the Redirection URIs preregistered at the IXP. The URI MUST follow the schemes outlined in section 1.4 of this Schedule.

state

REQUIRED. Un-guessable random string generated by the client used to protect against CSRF attacks. MUST contain sufficient entropy to avoid guessing and is returned to the Client in the authentication response.

promptOPTIONAL. A space delimited, case sensitive list of string values that specifies if the authorisation server prompts for the End-User to re-authenticate or provide consent. Defined values that a IXP MUST support are:none: The authorisation server MUST NOT display any authentication or consent user interface pages. An error is returned if the End-User is not already authenticated or not already provided consent for the requested claims or does not fulfil any other conditions for processing the request.login: The authorisation server MAY prompt the End-User for reauthentication.consent: The authorisation server MAY prompt the end user for consent before returning information to the client. Consent should be requested in accordance with the attribute sharing policies defined in Schedule 3 (AGDIS Attribute Profile).select_account: The authorisation server MAY prompt the End-User to select a user account. This allows an end user with multiple accounts at the authorisation server to select amongst their accounts that currently have an active session at the authorisation server.

displayOPTIONAL. A string value that specifies how the authorisation server displays the authentication and consent interface pages to the End-User.page: The authorisation server SHOULD display the authentication and consent user interface consistent with a full User Agent page view. This is the default where the display parameter is not specified.popup: The authorisation server MAY display the authentication and consent user interface consistent with a popup User Agent window. The popup User Agent window should be of an appropriate size for a login-focused dialog and should not obscure the entire window that it is popping up over.touch: The authorisation server MAY display the authentication and consent user interface consistent with a device that leverages a touch interface.wap: The authorisation server MAY display the authentication and consent user interface consistent with a "feature phone" type display.

nonceREQUIRED. Un-guessable random string generated by the client, used to protect against cross site request forgery attacks. MUST contain sufficient entropy to avoid guessing. Returned to the client in the ID Token.

acr_valuesOPTIONAL. A TRP may specify the required level(s) of assurance here. For permissible ACR values see section 1.9.3 of this Schedule.

code_challenge and code_challenge_methodOPTIONAL. If an IXP supports PKCE as described in section 1.2.2 of this Schedule, they MUST support these parameters.

max_ageOPTIONAL. Maximum Authentication Age. Specifies the allowable elapsed time in seconds since the last time the End-User was actively authenticated by the IXP. If the elapsed time is greater than this value, the IXP MUST attempt to actively re- authenticate the End-User.

ui_localesOPTIONAL. End-User’s preferred languages and scripts for the user interface, represented as a space-separated list of language tag values as specified in RFC 5646, ordered by preference.

id_token_hintOPTIONAL. ID Token previously issued by the authorisation server being passed as a hint about the End-User’s current or past authenticated session with the client. If the End-User identified by the ID Token is logged in or is logged in by the request, then the authorisation server returns a positive response; otherwise, it MAY return an error, such as login_required.

login_hintOPTIONAL. Hint to the authorisation server about the login identifier the End-User might use to log in (if necessary). This hint can be used by a TRP if it first asks the End-User for their e-mail address (or other identifier) and then wants to pass that value as a hint to the discovered authorisation service.

user_flowOPTIONAL. A string value that indicates the desired user flow for the individual. Defined values are:sign_in: A TRP requests this flow when it expects the user to already have a digital identity and sign in at the ISP.sign_up: A TRP requests this flow when it expects the user to need to create a digital identity at an ISP.mygov_link: A TRP requests this when it expects a user to set up a linkage between their myGov account and their digital ID.

claimsOPTIONAL. This parameter is used to request that specific Claims be returned. The value is a JSON object listing the requested Claims. This is made according to section 5.5 (Requesting Claims using the “claims” Request Parameter) of OpenID Connect Core 1.0

A sample HTTP GET request may look like the following example:

https://idexchange.gov.au/oidc/authorization?response_type=code &client_id=827937609728-m2mvqffo9bsefh4di90saus4n0diar2h &scope=profile%20openid%20email &redirect_uri=https%3A%2F%2Frp.agency.gov.au%2Foidc%2FloginResponse &state=2ca3359dfbfd0 &prompt=select_account &acr_values=urn%3Aid.gov.au%3Atdif%3Aacr%3Aip3%3Acl2

**Figure 2 Example authorisation request**

#### 1.7.2 Requests to the Token Endpoint

Requests to the Token Endpoint uses client authentication. The client authentication mechanism is signed JWT as defined in section 1.8.1.2 of this Schedule.

The JWT assertion used in the client authentication MUST be signed by the client using the client’s public key it has registered with the Authorisation server. Registration of keys should occur in accordance with process outlined section 1.5.1 of this Schedule.

For clients that are required to use PKCE as described in section 1.2.2 and section 1.4 of this Schedule, the following claims MUST be included in the request to the Token Endpoint.

code_verifierCode verifier generated by client to use PKCE with the S256 code challenge method (within the meaning of RFC 7636).

A TRP MUST include the following claims in the request to the Token Endpoint, when requesting authentication for an individual:

grant_typeMUST be set to authorization_code.

codeThe value of the code parameter returned in the authorisation response.

redirect_uriValue MUST be identical to the redirect_uri parameter that was included in the authorisation request as described above.

client_assertion_typeMUST be set to urn:ietf:params:oauth:client-assertion-type:jwt-bearer.

client_assertionThe value of the signed client authentication JWT generated as described in section

1.7.3.1 of this Schedule. The Client MUST generate a new assertion JWT for each call to the Token Endpoint.

These would be sent to the Token Endpoint as illustrated in the HTTP POST example below.

POST /token HTTP/1.1 Content-Type: application/x-www-form-urlencoded Host: idexchange.gov.au grant_type=authorization_code &code=sedaFh &scope=openid+email+profile &redirect_uri=https%3A%2F%2Frp.agency.gov.au%2Foidc%2FloginResponse &client_id=55f9f559-2496-49d4-b6c3-351a586b7484 &client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclientassertion- type%3Ajwt-bearer &client_assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.ew0KICAgImlzcy I6ICI1NWY5ZjU1OS0yNDk2LTQ5ZDQtYjZjMy0zNTFhNTg2Yjc0ODQiLA0KICAgInN1YiI 6ICI1NWY5ZjU1OS0yNDk2LTQ5ZDQtYjZjMy0zNTFhNTg2Yjc0ODQiLA0KICAgImF1ZCI6

ICJodHRwczovL2lkcC1wLmV4YW1wbGUuY29tL3Rva2VuIiwNCiAgICJpYXQiOiAxNDE4N jk4Nzg4LA0KICAgImV4cCI6IDE0MTg2OTg4NDgsDQogICAianRpIjogIjE0MTg2OTg3OD gvMTA3YzRkYTUxOTRkZjQ2M2U1MmI1Njg2NWM1YWYzNGU1NTk1Ig0KfQ.t_gX8JQGq3G2

OEc2kUCQ8zVj7pqff87Sua5nktLIHj28l5onO5VpsL4sRHIGOvrpo7XO6jgtPWy3iLXv3 NLyo1TWHbtErQEGpmf7nKiNxVCXlGYJXSDJB6shP3OfvdUc24urPJNUGBEDptIgT7Lhf6 BbwQNlMQubNeOPRFDqQoLWqe7UxuI06dKX3SEQRMqcxYSIAfP7CQZ4WLuKXb6oEbaqz6g L4l6p83G7wKGDeLETOTHsztjKR38v4F_MnSrx8e0iIqgZwurW0RtetEWvynOCJXkp166T 7qZR45xuCxgOotXY6O3et4n77GtgspMgOEKj3b_WpCiuNEwQ

**Figure 3 Sample Token Endpoint HTTP POST request**

#### 1.7.3 Token response

The token response includes an access token, which can be used to make a UserInfo request as per section 1.7.4 of this Schedule, and an ID token as per section 3.1.3.3 (Successful Token Response) of OpenID Connect Core 1.0. It MAY also include a Refresh token.

#### 1.7.3.1 ID Tokens

All clients MUST validate the signature of an ID Token before accepting it using the public key of the issuing server, published in JWK format.

An IXP MAY encrypt ID Tokens using the appropriate key of the requesting client. An IXP’s TRPs MUST verify the following in received ID tokens:

 iss

 aud

The Issuer field is the URL of the expected issuer.

The audience field contains the client ID of the client.

exp, iat, nbfThe expiration, issued at and not before tokens are dates (integer number of seconds since 00:00:00Z 1st January 1970, i.e. Unix epoch) are within acceptable ranges.

#### 1.7.4 Request to the UserInfo Endpoint

An IXP MUST be able to accept UserInfo Request from clients using either the HTTP GET or POST methods.

An IXP MUST only accept Access Tokens from its clients when presented as Bearer Tokens, as outlined in the RFC 6750.

#### 1.7.5 Request Object

A client MAY send request to the authorisation end point using the request parameters as outlined in OpenID Connect Core 1.0.

Request objects MUST be signed by the client’s public key.

A client MAY encrypt the request object with the authorisation server’s public key.

#### 1.7.6 Discovery

Clients and protected resources MAY cache an IXP’s OpenID Connect metadata once the IXP has been discovered, as outlined in this Schedule.

### 1.8 Identity Exchange OpenID Connect provider Profile

#### 1.8.1 Connecting to clients

1.8.1.1 Grant types

The authorization_code grant type is the only grant type that is supported under this Schedule. Accordingly, an IXP MUST only support the authorization_code grant type when fulfilling PRP authentication requests for individuals.

The authorisation code flow returns an authorisation code to the client. The client can then exchange this one-time code for an ID Token and an Access Token. This provides the benefit of not exposing any tokens to the User Agent and potentially malicious applications with access to the User Agent.

#### 1.8.1.2 Client authentication

An authorisation server MUST enforce client authentication for access to the authorisation server’s Token Endpoint.

An authorisation server MUST only authenticate clients using the private_key_jwt method as prescribed in the OpenID Connect Core 1.0.

An authorisation server MUST NOT authenticate clients using any other method.

The JWT used to authenticate the client MUST expire with a lifetime no longer than 300 seconds. An authorisation server MUST reject an JWT with an expiry time passed.

An authorisation server SHOULD:

allow for clock skew of 300 seconds between systems when assessing the expiry of a JWT; and

reject any JWT with expiry that is unreasonably far into the future.

The JWT MUST contain the following REQUIRED claims and MAY contain the following OPTIONAL claims:

iss

sub

aud

jti

REQUIRED. Issuer. This MUST contain the client_id of the client creating the token.

REQUIRED. Subject. This MUST contain the client_id of the client creating the token.

REQUIRED. Audience. The value that identifies the authorisation server as an intended audience. The authorisation server MUST verify that it is an intended audience for the token. The Audience MAY be the URL of the authorisation server’s Token Endpoint.

REQUIRED. JWT ID. A unique identifier for the token generated by the client, which can be used to prevent reuse of the token. This identifier MUST contain at least

exp

iat

128 bits of entropy and MUST NOT be re-used by any subsequent authentication token.

REQUIRED. Expiration time on or after which the ID Token MUST NOT be accepted for processing.

OPTIONAL. Time at which the JWT was issued.

The following is an example of the use of the REQUIRED claims for a client authentication JWT as defined in this Schedule. Noting that additional claims MAY be included in this set.

{

"iss": "55f9f559-2496-49d4-b6c3-351a586b7484",

"sub": "55f9f559-2496-49d4-b6c3-351a586b7484",

"aud": "https://idexchange.gov.au/token",

"iat": 1418698788,

"exp": 1418698848,

"jti": "1418698788/107c4da5194df463e52b56865c5af34e5595"

}

**Figure 4 Client authentication JWT example**

#### 1.8.1.3 Dynamic registration

An IXP MAY support the dynamic registration of clients.

#### 1.8.1.4 Discovery

Endpoints and parameters specified in the discovery document below MAY be considered public information regardless of the existence of the discovery document.

An IXP MUST provide a well-known endpoint for its configuration as described in the OpenID Connect Discovery 1.0.

An IXP MUST secure the well-known endpoint as outlined in OpenID Connect Discovery 1.0. An IXP MAY apply additional security controls if required by their business need.

The discovery document published by a IXP MUST as a minimum contain the following fields:

 issuer

o REQUIRED. The fully qualified issuer URL of the server.

 authorization_endpoint

o REQUIRED. The fully qualified URL of the server’s Authorisation Endpoint defined in RFC 6749.

 token_endpoint

o REQUIRED. The fully qualified URL of the server’s Token Endpoint defined in RFC 6749.

 introspection_endpoint

o OPTIONAL. The fully qualified URL of the server’s introspection endpoint defined in RFC 7662.

 revocation_endpoint

o OPTIONAL. The fully qualified URL of the server’s revocation endpoint as within the meaning of RFC 7009.

 jwks_uri

o REQUIRED. The fully qualified URI of the server’s public key in JWK Set format as defined in RFC 7517.

 scopes_supported

o REQUIRED. The list of scopes that MUST be made available by a IXP as defined in Schedule 3 (AGDIS Attribute Profile).

 claims_supported

o REQUIRED. The list of claims that MUST be made available by an IXP as defined in Schedule 3 (AGDIS Attribute Profile).

The following is sample of the current AGDIS IXP’s well-known endpoint response.

{

"issuer": "https://auth.identity.gov.au",

"authorization_endpoint": "https://auth.identity.gov.au/authorise",

"token_endpoint":

"https://auth.identity.gov.au/sso/sps/oauth/oauth20/token",

"userinfo_endpoint":\
"https://auth.identity.gov.au/sso/sps/oauth/oauth20/userinfo",

"jwks_uri":

"https://auth.identity.gov.au/.well-known/jwks.json",

"end_session_endpoint": "https://auth.identity.gov.au/logout",

"response_types_supported": [

"code"

],

"grant_types_supported": [

"authorization_code"

],

"subject_types_supported": [

"pairwise"

],

"id_token_signing_alg_values_supported": [

"RS256"

],

"scopes_supported": [

"openid",

"profile",

"email",

"phone",

"tdif_business_authorisations",

"tdif_doc",

"tdif_other_names"

],

"claims_supported": [

"tdif_business_authorisations",

"tdif_doc",

"acr"

],

"user_flows_supported": [

"sign_in",

"sign_up",

"mygov_link"

],

"prompts_supported": [

"none",

"login"

],

"acr_values_supported": [

"urn:id.gov.au:tdif:acr:ip1:cl1",

"urn:id.gov.au:tdif:acr:ip1:cl2",

"urn:id.gov.au:tdif:acr:ip2:cl2",

"urn:id.gov.au:tdif:acr:ip3:cl2"

],

"frontchannel_logout_supported": true,

"frontchannel_logout_session_supported": false

}

**Figure 5 Normative example of the well-known configuration**

#### 1.8.1.5 PKCE

An authorisation server MUST support the PKCE extension to the authorisation code flow, including support for the S256 code exchange methods (within the meaning of RFC 7636).

The authorisation server MUST NOT allow a client to use the plain code challenge method (within the meaning of RFC 7636).

#### 1.8.2 Response to Authorisation Requests

The authorisation code flow’s authorisation response MUST return the following fields in the response:

stateThe value of the state parameter passed in via the authentication request. This value MUST match exactly.

codeThe authorisation code, a random string issued by the OIDC provider to be used request to the Token Endpoint.

PKCE parameters MUST be associated with the “code” (refer above) within the meaning of RFC 7636.

This response MUST be sent to the client via a HTTP redirect to the URI specified in the request.

#### 1.8.2.1 Authentication Error Response

The Authentication Error Response is the message returned from an IXP’s Authorisation Endpoint in response to the Authorisation Request sent by the client.

If the End-User denies or cancels the request or the End-User authentication fails, the OIDC provider informs the TRP by using the error responses defined in either section 4.1.2.1 (Error Response) of RFC 6749 or the error codes defined in section 3.1.2.6 (Authentication Error Response) of the OpenID Connect Core 1.0. The additional authentication error responses defined in this Schedule are:

 authentication_cancelled

o The End-User did not proceed with the authentication interaction.

#### 1.8.2.2 Responding to Invalid Claims

A scope or claim is invalid if a IXP cannot source the underlying attributes from its ISPs or ASPs and from the IXP specific attributes outlined in Chapter 4 of Schedule 3 (AGDIS Attribute Profile).

If an IXP receives a request for a scope or claim it cannot fulfill, the IXP MUST ignore these scopes or claims.

An IXP MUST deny an authentication request with the access_denied error code (as described in RFC 6749) if its client requests a scope or claim that under the relevant attribute sharing policy it is not authorised to request. For example, if a client requests a restricted attribute set when they are not approved to an access_denied error code MUST be returned.

#### 1.8.3 Token Response

All tokens issued by an IXP MUST be signed with the IXP’s private key.

For clients using the Authorisation Code Grant type, access tokens MUST have a valid lifetime of no greater than one hour (which is 3,600 seconds).

If an IXP issues refresh token they MUST have a lifespan of no longer than 24 hours (which is 86,400 seconds).

Token lifespans MAY be shorter than these prescribed values to meet the requirements of an IXP’s security risk assessment.

#### 1.8.3.1 ID Token

An IXP MAY encrypt an ID Token or the ID Token’s fields with the requesting clients public key when the ID Token contains attributes of the individual.

An IXP issued ID Token MUST:

expire; and

have a lifespan of no longer than 300 seconds.

An IXP SHOULD assign lifespans of shorter than 300 seconds to an ID Token.

An IXP issued ID Token MUST contain the following fields that are defined as REQUIRED. An IXP issued ID Token MAY include the following fields that are defined as OPTIONAL. ID token fields:

iss

aud

sub

acr

REQUIRED. The issuer field is the URL of the expected issuer.

REQUIRED. The audience field contains the client ID of the client.

REQUIRED. The identifier of the user. Note it MUST be a pairwise identifier and be unique to the client’s sector.

REQUIRED. This is the level of assurance at which the user was authenticated at.

nonceIf a nonce value was supplied with the authentication request, then this value is REQUIRED.

jtiREQUIRED. A unique identifier for the token which can be used to prevent the reuse of the token.

exp, iat, nbfREQUIRED. The expiration, issued at, and not before timestamps for the tokens. They are dates presented as an integer representing the number of seconds since 1970- 01-01T00:00:00Z UTC (Unix epoch) within acceptable ranges.

#### 1.8.4 UserInfo Endpoint

An IXP MUST support returning claims via the UserInfo endpoint as prescribed by the requirements outlined in section 4.1.1 of Schedule 3 (AGDIS Attribute Profile).

When processing a UserInfo request, a IXP MUST only return the claims that are authorised within the authentication request associated with the presented access token.

An IXP MUST NOT return empty or null values for claims that cannot be fulfilled unless Chapter 2 and Chapter 3 of Schedule 3 (AGDIS Attribute Profile) specifically permits these values for a given attribute set.

The sub claim MUST always be present in the UserInfo response.

#### 1.8.5 Request Objects

An IXP operating as OpenID Connect provider MUST accept requests containing a request object signed by the client’s private key.

An IXP MUST validate the signature on request objects using the client’s public key.

An IXP MUST implement support for receiving requests objects encrypted with one of its public keys.

#### 1.8.6 Authentication Context

An IXP MUST provide an ACR in line with the claims outlined in section 4.4.1.3 of Schedule 3 (AGDIS Attribute Profile).

An IXP MUST return the acr attained by the individual during authentication at the ISP even if the acr was not marked as essential, the acr_values parameter was used, or no acr value was supplied in the TRP’s authentication request.

### 1.9 Entity information

#### 1.9.1 Claims supported

An authorisation server MUST return claims on best effort basis. An IXP asserting it can support specific claims does not guarantee it is available for all individuals.

An IXP MUST only return claims in accordance with data sharing requirements and data formats outlined in Chapter 4 of Schedule 3 (AGDIS Attribute Profile).

#### 1.9.2 Scope profiles

An authorisation server MUST fulfill scopes on best effort basis.

An IXP MUST only return scopes in accordance with the data sharing policies and data formats outlined in Chapter 4 of Schedule 3 (AGDIS Attribute Profile).

#### 1.9.3 Valid ACR Claims

Assurance levels are outlined in section 2.1.3 of Schedule 1 (AGDIS Onboarding Specifications).

An IXP MUST implement support to allow its PRPs to use either the acr_values or acr claim to request their required ACR.

An IXP MUST reject any request that include both the acr_values and acr claims.

When the acr claim is requested an IXP MUST support the acr claim being optionally marked as essential claim by the client. For example:

“claims”: {

“id_token”: {

“acr”: {

“essential”: true,

“values”: [“urn:id.gov.au:tdif:acr:ip2:cl3”]

}

}

}

**Figure 6 Requesting authentication assurance level with claims**

When the acr values are marked as an essential claim, the IXP MUST return a value that matches the requested values.

If the individual is unable to achieve the required level of assurance outlined in the request and the acr

claim is marked as essential, then an IXP MUST respond with an authentication error.

If the acr claim is not marked as essential or no acr value was supplied in the authentication request, then an IXP MUST respond with the level of assurance the individual was able to achieve.

### 1.10 User consent

Given IXPs operate as central trusted entity in the AGDIS, IXPs MUST collect consent of the individual to whom the digital ID relates before redirecting the individual to the client that originated the authentication request.

### 1.11 Privacy considerations

An IXP MUST adhere to all the attribute sharing policies set out in Chapter 2 and Chapter 3 of Schedule 3 (AGDIS Attribute Profile).

### 1.12 Security considerations

All clients of an IXP SHOULD consider the additional security considerations in section 5 (Security Considerations) of RFC 6819.

## 2. Identity service provider

This Chapter outlines the requirements for:

IXPs in their role as a TRP to ISPs; and

ISPs in their roles as OIDC providers to IXPs.

### 2.1 Client types

The resource owner password credential grant type as defined in RFC 6749 MUST NOT be used under this Schedule.

Given an IXP is only acting as a proxy, the Full Client with delegation is the only client available.

#### 2.1.1 Full Client with User Delegation

This client type applies to clients that act on behalf of a particular resource owner and require delegation of that user’s authority to access the protected resource. This client type can interact with a separate web browser application to facilitate the resource owner’s interaction with the authentication endpoint of the authorisation server.

An ISP MUST only support clients of this type.

All clients of an ISP MUST use the authorisation code flow of RFC 6749 by sending the resource owner to the Authorisation Endpoint to obtain authorisation.

An ISP MUST ensure that the user authenticates to the Authorisation Endpoint.

The user’s web browser is then redirected back to a URI hosted by the client service, from which the client can obtain an authorisation code passed as a query parameter. The client then presents that authorisation code along with its own credentials (private_key_jwt) to the authorisation server’s Token Endpoint to obtain an access token.

An ISP MUST associate the clients with a unique public key as described in section 2.4 of this Schedule.

If an ISP issues a refresh token to this type of client, they MUST only do so if the security parameters of the request permit its issuance.

### 2.2 Client registration

An IXP MUST register with the authorisation server.

Each client IXP MUST receive a unique client identifier from the authorisation server. Clients of the authorisation server MUST be statically configured.

An ISP MUST NOT support the dynamic registration of IXPs.

### 2.3 Redirect URI

An ISP MUST register an IXP’s full redirect URIs as required by the authorization_code grant type.

The authorisation server MUST validate the redirect URI passed to the authorisation end using strict string comparison.

An ISP MUST only permit TLS protected redirect URIs to be registered.

An ISP MUST NOT permit a IXP to have multiple redirect URIs on different domains.

An ISP MUST NOT forward values passed back to their redirect URIs to other arbitrary or user provided URIs.

An ISP MUST NOT permit open redirection.

### 2.4 Client keys

All connected IXPs acting as clients MUST have a public and private key that MUST be used when authenticating to the Token Endpoint.

As clients all IXPs MUST:

provide their public keys in their client registration metadata; or

provide an avenue for entities to obtain or reference their public keys. An ISP SHOULD support the use of jwks field, or registration of a jwks_uri.

If a IXP uses a jwks_uri to register its public key, the URI MUST be reachable by the authorisation server.

If an ISP supports the use of jwks_uri:

the IXP SHOULD use a jwks_uri to simplify key rotation; and

the ISP MUST validate the content of the clients registered jwks_uri document.

### 2.5 Grant types

An ISP MUST only support the authorization_code grant type when providing services to IXPs.

### 2.6 Technical Relying Party Profile

This section outlines the profile that an ISP MUST provide for the IXPs that are its TRPs.

#### 2.6.1 Audit Logging

An IXP MUST log all interactions with its ISPs using a unique audit identifier it has generated for an authentication request from its TRP.

To enable a traceable audit trail for requests sent to an ISP, an IXP MUST implement a scheme to ensure that each request is uniquely identifiable at the ISP.

A recommended scheme is for an IXPs to transport a unique generated value using the state

parameter. Note this unique value MUST NOT be the RP audit ID issued by an IXP to an PRP.

#### 2.6.2 Request to the Authorisation Endpoint

An IXP making a request to the Authorisation Endpoint MUST use an unpredictable value for the

state parameter with at least 128 bits of entropy.

An IXP MUST validate the state parameter upon return to the redirect URI.

An IXP MUST ensure that the state value is securely tied to the user’s current IXP session. An IXP MUST include their redirect URIs in the authorisation request.

An ISP MUST match the entire redirect URI using strict string comparison against registered values and reject request with missing or invalid redirect URIs.

The authentication request MUST contain the following REQUIRED parameters and MAY contain the following OPTIONAL parameters.

client_idREQUIRED. Client Identifier (within the meaning of RFC 6749) assigned to a IXP by the ISP.

response_typeREQUIRED. MUST be set to code.

scopeREQUIRED. Indicates the attributes being requested. The openid scope MUST always be present.

redirect_uriREQUIRED. Indicates the valid endpoint where the client will receive the authorisation response. The URI MUST exactly match one of preregistered redirect URIs at the ISP.

stateREQUIRED. An opaque value generated by the IXP used to protect against CSRF attacks. The value MUST contain sufficient entropy to avoid guessing and is returned to the IXP in the authentication response.An IXP SHOULD use a unique value for each authorisation request.

nonceREQURIED. Un-guessable random string generated by the client, used to protect against cross site request forgery attacks. The string MUST contain sufficient entropy to avoid guessing. The value is returned to the IXP in the ID Token.

acr_valuesOPTIONAL. If the originating PRP requesting authentication has supplied acr_values a IXP MUST pass these values in accordance with protocol brokering requirements outlined in section 2.8.3 of this Schedule.

user_flowOPTIONAL. A string value that indicates the desired user flow for the user. Defined values are:sign_in: An Exchange requests this when a TRP expects the user to already have a digital ID and sign in at the ISP.

sign_up: A IXP requests this when a TRP expects the individual to need to create a digital ID at an ISP.

claimsOPTIONAL. This parameter is used to request that specific Claims be returned. The value is a JSON object listing the requested Claims. This is made according to section 5.5 (Requesting Claims using the “claims” Request Parameter) of OpenID Connect Core 1.0.

The values of the claims, scope and acr_values parameters are mapped from the original authentication request to the IXP from one of its TRPs. Additional OpenID Connect Core 1.0 parameters MAY also be mapped from the original request to the IXP that triggered the request from the IXP to the ISP. Mapping of these parameters are described Chapter4 of this Schedule.

#### 2.6.3 Request to the Token Endpoint

Request to the Token Endpoint require client authentication. The client authentication mechanism is a signed JWT and defined in the Identity Provider profile outlined in section 2.7 of this Schedule.

The claims that are included in the JWT are summarised below:

iss

sub

aud

iat

exp

jti

The client Id of the client creating the JWT.

The client Id of the client creating the JWT.

The URL of the authorisation server’s Token Endpoint.

The time that the token was created by the client.

The expiration time after which the token MUST be considered invalid.

A unique, random, identifier generated by the client for this authentication.

An IXP making the request MAY include additional claims in this set.

The following is an example of the required claims for a client authentication JWT as defined in this profile.

{\
"iss": "8428fea9-2815-82e9-a9f3-a32a9e9b723c",\
"sub": "8428fea9-2815-82e9-a9f3-a32a9e9b723c ",\
"aud": "https://idp.gov.au/token",\
"iat": 1516986988,\
"exp": 1516986929,\
"jti": "1516986988/c4da1075193e524df46b5e565c5a59568f34"\
}

**Figure 7 Token Endpoint private JWT example**

The JWT assertion MUST be signed with the IXP’s private key from the key pair they have registered with the ISP.

The following claims MUST be included in a request to a Token Endpoint:

grant_typeMUST be set to authorization_code.

codeThe value of the code parameter returned in the authorisation response.

redirect_urivalue MUST be identical to the value of the redirect_uri parameters that was included in the authorisation request.

client_assertion_typeMUST be set to urn:ietf:params:oauth:client-assertion-type:jwt-bearer.

client_assertionThe value of the signed client authentication JWT generated as described below in the ID Tokens section (section 2.6.5 of this Schedule). The TRP MUST generate a new assertion JWT for each call to the Token Endpoint.

The following is an example of how these claims would be sent Token Endpoint:

POST /token HTTP/1.1

Content-Type: application/x-www-form-urlencoded

Host: idp.gov.au

grant_type=authorization_code\
&code=sedaFh\
&redirect_uri=https%3A%2F%2Fidexchange.gov.au%2Foidc%2FloginResponse\
&client_id=55f9f559-2496-49d4-b6c3-351a586b7484\
&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer\
&client_assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.ew0KICAgImlzcyI6ICI1NWY5ZjU1OS0yNDk2LTQ5ZDQtYjZjMy0zNTFhNTg2Yjc0ODQiLA0KICAgInN1YiI6ICI1NWY5ZjU1OS0yNDk2LTQ5ZDQtYjZjMy0zNTFhNTg2Yjc0ODQiLA0KICAgImF1ZCI6ICJodHRwczovL2lkcC1wLmV4YW1wbGUuY29tL3Rva2VuIiwNCiAgICJpYXQiOiAxNDE4Njk4Nzg4LA0KICAgImV4cCI6IDE0MTg2OTg4NDgsDQogICAianRpIjogIjE0MTg2OTg3ODgvMTA3YzRkYTUxOTRkZjQ2M2U1MmI1Njg2NWM1YWYzNGU1NTk1Ig0KfQ.t_gX8JQGq3G2OEc2kUCQ8zVj7pqff87Sua5nktLIHj28l5onO5VpsL4sRHIGOvrpo7XO6jgtPWy3iLXv3-NLyo1TWHbtErQEGpmf7nKiNxVCXlGYJXSDJB6shP3OfvdUc24urPJNUGBEDptIgT7Lhf6BbwQNlMQubNeOPRFDqQoLWqe7UxuI06dKX3SEQRMqcxYSIAfP7CQZ4WLuKXb6oEbaqz6gL4l6p83G7wKGDeLETOTHsztZjKR38v4F_MnSrx8e0iIqgZwurW0RtetEWvynOCJXk-p166T7qZR45xuCxgOotXY6O3et4n77GtgspMgOEKj3b_WpCiuNEwQ

**Figure 8 UserInfo endpoint example request**

#### 2.6.4 Request to the UserInfo Endpoint

An ISP MUST implement support for an IXP to send a UserInfo request using either the HTTP GET or POST methods.

The Access Token obtained from authentication request MUST be sent as a Bearer Token, as described in RFC 6750.

#### 2.6.5 ID Tokens

An IXP MUST validate the signature of an ID Token before accepting it by using the public key of the ISP that issued it.

An IXP MAY require an ISP to encrypt the ID Tokens it returns.

If an ISP supports encrypting ID Tokens, it MUST use the appropriate key of the requesting IXP. An IXP MUST verify the following in received ID Tokens:

issThe issue field is the URL of the expected issuer.

audThe audience field contains the client ID of the IXP.

nonceString value used to associate the client session with the ID Token.

exp, iat, nbfThe expiration, issued at and not before tokens are dates (integer number of seconds since 00:00:00Z 1st January 1970, i.e. Unix epoch) are within acceptable ranges.

#### 2.6.6 Request Objects

An IXP MAY optionally send requests to the Authorisation Endpoint using the request parameter as defined in the OpenID Connect Core 1.0.

An IXP MUST sign the request object with its registered key.

An IXP MAY encrypt the request object using the ISP’s public key.

#### 2.6.7 Discovery

An IXP MAY cache the ISP’s OIDC provider metadata once the ISP has been discovered and used by that IXP.

### 2.7 Identity Provider Profile

An ISP providing authentication services to an IXP using OpenID Connect Core 1.0 MUST implement this Schedule.

#### 2.7.1 Audit Logging

An ISP MUST log all authentication requests and responses, including the values of the client_id

and the state parameters associated with the request.

#### 2.7.2 Connecting to clients

2.7.2.1 Grant types

The only supported grant type is authorization_code.

The authorisation code flow is the only authentication flow support under this Schedule. The authorisation code flow returns an Authorisation Code to the client that the client can then exchange for an ID Token and an Access Token. This provides the benefit of not exposing any tokens to the User Agent and potentially malicious applications with access to the User Agent.

The ISP MUST validate all redirect URIs for the authorization_code grant type.

#### 2.7.2.2 Client authentication

An ISP MUST enforce client authentication for access to the authorisation server’s Token Endpoint.

An ISP MUST only authenticate clients using the private_jwt_key method as prescribed in the OpenID Connect Core 1.0.

An ISP’s authorisation server MUST NOT authenticate clients using any other method.

The JWT used to authenticate the client MUST expire and have a lifetime of no longer than 300 seconds.

An ISP’s authorisation server MUST reject a JWT with an expiry time that has passed. An ISP SHOULD:

allow for clock skew of 300 seconds between systems when assessing the expiry of a JWT; and

reject any JWT with expiry that is unreasonably far into the future.

The JWT MUST contain the following REQUIRED claims and MAY contain the following OPTIONAL claims:

iss

sub

aud

REQUIRED. Issuer. This MUST contain the client_id of the client creating the token.

REQUIRED. Subject. This MUST contain the client_id of the client creating the token.

REQUIRED. Audience. The value that identifies the authorisation server as an intended audience. The authorisation server MUST verify that it is an intended audience for the token. The Audience MAY be the URL of the authorisation server’s Token Endpoint.

jti

exp

iat

REQUIRED. JWT ID. A unique identifier for the token generated by the client, which can be used to prevent reuse of the token. This identifier MUST contain at least

128 bits of entropy and MUST NOT be re-used by any subsequent authentication token.

REQUIRED. Expiration time on or after which the ID Token MUST NOT be accepted for processing.

OPTIONAL. Time at which the JWT was issued.

#### 2.7.2.3 Dynamic registration

An ISP MUST NOT support dynamic registration of IXPs as clients.

#### 2.7.2.4 Discovery

Endpoints and parameters specified in the Discovery document MAY be considered public information regardless of the existence of the discovery document.

An ISP MAY provide a well-known endpoint for its OpenID configuration as described in the OpenID Connect Discovery 1.0.

If an ISP provides a well-known endpoint, it MUST secure the well-known endpoint as outlined in the OpenID Connect Discovery 1.0 specification. An IXP MAY apply additional security controls if required by their business need.

If an ISP publishes a discovery document, the document MUST as a minimum contain the following REQUIRED fields and MAY contain the OPTIONAL fields:

 issuer

o REQUIRED. The fully qualified issuer URL of the server.

 authorization_endpoint

o REQUIRED. The fully qualified URL of the server’s Authorisation Endpoint defined in RFC 6749.

 token_endpoint

o REQUIRED. The fully qualified URL of the server’s Token Endpoint defined in RFC 6749.

 introspection_endpoint

o OPTIONAL. The fully qualified URL of the server’s introspection endpoint defined in RFC 7662.

 revocation_endpoint

o OPTIONAL. The fully qualified URL of the server’s revocation endpoint as within the meaning of RFC 7009.

 jwks_uri

o REQUIRED. The fully qualified URI of the server’s public key in JWK Set format as defined in RFC 7517.

 scopes_supported

o REQUIRED. The list of scopes that MUST be made available by an ISP as defined in Schedule 3 (AGDIS Attribute Profile).

 claims_supported

o REQUIRED. The list of claims that MUST be made available by an ISP as defined in Schedule 3 (AGDIS Attribute Profile).

#### 2.7.3 Requests to the Authorisation Endpoint (Authentication Request)

An ISP MUST support all mechanisms for requesting a level of assurance as prescribed in section

2.8.3 of this Schedule.

#### 2.7.4 User consent

As a central and trusted participant of the AGDIS, all IXPs are responsible for collecting express consent from the individual in accordance with the attribute sharing policies outlined in Chapter 2 and Chapter 3 of Schedule 3 (AGDIS Attribute Profile).

An IXP MUST provide the mechanisms to capture express consent from the individual.

An ISP MAY gather consent from the individual to share attributes to the AGDIS but SHOULD take into consideration the end-to-end user experience impacts of additional consent gathering mechanisms.

#### 2.7.5 Response to Authorisation Requests

The authorisation response to the authorisation code flow MUST return the following fields in the response:

stateThe value of the state parameter passed in via the authentication request. This value MUST match exactly.

codeThe authorisation code, a random string issued by the OIDC provider to be used request to the Token Endpoint.

The key requirements for these fields are described in section 4.1.2 (Authorization Response) of RFC 6749.

This response MUST be sent to the client via a HTTP redirect to the URI specified in the request.

#### 2.7.5.1 Authentication Error Response

The Authentication Error Response is the message returned from an ISP’s Authorisation Endpoint in response to the Authorisation Request sent by an IXP.

If the individual denies or cancels the request, or the individual fails to authenticate, the ISP MUST inform the IXP by using the error responses defined in either:

section 4.1.2.1 (Error Response) of RFC 6749; or

section 3.1.2.6 (Authentication Error Response) of OpenID Connect Core 1.0. This profile defines an additional authentication error response: authentication_cancelled The End-User did not proceed with the authentication interaction.

#### 2.7.6 Token Response

A successful token response includes an access token, which can be used to make a UserInfo request, and as ID token (signed and optionally encrypted JWT) as per section 3.1.3.3 (Successful Token Response) of the OpenID Connect Core 1.0.

An ISP MAY also include a Refresh Token in the Token Response.

#### 2.7.6.1 ID Token

An ISP MAY encrypt ID Tokens using the appropriate key of the requesting IXP.

An ISP issued ID Token MUST expire with a lifespan of no longer than 300 seconds.

An ISP SHOULD assign lifespans shorter than 300 seconds to the ID Tokens it issues.

An ISP issued ID Token MUST contain the following fields that are defined as REQUIRED.

issREQUIRED. The issuer field is the URL of the expected issuer.

audREQUIRED. The audience field contains the client ID of the client.

subREQUIRED. The identifier of the user. Note it MUST be a pairwise anonymous identifier and be unique to the client’s OpenID Sector.

acrREQUIRED. This is the level of assurance at which the user was authenticated at.

nonce If a nonce value was supplied with the authentication request, then this value is REQUIRED.

jti REQUIRED. A unique identifier for the token which can be used to prevent the reuse of the token.

exp, iat, nbf REQUIRED. The expiration, issued at, and not before timestamps for the tokens. They are dates presented as an integer representing the number of seconds since 1970-01-01T00:00:00Z UTC (Unix epoch) within acceptable ranges.

The following is an example of an ID token signed using the server’s RSA key.

eyJhbGciOiJSUzI1NiJ9.eyJhdXRoX3RpbWUiOjE0\
MTg2OTg3ODIsImV4cCI6MTQxODY5OTQxMiwic3ViI\
joiNldaUVBwblF4ViIsIm5vbmNlIjoiMTg4NjM3Yj\
NhZjE0YSIsImF1ZCI6WyJjMWJjODRlNC00N2VlLTR\
iNjQtYmI1Mi01Y2RhNmM4MWY3ODgiXSwiaXNzIjoi\
aHR0cHM6XC9cL2lkcC1wLmV4YW1wbGUuY29tXC8iL\
CJpYXQiOjE0MTg2OTg4MTJ9mQc0rtL56dnJ7_zO_f\
x8-qObsQhXcn-qN-FC3JIDBuNmP8i11LRA_sgh_om\
RRfQAUhZD5qTRPAKbLuCD451lf7ALAUwoGg8zAASI\
5QNGXoBVVn7buxPd2SElbSnHxu0o8ZsUZZwNpircW\
NUlYLje6APJf0kre9ztTj-5J1hRKFbbHodR2I1m5q

8zQR0ql-FoFlOfPhvfurXxCRGqP1xpvLLBUi0JAw3\
F8hZt_i1RUYWMqLQZV4VU3eVNeIPAD38qD1fxTXGV\
Ed2XDJpmlcxjrWxzJ8fGfJrbsiHCzmCjflhv34O22\
zb0lJpC0d0VScqxXjNTa2-ULyCoehLcezmssg

**Figure 9 Sample ID Token signature**

Its claims are as follows:

{\
"auth_time": 1418698782,\
"exp": 1418699412,\
"sub": "6WZQPpnQxV",\
"nonce": "188637b3af14a",\
"aud": [\
"c1bc84e4-47ee-4b64-bb52-5cda6c81f788"\
],\
"iss": "https://idp.gov.au/",\
"acr":"urn:id.gov.au:tdif:acr:ip3:cl2",\
"iat": 1418698812,\
"nbf": 1418698812\
}

**Figure 10 Claims used to the generate the prior signature**

#### 2.7.7 UserInfo Endpoint

An ISP MUST support returning claims via the UserInfo endpoint as prescribed by the requirements outlined in Schedule 3 (AGDIS Attribute Profile).

When processing a UserInfo request an ISP MUST only return the claims that are authorised within the authentication request associated with the presented access token.

An ISP MUST NOT return empty or null values for claims that cannot be fulfilled unless Schedule 3 (AGDIS Attribute Profile) specifically permits these values for a given attribute set.

The sub claim MUST always be present in the UserInfo response.

#### 2.7.8 Request Object

An ISP MUST accept requests containing a request object signed by the requesting IXPs private key. An ISP MUST validate the signature on request objects using the requesting IXP’s public key.

An ISP MUST implement support for receiving requests objects encrypted with one of its public keys.

#### 2.7.9 Authentication context

An ISP MUST return the ACR value used for the authentication even if the acr claim was not marked as essential or the acr_values parameter was used.

### 2.8 Entity information

#### 2.8.1 Claims supported

IXPs and ISPs MUST return claims on a best effort basis.

An ISP or its connected IXPs asserting it can provide a user claim does not imply that the data is available for all users.

An IXP MAY returns claims outside of the claims_supported list but MUST ensure that they do not violate the data sharing and privacy constraints where prescribed under one or more of the following:

the Act;

the Accreditation Rules;

the Digital ID Rules; or

the Accreditation Data Standards.

#### 2.8.2 Scope profiles

An ISP MUST implement the OpenID Connect support ISP specific scopes and claims outlined as in Schedule 3 (AGDIS Attribute Profile).

#### 2.8.3 Valid ACR Claims

Assurance levels are outlined in Schedule 1 (AGDIS Onboarding Specifications).

An ISP MUST implement support to allow its TRPs to use either the acr_values or acr claim to request their required ACR.

An ISP MUST reject any request that include both the acr_values and acr claims.

When the acr claim is requested, an ISP MUST support the acr claim being optionally marked as essential claim by the client. For example:

“claims”: {

“id_token”: {

“acr”: {

“essential”: true,

“values”: [“urn:id.gov.au:tdif:acr:ip2:cl3”]

}

}

}

**Figure 11 Sample assurance level requests using claims**

When the acr values are marked as an essential claim, the ISP MUST return a value that matches the requested values.

If the individual is unable to achieve the required level of assurance outlined in the request and the acr

claim is marked as essential, then an ISP MUST respond with an authentication error.

If the acr claim is not marked as essential or no acr value was supplied in the brokered authentication request, then an ISP MUST respond with the level of assurance the individual was able to achieve.

### 2.9 Privacy Requirements

An ISP MUST adhere to all the ISP relevant attribute sharing policies set out in Chapter 2 and Chapter 3 of Schedule 3 (AGDIS Attribute Profile).

### 2.10 Security Considerations

All clients of an ISP:

MUST comply with the security considerations in section 10 (Security Considerations) of RFC 6749; and

SHOULD consider the additional security considerations in section 5 (Security Considerations) of RFC 6819.

## 3. Protocol brokering

An IXP MUST implement support to broker between the protocols used by its connected ISPs and PRPs.

The AGDIS only supports the OpenID Connect Core 1.0.

### 3.1 OIDC to OIDC brokering

When an IXP is accepting an authentication request from a TRP using OIDC, if the selected ISP implements this Schedule, an IXP MUST interact with the ISP using the ISP technical relying party profile as prescribed in section 2.6 of this Schedule.

#### 3.1.1 Mapping Claims and Scopes

If the sub claim is specified it MUST be handled as outlined in section 3.1.2 of this Schedule.

If the TRP’s authentication request includes attributes that are fulfilled by itself or an ASP, an IXP SHOULD NOT forward theses attribute requests to the ISP unless it is necessary.

All other attributes included in the TRP’s authentication request MUST be included in the IXPs authentication request to the ISP in accordance with the attribute sharing policies as prescribed in Chapter 4 of Schedule 3 (AGDIS Attribute Profile).

An IXP MAY expand the scopes defined in an authentication request into underlying claims when brokering an authentication request to its ISPs and ASPs.

Scopes and claims not outlined in Schedule 3 (AGDIS Attribute Profile) MUST be ignored by the IXP when brokering an authentication request. The IXP MUST NOT raise an error when scopes and claims are ignored.

#### 3.1.2 Handling of Subject ID

An IXP MAY support the sub claim in authentication requests.

If an IXP implements support the sub claim in authentication requests:

the IXP MUST resolve the pairwise identifier presented in the sub claim in the authentication request from the TRP to an existing pairwise identifier; and

the IXP MAY return an error if the pairwise identifier for the user cannot be resolved to the target ISP.

#### 3.1.3 Mapping assurance levels

If an IXP receives a single value for the acr_values or acr claim in an authentication request, the IXP MUST pass the set of ACR values that meet or exceed the requested value to the ISP in the brokered authentication request.

If the acr claim is marked as essential in the authentication request, an IXP MUST mark the acr claim as essential when sending the authentication request to the selected ISP.

An IXP MUST evaluate the ACR returned from the ISP and if the ACR meets or exceeds the originally requested value(s), return one of the originally requested values.

#### 3.1.4 Prompt Parameter

An IXP MUST implement these processing rules to broker the OIDC prompt parameter.

**Table 1 IXP prompt parameter brokering requirements**

| **From Relying Party** | **To Identity Service Provider** |
|---|---|
| None | None |
| Login | Login |
| Consent | Ignored.<br>An IXP MUST implement consent for the release of attributes in accordance with the attribute sharing policies as defined in Schedule 3 (AGDIS Attribute Profile). |
| Select Account | Service selection of identity or persona for user in context. |

#### 3.1.5 ID Token Hint Parameter

If an IXP has implemented support for the id_token_hint mechanism, the following processing rules apply:

where the IXP receives an id_token_hint within an authentication request from a TRP, the IXP is REQUIRED to validate the Identity Token and extract the subject;

the IXP MUST resolve the subject identifier at the ISP as per section 3.1.2 of this Schedule; and

the IXP MUST include the resolved subject identifier when brokering the authentication request to the ISP using the sub claim as per section 5.5 of the OpenID Connect Core 1.0 and mark the sub claim as essential.

## 4. Attributes

Schedule 3 (AGDIS Attribute Profile) outlines the attributes and attribute sets that are available to PRPs.

### 4.1 Restricted attributes

Schedule 3 (AGDIS Attribute Profile) MAY define access restrictions for certain attributes and attribute sets.

An IXP MUST implement access control mechanism on a per client basis to ensure restricted attributes are only accessible to approved PRPs.

An ISP MUST implement access control mechanism on a per IXP basis to ensure restricted attributes are only accessible in accordance with access restrictions where imposed by one or more of the following:

the Act;

the Accreditation Rules;

the Digital ID Rules; or

the Accreditation Data Standards.

### 4.2 OIDC Attribute Mapping

When an entity participating in the AGDIS is making or responding to a request using this Schedule, that entity MUST use the mapping of the attributes to the scopes and claims as defined in Schedule 3 (AGDIS Attribute Profile).

[image: Branding shape for Australia's Digital ID System]

Schedule 3 – AGDIS Attribute Profile

Contents

List of Tables

Table 1 Attribute profile consent models 2

Table 2 Attribute fulfilment requirement classes 3

Table 3 Access policies that MUST be applied to attributes 4

Table 4 Mutal Attribute Sets 6

Table 5 Core Attribute sharing policies 10

Table 6 Validated contact details attribute sharing policies 13

Table 7 Verified other names attribute sharing policies 14

Table 8 Verified Documents attribute sharing policy 15

Table 9 Verified document structure 17

Table 10 Default Verified Document attribute responses rules 18

Table 11 Document Type Code URNs 19

Table 12 Document verification method enumeration 19

Table 13 State and Territory name enumeration 20

Table 14 Medicare Card type enumeration 20

Table 15 Medicare Card type expiry patterns 20

Table 16 Travel Document gender enumeration 21

Table 17 Centrelink Concession Card enumeration 21

Table 18 Verified Birth Certificate schema 22

Table 19 Verified Change of Name Certificate schema 24

Table 20 Verified Marriage Certificate schema 26

Table 21 Verified Citizenship Certificate and Registration by Descent 28

Table 22 Verified ImmiCard schema 30

Table 23 Verified Visa Request schema 31

Table 24 Verified Driver Licence schema 32

Table 25 Verified Medicare Card schema 34

Table 26 Verified Passport schema 36

Table 27 Verified Centrelink Concession Card schema 38

Table 28 Identity System Metadata 40

Table 29 Authentication Assurance Levels 42

Table 30 Authentication Method URNs 43

Table 31 Identity System Metadata attributes 44

Table 32 Self-asserted address attribute fields 47

Table 33 Address types for a collections 48

Table 34 The telephony type for the other phone number attribute 48

Table 35 The category of contact and email or phone represents 49

Table 36 Self-Asserted Attributes 51

Table 37 ASP managed attributes and attribute sets 54

Table 38 AGDIS ASPs Attribute sharing policy summary 56

Table 39 Business Authorisation schema URNs 56

Table 40 Schema definition for Business Authorisations 57

Table 41 Business Authorisation entity type enumeraiton 58

Table 42 OIDC Attribute profile for IXP relying parties 61

Table 43 Self-asserted attribute scopes and claims for IXP relying parties 63

Table 44 OIDC Attribute profile for ISP relying parties 65

Table 45 Self-asserted attribute scopes and claims for ISP relying parties 67

Table 46 OpenID Connect attribute mapping 69

Table 47 OpenID Connect Mapping for Self-Asserted Attributes 72

Table 48 Simple data type definitions 75

Table 49 Other Names Object fields 76

Table 50 Address Object fields definitions 76

Table 51 Other Email Address type field definitions 77

Table 52 Other Phone Number type field definitions 77

Table 53 Core claim requirements 78

Table 54 Requirements for Validated Email claims 79

Table 55 Requirements for Validated Phone Number claims 79

Table 56 Requirements for Verified Other Names claims 80

Table 57 Verified Document Object schema 81

Table 58 Verified Document Identifiers with data types 82

Table 59 Verified Document Names with data types 84

Table 60 Verified Document Attributes with data types 85

Table 61 Common attributes definition 88

Table 62 Audit attribute definitions 89

Table 63 Self-Asserted Attributes types 90

Table 64 Business Authorisation data representation 95

Table 65 Core Attributes normative examples for claims 97

Table 66 Validated contact details normative examples for claims 99

Table 67 Validated contact details normative examples for scopes 101

Table 68 Verified other names normative examples for claims 105

Table 69 Birth certificate verified document claim normative example 108

Table 70 Centrelink concession card verified document claim normative example 110

Table 71 Change of Name Certificate verified document claim normative example 112

Table 72 Citizenship Certificate verified document claim normative example 114

Table 73 Registration by Descent Certificate verified document normative example 116

Table 74 Australian Driver Licence verified document normative example 118

Table 75 ImmiCard verified document normative example 120

Table 76 Marriage Certificate verified document normative example 122

Table 77 Medicare Card verified documents normative example 124

Table 78 Australian Travel Document verified document normative example 127

Table 79 Visa verified documents normative example 129

Table 80 Digital ID pairwise examples 131

Table 81 Authentication time and Update at examples 132

Table 82 Authentication Method examples 132

Table 83 Audit Identifier examples 133

Table 84 Addresses normative examples 134

Table 85 Other Email Addresses 135

Table 86 Other Phone Numbers normative examples 136

Table 87 Birthplace Normative Examples 137

Table 88 Personal Titles Normative Examples 138

Table 89 Business Authorisations 139

## Table of Figures

Figure 1 Verified Documents sample claim request 81

Figure 2 Self-asserted address sample claim request 91

Figure 3 Self-asserted other email address sample claim request 93

Figure 4 Self-asserted other email address scope equivalent claim request 93

Figure 5 Self-asserted other phone number sample claim request using the contact type 94

Figure 6 Self-asserted other phone number sample claim request using telephony type 94

Figure 7 Self-asserted other phone number scope equivalent claim request 94

## 1. Operation of attributes

This Chapter outlines how attributes operate within the context of the AGDIS and the components of an attribute sharing policy.

### 1.1 Attributes and attribute sets

Attributes, including those related to a transaction, a digital ID or the AGDIS consist of singular values or groups of values.

Singular values are attributes of an individual within the meaning of section 10 of the Act.

Groups of values are groups of attributes of an individual within the meaning of section 10 of the Act and referred to in the *Digital ID (AGDIS) Data Standards 2024* as an attribute set. The same value can be used as part of one or more attribute sets.

To support the objectives of the data minimisation principle, ASPs, ISPs and IXPs SHOULD, if possible, permit the elements of an attribute sets to be requested individually.

### 1.2 Attribute sharing policy

All attribute or attribute sets transmitted across the AGDIS MUST be subject to an attribute sharing policy.

All ASPs, ISPs and IXPs MUST comply with the attribute sharing policies in this Schedule that apply to them.

If an attribute or attribute set is not subject to an attribute sharing policy in this Schedule, ASPs, ISP and IXPs MUST NOT transmit that attribute or attribute set across the AGDIS.

An attribute sharing policy MUST outline:

the attribute or attribute set to which the policy is applied;

the consent type applied to the attributes;

the fulfilment requirements;

the access policy; and

the data representation.

#### 1.2.1 Consent types

Consent types prescribe requirements for gathering of express consent from the individual by an accredited entity participating in the AGDIS.

The consent types outlined in this Schedule are found in Table 1 below.

An attribute sharing policy MUST include a consent type and assign the management of that consent to either or both:

a specific entity (which is a named accredited entity such as myGov as an ASP); and

a specific role (such as the ASP, ISP and IXP).

**Table 1 Attribute profile consent models**

| **Consent type** | **Description** |
|---|---|
| Not required | Express consent is not required for the attribute or attribute set.<br>This consent type MUST only be applied to an attribute or attribute set when:<br>the attributes are explicitly exempt from the express consent requirements under one or more of the following:the Act;the Accreditation Rules;the Digital ID Rules; andthe Accreditation Data Standards;<br>the attributes are technical in nature and do not convey personal information on their own or when combined with other attributes; and<br>the attributes are classified as identity system meta data. |
| Every use | Express consent is required every time the attribute or attribute set is shared.<br>The consent MUST NOT be remembered or reused in subsequent requests for the attribute or attribute set. |
| Ongoing | Express consent is required at least the first time the attribute or attribute set is bound to the individual or shared.<br>The consent MAY be remembered for a fixed duration where determined by one or more of the following:<br>the Act;<br>the Accreditation Rules;<br>the Digital ID Rules;<br>the Accreditation Data Standards.<br>If the consent is remembered, the individual MUST:<br>be made aware of the use cases they are providing the consent to facilitate;<br>have the option for the consent to not be remembered; and<br>be provided with a clear and simple process to vary or withdraw the consent.<br>If the consent is remembered, the individual SHOULD be notified:<br>if the attribute is an authorisation and the authorisation is revoked by a third party, for example, by the owner or creator of the authorisation; and<br>when the consent facilitated use of their attributes in the execution of automated use cases. |

| **Consent type** | **Description** |
|---|---|
| Every Change | Express consent for the attribute or attribute set is required the first time the attribute or attribute set is shared with the PRP, and every time it is modified.<br>Accordingly, subsequent requests for express consent MUST occur when:<br>the attribute or attribute set has been modified;<br>the individual has varied or withdrawn any remembered on-going consent; and<br>the duration of the remembered consent has expired.<br>Attribute sharing policies SHOULD only apply this consent type when the underlying attributes support the detection of changes. |

#### 1.2.2 Fulfilment requirements

Not all attributes have guaranteed availability, and some may not be available for the IP level associated with the authenticated session.

The assertion of attributes in an individual’s digital ID account is dependent on the documents available to them, the documents they chose to verify their identity, and any additional linkages an individual has with ASP managed attributes. Accordingly, the fulfilment of some attributes may not be practical however some attributes may still be required.

The necessity to meet an attributes request is referred to as a fulfilment requirement in this Schedule.

An attribute sharing policy MUST have a fulfilment policy to inform the behaviours of entities participating in the AGDIS when attribute requests cannot be fulfilled.

The two fulfilment requirements used in this Schedule are outlined in Table 2 below.

**Table 2 Attribute fulfilment requirement classes**

| **Fulfilment requirement** | **Criteria and description** |
|---|---|
| Best effort | The attribute or attribute set MUST be fulfilled if the individual has verified or asserted the requested attributes or attribute set and has provided express consent to share them.<br>If the attributes request cannot be fulfilled or the individual has not provided express consent to share, an error SHOULD NOT be raised unless the attribute sharing policy requires it. |
| Required | The attribute or attribute set MUST be fulfilled.<br>If the attribute or attribute set cannot be fulfilled or the individual did not provide express consent to share, an error MUST be raised. |

#### 1.2.3 Access policy

Attributes shared with PRPs via the AGDIS are either readily available to PRPs or require approval to access. The rules defining if or why a PRP can request attributes or attribute sets is referred to as an access policy in this Schedule.

An attribute sharing policy MUST outline the access policy that applies to its attributes or attribute sets.

An attribute sharing policy MAY extend the access policy for a given context provided the intent of the policy is not overridden.

The 4 access policies available under this Schedule are outline in Table 3 below.

**Table 3 Access policies that MUST be applied to attributes**

| **Policy** | **Details** |
|---|---|
| Open | Any PRP MAY request an attribute or attribute set with this access control.<br>If attributes are available, an ASP, ISP and IXP MUST fulfill requests for attributes subject to this access policy. |
| Not available | The attribute request MUST NOT be fulfilled.<br>An ASP, ISP and IXP MAY respond with an error. |
| Restricted | A PRP MUST be approved to request this attribute or attribute set.<br>An IXP MUST only broker requests to the ASP, ISP and IXP that are permitted to fulfill the request. |
| Platform | A PRP MUST meet the platform specific requirements to have the attribute request fulfilled.<br>An IXP MUST only broker these attribute requests to the ASP, ISP and IXP that can fulfill the requests.<br>An IXP MAY respond with an error if the PRP is not a member of the attribute’s related platform or approved by the platform to request the attribute or attribute set. |

#### 1.2.4 Data representation

An attribute sharing policy MUST be accompanied by a high-level specification of an attribute or attribute set’s underlying values.

The specification MUST outline the implementation agnostic features of the attribute or attribute set including the data type and the range of acceptable values.

The default character encoding used for attributes being transmitted across the AGDIS is UTF-8.

If an attribute set for a given federation protocol uses a different character encoding the data representation MUST stipulate the character encoding used.

## 2. Core Attributes

This Chapter outlines the attribute sharing policies for the Core Attributes available from the AGDIS.

### 2.1 Mutual attributes

An IXP MUST support brokering attribute requests for all mutual attributes. An ISP MUST support processing attribute requests for all mutual attributes.

The available mutual attributes supported under this profile are outlined in Table 4 below.

**Table 4 Mutal Attribute Sets**

| **Attribute set** | **Attributes** | **Description** |
|---|---|---|
| Core | Full Name Family Name Given Names Middle Names Preferred Name Date of Birth<br>Core Attributes Last Updated | The core attributes that describe an individual – name and date of birth. |
| Validated Contact Details | Validated Email<br>Validated Email Last Updated Validated Phone Number<br>Validated Phone Number Last Updated | The validated email address and validated mobile phone number that is linked to a digital ID account at the ISP. |
| Verified Other Names | Verified Other Names<br>Verified Other Names Last Updated | Other names an individual has verified during the initial or subsequent identity proofing processes at the ISP. |
| Verified Documents | Verified Documents | The verified attributes from the documents an individual used to prove their identity at an ISP during the initial or subsequent identity proofing processes.<br>Access to this attribute set is restricted. |

#### 2.1.1 Core

Core Attributes are foundational elements used to identify an individual.

A summary of the attribute sharing policies, outlined here for Core Attributes, is provided in Table 5 below.

All Core Attributes are subject to an Open access policy as provided in Table 4 above. Not all the Core Attributes are verified as outlined in Table 5 below.

An IXP MUST request express consent from the individual for Core Attributes which have changed since consent was last recorded by the IXP.

An IXP MUST support brokering requests to its ISPs for all Core Attributes for requested IP Level of IP1 Plus or stronger.

At IP1 Plus or stronger, an ISP MUST fulfill an attribute request for:

Family Name;

Date of Birth;

Core Attributes Last Updated.

An ISP MUST return an error if it cannot fulfill a request for the above attributes.

At IP1 Plus or stronger, an ISP MUST fulfill requests for the following attributes if they are available:

Given Names;

Middle Names.

At IP1 Plus or stronger, an ISP MAY fulfill an attribute request for Full Name.

At an IP Level less than IP1 Plus, an ISP SHOULD1 NOT fulfill a request for Core Attributes other than Preferred Name.

An ISP MAY fulfill requests for Preferred Name at any IP Level. Noting that Preferred Name should be considered a self-asserted attribute as defined in section 2.3.1 of this Schedule.

Any attribute returned at IP1 should be assumed self-asserted.

An ISP MUST note every change made to the Core Attributes set by recording the date and time of the last change in the Core Attributes Last Updated attribute.

An IXP SHOULD use the Core Attributes Last Updated attribute to determine if the individual is required to provide consent before responding to the PRP’s attribute request.

#### 2.1.2 Validated Contact Details

Contact details like an email address and mobile phone number are sourced by the ISP during the identity proofing process or the individual’s ongoing use of their digital ID. Contact details are only referred to as validated due to ownership of an email address or phone number not being readily verifiable. A summary of the attribute sharing policies for these attributes is outlined in Table 6 below.

Validated Contact Details attributes are subject to an Open access policy.

[image]

1 It is intended that this requirement will change to become ‘MUST’ (rather than ‘SHOULD’) 12 months from commencement of the Act.

An IXP MUST request express consent from the individual for Validated Contact Details attributes which have changed since consent was last recorded by the IXP.

An ISP SHOULD support one or both Validated Email Address and Validated Phone Number attributes.

If the individual has not validated a phone number or email address, an ISP MUST ignore a request for these attributes.

An IXP MUST support brokering attribute requests for Validated Contact Details.

An ISP MAY fulfill attribute requests for Validated Contact Details at all requestable assurance levels. Where an ISP or IXP support a Validated Email Address, the ISP or IXP:

MUST ensure the email address complies with RFC 5322;

MUST ensure the email address has a maximum length of 254 characters in compliance with RFC 5321; and

SHOULD consider the guidance outlined in RFC 3696.

An ISP MUST note every change made to the Validated Email Address attribute by recording the date and time of the last change in the Validated Email Address Last Updated attribute.

Where an ISP or IXP support a Validated Phone Number, the ISP or IXP MUST ensure the phone number is compliant with ITU E.164.

An ISP MUST note every change made to the Validated Phone attribute by recording the date and time of the last change in the Validated Phone Last Updated attribute.

#### 2.1.3 Verified Other Names

Additional names an individual is or was known by are verified by ISPs from the EoI documents presented during the initial or subsequent identity proofing process.

These Attributes include the variations of the individual’s name from those recorded in the Core Attributes and are only sourced from the following document types:

Commencement of Identity Documents;

Linking Documents;

Photo ID Documents.

A summary of the attribute sharing policy for Verified Other Names is outlined in Table 7 below.

The Verified Other Names attribute set is subject to an Open access policy (as defined above) at IP1 Plus and stronger.

An IXP MUST NOT broker requests for Verified Other Names for IP levels weaker than IP1 Plus.

An IXP MAY ignore attribute requests or raise an error if the requested assurance level is less than IP1 Plus.

An IXP MUST request express consent from the individual for the Verified Other Names attribute set which have changed since consent was last recorded by the IXP.

An ISP MUST support attribute requests for Verified Other Names.

An ISP MAY only fulfill attribute requests for Verified Other Names when the requested IP level is IP1 Plus or stronger and appropriate documents have been verified.

An IXP MUST support brokering attribute requests for Verified Other Names.

The Verified Other Name attribute set is represented by a set of verified other names, or a collection verified other name sets.

The attribute response MUST include an Other Names Object for each document the verified other names were sourced from.

A Verified Other Names collection MUST NOT be empty.

Each Verified Other Name attribute SHOULD follow the rules outlined in Table 5 below for Family Name, Middle Names and Given Names with respect to access policy, provenance, consent, and data representation.

If the individual has not verified any additional names an ISP MUST ignore a request for this attribute set.

An ISP MUST note every change made to the Verified Other Names attribute set by recording the date and time of the last change in the Verified Other Names Last Updated attribute.

**Table 5 Core Attribute sharing policies**

| **Attribute** | **Description** | **Access policy** | **IP**<br>**Level** | **Fulfil- ment** | **Proven- ance** | **Consen t** | **Data representation** |
|---|---|---|---|---|---|---|---|
| Full Name | Individual’s full name.<br>Individual full name MUST contain a family name.<br>Given name and/or middle name may not be available.<br>If given names and/or middle names are available, the structure of full name MUST be a space separated concatenation of the attributes available.<br>For the attributes available that form the full name, they MUST follow the structure of the given names followed by available middle names followed by family name. | Open | IP1 Plus and stronger | Required | Verified | Every change | MUST be a non-empty string with a maximum length determined by possible constituent values.<br>It MUST only be composed of alpha characters, hyphens, apostrophes, and spaces. |
| Family Name | Individual’s family name.<br>If the individual only has one name verified it MUST be presented in this attribute. | Open | IP1 Plus and stronger | Required | Verified | Every change | MUST be a non-empty string with a maximum length of 100 characters.<br>It MUST only be composed of alpha characters, hyphens, |

|  |  |  |  |  |  |  | apostrophes, and spaces. |
|---|---|---|---|---|---|---|---|
| Given Names | Individual’s given names.<br>There may be zero or more names stored in this attribute. | Open | IP1 Plus and stronger | Best effort | Verified | Every change | If available MUST be a non-empty string with a maximum length of 100 characters.<br>It MUST only be composed of alpha characters, hyphens, apostrophes, and spaces. |
| Middle Names | Individual’s middle names.<br>There may be zero or more names stored in this attribute. | Open | IP1 Plus and stronger | Best effort | Verified | Every change | If available MUST be a non-empty string with a maximum length of 100 characters.<br>It MUST only be composed of alpha characters, hyphens, apostrophes, and spaces. |
| Preferred Name | Individual’s preferred name.<br>This is an attribute the individual MAY self-assert to indicate the name they prefer to be known by at the PRP. | Open | IP1 and stronger | Best effort | Self- asserted | Every change | If available MUST be a non-empty string with a maximum length of 100 characters.<br>It MUST only be composed of alpha characters, hyphens, apostrophes, and spaces. |
| Date of Birth | Individual’s date of birth. | Open | IP1 Plus and stronger | Required | Verified | Every change | RFC 3339 compliant time and date string of the form YYYY, YYYY- |

|  |  |  |  |  |  |  | MM, or YYYY-MM-DD. |
|---|---|---|---|---|---|---|---|
| Core Attributes Last Updated | Date and time of when the Core Attributes for this digital identity were updated. | Open | IP1 and stronger | Required | ISP<br>managed | Every change | A date and time representation specified in the attribute profile for the implementer’s federation protocol. |

**Table 6 Validated contact details attribute sharing policies**

| **Attribute** | **Description** | **Access policy** | **IP**<br>**Level** | **Fulfil- ment** | **Proven- ance** | **Consen t** | **Data representation** |
|---|---|---|---|---|---|---|---|
| Validated Email | The email address an individual has validated at the ISP. | Open | IP1 and stronger | Best effort | Validated | Every change | Email address conforming to RFC 5322 address syntax with a maximum length of 254 characters in compliance with RFC 5321 and SHOULD be conformant to guidance outlined in RFC 3696. |
| Validated Email Last Updated | The date and time at which the individual last validated the email address. | Open | IP1 and stronger | Best effort | Validated | Every change | A date and time representation specified in the attribute profile of each federation protocol. |
| Validated Phone Number | The mobile phone number an individual has validated at the ISP. | Open | IP1 and stronger | Best effort | Validated | Every change | A mobile number in E.164 format. |
| Validated Phone Number Updated | The date and time at which the individual last validated the mobile phone number. | Open | IP1 and stronger | Best effort | Validated | Every change | A date and time representation specified in the attribute profile for the implementer’s federation protocol. |

**Table 7 Verified other names attribute sharing policies**

| **Attribute** | **Description** | **Access policy** | **IP**<br>**level** | **Fulfil- ment** | **Proven- ance** | **Consent** | **Data representation** |
|---|---|---|---|---|---|---|---|
| Verified Other Names | A collection of Family Name, Middle Names and Given Names for each of the person’s other verified names.<br>The requirements Family Name, Middle Names and Given Names attributes are as specified in the Core Attributes set. | Open | IP1 Plus and stronger | Best effort | Verified | Every change | A collection of verified other name sets. Each verified other name set MUST contain labelled elements for at least one of Family Name, Middle Names and Given Names.<br>The data representation for each name MUST be compliant with the relevant data representation outlined for the Core Attribute set. |
| Verified Other Names Last Updated | Date and time at which the individual last verified the Verified Other Names. | Open | IP1 Plus and stronger | Best effort | ISP<br>managed | Every change | A date and time representation determined aligned to data types used by the federation protocol. |

**Table 8 Verified Documents attribute sharing policy**

| **Attribute** | **Description** | **Access policy** | **IP**<br>**level** | **Fulfil- ment** | **Proven- ance** | **Consent** | **Data representation** |
|---|---|---|---|---|---|---|---|
| Verified Documents | Collection of verified documents including document metadata, document identifiers, document names, date of birth, and additional attributes specific to a document type. | Restricted | IP2 and stronger | Required | Verified | Every use | A collection of distinct verified document types where each element of the collection is conformant to the schema for its document type. |

#### 2.1.4 Verified Documents

The verified fields from the documents an individual submitted during the identity proofing process at their chosen ISP are available as the Verified Documents attribute set. The attributes in the Verified Documents attribute sets are sourced from:

Commencement of Identity Documents;

Linking Documents;

Photo ID Documents;

Use in the Community Documents.

Not all fields/attributes from a verified document can be readily verified.

The ISP MUST return all available verified attributes associated to the verified document request. A summary of the attribute sharing policy for verified documents is presented in Table 8 above.

An IXP MUST request express consent from the individual on every use of the Verified Documents attribute set.

An IXP MUST NOT broker requests for Verified Documents for assurance levels weaker than IP2. An IXP MUST support brokering of attribute requests for a single or multiple Verified Documents. An IXP MUST only broker attribute requests for Verified Documents from approved PRPs.

An ISP MUST support attribute request for single or multiple Verified Documents.

When processing generic requests for Verified Documents, an ISP MUST prepare a response that conforms to IP2 or higher.

When processing requests for specific Verified Documents, an ISP MUST only respond to request for valid document types and for documents the individual has verified. Valid document types are outlined in Table 11 below.

The data representation for a Verified Document is set of named simple and complex attributes. Each set representing an instance of a Verified Document MUST have the following members:

Document Type Code with a value that MUST be one of the URNs outlined in Table 11 below;

Document Verification Method that MUST be one of the enumerated values in Table 12 below;

Document Verification Date MUST be valid a date and time value;

Document Date of Birth MUST be a valid date extracted from the document;

Document Identifiers is a collection that MUST contain one or more document identifiers outlined in the document type’s schema;

Document Names is a collection that MUST contain the required document names for the document type’s schema;

Document Attributes is a collection that MUST contain the required document attributes outlined in the document type’s schema.

A more detailed overview of the fields is provided in Table 9 below.

An ISP’s attribute response for each document MUST be conformant to the schema for that document’s type. Schemas for each document type make use of the enumerations outlined in the following tables and the schemas for each document type are outlined in the following sections.

**Table 9 Verified document structure**

| **Field** | **Description** | **Data representation** |
|---|---|---|
| Document Type Code | A URN representing the type of document. To be a valid the URN MUST be specified in this profile. | The valid URNs are enumerated in Table 11 below. |
| Document Verification Method | The verification method that was used to verify the document during the identity proofing process.<br>The Verification Method in the response MUST match one the values outlined in this profile. | A single character string enumerating the document verification methods.<br>The enumeration is outlined in Table 12 below of these values for the AGDIS. |
| Document Verification Date | The date and time the document was verified. | A string representing the RFC 3339 date time coordinated to coordinated universal time. |
| Document Names | A collection of key-values pairs representing the names, by-parts or full, extracted from the document and verified during the identity proofing process.<br>All name names values marked as required in the document type’s schema MUST be present. | The keys denoting entries in the set MUST be non-empty strings with values matching the enumerated name values for the document type.<br>The names values MUST be non- empty strings compliant with constraints outlined for the document type. |
| Document Date of Birth | The date of birth as submitted and verified during the identity proofing process. | An RFC 3339 date string of the format YYYY-MM-DD. |
| Document Identifiers | A collection of identifiers extracted from the document and verified during the identity proofing process.<br>The elements of the collection MUST each have a type and value field. | The type field MUST be a string with a value that matches one of the enumerated document identifier attributes for the given document type. |

|  | The identifier attributes marked as required in document type’s schema type MUST be present. | The data types of the value field MUST match the data type defined in the schema of the document type. |
|---|---|---|
| Document Attributes | A collection of attributes extracted from the document and verified during the identity proofing process.<br>The elements of the collection MUST each have a type and value field.<br>The attributes marked as required in the document type’s schema MUST be present. | The type field MUST be a string with a value that matches one of the enumerated document attributes for the given document type.<br>The data types of the value field MUST match the data type defined in the document types schema for a given document attribute. |

**Table 10 Default Verified Document attribute responses rules**

| **IP level** | **Default attribute response** |
|---|---|
| IP1 | Nil response. |
| IP1 Plus | Nil response. |
| IP 2 and higher | A PRP must be authorised to request Verified Documents.<br>This authorisation may be restricted to specific document types. |

**Table 11 Document Type Code URNs**

| **Document Type** | **Verification authority** | **Verification authority document type code** | **AGDIS document type code URN** |
|---|---|---|---|
| Birth Certificate | DVS | BC | urn:id.gov.au:tdif:doc:type_code:BC |
| Change of Name Certificate | DVS | NC | urn:id.gov.au:tdif:doc:type_code:NC |
| Marriage Certificate | DVS | MC | urn:id.gov.au:tdif:doc:type_code:MC |
| Citizenship Certificate | DVS | CC | urn:id.gov.au:tdif:doc:type_code:CC |
| Registration by Descent | DVS | RD | urn:id.gov.au:tdif:doc:type_code:RD |
| ImmiCard | DVS | IM | urn:id.gov.au:tdif:doc:type_code:IM |
| Visa | DVS | VI | urn:id.gov.au:tdif:doc:type_code:VI |
| Australian Driver Licence | DVS | DL | urn:id.gov.au:tdif:doc:type_code:DL |
| Medicare Card | DVS | MD | urn:id.gov.au:tdif:doc:type_code:MD |
| Australian Travel Document | DVS | PP | urn:id.gov.au:tdif:doc:type_code:PP |
| Centrelink Concession Card | DVS | CO | urn:id.gov.au:tdif:doc:type_code:CO |

**Table 12 Document verification method enumeration**

| **Document verification method** | **Enumeration** |
|---|---|
| Technical Verification | T |
| Source Verification | S |
| Visual Verification | V |

**Table 13 State and Territory name enumeration**

| **State/Territory** | **Enumeration** |
|---|---|
| Australian Capital Territory | ACT |
| New South Wales | NSW |
| Northern Territory | NT |
| Queensland | QLD |
| South Australian | SA |
| Tasmania | TAS |
| Victoria | VIC |
| Western Australia | WA |

**Table 14 Medicare Card type enumeration**

| **Medicare Card type** | **Enumeration** |
|---|---|
| Blue | B |
| Green | G |
| Yellow | Y |

**Table 15 Medicare Card type expiry patterns**

| **Medicare Card Type** | **Expiry Pattern** | **DVS Pattern** |
|---|---|---|
| Blue | YYYY-MM-DD | ^[0-9]{4}\\-[0-9]{2}\\-[0-9]{2} |
| Green | YYYY-MM | ^[0-9]{4}\\-[0-9]{2} |
| Yellow | YYYY-MM-DD | ^[0-9]{4}\\-[0-9]{2}\\-[0-9]{2} |

**Table 16 Travel Document gender enumeration**

| **Gender** | **Enumeration** |
|---|---|
| Male | M |
| Female | F |
| Other | X |

**Table 17 Centrelink Concession Card enumeration**

| **Card Type** | **Enumeration** |
|---|---|
| Health Care Card | HCC |
| Pensioner Concession Card | PCC |
| Commonwealth Seniors Health Card | SHC |

#### 2.1.4.1 Verified Birth Certificate schema

**Table 18 Verified Birth Certificate schema**

| **Section** | **Field Name(s)** | **Required** | **Type** | **Constraints** |
|---|---|---|---|---|
| Document Type Code | - | Y | URN | Value MUST be “urn:id.gov.au:tdif:doc:type_code:BC”. |
| Document Verification Method | - | Y | String | Only source verification is permitted for Birth Certificates. See Table 12 above for accepted values. |
| Document Verification Date | - | Y | String | MUST be an RFC 3339 formatted date time value in coordinated universal time. |
| Document Names | Family Name Given Name | Y | String | For NSW, VIC or WA issued Birth Certificates:<br>Given Name MAY be left blank if Family Name has a value;<br>Family Name MAY be left blank if Given Name has a value.<br>All other state and territory BDM issued certificates the string MUST be non- empty and have a maximum length of 80 characters.<br>Values MUST only be composed of alpha characters, apostrophes, hyphens, and spaces. |
| Document Date of Birth | Date of Birth | Y | String | MUST be an RFC 3339 formatted date value or year value of the format YYYY, YYYY-MM, or YYYY-MM-DD. Where the year value MUST be in |

|  |  |  |  | the range 1753 to 3000. |
|---|---|---|---|---|
| Document Identifiers | Registration Number | N | String | If available MUST be a string of numeric values with a maximum length of 10 characters.<br>Only available for certificates issued by BDM registries from NSW, WA, TAS, NT, ACT and VIC. |
|  | Certificate Number | N | String | If available MUST be a string of numeric values with a maximum length of 12 characters.<br>Only available for certificates issued by BDM registries from NSW, TAS, ACT, NT, SA, or VIC. |
| Document Attributes | Registration State | Y | Enumeration | MUST use the abbreviations outlined in Table 13 above. |
|  | Registration Date Registration Year | N | String | MUST be an RFC 3339 formatted date value or year value of the format YYYY or YYYY-MM-DD. Where the year value MUST be in the range 1753 to 3000. |

#### 2.1.4.2 Verified change of name schema

**Table 19 Verified Change of Name Certificate schema**

| **Section** | **Field Name(s)** | **Required** | **Type** | **Constraints** |
|---|---|---|---|---|
| Document Type Code | - | Y | URN | Value MUST be “urn:id.gov.au:tdif:doc:type_code:NC”. |
| Document Verification Method | - | Y | String | Only source verification is permitted for Change of Name Certificates. See Table 12 above for legitimate values. |
| Document Verification Date | - | Y | String | MUST be an RFC 3339 formatted date time value in coordinated universal time. |
| Document Names | Family Name Given Name | Y | String | For NSW, VIC or WA issued Birth Certificates:<br>Given Name MAY be left blank if Family Name has a value;<br>Family Name MAY be left blank if Given Name has a value.<br>All other state and territory BDM issued certificates the string MUST be non- empty and have a maximum length of 80 characters.<br>Values MUST only be composed of alpha characters, apostrophes, hyphens, and spaces. |
| Document Date of Birth | Date of Birth | N | String | MUST be an RFC 3339 formatted date value or year value of the format YYYY or YYYY-MM-DD. Where the year value MUST be in the range 1753 to 3000. |

| Document Identifiers | Registration Number | N | String | If available MUST be a string of numeric values with a maximum length of 10 characters.<br>Only available for certificates issued by BDM registries from NSW, WA, TAS, NT, ACT and VIC. |
|---|---|---|---|---|
|  | Certificate Number | N | String | If available, the value MUST be a string of numeric values with a maximum length of 12 characters.<br>Only available for certificates issued by BDM registries from NSW, TAS, ACT, NT, SA, or VIC. |
| Document Attributes | Registration State | Y | Enumeration | MUST use the abbreviations outlined in Table 13 above. |
|  | Registration Date Registration Year | N | String | MUST be an RFC 3339 formatted date value or year value of the format YYYY or YYYY-MM-DD. Where the year value MUST be in the range 1753 to 3000. |

#### 2.1.4.3 Verified Marriage Certificate schema

**Table 20 Verified Marriage Certificate schema**

| **Section** | **Field Name(s)** | **Required** | **Type** | **Constraints** |
|---|---|---|---|---|
| Document Type Code | - | Y | URN | Value MUST be “urn:id.gov.au:tdif:doc:type_code:MC”. |
| Document Verification Method | - | Y | String | Only source verification is permitted for Marriage Certificates. See Table 12 above for legitimate values. |
| Document Verification Date | - | Y | String | MUST be an RFC 3339 formatted date time value in coordinated universal time. |
| Document Names | Family Name Given Name Family Name 2<br>Given Name 2 | Y | String | For NSW, VIC or WA issued Marriage Certificates:<br>Given Name MAY be left blank if Family Name has a value;<br>Family Name MAY be left blank if Given Name has a value.<br>All other state and territory BDM issued certificates the string MUST be non- empty and have a maximum length of 80 characters.<br>Values MUST only be composed of alpha characters, apostrophes, hyphens, and spaces. |
| Document Date of Birth | Date of Birth | N | String | MUST be an RFC 3339 formatted date value or year value of the format YYYY or YYYY-MM-DD. Where the year value MUST be in the range 1753 to 3000. |

| Document Identifiers | Registration Number | N | String | String of numeric values with a maximum length of 10 characters.<br>Only available for Marriage Certificates issued by BDM registries from NSW, WA, TAS, NT, ACT and VIC. |
|---|---|---|---|---|
|  | Certificate Number | N | String | If available, the value MUST be a string of numeric values with a maximum length of 12 characters.<br>Only available for certificates issued by BDM registries from NSW, TAS, ACT, NT, SA, or VIC. |
| Document Attributes | Registration State | Y | Enumeration | MUST use the abbreviations outlined in Table 13 above. |
|  | Registration Date Registration Year | N | String | MUST be an RFC 3339 formatted date value or year value of the format YYYY or YYYY-MM-DD. Where the year value MUST be in the range 1753 to 3000 |

#### 2.1.4.4 Verified Citizenship Certificate schema

**Table 21 Verified Citizenship Certificate and Registration by Descent**

| **Section** | **Field Name(s)** | **Required** | **Type** | **Constraints** |
|---|---|---|---|---|
| Document Type Code | - | Y | URN | Value MUST be “urn:id.gov.au:tdif:doc:type_code:RD”.for Registration by Descent<br>Value MUST be “urn:id.gov.au:tdif:doc:type_code:CC”.for Citizenship Certificate |
| Document Verification Method | - | Y | String | Only source verification is permitted for Certificates of Registration by Descent. See Table 12 above for legitimate values. |
| Document Verification Date | - | Y | String | MUST be an RFC 3339 formatted date time value in coordinated universal time. |
| Document Names | Family Name | Y | String | MUST only be comprised of alpha characters (including spaces, hyphens, and apostrophes) and MUST be a non-empty string with a maximum length of 100 characters.<br>MUST only be composed of alpha characters, apostrophes, hyphens, and spaces. |
|  | Given Name | N | String | If provided MUST only be comprised of alpha characters (including spaces, hyphens, and apostrophes) and MUST be a non-empty string with a maximum length of 100 characters. |

|  |  |  |  | MUST only be composed of alpha characters, apostrophes, hyphens, and spaces. |
|---|---|---|---|---|
| Document Date of Birth | Date of Birth | Y | String | MUST be an RFC 3339 formatted date value or year value of the format YYYY or YYYY-MM-DD. Where the year value MUST be in the range 1753 to 3000. |
| Document Identifiers | Stock Number | Y | String | MUST be a non-empty string with a maximum length of 11 characters. |
| Document Attributes | Acquisition date | Y | String | MUST be a RFC 3339 formatted date value of the format YYYY-MM-DD. Exclusive to Registration by Descent only. Not applicable to Citizen Certificate. |

#### 2.1.4.5 Verified Immigration Card schema

**Table 22 Verified ImmiCard schema**

| **Section** | **Field Name(s)** | **Required** | **Type** | **Constraints** |
|---|---|---|---|---|
| Document Type Code | - | Y | URN | Value MUST be “urn:id.gov.au:tdif:doc:type_code:IM”. |
| Document Verification Method | - | Y | String | Only source verification is permitted for ImmiCards. See Table 12 above for legitimate values. |
| Document Verification Date | - | Y | String | MUST be an RFC 3339 formatted date time value in coordinated universal time. |
| Document Names | Family Name Given Name | Y | String | Values MUST be a non-empty string with a maximum of 49 characters in length.<br>Values MUST only be composed of alpha characters, apostrophes, hyphens, and spaces. |
| Document Date of Birth | Date of Birth | Y | String | MUST be an RFC 3339 formatted date value or year value of the format YYYY- MM-DD. Where the year value MUST be in the range 1753 to 3000. |
| Document Identifiers | ImmiCard Number | Y | String | MUST be a string of characters in length 9. The string MUST be composed of 3 leading alpha characters, followed by 6 numeric characters, e.g., ABC123456. |
| Document Attributes | - | - | - | No attributes for the document. |

#### 2.1.4.6 Verified Visa Request schema

**Table 23 Verified Visa Request schema**

| **Section** | **Field Name(s)** | **Required** | **Type** | **Constraints** |
|---|---|---|---|---|
| Document Type Code | - | Y | URN | Value MUST be “urn:id.gov.au:tdif:doc:type_code:VI”. |
| Document Verification Method | - | Y | String | Only source verification is permitted for Visa Requests. See Table 12 above for legitimate values. |
| Document Verification Date | - | Y | String | MUST be an RFC 3339 formatted date time value in coordinated universal time. |
| Document Names | Family Name Given Name | Y | String | MUST be a non-empty string with a maximum length of 49 characters.<br>MUST only be composed of alpha characters, apostrophes, hyphens, and spaces. |
| Document Date of Birth | Date of Birth | Y | String | MUST be an RFC 3339 formatted date value or year value of the format YYYY- MM-DD. Where the year value MUST be in the range 1753 to 3000. |
| Document Identifiers | Passport Number | Y | String | MUST be non-empty string with a length of 14 upper and lower case alphanumeric characters, in any order. |

#### 2.1.4.7 Verified Driver Licence schema

**Table 24 Verified Driver Licence schema**

| **Section** | **Field Name(s)** | **Required** | **Type** | **Constraints** |
|---|---|---|---|---|
| Document Type Code | - | Y | URN | Value MUST be “urn:id.gov.au:tdif:doc:type_code:DL”. |
| Document Verification Method | - | Y | String | Only source verification is permitted for Driver Licences. See Table 12 above for legitimate values. |
| Document Verification Date | - | Y | String | MUST be an RFC 3339 formatted date time value in coordinated universal time. |
| Document Names | Family Name | Y | String | MUST be a non-empty string and only be comprised of alpha characters (including spaces, hyphens, and apostrophes), and have a maximum length of 40 characters. |
|  | Given Name | Y | String | MUST be a non-empty string and only be comprised of alpha characters (including spaces, hyphens, and apostrophes), and have a maximum length of 20 characters. |
|  | Middle Name | N | String | If available it MUST be a non-empty string and only be comprised of alpha characters (including spaces, hyphens, and apostrophes), and have a maximum length of 20 characters. |

| Document Date of Birth | Date of Birth | Y | String | MUST be an RFC 3339 formatted date value or year value of the format YYYY- MM-DD. Where the year value MUST be in the range 1753 to 3000. |
|---|---|---|---|---|
| Document Identifiers | Licence Number | Y | String | MUST be a non-empty alphanumeric string to with maximum length of 10 characters. |
|  | Card Number | N | String | If available, MUST be a non-empty alphanumeric string to with maximum length of 10 characters. |
| Document Attributes | State of Issue | Y | Enumeration | Follow the enumeration outline in Table 13 above. |

#### 2.1.4.8 Verified Medicare Card schema

**Table 25 Verified Medicare Card schema**

| **Section** | **Field Name(s)** | **Required** | **Type** | **Constraints** |
|---|---|---|---|---|
| Document Type Code | - | Y | URN | Value MUST be “urn:id.gov.au:tdif:doc:type_code:MD”. |
| Document Verification Method | - | Y | String | Only source verification is permitted for Medicare Cards. See Table 12 above for legitimate values. |
| Document Verification Date | - | Y | String | MUST be an RFC 3339 formatted date time value in coordinated universal time. |
| Document Date of Birth | Date of Birth | Y | String | MUST be an RFC 3339 formatted date value or year value of the format YYYY- MM-DD. Where the year value MUST be in the range 1753 to 3000. |
| Document Identifiers | Card Number | Y | String | MUST be a string of 10 numerical characters. |
|  | Individual Ref Number | Y | String | MUST be a single numeric character within the range of 1 to 9 inclusive. |
| Document Attributes | Card Expiry | Y | Date | MUST meet the data format for the Card Type. See Table 15 for expiry date formats date. |

|  | Card Type | Y | Enumeration | MUST be one of the single character values outlined in Table 14 above. |
|---|---|---|---|---|
|  | Full Name 1 | Y | String | Name line 1 from the card.<br>MUST be a non-empty string with a maximum length of 27 characters. It MUST only be composed of alpha characters, hyphens, apostrophes, and spaces. |
|  | Full Name 2 | Y | String | Name line 2 from the card.<br>If available, MUST be a non-empty string with a maximum length of 25 characters. It MUST only be composed of alpha characters, hyphens, apostrophes, and spaces.<br>Can be NULL if not available. |
|  | Full Name 3 | Y | String | Name line 3 from the card.<br>If available, MUST be a non-empty string with a maximum length of 23 characters. It MUST only be composed of alpha characters, hyphens, apostrophes, and spaces.<br>Can be NULL if not available. |
|  | Full Name 4 | Y | Sting | Name line 4 from the card.<br>If available, MUST be a non-empty string with a maximum length of 21 characters. It MUST only be composed of alpha characters, hyphens, apostrophes, and spaces. |

|  |  |  |  | Can be NULL if not available. |
|---|---|---|---|---|

#### 2.1.4.9 Verified Passport schema

**Table 26 Verified Passport schema**

| **Section** | **Field Name(s)** | **Required** | **Type** | **Constraints** |
|---|---|---|---|---|
| Document Type Code | - | Y | URN | Value MUST be “urn:id.gov.au:tdif:doc:type_code:PP”. |
| Document Verification Method | - | Y | String | Only source verification is permitted for Passports and Australian Travel Documents. See Table 12 above for legitimate values. |
| Document Verification Date | - | Y | String | MUST be an RFC 3339 formatted date time value in coordinated universal time. |
| Document Names | Family Name | Y | String | MUST be a non-empty string with a maximum length of 31 characters.<br>MUST only be composed of alpha characters, hyphens, apostrophes, and spaces. |
|  | Given Name | N | String | If available, MUST be a non-empty string with a maximum length of 31 characters.<br>MUST only be composed of alpha characters, hyphens, apostrophes, and spaces. |

| **Section** | **Field Name(s)** | **Required** | **Type** | **Constraints** |
|---|---|---|---|---|
| Document Date of Birth | Date of Birth | Y | String | MUST be an RFC 3339 formatted date value of the format YYYY-MM-DD. Where the year value MUST be in the range 1753 to 3000. |
| Document Identifiers | Travel Document Number | Y | String | Either one or two alpha characters followed by seven numeric characters. No spaces. |
| Document Attributes | Gender | Y | Enumeration | MUST use the abbreviated Gender enumeration in Table 16 above. |

#### 2.1.4.10 Verified Centrelink Concession Card schema

**Table 27 Verified Centrelink Concession Card schema**

| **Section** | **Field Name(s)** | **Required** | **Type** | **Constraints** |
|---|---|---|---|---|
| Document Type Code | - | Y | URN | Value MUST be “urn:id.gov.au:tdif:doc:type_code:CO”. |
| Document Verification Method | - | Y | String | Only source verification is permitted for Centrelink Concession Cards. See Table 12 above for legitimate values. |
| Document Verification Date | - | Y | String | MUST be an RFC 3339 formatted date time value in coordinated universal time. |
| Document Names | Name | Y | String | MUST be a non-empty string with a maximum length of 32 characters.<br>MUST only be composed of alpha characters, hyphens, apostrophes, and spaces. |
| Document Date of Birth | Date of Birth | N | String | MUST be an RFC 3339 formatted date value or year value of the format YYYY, YYYY-MM, or YYYY-MM-DD. Where the year value MUST be in the range 1753 to 3000. |
| Document Identifiers | CRN | Y | String | MUST be a string of 10 characters.<br>The first 9 characters MUST be numerical values and the last character MUST be an alpha character, e.g., 123456789A |

| Document Attributes | Card Expiry | Y | Date | MUST be an RFC 3339 formatted date value of the format YYYY-MM-DD. Where the year value MUST be in the range 1753 to 3000. |
|---|---|---|---|---|
|  | Card Type | Y | Enumeration | MUST be one of the values enumerated in Table 17 above. |

### 2.2 Identity System Metadata

Identity System Metadata attributes defined in this section are values that do not convey any personal information about an individual but facilitate core AGDIS functionality.

Unless explicitly stated, all Identity System Metadata attributes:

do not require express consent to be requested from the individual when sharing;

are subject to an Open access policy; and

MAY be fulfilled at all assurance levels.

A summary of the sharing policies outlined for these attributes can be found in Table 31 below.

**Table 28 Identity System Metadata**

| **Metadata Set** | **Attributes** | **Description** |
|---|---|---|
| Common | Digital ID user identifier Authentication Time Identity Proofing Level Authentication Level Authentication Method Last Updated | Common attributes that support the use of a digital ID across the AGDIS.<br>Implementers should review attribute sharing policy for each attribute to determine if they need to support its generation, management, or use. |
| Audit | RP Audit ID | An identifier unique to every logical interaction between an IXP and a PRP.<br>The RP Audit identifier MUST not be shared with ISPs. |

#### 2.2.1 Common

#### 2.2.1.1 Digital ID Identifier

The Digital ID Identifier is a unique identifier for an individual. The Digital ID Identifier:

(a) For PRPs, is the pairwise identifier assigned to an individual by an IXP; and

(b) for IXPs, the GPI or pairwise identifier assigned to an individual by an ISP.

The generation and assignment of these unique identifiers MUST be compliant with the relevant requirements outlined in section 1.2.1 and section 1.2.2 of Schedule 1 (AGDIS Onboarding Specifications).

The Digital ID identifiers MUST be compliant with data representation prescribed in section 2.4.4 of Schedule 1 (AGDIS Onboarding Specifications).

#### 2.2.1.2 Authentication Time

Authentication Time is the date and time when the individual successfully authenticated at the ISP. An ISP MUST support this metadata value.

An IXP MUST support brokering requests for this metadata value.

The data representation for the date-time value is dependent upon the federation protocols being brokered. An IXP MAY need to translate values between types when brokering between different federation protocols in a transaction.

#### 2.2.1.3 Assurance Level

The Assurance Level of the authenticated digital ID outlines the IP level and authentication level attained during authentication at the ISP.

An IXP MUST broker requests for this value as requested from a PRP to the ISPs in accordance with the requirements in section 2.1.9 of Schedule 1 (AGDIS Onboarding Specifications) and requirements outlined by the federation protocols being used.

An ISP MUST process and respond to request for the value in accordance with the requirements in section 2.1.3 of Schedule 1 (AGDIS Onboarding Specifications) and requirements outlined in the relevant federation protocols.

The data representation for this value is specified in Schedule 1 (AGDIS Onboarding Specifications) and illustrated in Table 29 below.

#### 2.2.1.4 Authentication Method

The Authentication Method value communicates to the PRP which ISP the individual used to authenticate themselves. The Authentication Method is an IXP managed value.

An IXP MAY provide the Authentication Method based on the ISP the individual has successfully authenticated themselves if required.

An IXP MAY cache the attribute to support subsequent SSO requests.

An IXP MUST NOT return any information about the Authentication Method if the authentication fails or is cancelled by the individual.

The data representation for the Authentication Method is a URN presented in Table 30 below.

#### 2.2.1.5 Last Updated

Last Updated is the date and time that any of the individual’s attributes were last updated.

An IXP MUST support brokering attribute request for this value. An ISP MUST implement support for this value.

The data representation for this attribute is dependent upon the federation protocols in use.

#### 2.2.2 Audit

#### 2.2.2.1 RP audit Identifier

The RP audit ID requirements are outlined in section 2.1.2 of Schedule 1 (AGDIS Onboarding Specifications).

The RP audit ID is an IXP specific value that ISPs do not need to support.

An RP audit ID is a unique audit identifier generated for every logical interaction between a PRP and an IXP to enable an audit trail.

An IXP MUST NOT share the RP audit ID it has generated for a PRP with ISPs.

To ensure uniqueness of the RP audit ID within the AGDIS a UUID is used. The UUID generation MUST conform to RFC 4122.

**Table 29 Authentication Assurance Levels**

| **IP level** | **Authenticator level** | **URN** |
|---|---|---|
| IP1 | AL1 | urn:id.gov.au:tdif:acr:ip1:cl1 |
|  | AL2 | urn:id.gov.au:tdif:acr:ip1:cl2 |
|  | AL3 | urn:id.gov.au:tdif:acr:ip1:cl3 |
| IP1 PLUS | AL1 | urn:id.gov.au:tdif:acr:ip1p:cl1 |
|  | AL2 | urn:id.gov.au:tdif:acr:ip1p:cl2 |
|  | AL3 | urn:id.gov.au:tdif:acr:ip1p:cl3 |
| IP2 | AL2 | urn:id.gov.au:tdif:acr:ip2:cl2 |
|  | AL3 | urn:id.gov.au:tdif:acr:ip2:cl3 |
| IP2 PLUS | AL2 | urn:id.gov.au:tdif:acr:ip2p:cl2 |
|  | AL3 | urn:id.gov.au:tdif:acr:ip2p:cl3 |
| IP3 | AL2 | urn:id.gov.au:tdif:acr:ip3:cl2 |
|  | AL3 | urn:id.gov.au:tdif:acr:ip2p:cl2 |
| IP4 | AL3 | urn:id.gov.au:tdif:acr:ip4:cl3 |

**Table 30 Authentication Method URNs**

| **ISP** | **Abbreviation** | **URN** |
|---|---|---|
| myID | myID | urn:id.gov.au:idp:myid |

Schedule 3 – AGDIS Attribute Profile. Page 44

**Table 31 Identity System Metadata attributes**

| **Attribute** | **Description** | **Access policy** | **IP**<br>**level** | **Fulfilme nt** | **Proven- ance** | **Consent Type** | **Data representation** |
|---|---|---|---|---|---|---|---|
| Digital Pairwise Identifier | The Digital ID Identifier is a unique identifier for an individual.<br>The Digital ID Identifier:<br>For PRPs, is the pairwise identifier assigned by an IXP; and<br>for IXPs, the GPI or pairwise identifier assigned by an ISP. | Open | IP1 and stronger | Required | Provider managed | Not required | Regardless of the federation protocol used this attribute MUST be generate pairwise identifiers in accordance with algorithm outlined in section 8.1 of the OpenID Connect Core 1.0 specification. |
| Authentication Time | The date and time when the individual successfully authenticated at the ISP. | Open | IP1 and stronger | Required | ISP<br>managed | Not required | A date and time representation aligned to data types used by the federation protocol. |
| Assurance Level | The assurance level of the authenticated Digital ID outlines the IP level and authentication level attained during authentication at the ISP. | Open | IP1 and stronger | Required | ISP<br>managed | Not required | The assurance level MUST be one of the assurance level URNs outlined in Table 29 above. |
| RP Audit Identifier | The RP Audit Identifier requirements are outlined in Schedule 1 (AGDIS Onboarding Specifications). | Open | IP1 and stronger | Required | IXP<br>managed | Not required | To ensure uniqueness the RP Audit Identifiers within the AGDIS a UUID is used. The UUID generation MUST conform to RFC4122. |

### 2.3 Assumed Self-Asserted Attributes

Assumed Self-Asserted Attributes are attributes provided by an individual that can assist with service delivery and enhance the overall user experience for example by prefilling online forms.

An ISP SHOULD support the Self-Asserted Attributes outlined in this section. An IXP SHOULD support brokering request for these attributes.

Self-asserted attributes are subject to an Open access policy and attribute requests MAY be fulfilled at any assurance level unless an attribute’s sharing policy explicitly states otherwise.

An IXP MUST request express consent from the individual on changes it is aware of to any Self- Asserted Attributes.

#### 2.3.1 Preferred Name

An individual may nominate a name they prefer to be known as at the PRPs they access. A Preferred Name can reflect an individual’s personal preference or may be culturally significant. Ideally an individual should be able to nominate a preferred name they wish to use on the AGDIS.

Given an individual may use the attribute at their ISP to satisfy cultural requirements the preferred name SHOULD be easy to update.

Preferred Name attribute SHOULD be assumed to be self-asserted.

Although it is a Core Attribute, a Preferred Name MUST not be used as an authoritative attribute in the same manner as a PRP would use any of the verified name attributes (Family Name, Give Names or Middle Names).

The data representation for preferred names follows the requirements for the verified name attributes, and the data representation of the federation protocol(s) used to fulfill an attribute request.

#### 2.3.2 Addresses

An individual MAY self-assert a residential, postal, business, or other addresses.

Addresses MAY be collected during the identity proofing process or added by the individual during the normal use and management of their digital ID.

The attribute response for addresses MAY be a single address or a collection of addresses. The data representation for an Address attribute MUST contain the following fields:

the address type;

street address;

locality;

region;

post code; and

validated.

The data representation MAY also contain the following fields:

country; and

formatted.

A list valid address type URNs is outlined in Table 33 below.

The field locality maps to suburb, city, administrative area, or place name.

The field region maps to the larger administrative areas like state, territory, province, or prefecture. The field formatted, a print-ready string of the address, MAY also be included in the address object. A detailed description of the fields in an address are outlined in Table 32 below.

An ISP fulfilling an address attribute request where the type of address is not specified SHOULD return a default value nominated by the individual.

#### 2.3.3 Other Email Addresses

An individual MAY self-assert additional email addresses for use in different contexts, for example when accessing business services with their personal digital ID.

An ISP MUST NOT permit an individual to add an email address that is currently claimed as the validated email address for the individual’s or other active digital ID accounts on their system.

If an ISP uses the Validated Email Address as the account identifier, the ISP MAY use any of the other email addresses asserted by an individual as an ad hoc replacement for the individual’s account identifier.

An ISP MUST validate the individual has control over all other email addresses they assert if it is used as a replacement for the account identifier.

The attribute response for other email addresses MAY be a single email address or a collection of email addresses.

Each Other Email Address MUST contain:

the email address;

a flag indicating if the email address has been validated; and

a contact type label.

The data representation for each other email address string MUST conform to the requirements outlined above for Validated Email Address in section 2.1.2 of this Schedule.

The contact type value MUST be one the contact type URNs enumerated in Table 35 below.

An ISP fulfilling an attribute request for other email address where the contact type of address being requested is not specified SHOULD return a default value nominated by the individual.

#### 2.3.4 Other Phone Numbers

An individual may self-assert additional phone numbers to use with their digital ID, for example an additional phone number may be a personal landline number or business phone number.

The attribute response for other phone numbers MAY be a single phone number object or a collection of phone number objects.

The data representation for each Other Phone Number object MUST contain:

the phone number;

a telephony type;

a flag indicating if the phone number has been validated; and

a contact type label.

The data representation for each Other Phone Number string MUST conform to the requirements outlined for the validated phone number in section 2.1.2 of this Schedule.

The telephony type MUST be one of the URNs enumerated in Table 34 below.

The contact type value MUST be one the contact type URNs enumerated in Table 35 below.

An ISP fulfilling an attribute request for Other Phone Numbers where one of contact type or telephony type is not specified SHOULD return a default value nominated by the individual.

**Table 32 Self-asserted address attribute fields**

| **Field** | **Required** | **Description** |
|---|---|---|
| Address Type | Y | One of the enumerated values in Table 33 below. |
| Formatted | N | A print ready formatted string representation of the address. |
| Street Address | Y | Full street address string, which MAY include house number, street name, Post Office Box, and multi-line extended street address information. The field MAY contain multiple lines separated by newline delimiters. The new line can be delimited by a carriage return (‘\\n’) or a carriage return and line feed character (‘\\r\\n’). |
| Locality | Y | A string representing the city, suburb, or placename of the address. |
| Region | N | A string representing the state, territory, province, prefecture or region. |
| Post Code | Y | A string representing the postal or zip code. |
| Country | N | A string representing the country of the address. |
| Validated | Y | A Boolean value indicating if the legitimacy of the address has been validated. |

**Table 33 Address types for a collections**

| **Address Type** | **URN** | **Notes** |
|---|---|---|
| Default | urn:id.gov.au:agdis:address:default | Used in requests only. Selects the default address type nominated by the individual. |
| Residential | urn:id.gov.au:agdis:address:residential | - |
| Postal | urn:id.gov.au:agdis:address:postal | - |
| Business | urn:id.gov.au:agdis:address:business | - |
| Work | urn:id.gov.au:agdis:address:work | - |
| Other | urn:id.gov.au:agdis:address:other | - |

**Table 34 The telephony type for the other phone number attribute**

| **Phone Type** | **URN** | **Notes** |
|---|---|---|
| Default | urn:id.gov.au:agdis:tel:default | Used in requests only. Selects the default address type nominated by the individual. |
| Text | urn:id.gov.au:agdis:tel:text | - |
| Voice | urn:id.gov.au:agdis:tel:voice | - |
| Fax | urn:id.gov.au:agdis:tel:fax | - |
| Cell | urn:id.gov.au:agdis:tel:cell | - |
| Mobile | urn:id.gov.au:agdis:tel:mobile | - |
| Video | urn:id.gov.au:agdis:tel:video | - |
| Pager | urn:id.gov.au:agdis:tel:pager | - |
| Textphone | urn:id.gov.au:agdis:tel:textphone | - |
| Other | urn:id.gov.au:agdis:tel:other | - |

**Table 35 The category of contact and email or phone represents**

| **Contact Type** | **URN** | **Notes** |
|---|---|---|
| Default | urn:id.gov.au:agdis:contact:default | Used in requests only. Selects the default contact type nominated by the individual |
| Personal | urn:id.gov.au:agdis:contact:personal |  |
| Business | urn:id.gov.au:agdis:contact:business |  |
| Work | urn:id.gov.au:agdis:contact:work |  |
| Other | urn:id.gov.au:agdis:contact:other |  |

#### 2.3.5 Place of Birth

An individual can self-assert their place of birth. For individuals holding an Australian Birth Certificate the Place of Birth field is not verified during the identity proofing process and presently there are no readily available mechanisms to validate foreign birth certificates and their attributes.

If an ISP supports this self-asserted attribute, they SHOULD ensure the location supplied by the individual is real if practical to do so.

The data representation for this attribute is a string with a maximum length of 255 characters.

#### 2.3.6 Personal Titles

Qualification, honorific or gender-based titles can be asserted by the individual to tailor user experiences at a PRP.

An ISP MAY allow an individual to specify their preferred title.

An ISP SHOULD appropriately limit the types of titles an individual may choose.

The data representation for this attribute is string with a maximum length of 100 characters.

### 2.4 Computed Attributes

There are no Computed Attributes outlined in this Schedule or presently shared in the AGDIS.

Computed Attributes MUST be used to help the AGDIS achieve the requirements of the data minimisation principle, and limit the data transmitted across its digital ID data environment.

Computed Attributes are dynamically derived from existing attributes and attribute sets using a defined algorithm and SHOULD assert a statement about an individual without necessarily containing any identity information.

Attributes sharing policies for Computed Attributes MUST align with the underlying attributes the computed value is derived from. Specifically, a Computed Attribute derived from attributes subject to a Restricted access policy SHOULD also be a restricted attribute.

**Table 36 Self-Asserted Attributes**

| **Attribute** | **Description** | **Access policy** | **IP level** | **Fulfilment** | **Provenance** | **Consent** | **Data representation** |
|---|---|---|---|---|---|---|---|
| Preferred Name | A name or names asserted by the individual that may not be verifiable. | Open | IP1 and stronger | Best effort | ISP managed | Every change | A non-zero length string or a collection of non-zero length strings. |
| Address | A<br>residential, postal, or other address that can be gathered from the individual during the identity proofing process or the normal management of their<br>digital ID | Open | IP1 and stronger | Best effort | ISP managed | Every change | A single address or collection of addresses. Each address MUST adhere to the data representation outlined in section 2.3.2 of this Schedule. |

Schedule 3 – AGDIS Attribute Profile. Page 52

| **Attribute** | **Description** | **Access policy** | **IP level** | **Fulfilment** | **Provenance** | **Consent** | **Data representation** |
|---|---|---|---|---|---|---|---|
|  | account at their ISP. |  |  |  |  |  |  |
| Other Email Addresses | Addition email address. |  | IP1 and stronger |  |  |  |  |
| Other Phone Numbers | Additional phone numbers provided by the individual during the identity proofing process or the normal management of their digital ID account at their ISP. | Open | IP1 and stronger | Best effort | ISP managed | Every change | A phone object or collection phone numbers. Each phone number MUST adhere to the data representation outlined in section 2.3.4 of this Schedule. |
| Personal Titles | A free text attribute allowing individuals<br>to specify | Open | IP1 and stronger | Best effort | ISP managed | Every change | A non-zero length string. |

| **Attribute** | **Description** | **Access policy** | **IP level** | **Fulfilment** | **Provenance** | **Consent** | **Data representation** |
|---|---|---|---|---|---|---|---|
|  | their qualification, honorific or gender- based titles. |  |  |  |  |  |  |

Schedule 3 – AGDIS Attribute Profile. Page 54

## 3. Attribute Service Provider (ASP) Profiles

This Chapter provides the attribute sharing policies for the attributes and attribute sets provided by ASPs.

An IXP MUST implement support to broker access to these attributes in accordance with this Chapter’s attribute sharing policies.

An IXP MUST not broker requests for ASP managed attributes or attribute sets to ISPs to ensure AGDIS privacy requirements are maintained.

**Table 37 ASP managed attributes and attribute sets**

| **Attribute Set** | **Attributes** | **Description** |
|---|---|---|
| Business Authorisations | Authorisation Schemas Unique Relationship ID Entity ID<br>Entity Type Entity Name Contact Emails Relationship Type<br>Relationship Start Time Relationship End Time Roles<br>Entitlements<br>Attributes Last Updated | The Australian Taxation Office’s Relationship Authorisation Manager (RAM) manages the authorisation for a person to act on behalf of a business entity that is registered with the Australian Business Register (ABR) and issued with an Australian Business Number (ABN). |
| myGov linkID | myGov linkID | A pairwise identifier used by the myGov platform. This is attribute is subject to restrictions. |

### 3.1 Business Authorisations

Business Authorisations are an attribute set managed by the Australian Taxation Office’s Relationship Authorisation Manager (RAM). A Business Authorisation represents a relationship between an individual, an Australian business, and a government service provider.

Business Authorisations have the following 4 key components:

the individual or subject of the authorisation;

the business on behalf of which the authorisation allows the individual to act, represented by an Australian Business Number (ABN);

the service provider the individual’s business authorisation is for; and

the creator of the authorisation, a principal authority or administrator.

A summary of the attribute sharing policy for business documents is presented below.

Business Authorisations are subject to an Open access sharing policy. With the caveat that a PRP SHOULD be established in RAM as a service provider before making an attribute request for Business Authorisations.

Acting in its capacity as an ASP, RAM:

MUST request express consent from the individual when they accept a Business Authorisation;

if the consent is remembered – MUST inform the individual of the terms of the ongoing consent and the use cases it covers, and how consent can be varied or withdrawn;

if the consent is remembered – MUST provide the individual with a clear and simple process to vary or withdraw consent;

MAY notify a service provider when an authorisation has been issued, revoked, or expired; and

SHOULD notify the subject of a Business Authorisation when the authorisation has been revoked or expired.

An IXP brokering attribute requests to RAM MUST facilitate the mapping of the IXP’s issued PRP client identifier(s) to the identifier RAM has assigned to a service provider.

The data representation for Business Authorisation is a collection of business authorisations, where each business authorisation contains the values outlined below.

### 3.2 myGov linkID

The myGov linkID is a pairwise identifier assigned by myGov to map the relationship between an individual and myGov’s member service. It serves a similar purpose to digital ID pairwise identifiers outlined in section 1.2.2 of Schedule 1 (AGDIS Onboarding Specifications).

The myGov linkID is subject to the platform access policy as outlined in section 1.2.3 of this Schedule.

An IXP MUST NOT broker requests for the myGov linkID to an ISP.

An IXP MUST only broker requests for the myGov linkID to PRPs that are myGov member service.

The data representation for the myGov linkID is managed by myGov and shared directly with its member services.

Schedule 3 – AGDIS Attribute Profile. Page 56

**Table 38 AGDIS ASPs Attribute sharing policy summary**

| **Attribute** | **Description** | **Access policy** | **Fulfil- ment** | **Proven- ance** | **Consent** | **Data representation** |
|---|---|---|---|---|---|---|
| Business Authorisations | A collection of business authorisations that permit and individual to act on behalf of a business at a government service. | Open | Best effort | ASP<br>managed | Ongoing | Each entry in the collection MUST follow the data representation outlined in Table 40 below. |
| myGov linkID | Specific to the myGov platform, the myGov linkID is a pairwise ID used to map relationships between myGov and its member services. | Platform | Best effort | ASP<br>managed | Every change | Determined by myGov. |

**Table 39 Business Authorisation schema URNs**

| **Version** | **URN** | **Notes** |
|---|---|---|
| $VERSION | urn:id.gov.au:tdif:authorisatons:business:$VERSION | The generic URN format for Business Authorisations. |
| 1.0 | urn:id.gov.au:tdif:authorisatons:business:1.0 | The legacy version for Business Authorisations. |

**Table 40 Schema definition for Business Authorisations**

| **Field** | **Description** | **Data representation** |
|---|---|---|
| Schemas | A URN or collection of URNs denoting the version of the Business Authorisation payload. | The collection MUST contain at least one URN denoting the version of data representation for this Business Authorisation. The format for the mandatory URNs is prescribed in Table 39 above. |
| Unique Entity Relationship ID | Unique identifier for the relationship between the individual and the entity issued by RAM. | A string representation of a unique identifier. |
| Entity ID | The unique identifier for the entity. In practice this is the ABN of the entity and in the future may represent additional identifiers. | A string with constraints determined by the Entity Type field. |
| Entity Type | The type of entity identifier. | A string that MUST be one of the enumerated values defined in Table 41 below. |
| Entity Name | The name of the entity. Information about the entity may be separately available from ABR using the Entity ID. | A string with a maximum length of 200 characters. |
| Contact Details | The email address for the individual may not match the individual’s validated email address. | Email address conforming to RFC 5322 address syntax with a maximum length of 254 characters in compliance with RFC 5321 and SHOULD be<br>conformant to guidance outlined in RFC 3696. |
| Relationship Type | The type of relationship the individual has with the entity. | A non-empty string. |
| Relationship Start Time | The date and time from which the authorisation is becomes valid. | RFC 3339 date and time in coordinated universal time format. |

| **Field** | **Description** | **Data representation** |
|---|---|---|
| Relationship End Time | The date and time after which the authorisation is no longer valid. | RFC 3339 date and time in coordinated universal time format. |
| Attributes | A collection of key-value pairs describing the Business Authorisation. | A collection of objects with only 2 fields – name and value.<br>An enumeration of these values is defined by RAM. |
| Roles | A list of literal values that define the roles an individual can assume on behalf of the entity. | A collection of literals defined by RAM. |
| Entitlements | Additional privileges or permissions the individual may have when acting on behalf of the entity. The entitlements may be specific to a given PRP context. | A collection of literals defined by RAM or the service provider. |
| Attributes Last Updated | Date and time of when the authorisation was last modified. | RFC 3339 date and time in coordinated universal time format. |

**Table 41 Business Authorisation entity type enumeraiton**

| **Entity Type** | **Description** | **Entity ID constraints** |
|---|---|---|
| ABN | Australian Business Number | A numeric string of 11 characters in length. |

## 4. OpenID Connect Attribute Profile

To enable the use of attributes and attribute sets across the AGDIS an idiomatic mapping from this profile to Schedule 2 (AGDIS OpenID Connect Profile) is outlined in this Chapter.

The mapping outlines requirements to ensure interoperability amongst entities participating in the AGDIS making and fulfilling attribute requests. The data types assigned to the mapped OIDC scopes and claims, for each attribute, are also defined here along with their representation.

### 4.1 Attribute mapping

This Schedule outlines 2 attribute mappings:

IXP to PRP; and

ISP to IXP.

An IXP MUST implement support for the IXP relying party mapping (section 4.1.1 of this Schedule) for its PRPs.

PRPs using OpenID Connect Core 1.0 as their federation protocol SHOULD use the IXP relying party mapping (section 4.1.1 of this Schedule) when configuring their service.

An ISP MUST implement support for the ISP scopes and claims (section 4.1.2 of this Schedule) for its connected AGDIS IXPs.

An IXP MUST support brokering attribute requests from the IXP relying party mapping to the ISP relying party mapping to support ISPs and PRPs using OpenID Connect Core 1.0 as their federation protocol (as outlined in Schedule 2 (AGDIS Open ID Connect Profile)).

#### 4.1.1 Identity Exchange Provider Relying Party Mapping

The scopes an IXP MUST make available for a PRP to request are:

openid

profile

email

phone

tdif_other_names

tdif_docs

tdif_business_authorisations

The attribute sets mapped to these OpenID Connect Core 1.0 scopes along with the relevant sets of claims is outlined in Table 42 below. A detailed attribute mapping to claims, along with data types, is presented in Table 46 below.

Additional scopes for Self-Asserted Attributes that an IXP SHOULD support brokering attribute requests for are:

adgis_address

agdis_other_email

agdis_other_phone

agdis_birth_place

agdis_personal_title

The Self-Asserted Attributes are mapped to OIDC scopes and claims are outlined in Table 43 below, with detailed mapping from attributes to claims provided in Table 46 below.

An IXP SHOULD support brokering of attributes requests for each claim outlined in Table 42 below and Table 43 below.

An IXP MAY fulfill attributes request via either the Token or UserInfo Endpoints.

An IXP MUST encrypt all scopes and claims, except for the common attributes set, when fulfilling attribute requests via the Token Endpoint.

#### 4.1.2 Identity provider scopes and claims

The scopes an ISP MUST make available for its IXPs to request are:

openid

tdif_core

tdif_email

tdif_phone

tdif_other_names

tdif_docs

The attribute sets mapped to these OpenID Connect Core 1.0 scopes along with the relevant sets of claims are outlined in Table 44. A detailed attribute mapping to claims, along with data types, is presented in Table 46.

Additional scopes for Self-Asserted Attributes an ISP SHOULD make available for its IXPs to request are:

adgis_address

agdis_other_email

agdis_other_phone

agdis_birth_place

agdis_personal_title

The self-asserted attribute sets are mapped to OpenID Connect Core 1.0 scopes and claims are outlined in Table 45, with detailed mapping from attributes to claims in Table 46.

An ISP SHOULD support attribute requests for each individual claim outlined in Table 44 and Table 45.

An ISP MAY fulfill attributes request via either the Token or UserInfo Endpoints.

An ISP SHOULD encrypt all scopes and claims, except for the common attributes set, when fulfilling and attribute requests via the Token Endpoint.

**Table 42 OIDC Attribute profile for IXP relying parties**

| **Attribute Set** | **Scope** | **Claims** | **Endpoint** | **Notes** |
|---|---|---|---|---|
| Common | openid | sub auth_time acr<br>amr tdif_audit_id | Token UserInfo | An IXP SHOULD ignore or respond with an error to attribute requests if this scope is missing.<br>All common claims MUST be present in the response. |
| Core | profile | name family_name given_name middle_name<br>preferred_username birthdate updated_at | Token UserInfo | Preferred Name is a self-asserted attribute, see section 2.3.1 of this Schedule |

| **Attribute Set** | **Scope** | **Claims** | **Endpoint** | **Notes** |
|---|---|---|---|---|
| Validated Email | email | email email_verified<br>tdif_email_updated_at | Token UserInfo | An IXP MUST return all claims when fulfilling the scope. |
| Validated Phone | phone | phone phone_number_verified tdif_phone_updated_at | Token UserInfo | An IXP MUST return all claims when fulfilling the scope. |
| Verified Other Names | tdif_other_names | tdif_other_names tdif_other_names_updated | Token UserInfo | An IXP MUST return all claims when fulfilling the scope. |
| Verified Documents | tdif_doc | tdif_doc | UserInfo | Access to these scopes and claims is restricted. |
| Business Authorisations | tdif_business_authoristions | tdif_business_authoristions | UserInfo | Supplied by the Australian Taxation Office’s Relationship Authorisation Manager (RAM). |

**Table 43 Self-asserted attribute scopes and claims for IXP relying parties**

| **Attribute Set** | **Scope** | **Claims** | **Endpoint** | **Notes** |
|---|---|---|---|---|
| Preferred Name | profile | preferred_username | Token UserInfo | This is the same attribute from Table 42 above an IXP MUST support brokering this claim. |
| Addresses | adgis_address | adgis_address | Token UserInfo | A PRP may specify values for the desired address type using the address type URNs outlined in Table 33 above when requesting this attribute via the claim parameter. |
| Other Email Address | agdis_other_email | agdis_other_email | Token UserInfo | A PRP may specify values for the desired email contact type using the contact type URNs outlined in Table 35 above when requesting this attribute via the claim parameter. |
| Other Phone Numbers | agdis_other_phone | agdis_other_phone | Token UserInfo | A PRP may specify the desired contact category or telephony type using the URNs outlined in<br>Table 34 and Table 35 above when requesting this attribute via the claim parameter. |

| **Attribute Set** | **Scope** | **Claims** | **Endpoint** | **Notes** |
|---|---|---|---|---|
| Place of Birth | agdis_birth_place | agdis_birth_place | Token UserInfo |  |
| Personal Title | agdis_personal_title | agdis_personal_title | Token UserInfo |  |

**Table 44 OIDC Attribute profile for ISP relying parties**

| **Attribute Set** | **Scope** | **Claims** | **Endpoint** | **Notes** |
|---|---|---|---|---|
| Common | openid | sub auth_time acr | Token UserInfo | As per OpenID Connect Core 1.0 this scope MUST be present. |
| Core | tdif_core | name family_name given_name middle_name<br>preferred_username birthdate updated_at tdif_core_updated_at | Token UserInfo |  |
| Validated Email | tdif_email | email email_verified<br>tdif_email_updated_at | Token UserInfo |  |

| **Attribute Set** | **Scope** | **Claims** | **Endpoint** | **Notes** |
|---|---|---|---|---|
| Validated Phone | tdif_phone | phone phone_number_verified tdif_phone_updated_at | Token UserInfo |  |
| Verified Other Names | tdif_other_names | tdif_other_names tdif_other_names_updated | Token UserInfo |  |
| Verified Documents | tdif_doc | tdif_doc | UserInfo | An IXP MUST only request this attribute set when brokering attribute request for approved PRPs.<br>The scope payload is defined in section 4.3.4 of this Schedule. |

**Table 45 Self-asserted attribute scopes and claims for ISP relying parties**

| **Attribute Set** | **Scope** | **Claims** | **Endpoint** | **Notes** |
|---|---|---|---|---|
| Preferred Name | tdif_core | preferred_username | Token UserInfo | This is the same attribute from Table 44 above an ISP MUST support brokering this claim. |
| Addresses | adgis_address | adgis_address | Token UserInfo | When brokering request for a specific address type an IXP MUST ensure the requested address type(s) conform to the address type URNs outlined in Table 33 above. |
| Other Email Address | agdis_other_email | agdis_other_email | Token UserInfo | When brokering requests for a specific category of email address an IXP MUST ensure the requested contact type conforms to the URNs outlined in Table 35 above. |
| Other Phone Numbers | agdis_other_phone | agdis_other_phone | Token UserInfo | When brokering requests for a specific type of phone number an IXP MUST ensure the requested telephony type or contact type conform to the URNs specified in Table 34 and Table 35 above. |

| **Attribute Set** | **Scope** | **Claims** | **Endpoint** | **Notes** |
|---|---|---|---|---|
| Place of Birth | agdis_birth_place | agdis_birth_place | Token UserInfo |  |
| Personal Title | agdis_personal_title | agdis_personal_title | Token UserInfo |  |

**Table 46 OpenID Connect attribute mapping**

| **Attribute** | **OIDC claim** | **JSON type** | **AGDIS type** | **Requestable from** | **Reference** |
|---|---|---|---|---|---|
| Digital Identity (user identifier) | sub | string | - | ISP, IXP | OIDC Core 1.0, section 2<br>OIDC Core 1.0, section 8 |
| Full Name | name | string | RequiredNameString | ISP, IXP | OIDC Core 1.0, section 5.1 |
| Family Name | family_name | string | RequiredNameString | ISP, IXP | OIDC Core 1.0, section 5.1 |
| Middle Names | middle_name | string | NameString | ISP, IXP | OIDC Core 1.0, section 5.1 |
| Given Names | given_name | string | NameString | ISP, IXP | OIDC Core 1.0, section 5.1 |
| Preferred Name | preferred_username | string | NameString | ISP, IXP | OIDC Core 1.0, section 5.1 |
| Date of birth | birthdate | string | Date | ISP, IXP | OIDC Core 1.0, section 5.1 |
| Core Attributes Last Updated | tdif_core_upadated_at | number | Unix timestamp | ISP, IXP | Section 4.2.2.6 of this Schedule |
| Validated Email | email | string | Email | ISP, IXP | OIDC Core 1.0, section 5.1 |
| Email Validated Indicator | email_verified<br>Note: Under this profile this claim MUST always be True | literal | Boolean | ISP, IXP | OIDC Core 1.0, section 5.1 |

| **Attribute** | **OIDC claim** | **JSON type** | **AGDIS type** | **Requestable from** | **Reference** |
|---|---|---|---|---|---|
| Validated Email Last Updated | tdif_email_updated_at<br>Note: Under this profile this claim MUST always be True | number | Unix timestamp | ISP, IXP | Section 2.1.2,<br>section 4.2.2.6 of this Schedule |
| Validated Mobile Phone Number | phone_number | string | Phone | ISP, IXP | OIDC Core 1.0, section 5.1 |
| Mobile Phone Number Validated Indicator | phone_number_verified<br>Note: Under this profile this claim MUST always be True | literal | Boolean | ISP, IXP | OIDC Core 1.0, section 5.1 |
| Validated Mobile Phone Last Updated | tdif_phone_number_updated_at | number | Unix timestamp | ISP, IXP | Section 2.1.2,<br>section 4.2.2.6 of this Schedule |
| Verified Other Names | tdif_other_names | complex type | Other Names Object | ISP, IXP | Section 2.1.3,<br>section 4.2.3.1 of this Schedule |
| Other Verified Names Last Updated | tdif_other_names_updated_at | number | Unix timestamp | ISP, IXP | Section 2.1.3,<br>section 4.2.2.6 of this Schedule |
| Verified Documents | tdif_doc | complex type | Verified Documents | ISP, IXP | Section2.1.4,<br>section 4.3.4 of this Schedule |

| **Attribute** | **OIDC claim** | **JSON type** | **AGDIS type** | **Requestable from** | **Reference** |
|---|---|---|---|---|---|
| Assurance Level | acr | string | URN | ISP, IXP | OIDC Core 1.0, section 2<br>Section 2.2.1.3 of this Schedule |
| Authentication Method | amr | string | URN | IXP | OIDC Core 1.0, section 2<br>Section 2.2.1.4 of this Schedule |
| Authentication Time | auth_time | number | Unix timestamp | ISP, IXP | OIDC Core 1.0. section 2 |
| RP Audit ID | tdif_audit_id | string | UUID | IXP | Schedule 1 (AGDIS Onboarding Specifications) |
| myGov linkID | mygov_link_id | string | - | IXP | myGov defined payload |
| Business Authorisations | tdif_business_authorisations | complex type | Business Authorisation | IXP, ASP | Section 3.1 of this Schedule |
| Last Updated | update_at | number | Unix Timestamp | ISP, IXP | OIDC Core 1.0, section 5.1 |

**Table 47 OpenID Connect Mapping for Self-Asserted Attributes**

| **Attribute** | **OIDC claim** | **JSON type** | **AGDIS type** | **Requestable from** | **Reference** |
|---|---|---|---|---|---|
| Preferred Name | preferred_username | string | NameString | ISP, IXP | Section 2.1.1 of this Schedule Section 2.3.1 of this Schedule |
| Address | agdis_address | complex type | Address Object or Address Object<br>Collection | ISP, IXP | Section 2.3.2 of this Schedule |
| Other Email Addresses | agdis_other_email | complex type | Other Email Address Object or<br>Other Email Address<br>Object Collection | ISP, IXP | Section 2.3.3 of this Schedule |
| Other Phone Number | agdis_other_phone | complex type | Other Phone Number Object or<br>Other Phone Number<br>Object Collection | ISP, IXP | Section 2.3.4 of this Schedule |
| Place of Birth | agdis_birthplace | string | - | ISP, IXP | Section 2.3.5 of this Schedule |
| Personal Title | agdis_personal_title | string | - | ISP, IXP | Section 2.3.6 of this Schedule |

### 4.2 Data types

#### 4.2.1 JavaScript Object Notation types

The primitive data types assigned to attributes conveyed via claims and scopes conform to the JSON data interchange format as outlined in RFC 8529. The primitive JSON data types are the building blocks used in the data type definitions for the simple and complex types used in the AGDIS.

#### 4.2.2 Simple data types

Simple data types are JSON primitives with additional constraints applied that MUST be applied to the held value for an attribute. The AGDIS type and its associated JSON type with constraints are presented in Table 48 below.

#### 4.2.2.1 NameString

A JSON string that can represent name attributes that are not mandatory. The value has a:

(a) minimum length of zero characters; and

(b) maximum length of 100 characters.

#### 4.2.2.2 RequiredNameString

A JSON string that can represent name attributes that are mandatory. The value has a:

(a) minimum length of 1 character; and

(b) maximum length of 100 characters.

#### 4.2.2.3 Boolean

#### 4.2.2.4 A JSON literal with values that can be true or false.Date

RFC 3339 compliant date string that MUST conform to one of the following:

YYYY

YYYY-MM

YYYY-MM-DD

This value is commonly used to represent birth dates.

#### 4.2.2.5 DateTime

RFC 3339 compliant date and time string capturing a significant date and time in Coordinated Universal Time (UTC). Values MUST assume one of the following forms:

YYYY-MM-DDTHH:MM:SSZ

YYYY-MM-DDTHH:MMZ

#### 4.2.2.6 Unix Timestamp

A JSON number representing a date and time as the number of seconds since 1970-01-01T00:00:00Z up to when the time was observed.

Note: Follows the same format as the OIDC updated_at claim outlined in section 5.1 of the OpenID Connect Core 1.0 profile.

#### 4.2.2.7 Email

A non-empty JSON string with a maximum length of 254 characters (defined by RFC 5321) with a format that conforms to the syntax defined in RFC 5322 and SHOULD be conformant to guidance outlined in RFC 3696.

#### 4.2.2.8 PhoneNumber

A non-empty JSON string with a maximum length of 15 characters with format the confirms to the phone numbering for prescribed in ITU-T E.164.

#### 4.2.2.9 UUID

A JSON string that MUST be at most 36 characters in length and is generated in accordance with RFC 4122.

Selection of an appropriate version of the UUID version to be used is at the discretion of the participant. The UUID version choice MUST be suitable to avoid collisions.

**Table 48 Simple data type definitions**

| **AGDIS type** | **JSON type** | **Constraints** |
|---|---|---|
| Name string | string | Minimum length 0 characters. Maximum length 100 characters. |
| Required Name String | string | A non-empty string.<br>Maximum length 100 characters. |
| Boolean | JSON literal | Either true or false. |
| Date | string | RFC 3339 compliant date string that MUST conform to one of the following:<br>YYYY<br>YYYY-MM YYYY-MM-DD |
| Date Time | string | RFC 3339 compliant date and time string of the form YYYY- MM-DDTHH:MM:SSZ. |
| Unix Timestamp | number | A JSON number that represents the time as the number of seconds from 1970-01-01T00:00:00Z as measured in coordinated universal time until the present time.<br>Note: Follows the same format as the OIDC updated_at claim outlined in section 5.1 of the OpenID Connect Core 1.0 profile. |
| Email | string | A non-empty string with a maximum length of 254 characters (defined by RFC 5321) with a format that conforms to the syntax defined in RFC 5322 and SHOULD be conformant to guidance outlined in RFC 3696. |
| Phone Number | string | A string with a maximum length of 15 characters with format the confirms to the phone numbering for prescribed in ITU-T E.164. |
| UUID | string | A string that MUST be 36 characters in length and is generated in accordance with RFC 4122. |

#### 4.2.3 Complex data types

#### 4.2.3.1 Other Names Object

An Other Names Object is a JSON Object that represents an instance of a Verified Other Name. The data types outlined in Table 46 above for the encapsulated claims MUST be applied.

At least one value of the claims MUST be present for the Other Name Object to be valid.

**Table 49 Other Names Object fields**

| **Attribute** | **Claim/Field name** | **Required** |
|---|---|---|
| Family Name | family_name | Y |
| Given Name | given_name | N |
| Middle Name | middle_name | N |
| Full Name | full_name | Y |

#### 4.2.3.2 Address Object

The Address Object is a JSON Object that is intended to be used for the self-asserted address scope and claims. The specification for this data type maps directly to the definition outlined in Table 32 above.

**Table 50 Address Object fields definitions**

| **Attribute** | **Field name** | **Data type** | **Required** |
|---|---|---|---|
| Address Type | address_type | URN from values outlined in Table 33above | Y |
| Formatted | formatted | string | N |
| Street Address | street_address | string | Y |
| Locality | locality | string | Y |
| Region | region | string | Y |
| Post Code | post_code | string | Y |
| Country | country | string | N |
| Validated | validated | Boolean | Y |

#### 4.2.3.3 Other Email Address Object

The Other Email Address Object is a JSON Object that is intended to be used for the self-asserted other email address scope and claim.

The data types for the fields of the Other Email Address JSON Object, outlined in section 2.3.3 of this Schedule, are presented in Table 51 below.

**Table 51 Other Email Address type field definitions**

| **Attribute** | **Field name** | **Data type** | **Required** |
|---|---|---|---|
| Email | email | Email | Y |
| Email Validated | email_validated | Boolean | Y |
| Contact Type | contact_type | URN from the values prescribed in Table 35 above | Y |

#### 4.2.3.4 Other Phone Number Object

The Other Phone Number Type is a JSON Object that is intended to be sued for the self-asserted other phone numbers scope and claim.

The data types for the fields Other Phone Number JSON Object, outlined in section 2.3.4 of this Schedule, are presented in Table 52 below.

**Table 52 Other Phone Number type field definitions**

| **Attribute** | **Field name** | **Data type** | **Required** |
|---|---|---|---|
| Other Phone | other_phone | Phone | Y |
| Other Phone Validated | other_phone_validated | Boolean | Y |
| Other Phone Telephony Type | telephony_type | URN from the values prescribed in Table 34 above | Y |
| Contact Type | contact_type | URN from the values prescribed in Table 35 above | Y |

### 4.3 Mutual attributes

#### 4.3.1 Core

Each of the Core Attributes are assigned a simple data type (see Table 46 above). Additional requirements for the Core Attribute data representation are outlined in Table 53 below. Normative examples are available in section 4.8 of this Schedule.

**Table 53 Core claim requirements**

| **Claim** | **AGDIS data type** | **Requirements** |
|---|---|---|
| name | RequiredNameString | Value MUST be a concatenation of given_name, middle_name and family_name.<br>The joining character SHOULD be a space. |
| family_name | RequiredNameString | MUST NOT be an empty string. |
| given_name | NameString | MAY be excluded from attribute responses when value is an empty string. |
| middle_name | NameString | MAY be excluded from attribute responses when value is an empty string. |
| birthdate | Date | SHOULD be validated to ensure dates that satisfying the RFC 3339 format and are reasonable. |
| updated_at | Unix Timestamp | MUST be derived from the most recently updated Core Attribute. |
| tdif_core_updated_at | Unix Timestamp | IXPs MUST NOT broker this claim to PRPs.<br>ISPs MUST supply this claim. |

#### 4.3.2 Validated Contact Details

As outlined in section 2.1.2 of this Schedule the Validated Contact attributes cover the individual’s validated email and phone. The data types applied to the claims in the attribute response MUST conform to the values outlined in Table 46 above.

All claims MUST be returned when fulfilling the email and phone scopes.

An ISP MUST not fulfill this request if the related email or phone number have not been validated.

**Table 54 Requirements for Validated Email claims**

| **Claim** | **AGDIS**<br>**data type** | **Required for scope** | **Constraints** |
|---|---|---|---|
| email | Email | Y |  |
| email_verified | Boolean | Y | If the email has not been successfully validated the scope for these claims should not be fulfilled. |
| tdif_email_updated_at | Unix Timestamp | Y |  |

**Table 55 Requirements for Validated Phone Number claims**

| **Claim** | **AGDIS**<br>**data type** | **Required for scope** | **Constraints** |
|---|---|---|---|
| phone | Phone Number | Y |  |
| phone_verified | Boolean | Y | If the phone number has not been validated successfully the scope for these claims should not be fulfilled. |
| tdif_phone_number_updated_at | Unix Timestamp | Y |  |

#### 4.3.3 Verified Other Names

The Verified Other Names scope and claim uses the Other Names object for each of the verified other names returned in an attribute request.

An ISP fulfilling this request MAY return a single Other Name object or a JSON array containing the single value when only one Verified Other Name set is available.

An ISP fulfilling this request MUST return a JSON array of Other Name object when two or more Other Verified Names are available.

**Table 56 Requirements for Verified Other Names claims**

| **Claim** | **AGDIS**<br>**data type** | **Required for scope** | **Constraints** |
|---|---|---|---|
| tdif_other_names | Other Names Object or an Array of Other Names Objects | Y | Returning a single OtherNameObject is only permitted when a single other name has been verified. |
| tdif_other_names_updated_at | Unix Timestamp | Y | - |

#### 4.3.4 Verified Documents

A Verified Document MUST be represented as a JSON Object with a structure conformant to the schema outlined in Table 10 above with the literal field names and data types outlined in Table 58 below.

The responses to an attribute request for a single verified document MAY be serialised as a single Verified Document Object or as wrapped in a JSON Array.

An attribute response for multiple verified documents MUST be serialised as a JSON Array of Verified Document Objects.

An ISP MUST apply the rules outlined in Table 10 above when preparing an attribute response if the attribute request for verified documents comes via the scope parameter.

Using the claims request parameter an attribute request for one or more specific documents can be made, using the document type code URNs outlined in Table 11 above. An example request is illustrated below in Figure 1.

{\
…,\
“userinfo”: {\
…,\
“tdif_docs”: {\
“values”: [\
“urn:id.gov.au:tdif:doc:type_code:MD”,\
“urn:id.gov.au:tdif:doc:type_code:DL”,\
“urn:id.gov.au:tdif:doc:type_code:PP”\
]\
},\
…\
},\
…\
}

**Figure 1 Verified Documents sample claim request.**

**Table 57 Verified Document Object schema**

| **Document attribute** | **Payload name** | **JSON**<br>**type** | **AGDIS**<br>**data type** | **Requirements** |
|---|---|---|---|---|
| Document Type Code | type_code | string | URN | MUST be one of the values defined in Table 11 above. |
| Document Verification Method | verification_method | string | - | MUST be one of values defined in Table 12 above.<br>MUST be 1 character in length. |
| Document Verification Date | verification_date | string | Date Time | - |
| Document Identifiers | identifiers | Object | Document Identifiers Object | See section 4.3.4.1of this Schedule. |

| **Document attribute** | **Payload name** | **JSON**<br>**type** | **AGDIS**<br>**data type** | **Requirements** |
|---|---|---|---|---|
| Document Names | names | Object | Document Names Object | See section 4.3.4.2of this Schedule. |
| Document Date of Birth | birthdate | string | Date | Valid DVS dates are between 1753-01-01<br>to 3000-12-31 |
| Document Attributes | attributes | Object | Document Attribute Object |  |

#### 4.3.4.1 Document Identifiers Object

The Document Identifiers field of a Verified Document Object is a JSON Object with keys and values determined by the parent objects document type.

The document type, held in the type_code claim, is mapped to an enumeration of permitted values in Table 58 below. The mapping does not imply the required the presence of a document identifier, for the specified verified document type, for the payload to be valid. For a given document type, the availability of document identifiers is dependent upon an identity document’s issuing authority and when it was issued.

For a Document Identifiers Object to be valid it MUST:

(a) only have keys that map to the parent object’s Document Type field; and

(b) be compliant with value data types prescribed in Table 58 below for a given identifier.

**Table 58 Verified Document Identifiers with data types**

| **Document identifier string** | **Value data type** | **Value requirements** | **Used by document types** |
|---|---|---|---|
| **Registration Number** | string | Maximum length 10 characters.<br>Only available for ACT, NT, NSW, TAS, VIC, and WA. | BC, MC, NC |
| **Registration Date** | Date | - | BC, MC, NC |
| **Registration Year** | Number | Integer value for the year. | BC, MC, NC |

| **Certificate Number** | string | Max length 11 characters.<br>Only composed of numeric characters.<br>Only available for NSW, TAS, ACT, NT, SA, and VIC. | BC, MC, NC |
|---|---|---|---|
| **Stock Number** | string | Minimum length 1 character. Maximum length 10 characters. | CC, RD |
| **ImmiCard Number** | string | Minimum length 1 character. Maximum length 9 characters. | IM |
| **Passport Number** | string | Minimum length 1 character. Maximum length 14 characters. | VI |
| **Licence Number** | string | Minimum length 1 character. Maximum length 10 characters. | DL |
| **Card Number** | string | Maximum length 10 characters. | DL, MD |
| **Individual Ref Number** | number | Value from 1 to 9. | MD |
| **Travel Document Number** | string | Minimum length 8 character. Maximum length 9 characters. | PP |
| **CRN** | string | Length MUST be 10 characters. | CO |

#### 4.3.4.2 Document Names Object

The Document Names Object field of a Verified Document Object is a JSON Object with keys and values determined by the parent objects document type.

The document type, held in the type_code claim, is mapped to an enumeration of permitted values in Table 58 above. The mapping does not imply the presence of a document name attribute is required

for the specified verified document type. For a given document type, the availability of document name attributes is dependent upon the underlying identity document’s issuing authority and when it was issued.

For a Document Names Object to be valid it MUST:

(a) only have keys that map to the parent object’s Document Type field; and

(b) be compliant with value data types prescribed in Table 58 above for a given Name Attribute.

**Table 59 Verified Document Names with data types**

| **Document name attribute literal** | **Value data type** | **Value requirements** | **Used by document types** |
|---|---|---|---|
| Family Name | string | Maximum length 100 characters.<br>May be empty if Give Names has a value for documents issued by NSW, VIC, or WA Births Deaths & Marriages. | BC, MC, NC, CC, RD, IM, VI, DL, PP |
| Given Names | string | Maximum length 100 characters.<br>May be empty if Family Name has a value for a document issued by NSW, VIC, or WA Births Deaths & Marriages. | BC, MC, NC, CC, RD, IM, VI, DL, PP |
| Family Name 2 | string | Maximum length 50 characters. May be empty if<br>Given Names 2 has a value for a document issued by NSW, VIC, or WA Births Deaths & Marriages. | MC |
| Given Names 2 | string | Maximum length 60 characters. May be empty if<br>Family Name 2 has a value for a document issued by NSW, VIC, or WA Births Deaths & Marriages. | MC |
| Middle Name | string | Maximum length 20 characters. | DL |

| **Document name attribute literal** | **Value data type** | **Value requirements** | **Used by document types** |
|---|---|---|---|
| Name | string | Maximum length 32 characters | CO |

#### 4.3.4.3 Document Attributes Object

The Document Attributes field of a Verified Document Object is a JSON Object with keys and values determined by the parent objects document type.

The document type, held in the type_code claim, is mapped to an enumeration of permitted values in Table 60 below. The mapping does not imply the required presence of a document attribute, for the specified verified document type, for the payload to be valid. For a given document type, the availability of document attributes is dependent upon an identity document’s issuing authority and when it was issued.

For a Document Identifiers Object to be valid it MUST:

only comprise keys that map to the parent object’s Document Type field; and

have values that are compliant with data types prescribed in Table 60 below for a given identifier.

**Table 60 Verified Document Attributes with data types**

| **Document attribute string** | **Value data type** | **Value requirements** | **Used by document types** |
|---|---|---|---|
| Registration State | string | An up to 3 letter abbreviation of the registration state name.<br>See Table 13 above for accepted values. | BC, MC, NC |
| Date of Event | Date | DVS valid dates are between 1753-01-01 to 3000-12-31. | MC |
| Acquisition Date | Date | DVS valid dates are between 1753-01-01 to 3000-12-31. | CC, RD<br>DVS request input field but is not checked. |

| **Document attribute string** | **Value data type** | **Value requirements** | **Used by document types** |
|---|---|---|---|
| Country of Issue | string | A non-empty string.<br>DVS does not specify any additional constraints on the verified value. | VI |
| State of Issue | string | An up to 3 letter abbreviation of the registration state name.<br>See Table 13 above for legal values. | DL |
| Card Type | string | Single character matching the enumeration in Table 14 above. | MD |
| Card Expiry | string | Medicare Card expiry values are determined by the Card Type.<br>See Table 15 above for patterns. | MD |
| Full Name 1 | string | Maximum length 27 characters.<br>Line 1 of the Medicare Card full name. | MD |
| Full Name 2 | string | Maximum length 25 characters.<br>Line 2 of the Medicare Card full name. | MD |
| Full Name 3 | string | Maximum length 23 characters.<br>Line 3 of the Medicare Card full name. | MD |
| Full Name 4 | string | Maximum length 21 characters.<br>Line 4 of the Medicare Card full name. | MD |

| **Document attribute string** | **Value data type** | **Value requirements** | **Used by document types** |
|---|---|---|---|
| Gender | string | Single character enumeration of the gender value the travel document.<br>See Table 16 above for accepted values. | PP |
| CardType | string | 3-character enumeration of the concession card type.<br>Set Table 17 above for accepted values. | CO |
| CardExpiry | Date | DVS valid dates are between 1753-01-01 to 3000-12-31 | CO |

### 4.4 Identity System Metadata

#### 4.4.1 Common

OpenID Connect Core 1.0 data representation for the common attribute sets defined in section 2.2.1 of this Schedule.

**Table 61 Common attributes definition**

| **Claim** | **AGDIS Data Type** | **Constraints** |
|---|---|---|
| sub | string | Maximum length 255 characters. |
| auth_time | Unix Timestamp | - |
| acr | URN<br>or<br>Array of URNs | See section 2.2.1.3, section 4.4.1.3 of this Schedule. |
| amr | URN | Must be one of the values outlined in Table 30 above. |
| updated_at | Unix Timestamp | - |

#### 4.4.1.1 Subject ID

Commonly referred to as the subject identifier or subject ID the sub claim’s data definition is outlined in OpenID Connect attribute found in Table 47 above.

ISPs and IXPs assigned subject IDs MUST be conform to the requirements outlined in section 1.2 of Schedule 1 (AGDIS Onboarding Specifications).

#### 4.4.1.2 Authentication Time

An ISP MUST implement support for authentication time, the auth_time claim, as outlined in Table 47 above.

#### 4.4.1.3 Assurance Level

When making, brokering, or fulfilling request for an Assurance Level, in compliance with the role specific requirements outlined in Schedule 2 (AGIDS OpenID Connect Profile), all entities

participating the AGDIS (including PRPs) MUST submit ACR values conforming to the URNs enumerated in Table 29 above.

#### 4.4.1.4 Authentication Method

When fulfilling the Authentication Method claim an IXP MUST use URN values conformant with the values outlined in Table 30 above to communicate the ISP chosen and authenticated at by the individual.

The addition of other values Internet Assigned Numbers Authority registered in line with the specification for the Authentication Method Reference response are permitted.

#### 4.4.1.5 Last Updated

An ISP MUST implement support for this claim as outlined in Table 44 above using a Unix Timestamp.

#### 4.4.2 Audit

The claim outlined in this section is for the RP Audit ID only.

Audit and transaction identifiers for the ISP to IXP transactions are left to the discretion of IXPs and accordingly not defined here.

**Table 62 Audit attribute definitions**

| **Claim** | **AGDIS**<br>**data type** | **Constraints** |
|---|---|---|
| tdif_audit_id | UUID | - |

#### 4.4.2.1 RP Audit Identifier

An IXP MUST implement RP Audit ID, the tdif_audit_id claim, as outlined in section 2.2.2.1 of this Schedule.

### 4.5 Self-Asserted Attributes

Assumed Self-Asserted Attributes are not mandatory under this profile, however if an ISP supports these attributes, they MUST implement the definitions outlined in Table 63 below to ensure interoperability.

**Table 63 Self-Asserted Attributes types**

| **Claim** | **AGDIS**<br>**Data Type** | **Constraints** |
|---|---|---|
| preferred_username | NameString | Section 2.1.1,<br>section 2.3.1 of this Schedule.<br>Non-empty string with a maximum length 100 characters. |
| agdis_address | Address Object or<br>Array of Address Objects | Section 2.3.2,<br>section 4.5.2 of this Schedule. |
| agdis_other_email | Other Email Object or<br>Array of Other Email Objects | Section 2.3.3,<br>section 4.5.3 of this Schedule. |
| agdis_other_phone | Other Phone Object or<br>Array of Other Phone Objects | Section 2.3.4,<br>section 4.5.4 of this Schedule. |
| agdis_birthplace | String | Section 2.3.5,<br>section 4.5.5 of this Schedule.<br>Non-empty string with a maximum length 255 characters. |
| agdis_personal_title | String | Section 2.3.6,<br>section 4.5.6 of this Schedule.<br>Non-empty string with a maximum length of 100 characters. |

#### 4.5.1 Preferred Name

The Preferred Name follows the same data definitions for name claims in the Core Attribute set. If fulfilled it MUST be a non-empty string with a maximum length of 100 characters.

#### 4.5.2 Addresses

The Address claim MAY represent one or more Address Objects.

A request for a single address MAY be returned as a single Address object or as a JSON Array containing a single entry.

A request for one or more addresses MUST be returned as a JSON array of Address Objects.

An attribute requests for multiple or a specific address type can be done via the claim requests parameter using the Address Type URNs in Table 33 above.

A request MAY include the default address along with other address types.

The example request is illustrated in Figure 2 will return the default address and the residential address, if they are not the same value.

#### 4.5.3 Other Email Addresses

The Other Email Addresses scope MUST only return the default email address nominated by the individual.

The Other Email Address claim MAY represent one or more Other Email Address Objects.

A request for a single other email address MAY be returned as a single Other Email Address object or as a JSON Array containing a single entry.

A request for one or more other email addresses MUST be returned as a JSON array of Other Email Address Objects.

An attribute requests for multiple or a specific other email address type can be done via the claim requests parameter using the Contact Type URNs defined in Table 36 above. An example request is illustrated in Figure 3.

A request MAY include the default contact type along with other contact type URNs.

{\
…,\
“userinfo”: {\
…,\
“agdis_address”: {\
“values”: [\
“urn:id.gov.au:agdis:address:default”,\
“urn:id.gov.au:agdis:address:residential”\
]\
},\
…\
},\
…\
}

**Figure 2 Self-asserted address sample claim request**

#### 4.5.4 Other Phone Numbers

The Other Phone Numbers scope request MUST only return the default other phone number nominated by the individual.

The Other Phone Numbers claim MAY represent one or more Other Phone Number Objects.

A request for a single other phone number MAY be returned as a single Other Phone Number object or as a JSON Array containing the object as its single entry.

A request for one or more other phone numbers MUST be returned as a JSON array of Other Phone Number Objects.

An attribute requests for multiple or a specific other phone number types can be done via the claim requests parameter using the Telephony (Table 34) or Contact Type (Table 35) URNs. An example request is illustrated in Figure 3.

{\
…,\
“userinfo”: {\
…,\
“agdis_email_address”: {\
“values”: [\
“urn:id.gov.au:agdis:contact:personal”,\
“urn:id.gov.au:agdis:contact:work”\
]\
},\
…\
},\
…\
}

**Figure 3 Self-asserted other email address sample claim request**

{\
…,\
“userinfo”: {\
…,\
“agdis_email_address”: {\
“values”: [\
“urn:id.gov.au:agdis:contact:default”,\
]\
},\
…\
},\
…\
}

**Figure 4 Self-asserted other email address scope equivalent claim request**

{\
…,\
“userinfo”: {\
…,\
“agdis_other_phone”: {\
“values”: [\
“urn:id.gov.au:agdis:contact:personal”,\
“urn:id.gov.au:agdis:contact:work”\
]\
},\
…\
},\
…\
}

**Figure 5 Self-asserted other phone number sample claim request using the contact type**

{\
…,\
“userinfo”: {\
…,\
“agdis_other_phone”: {\
“value”: “urn:id.gov.au:agdis:tel:video”,\
},\
…\
},\
…\
}

**Figure 6 Self-asserted other phone number sample claim request using telephony type**

{\
…,\
“userinfo”: {\
…,\
“agdis_other_phone”: {\
“value”: “urn:id.gov.au:agdis:tel:default”,\
},\
…\
},\
…\
}

**Figure 7 Self-asserted other phone number scope equivalent claim request**

#### 4.5.5 Place of Birth

Place of Birth MUST be a non-empty string with a maximum length of 255 characters.

#### 4.5.6 Personal Titles

A personal title MUST be a non-empty string with a maximum length of 100 characters.

### 4.6 Computed Attributes Data Definitions

Presently no Computed Attributes are defined in this Schedule.

### 4.7 Attribute Service Providers

The OpenID Connect attribute for AGDIS ASP is presented in this section.

#### 4.7.1 Business Authorisations

The Business Authorisations attribute set mapping in Table 64 below maps the field names defined in section 3.1 of this Schedule to concrete payload names with type definitions.

As the ASP providing these attributes RAM SHOULD provide guidance to PRPs consuming these attributes to support use.

**Table 64 Business Authorisation data representation**

| **Field** | **OIDC payload field name** | **Data type** | **Constraints** |
|---|---|---|---|
| Schemas | schemas | Arry of URNs | MUST contain a URN that maps to the schema version follow the format defined in Table 39 above. |
| Unique Entity Relationship ID | id | string | A unique value as a non-empty string with a format defined by RAM, and a maximum length of 256 characters. |
| Entity ID | subjectId | string | A JSON string that MUST adhere the lengths constraints of the entity type. |
| Entity Type | subjectIdType | string | A value from the enumeration defied in Table 41 above. |

| **Field** | **OIDC payload field name** | **Data type** | **Constraints** |
|---|---|---|---|
| Entity Name | subjectName | string | A non-empty string with a maximum length of 200 character. |
| Contact Details | email | Email | Only a single email address is provided. |
| Relationship Type | relationshipType | string | A non-empty string. |
| Relationship Start Time | startTimestamp | DateTime | - |
| Relationship End Time | endTimestamp | DateTime | - |
| Attributes | attributes | JSON Object | A JSON object of objects with the fields name and value.<br>The literals use for the names field, and data types for values are defined by RAM. |
| Roles | roles | Array of strings | Values defined by RAM. |
| Entitlements | permissions | Array of strings | Values defined by RAM |
| Attributes Last Updated | lastModified | DateTime | - |

#### 4.7.2 myGov

Detailed definition of the data representation for the myGov linkID is not defined in this Schedule.

An IXP or a PRP seeking further information on the format of this attribute SHOULD consult the myGov member service documentation.

### 4.8 Normative OIDC Profile Attribute Examples

#### 4.8.1 Core

Each Core Attribute example is presented on its own. In practice these values would be presented in the ID Token or UserInfo response.

**Table 65 Core Attributes normative examples for claims**

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Family Name Full Name | family_name name | Valid:<br>“family_name”: “Moore”<br>“name”: “John David Citizen”<br>Invalid<br>“family_name”: “”<br>“family_name”: &lt;string longer than 100 characters&gt;<br>“family_name”: null |
| Given Name Middle Name Preferred Name | given_name middle_name preferred_username | Valid:<br>“given_name”: “Trentino”<br>“given_name”: “”<br>Invalid:<br>“given_name”: &lt;string longer than 100 characters&gt;<br>“given_name”: null |

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Date of Birth | birthdate | Valid:<br>“birthdate”: “1970-04-01”<br>“birthdate”: “1970-04”<br>“birthdate”: “1970”<br>Invalid:<br>“birthdate”: 1970<br>“birthdate”: “70-04-01”<br>“birthdate”: “1984-30-04” |
| Updated at claims | updated_at tdif_core_updated_at | Valid:<br>“tdif_core_updated_at”: 1674539150<br>“tdif_other_names_updated_at”: 1674539150<br>Invalid:<br>“tdif_core_updated_at”: “1674539150”<br>“tdif_core_updated_at”: “2022-03-19 00:03:33.33” |

#### 4.8.2 Validated Contact Details

Note grouped examples claims are where the data types are the same. The examples provided for the group claims may be used interchangeably.

**Table 66 Validated contact details normative examples for claims**

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Validated Email | email | Valid:<br>“email”: “jane.citizen@example.com”<br>Invalid<br>“email”: null<br>“email”: “malformed.email.address” |
| Validated Phone | phone_number | Valid:<br>“given_name”: “Trentino”<br>“given_name”: “”<br>Invalid:<br>“given_name”: &lt;string longer than 100 characters&gt;<br>“given_name”: null |

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Email Verified<br>Phone Number Verified | email_verified phone_number_verified | Valid:<br>“email_verified”: true<br>“phone_number_verified”: true<br>Invalid:<br>“email_verified”: false<br>“email_verified”: “true”<br>“email_verified”: null<br>“phone_number_verified”: false<br>“phone_number_verified”: “true”<br>“phone_number_verified”: null |
| Email updated at Phone updated at | tdif_email_updated_at tdif_phone_number_updated_at | Valid:<br>“tdif_email_updated_at”: 1674539151<br>“tdif_phone_number_updated_at”: 1674539150<br>Invalid (not the claims should be interpreted interchangeably):<br>“tdif_email_updated_at”: “1674539151”<br>“tdif_phone_number_updated_at”: “1674539150”<br>“tdif_email_updated_at”: “2024-04-01T00:00.00Z”<br>“tdif_email_updated_at”: “”<br>“tdif_phone_number_updated_at”: null<br>“tdif_email_updated_at”: “2024-04-01T00:00.00Z”<br>“tdif_email_updated_at”: “2024-04-01T00:00.00Z” |

**Table 67 Validated contact details normative examples for scopes**

| **Attribute** | **OIDC Scope** | **Normative Example** |
|---|---|---|
| Validated Email | email | Each example presented here is a subset of the top-level fields in the JWT response.<br>**Valid**<br>All fields present and with legal values.<br>{<br>…<br>“email”: “jane.citizen@example.com”, “email_verified”: true, “tdif_email_updated_at”: 956386037<br>…<br>}<br>**Invalid**<br>Email verified MUST NOT be false:<br>{<br>…<br>“email”: “jane.citizen@example.com”, “email_verified”: false, “tdif_email_updated_at”: 956386037<br>…<br>}<br>The updated at field is not a Unix Timestamp. |

| **Attribute** | **OIDC Scope** | **Normative Example** |
|---|---|---|
|  |  | {<br>…<br>“email”: “jane.citizen@example.com”, “email_verified”: true, “tdif_email_updated_at”: “2024-01-01T00:00Z”<br>…<br>}<br>Missing fields:<br>{<br>…<br>“email”: “jane.citizen@example.com”, “email_verified”: true,<br>…<br>} |
| Validated Phone | phone | **Valid**<br>All fields present and have legal values.<br>{<br>…<br>“phone_number”: “jane.citizen@example.com”, “phone_number_verified”: True, “tdif_email_updated_at”: 956386037 |

| **Attribute** | **OIDC Scope** | **Normative Example** |
|---|---|---|
|  |  | …<br>}<br>**Invalid**<br>Phone number verified MUST NOT be false:<br>{<br>…<br>“phone_number”: “jane.citizen@example.com”, “phone_number_verified”: false, “tdif_email_updated_at”: 956386037<br>…<br>}<br>The updated at field is not a Unix Timestamp.<br>{<br>…<br>“phone_number”: “jane.citizen@example.com”, “phone_number_verified”: true, “tdif_phone_numner_updated_at”: “2024-01-01T00:00Z”<br>…<br>}<br>Missing fields (e.g., the last updated field): |

| **Attribute** | **OIDC Scope** | **Normative Example** |
|---|---|---|
|  |  | {<br>…<br>“phone_number”: “jane.citizen@example.com”, “phone_number_verified”: true,<br>…<br>} |

#### 4.8.3 Verified Other Names

**Table 68 Verified other names normative examples for claims**

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Verified Other Names | tdif_other_names | **Valid**<br>Single Other Verified Name available (no array):<br>“tdif_other_names”: { “family_name”: “Moore”, “given_name”: “Trentino”<br>}<br>**Valid**<br>Single Other Verified Name available in an array:<br>“tdif_other_names”: [<br>{“family_name”: “Moore”, “given_name”: “Trentino” }<br>] |

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
|  |  | **Valid:**<br>Multiple Other Verified Name available:<br>“tdif_other_names”: {<br>{“family_name”: “Moore”, “given_name”: “Trentino”},<br>{“family_name”: Moore”, “given_name”: “Trentino Vino”}<br>}<br>Multiple Other Verified Name available:<br>“tdif_other_names”: [{ “family_name”: “Vass”, “middle_name”: “Steven”, “given_name”: “Ahgan”<br>}, {<br>“family_name”: “Vass”, “given_name”: “Ahgan”<br>}] |

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
|  |  | **Invalid**<br>Family MUST NOT be an empty value:<br>“tdif_other_names”: [{<br>“family_name”: “”, “given_name”: “Ahgan”<br>}]<br>**Invalid**<br>null values are not permitted:<br>“tdif_other_names”: [{<br>“family_name”: “Vass”, “given_name”: null<br>}] |

#### 4.8.4 Verified Documents

#### 4.8.4.1 Birth Certificate

**Table 69 Birth certificate verified document claim normative example**

<table>
<tr>
<td><b>Field</b></td>
<td><b>Sub-field(s)</b></td>
<td><b>Required</b></td>
<td><b>Example</b></td>
</tr>
<tr>
<td>type_code</td>
<td></td>
<td>Y</td>
<td rowspan="9">{<br>"type_code": "urn:id.gov.au:tdif:doc:type_code:BC", "verification_method": "S",<br>"verification_date": "2022-12-06T23:21:19.0231031Z", "names": {<br>"family_name": "Maximus", "given_name": "Michael"<br>},<br>"birthdate": "1989-01-03",</td>
</tr>
<tr>
<td>verification_method</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>verification_date</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>names2</td>
<td>family_name</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>given_name</td>
<td>Y</td>
</tr>
<tr>
<td>birthdate</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>identifiers3</td>
<td>Registration Number</td>
<td>N</td>
</tr>
<tr>
<td></td>
<td>Certificate Number</td>
<td>N</td>
</tr>
<tr>
<td>attributes</td>
<td>Registration Date</td>
<td>N</td>
</tr>
</table>

[image]

2 On birth certificates issued by the NSW, VIC, WA BDM, given name may be left blank if family name has a value, and family name may be left blank if given name has a value.

3 The identifiers used for birth certificates will vary significantly depending on the state and territory which issued the birth certificate.

<table>
<tr>
<td></td>
<td>Registration State</td>
<td>Y</td>
<td rowspan="3">"identifiers": [<br>{<br>"type": "Registration Number", "value": "1234567890"<br>}<br>],<br>"attributes": [<br>{<br>"type": "Registration State", "value": "ACT"<br>}<br>]<br>}</td>
</tr>
<tr>
<td></td>
<td>Registration Year</td>
<td>N</td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
</table>

#### 4.8.4.2 Centrelink Concession Card

**Table 70 Centrelink concession card verified document claim normative example**

<table>
<tr>
<td><b>Field</b></td>
<td><b>Sub-field(s)</b></td>
<td><b>Required</b></td>
<td><b>Example</b></td>
</tr>
<tr>
<td>type_code</td>
<td></td>
<td>Y</td>
<td rowspan="9">{<br>"type_code": "urn:id.gov.au:tdif:doc:type_code:CO", "verification_method": "S",<br>"verification_date": "2022-12-06T23:21:19.0231031Z", "names": {<br>"name": "Jane Citizen"<br>},<br>"birthdate": "1976-02-15", "identifiers": [<br>{<br>"type": "CRN", "value": "1234567890"</td>
</tr>
<tr>
<td>verification_method</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>verification_date</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>names</td>
<td>name</td>
<td>Y</td>
</tr>
<tr>
<td>birthdate</td>
<td></td>
<td>N</td>
</tr>
<tr>
<td>identifiers</td>
<td>CRN</td>
<td>Y</td>
</tr>
<tr>
<td>attributes</td>
<td>CardExpiry</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>CardType</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</table>

|  |  |  | }<br>],<br>"attributes": [<br>{<br>"type": "CardExpiry ", "value": "2024-03"<br>}, {<br>“type”: “CardType”,<br>“value”: ”PCH”,<br>}<br>]<br>} |
|---|---|---|---|

#### 4.8.4.3 Change of Name Certificate

Please see footnotes 2 and 3 in Table 69 to clarify name handling.

**Table 71 Change of Name Certificate verified document claim normative example**

<table>
<tr>
<td><b>Field</b></td>
<td><b>Sub-field(s)</b></td>
<td><b>Required</b></td>
<td><b>Example</b></td>
</tr>
<tr>
<td>type_code</td>
<td></td>
<td>Y</td>
<td rowspan="10">{<br>"type_code": "urn:id.gov.au:tdif:doc:type_code:NC", "verification_method": "S",<br>"verification_date": "2022-12-07T00:52:48.2Z", "names": {<br>"family_name": "Southsoil", "given_name": "Jakub"<br>},<br>"birthdate": "1992-12-07", "identifiers": [</td>
</tr>
<tr>
<td>verification_method</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>verification_date</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>names4</td>
<td>family_name</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>given_name</td>
<td>Y</td>
</tr>
<tr>
<td>birthdate</td>
<td></td>
<td>N</td>
</tr>
<tr>
<td>identifiers</td>
<td>Registration Number</td>
<td>N</td>
</tr>
<tr>
<td></td>
<td>Certificate Number</td>
<td>N</td>
</tr>
<tr>
<td>attributes</td>
<td>Registration Date</td>
<td>N</td>
</tr>
<tr>
<td></td>
<td>Registration State</td>
<td>Y</td>
</tr>
</table>

[image]

4 For Change of Name Certificates issued by the NSW, VIC or WA BDM, given name may be left blank if family name has a value, and family name may be left blank if given name has a value.

<table>
<tr>
<td></td>
<td>Registration Year</td>
<td>N</td>
<td rowspan="2">{<br>"type": "Registration Number", "value": "1563160"<br>}<br>],<br>attributes": [<br>{<br>"type": "Registration State", "value": "ACT"<br>}<br>]<br>}</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</table>

#### 4.8.4.4 Citizenship Certificate

**Table 72 Citizenship Certificate verified document claim normative example**

<table>
<tr>
<td><b>Field</b></td>
<td><b>Sub-field(s)</b></td>
<td><b>Required</b></td>
<td><b>Example</b></td>
</tr>
<tr>
<td>type_code</td>
<td></td>
<td>Y</td>
<td rowspan="9">{<br>"type_code": "urn:id.gov.au:tdif:doc:type_code:CC", "verification_method": "S",<br>"verification_date": "2022-12-06T23:22:01.6116772Z", "names": {<br>"family_name": "Doe", "given_name": "John"<br>},<br>"birthdate": "1986-04-18", "identifiers": [<br>{</td>
</tr>
<tr>
<td>verification_method</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>verification_date</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>names</td>
<td>family_name</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>given_name</td>
<td>N</td>
</tr>
<tr>
<td>birthdate</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>identifiers</td>
<td>Stock Number</td>
<td>Y</td>
</tr>
<tr>
<td>attributes5</td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
</table>

[image]

5 Please note that the Acquisition Date field, while requested input for the DVS, is not checked nor is it currently available on the AGDIS.

|  | "type": "Stock Number",<br>"value": "ACC1000112"<br>}<br>],<br>"attributes": [],<br>} |
|---|---|

#### 4.8.4.5 Registration by Descent Certificate

**Table 73 Registration by Descent Certificate verified document normative example**

<table>
<tr>
<td><b>Field</b></td>
<td><b>Sub-field(s)</b></td>
<td><b>Required</b></td>
<td><b>Example</b></td>
</tr>
<tr>
<td>type_code</td>
<td></td>
<td>Y</td>
<td rowspan="9">{<br>"type_code": "urn:id.gov.au:tdif:doc:type_code:RD", "verification_method": "S",<br>"verification_date": "2022-12-06T23:22:01.6116772Z", "names": {<br>"family_name": "Citizen", "given_name": "Birdy"<br>},<br>"birthdate": "1986-04-18", "identifiers": [<br>{</td>
</tr>
<tr>
<td>verification_method</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>verification_date</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>names</td>
<td>family_name</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>given_name</td>
<td>N</td>
</tr>
<tr>
<td>birthdate</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>identifiers</td>
<td>Stock Number</td>
<td>Y</td>
</tr>
<tr>
<td>attributes6</td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
</table>

[image]

6 Please note that the Acquisition Date field, while supported by requested input for the DVS, is not checked nor is it currently available on the AGDIS

|  | "type": "Stock Number",<br>"value": "ACC1000342"<br>}<br>],<br>"attributes": [<br>{<br>“type”: “Acquisition Date”,<br>“value”: “2013-04-20”<br>}<br>],<br>} |
|---|---|

#### 4.8.4.6 Australian Driver Licence

**Table 74 Australian Driver Licence verified document normative example**

<table>
<tr>
<td><b>Field</b></td>
<td><b>Sub-field(s)</b></td>
<td><b>Required</b></td>
<td><b>Example</b></td>
</tr>
<tr>
<td>type_code</td>
<td></td>
<td>Y</td>
<td rowspan="10">{<br>"type_code": "urn:id.gov.au:tdif:doc:type_code:DL", "verification_method": "S",<br>"verification_date": "2022-12-06T23:22:01.6116772Z", "names": {<br>"family_name": "Bisan", "given_name": "Wizard"<br>},<br>"birthdate": "1986-04-18",</td>
</tr>
<tr>
<td>verification_method</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>verification_date</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>names</td>
<td>family_name</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>given_name</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>middle_name</td>
<td>N</td>
</tr>
<tr>
<td>birthdate</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>identifiers</td>
<td>Licence Number</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>Card Number7</td>
<td>N</td>
</tr>
<tr>
<td>attributes</td>
<td>State of Issue</td>
<td>Y</td>
</tr>
</table>

[image]

7 If Card Number is recorded by an ISP, it is expected to be passed as part of a Driver Licence. Refer to DVS Match Specification Driver Licence for details of Driver Licence Card Number across jurisdictions.

|  | "identifiers": [<br>{<br>"type": "Licence Number",<br>"value": "65493621"<br>}<br>],<br>"attributes": [<br>{<br>“type”: “State of Issue”,<br>“value”: “QLD”<br>}<br>]<br>**}** |
|---|---|

#### 4.8.4.7 ImmiCard

**Table 75 ImmiCard verified document normative example**

<table>
<tr>
<td><b>Field</b></td>
<td><b>Sub-field(s)</b></td>
<td><b>Required</b></td>
<td><b>Example</b></td>
</tr>
<tr>
<td>type_code</td>
<td></td>
<td>Y</td>
<td rowspan="8">{<br>"type_code": "urn:id.gov.au:tdif:doc:type_code:IM", "verification_method": "S",<br>"verification_date": "2022-12-06T23:22:01.6116772Z", "names": {<br>"family_name": "Moore", "given_name": "Trentino Bici"</td>
</tr>
<tr>
<td>verification_method</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>verification_date</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>names</td>
<td>family_name</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>given_name</td>
<td>Y</td>
</tr>
<tr>
<td>birthdate</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>identifiers</td>
<td>ImmiCard Number</td>
<td>Y</td>
</tr>
<tr>
<td>attributes</td>
<td><i>empty</i></td>
<td>Y</td>
</tr>
</table>

|  | },<br>"birthdate": "1986-04-18",<br>"identifiers": [<br>{<br>"type": "ImmiCard Number",<br>"value": "PRE123456"<br>}<br>],<br>"attributes": []<br>} |
|---|---|

#### 4.8.4.8 Marriage Certificate

**Table 76 Marriage Certificate verified document normative example**

<table>
<tr>
<td><b>Field</b></td>
<td><b>Sub-field(s)</b></td>
<td><b>Required</b></td>
<td><b>Example</b></td>
</tr>
<tr>
<td>type_code</td>
<td></td>
<td>Y</td>
<td rowspan="12">{<br>"type_code": "urn:id.gov.au:tdif:doc:type_code:MC", "verification_method": "S",<br>"verification_date": "2022-12-06T23:21:19.0231031Z", "names": {<br>"family_name": "O’Keeffe", "given_name": "Mickey", "family_name2": "Louis", "given_name2": "Jesse"<br>},<br>"birthdate": "1989-01-03", "identifiers": [</td>
</tr>
<tr>
<td>verification_method</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>verification_date</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>names</td>
<td>family_name</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>given_name</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>family_name2</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>given_name2</td>
<td>Y</td>
</tr>
<tr>
<td>birthdate</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>identifiers</td>
<td>Registration Number</td>
<td>N</td>
</tr>
<tr>
<td></td>
<td>Certificate Number</td>
<td>N</td>
</tr>
<tr>
<td>attributes</td>
<td>Registration Date</td>
<td>N</td>
</tr>
<tr>
<td></td>
<td>Registration State</td>
<td>Y</td>
</tr>
</table>

<table>
<tr>
<td></td>
<td>Registration Year</td>
<td>N</td>
<td rowspan="2">{<br>"type": "Registration Number", "value": "1234567890"<br>}<br>],<br>"attributes": [<br>{<br>"type": "Registration State", "value": "ACT"<br>}<br>]<br>}</td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
</table>

#### 4.8.4.9 Medicare Card

**Table 77 Medicare Card verified documents normative example**

<table>
<tr>
<td><b>Field</b></td>
<td><b>Sub-field(s)</b></td>
<td><b>Required</b></td>
<td><b>Example</b></td>
</tr>
<tr>
<td>type_code</td>
<td></td>
<td>Y</td>
<td rowspan="12">{<br>"type_code": "urn:id.gov.au:tdif:doc:type_code:MD",<br>"verification_method": "S",<br>"verification_date": "2022-12-06T23:21:19.0231031Z",<br>"birthdate": "1989-01-03",<br>"identifiers": [<br>{<br>"type": "Card Number",<br>"value": "1234567890"<br>},<br>{<br>"type": "Individual Ref Number",</td>
</tr>
<tr>
<td>verification_method</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>verification_date</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>birthdate</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>identifiers</td>
<td>Card Number</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>Individual Ref Number</td>
<td>Y</td>
</tr>
<tr>
<td>attributes</td>
<td>Card Type</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>Card Expiry</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>Full Name 1</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>Full Name 2</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>Full Name 3</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>Full Name 4</td>
<td>Y</td>
</tr>
</table>

|  | "value": "1"<br>},<br>],<br>"attributes": [<br>{<br>"type": "Card Type",<br>"value": "G"<br>},<br>{<br>"type": "Card Expiry",<br>"value": "2022-12"<br>},<br>{<br>"type": "Full Name 1",<br>"value": "Lachlan Murramarang"<br>},<br>{ |
|---|---|

|  | "type": "Full Name 2",<br>"value": null<br>},<br>{<br>"type": "Full Name 3",<br>"value": null<br>},<br>{<br>"type": "Full Name 4",<br>"value": null<br>},<br>]<br>} |
|---|---|

#### 4.8.4.10 Australian Travel Document

**Table 78 Australian Travel Document verified document normative example**

<table>
<tr>
<td><b>Field</b></td>
<td><b>Sub-field(s)</b></td>
<td><b>Required</b></td>
<td><b>Example</b></td>
</tr>
<tr>
<td>type_code</td>
<td></td>
<td>Y</td>
<td rowspan="9">{<br>"type_code": "urn:id.gov.au:tdif:doc:type_code:PP",<br>"verification_method": "S",<br>"verification_date": "2022-12-06T23:22:01.6116772Z",<br>"names": {<br>"family_name": "Mason",<br>"given_name": "Master"<br>},<br>"birthdate": "1930-04-18",<br>"identifiers": [<br>{<br>"type": "Travel Document Number",<br>"value": "PA0002020"<br>}<br>],<br>"attributes": [<br>{<br>“type”: “Gender”,<br>“value”: “F”<br>}<br>]<br>}</td>
</tr>
<tr>
<td>verification_method</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>verification_date</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>names</td>
<td>family_name</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>given_name</td>
<td>N</td>
</tr>
<tr>
<td>birthdate</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>identifiers</td>
<td>Travel Document Number</td>
<td>Y</td>
</tr>
<tr>
<td>attributes</td>
<td>Gender</td>
<td>N</td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
</table>

#### 4.8.4.11 Visa

**Table 79 Visa verified documents normative example**

<table>
<tr>
<td><b>Field</b></td>
<td><b>Sub-field(s)</b></td>
<td><b>Required</b></td>
<td><b>Example</b></td>
</tr>
<tr>
<td>type_code</td>
<td></td>
<td>Y</td>
<td rowspan="9">{<br>"type_code": "urn:id.gov.au:tdif:doc:type_code:VI", "verification_method": "S",<br>"verification_date": "2022-12-06T23:22:01.6116772Z", "names": {<br>"family_name": "Vino", "given_name": "Trentino"<br>},<br>"birthdate": "1962-08-10", "identifiers": [<br>{<br>"type": "Passport Number",</td>
</tr>
<tr>
<td>verification_method</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>verification_date</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>names</td>
<td>family_name</td>
<td>Y</td>
</tr>
<tr>
<td></td>
<td>given_name</td>
<td>Y</td>
</tr>
<tr>
<td>birthdate</td>
<td></td>
<td>Y</td>
</tr>
<tr>
<td>identifiers</td>
<td>Passport Number</td>
<td>Y</td>
</tr>
<tr>
<td>attributes</td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
</table>

|  | "value": "NN123456"<br>}<br>],<br>"attributes": []<br>} |
|---|---|

#### 4.8.5 Identity System Metadata

#### 4.8.5.1 Digital ID Pairwise Identifier

**Table 80 Digital ID pairwise examples**

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Digital ID Pairwise Identifier | sub | Valid:<br>“sub”: “234932875989812”<br>“sub”: &lt;a string up to 255 characters in length&gt;<br>Invalid:<br>“sub”: &lt;a string longer than 255 characters&gt;<br>“sub”: null<br>“sub”: 123145124 |

#### 4.8.5.2 Authentication Time and Updated At

**Table 81 Authentication time and Update at examples**

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Authentication Time Last Updated | auth_time updated_at | Valid:<br>“auth_time”: 1711929600<br>“updated_at”: 1585699200<br>Invalid:<br>“auth_time”: “1711929600”<br>“updated_at”: “20240401T00:00Z” |

#### 4.8.5.3 Authentication Method

**Table 82 Authentication Method examples**

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Authentication Method Reference | amr | Valid:<br>“amr”: [“urn:id.gov.au:idp:myid”]<br>Invalid:<br>“amr”: “urn:id.gov.au:idp:myid” |

#### 4.8.5.4 Audit Identifiers

**Table 83 Audit Identifier examples**

| **Attribute** | **OIDC Claim** | **Informative Example** |
|---|---|---|
| RP Audit ID | tdif_audit_id | Valid:<br>“tdif_audit_id”: “702b45ce-d2d6-451d-84cd-9fbcf299533b”<br>Invalid:<br>“tdif_audit_id”: 4093809<br>“tdif_audit_id”: “”<br>“tdif_audit_id”: null |

#### 4.8.6 Self-Asserted Attributes

#### 4.8.6.1 Addresses

**Table 84 Addresses normative examples**

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Addresses | agdis_address | Valid all fields:<br>{<br>“address_type”: “urn:id.gov.au:agdis:address:postal”, “street_address”: “1 Canberra Ave”,<br>“locality”: “Forrest”, “region”: “ACT”,<br>“post_code”: “2603”, “country”: “Australia”,<br>“formatted”: “1 Canberra Ave\\nForrest ACT 2603\\nAustralia”, “validated”: false<br>}<br>Valid only required fields:<br>{<br>“address_type”: “urn:id.gov.au:agdis:address:postal”, “street_address”: “1 Canberra Ave”,<br>“locality”: “Forrest”, “region”: “ACT”,<br>“post_code”: “2603”, “validated”: false<br>} |

#### 4.8.6.2 Other Email Addresses

**Table 85 Other Email Addresses**

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Other Email Addresses | agdis_other_email | Valid:<br>{<br>“email”: “jane.cizten@exmaplebusiness.com.au”, “email_validated”: false,<br>“contact_type”: “urn:id.gov.au:agdis:contact:business”<br>}<br>{<br>“email”: “jane.cizten@exmaple.com.au”, “email_validated”: true,<br>“contact_type”: “urn:id.gov.au:agdis:contact:other”<br>}<br>Invalid:<br>{<br>“email”: “not-a-valid-email”, “email_validated”: true,<br>“contact_type”: “urn:id.gov.au:agdis:contact:other”<br>} |

#### 4.8.6.3 Other Phone Numbers

**Table 86 Other Phone Numbers normative examples**

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Other Phone Numbers | agdis_other_phone_numbers | Valid individual claims:<br>{<br>“other_phone”: “+83 (4) 555 2401”, “other_phone validated”: false, “telephony type”: mobile,<br>“contact_type”: “urn:id.gov.au:agdis:contact:personal”<br>}<br>Invalid:<br>{<br>“other_phone”: “not a valid number”, “other_phone validated”: false, “telephony type”: mobile,<br>“contact_type”: “urn:id.gov.au:agdis:contact:personal<br>} |

**Table 87 Birthplace Normative Examples**

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Birthplace | agdis_birth_place | Valid:<br>“agdis_birth_place”: “Ngunnawal Country”<br>“agdis_birth_place”: &lt;a non-empty string up to 100 characters in length&gt;<br>Invalid:<br>“agdis_birth_place”: “”<br>“agdis_birth_place”: null<br>“agdis_birth_place”: &lt;a string over100 characters in length&gt; |

#### 4.8.6.4 Personal Title Normative Examples

**Table 88 Personal Titles Normative Examples**

| **Attribute** | **OIDC Claim** | **Normative Example** |
|---|---|---|
| Personal Title | agdis_personal_title | Valid:<br>“agdis_personal_title”: “Professor”<br>“agdis_personal_title”: &lt;a non-empty string up to 100 characters in length&gt;<br>Invalid:<br>“agdis_personal_title”: “”<br>“agdis_personal_title”: null<br>“agdis_personal_title”: &lt;a string over100 characters in length&gt; |

#### 4.8.7 Business Authorisations

**Table 89 Business Authorisations**

| **Attribute** | **OIDC Scope and Claim** | **Normative Example** |
|---|---|---|
| Business Authorisations | tdif_business_authorisations | {<br>"schemas": [<br>"urn:id.gov.au:tdif:authorisations:business:1.0"<br>],<br>"id": "78dfcb8c-dbb7-4c36-9807-70125dca90ca", "subjectId": "49090058647",<br>"subjectIdType": "ABN", "subjectName": "ALTONWAY LTD", "relationshipType":"ASSOCIATE",<br>"startTimestamp":"2019-08-09T14:00:00Z", "endTimestamp":null,<br>"attributes":[<br>{"name":"pid","value":"668"},<br>{"name":"subId","value":"ABRP:49090058647_668"},<br>{"name":"previousPid","value":null},<br>{"name":"previousSubId","value":null}<br>],<br>"permissions":[ "QLD_IDENTITY_LOGIN/FULL"<br>],<br>"roles":[<br>"AUTHORISATION_ADMINISTRATOR", "MACHINE_CREDENTIAL_ADMINISTRATOR", "PRINCIPAL_AUTHORITY"<br>],<br>"email": "IndustryRDTI1@test.gov.au", "lastModified": "2021-01-04T00:20:14.2453821Z"<br>} |
