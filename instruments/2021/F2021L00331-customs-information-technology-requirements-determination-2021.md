---
title: Customs (Information Technology Requirements) Determination 2021
identifier: F2021L00331
register_id: F2025C00717
type: legislative_instrument
number: LIN 21/028
jurisdiction: au
language: en
date: "2021-03-23"
compilation_number: 4
last_amended: "2025-07-01"
version_start: "2025-07-01"
status: in_force
source: "https://www.legislation.gov.au/F2021L00331/latest/text"
retrieved: "2026-10-11"
---

# Customs (Information Technology Requirements) Determination 2021

made under section 126DA of the

Customs Act 1901

**Compilation No. 4**

**Compilation date:** 1 July 2025

**Includes amendments:** F2025L00744

**About this compilation**

**This compilation**

This is a compilation of the *Customs (Information Technology Requirements) Determination 2021* that shows the text of the law as amended and in force on 1/7/2025 (the ***compilation date***).

The notes at the end of this compilation (the ***endnotes***) include information about amending laws and the amendment history of provisions of the compiled law.

**Uncommenced amendments**

The effect of uncommenced amendments is not shown in the text of the compiled law. Any uncommenced amendments affecting the law are accessible on the Register (www.legislation.gov.au). The details of amendments made up to, but not commenced at, the compilation date are underlined in the endnotes. For more information on any uncommenced amendments, see the Register for the compiled law.

**Application, saving and transitional provisions for provisions and amendments**

If the operation of a provision or amendment of the compiled law is affected by an application, saving or transitional provision that is not included in this compilation, details are included in the endnotes.

**Modifications**

If the compiled law is modified by another law, the compiled law operates as modified but the modification does not amend the text of the law. Accordingly, this compilation does not show the text of the compiled law as modified. For more information on any modifications, see the Register for the compiled law.

**Self‑repealing provisions**

If a provision of the compiled law has been repealed in accordance with a provision of the law, details are included in the endnotes.

Contents

### Part 1—Preliminary

###### 1 Name

This instrument is the *Customs (Information Technology Requirements) Determination 2021*.

###### 3 Authority

This instrument is made under section 126DA of the *Customs Act 1901*.

###### 4 Definitions

Note: A number of expressions used in this instrument are defined in subsection 4(1) of the *Customs Act 1901*, including the following:

(a) customs broker

(b) duty;

(c) goods;

(d) importer;

(e) nominee;

(f) self-assessed clearance declaration;

(g) specified low value goods.

In this instrument:

***ABN*** has the same meaning as in the *A New Tax System (Australian Business Number) Act 1999*.

***Act*** means the *Customs Act 1901*.

***API*** means Application Programming Interface, which acts as an intermediary that enables software applications to communicate with a server to access data and functions.

***ATT Portal*** means the Australian Trusted Trader Portal, which is the website operated by the Department to receive nominations by entities to join the Australian Trusted Trader Programme.

***Australia Travel Declaration*** has the meaning given by section 4 of the Customs Regulation.

***Claim for the Return of Seized Goods web form*** means the website operated by the Department to process electronic applications for the return of seized goods.

***Collector*** has the meaning given by section 8 of the Act.

***Customs Regulation*** means the *Customs Regulation 2015*.

***Department*** means the Department of Home Affairs.

***EDI*** means Electronic Data Interchange.

***Endpoint*** means a digital location where an Application Programming Interface (API) receives API calls, also known as API requests, for resources on its server.

***Home Affairs Access Manager*** means the website that is used to manage access and permissions for external organisations to Departmental systems at https://am.homeaffairs.gov.au.

***HTTPS*** means Hypertext Transfer Protocol Secure.

***ICS*** means Integrated Cargo System.

***MQ*** means the secure message delivery platform known as IBM MQ.

***S/MIME*** means Secure/Multipurpose Internet Mail Extensions.

***SMTP*** means Simple Mail Transfer Protocol.

***Subdivision AA goods*** has the meaning given by section 71AAAA of the Act.

***UN/EDIFACT*** means the international standard, known as Electronic Data Interchange for Administration, Commerce and Transport, administered by the United Nations.

### Part 2—Information technology requirements for specified communications

###### 6 Communicating import declaration for goods imported through the post

(1) Subsection (2) applies if:

(a) a person has personal property in goods:

(i) to which section 68 of the Act applies; and

(ii) that are intended to be entered for home consumption; and

(iii) that are imported into Australia through the post; and

(b) the person wishes to communicate with the Department electronically; and

(c) the communication is an import declaration under 71A of the Act for the goods, in an approved statement in accordance with section 71L of the Act.

(2) The communication may be by a SMTP email addressed to a nominated Department email address dedicated to the receipt of such messages.

###### 7 Communicating application to move, alter or interfere with certain goods

(1) Subsection (2) applies if:

(a) a person wishes to communicate with the Department electronically; and

(b) the communication is an application under section 119AA or 119AB of the Act, in an approved statement, for permission to move, alter or interfere with goods in a particular way.

(2) The communication must be by a SMTP email addressed to a nominated Department email address dedicated to the receipt of such messages.

###### 8 Communicating nomination to participate in Australian Trusted Trader Programme

(1) Subsection (2) applies if a person wishes to electronically make a nomination to participate in the Australian Trusted Trader Programme under section 176B of the Act.

(2) The nomination must be made using the website, known as the ATT Portal, administered by the Department.

###### 8A Submitting an Australia Travel Declaration

(1) Subsection (2) applies if:

(a) a person wishes to submit to the Department an Australia Travel Declaration in respect of the importation of the person’s Subdivision AA goods that includes the information specified in subsection 27(2) of the Customs Regulation about the goods; and

(b) the person causes the completed Australia Travel Declaration to be submitted to the Department, including for the purposes of sections 71 and 71AAAB of the Act.

Note 1: Subsection 27(2) of the Customs Regulation sets out the specified information that is sought for the purposes of sections 71 and 71AAAB of the Customs Act.

Note 2: Section 71 of the Act empowers a Collector to decide whether to grant or refuse giving an authority to deal with goods.

Note 3: Section 71AAAB of the Act empowers a Collector to, upon considering information that the Collector must have regard to, decide whether to authorise or refuse to authorise the delivery of Subdivision AA goods into home consumption.

(2) The submission of an Australia Travel Declaration must be:

(a) a message using HTTPS that is capable of being received by the departmental system that processes the Australia Travel Declaration; or

(b) made using the web form known as the Australia Travel Declaration administered by the Department for that purpose.

(3) The person causing an Australia Travel Declaration to be submitted to the Department under subsection (2) must sign the Australia Travel Declaration by inserting the person’s full name as text.

###### 8B Claim for return of goods seized under section 205B of the Customs Act

(1) Subsection (2) applies if a person wishes to electronically make a claim for the return of goods seized under section 205B(2A) of the Act.

(2) The claim must be made using the web form, known as the Claim for the Return of Seized Goods web form, administered by the Department.

###### 9 Signature

(1) This section applies if:

(a) a person, including a person acting on behalf of an organisation, communicates electronically with the Department using an SMTP email; and

(b) the person is required to provide the person’s signature; and

(c) the communication contains:

(i) an import declaration made under section 71A of the Act; or

(ii) an application for permission to move, alter or interfere with goods for export made under section 119AA of the Act; or

(iii) an application for permission to move, alter or interfere with goods that are no longer for export made under section 119AB of the Act.

(2) The person must place the person’s full name in the SMTP email.

(3) If the communication is made on behalf of an organisation that has an ABN, the SMTP email must include the name and ABN of the organisation.

### Part 2A–Information Technology Requirements for the Self-Assessed Clearance Declaration Pilot

###### 9A Simplified Outline–Self-Assessed Clearance Declaration Pilot

The Self-Assessed Clearance Declaration Pilot is a time-limited trial of novel information technology systems.

Pilot participants will lodge self-assessed clearance declarations through the Trade Portal. Pilot participants must register with the Home Affairs Access Manager and also be registered in the ICS. In order to use the Trade Portal and Home Affairs Access Manager, individuals communicating with the Department on behalf of pilot participants must authenticate their identity using myID and be linked to an ABN in RAM, in accordance with the Trusted Digital Identity Framework.

###### 9B Interpretation

In this Part, unless the contrary intention appears:

***ABF Trade Portal*** means the interactive portal for online services available through the Department’s website at https://trade.abf.gov.au.

***pilot participant*** is an importer, customs broker, nominee or other person or entity who has joined the Self-Assessed Clearance Declaration Pilot.

***RAM*** means the Australian Taxation Office Relationship Authorisation Manager.

***Self-Assessed Clearance Declaration Pilot*** means the pilot of electronic lodgement of self-assessed clearance declarations described in section 9A.

###### 9C Communicating a short-form self-assessed clearance declaration for the purposes of the Self-Assessed Clearance Declaration Pilot

The information technology requirements in this Part apply if a pilot participant who is the owner of specified low value goods, or is acting on behalf of the owner of specified low value goods, wishes to communicate with the Department to lodge a short-form self-assessed clearance declaration for the purposes of section 71AAAF of the Act.

###### 9D Requirements for electronic communications for the purposes of the Self-Assessed Clearance Declaration Pilot

A pilot participant communicating electronically with the Department for the purposes of the Self-Assessed Clearance Declaration Pilot must:

(a) communicate via the ABF Trade Portal; and

(b) be registered in Home Affairs Access Manager and ICS.

###### 9E Authentication to ABF Trade Portal

A pilot participant using the ABF Trade Portal for the purposes of the Self-Assessed Clearance Declaration Pilot must:

(a) establish their Digital Identity inmyID; and

(b) link their myID with the ABN of the pilot participant in RAM in accordance with the Trusted Digital Identity Framework.

Note: The Trusted Digital Identity Framework is available on the Digital ID website https://www.digitalidentity.gov.au/.

### Part 3—Information technology requirements for general communications

###### 10 Communications generally

(1) The information technology requirements in this Part apply to a person who:

(a) is required or permitted to make a communication with the Department under:

(i) Division 3 or 4 of Part IV of the Act; or

(ii) Division 2 of Part VI of the Act; or

(iii) Section 163 of the Act; or

(iv) Part IX of the Act; and

(b) wishes to communicate with the Department electronically.

(2) However, the information technology requirements in this Part do not apply to a person who wishes to communicate electronically with the Department in the circumstances mentioned in Part 2.

###### 11 General requirements for electronic communications

(1) A person who communicates electronically with the Department must communicate by:

(a) an EDI message attached to an S/MIME SMTP email to an email address specified by the Department; or

(b) an EDI message delivered by MQ over an MQ channel preconfigured by agreement with the Department; or

(c) the Cargo Interactive Facility using HTTPS to a Departmental website using a version of an internet browser that is supported by the Department for such transactions; or

(d) an API to a nominated Departmental Endpoint.

(2) For the purposes of subparagraphs 11(1)(a)-(c), a person who communicates electronically with the department must:

(a) be registered in:

(i) the Common Connect Facility; and

(ii) the ICS; and

(b) communicate with the Department using Public Key Infrastructure (PKI) in accordance with the Commonwealth’s Gatekeeper® strategy administered by the Digital Transformation Agency; and

(c) configure the person’s email software with the appropriate digital certificate to be able to decrypt encrypted emails sent to the person by the Department.

Note: The Commonwealth Gatekeeper® strategy could in 2025 be viewed on the Australian Government Digital Transformation Agency’s website (https://www.dta.gov.au).

(3) For the purposes of subparagraph 11(1)(d), a person who communicates electronically with the Department by an API to a Departmental endpoint must:

(a) be registered in Home Affairs Access Manager; and

(b) use an authenticated and authorised digital machine certificate linked to the organisation’s ABN.

###### 12 Standards and specifications for EDI messages

A person who communicates electronically with the Department by an EDI message attached to an S/MIME SMTP email or delivered by MQ must comply with the UN/EDIFACT D99B standards, in accordance with the ICS Message Implementation Guidelines of the ICS Software Developers Guide, as in force at the commencement of this Determination and published on the Department’s website.

Note: The ICS Message Implementations Guidelines of the ICS Software Developers Guide could in 2021 be viewed on the Department’s website (www.homeaffairs.gov.au)

###### 12A Standards and Specifications for APIs

A person who communicates electronically with the Department by an API must comply with the API specifications outlined in the API Developer Portal Guidelines.

Note: The Department’s API Developer Portal Guidelines could in 2025 be viewed on the Australian Government Department of Home Affairs website (https://homeaffairs.gov.au).

###### 13 Information technology requirements for signature

(1) The information technology requirements in this section and section 15 apply to a person who is required to sign an electronic communication with the Department under:

(a) Division 3 or 4 of Part IV of the Act; or

(b) Division 2 of Part VI of the Act; or

(c) Section 163 of the Act; or

(d) Part IX of the Act.

(2) A communication by an EDI message attached to an S/MIME SMTP email or delivered by MQ must be digitally signed and encrypted using PKI in accordance with the Commonwealth’s Gatekeeper® strategy.

(3) A communication by an API must be digitally authenticated with a machine credential that is registered in Home Affairs Access Manager in accordance with the Commonwealth’s Gatekeeper® Strategy.

###### 14 Authentication to the Cargo Interactive Facility

(1) A person using the Cargo Interactive Facility must authenticate the communication using a digital certificate issued in accordance with the Commonwealth’s Gatekeeper® strategy.

(2) A communication using the Cargo Interactive Facility must be digitally authenticated and encrypted using PKI in accordance with the Commonwealth’s Gatekeeper® strategy.

###### 14A Authentication to Home Affairs Access Manager

A person using Home Affairs Access Manager for the purposes of communicating with the Department via an API must:

(a) establish their Digital Identity in myID; and

(b) link their myID with the ABN of the organisation in accordance with the Trusted Digital Identity Framework.

Note: The Trusted Digital Identity Framework could in 2025 be viewed on the Digital ID website (https://www.digitalidentity.gov.au/).

###### 15 Digital signature and certificate

(1) The person must use the digital signature and associated digital certificate appropriate to the nature of the communication.

(2) Any digital certificate for the communication must be issued:

(a) by a Gatekeeper® accredited Certification Authority; and

(b) in accordance with a Gatekeeper® Certificate Policy and Certificate Practice Statement.

(3) The Gatekeeper® accredited Certification Authority referred to in subsection (2) must be an Authority that has been approved by the Department for that purpose.

### Part 4—Electronic production of documents

###### 16 Information technology requirements for producing documents

(1) This section applies if:

(a) a person is required to produce a document to the Department; and

(b) the person wishes to produce the document electronically.

(2) The document must be produced by sending an SMTP email addressed to a nominated Department email address attaching the document as a MIME attachment.

(3) The attached document must be in a version of one of the following standard document formats supported by the Department:

(a) Microsoft Word;

(b) Microsoft Excel;

(c) HTML;

(d) PDF;

(e) plain text;

(f) JPEG.

## Endnotes

### Endnote 1—About the endnotes

The endnotes provide information about this compilation and the compiled law.

The following endnotes are included in every compilation:

Endnote 1—About the endnotes

Endnote 2—Abbreviation key

Endnote 3—Legislation history

Endnote 4—Amendment history

**Abbreviation key—Endnote 2**

The abbreviation key sets out abbreviations that may be used in the endnotes.

**Legislation history and amendment history—Endnotes 3 and 4**

Amending laws are annotated in the legislation history and amendment history.

The legislation history in endnote 3 provides information about each law that has amended (or will amend) the compiled law. The information includes commencement details for amending laws and details of any application, saving or transitional provisions that are not included in this compilation.

The amendment history in endnote 4 provides information about amendments at the provision (generally section or equivalent) level. It also includes information about any provision of the compiled law that has been repealed in accordance with a provision of the law.

**Misdescribed amendments**

A misdescribed amendment is an amendment that does not accurately describe how an amendment is to be made. If, despite the misdescription, the amendment can be given effect as intended, then the misdescribed amendment can be incorporated through an editorial change made under section 15V of the *Legislation Act 2003*.

If a misdescribed amendment cannot be given effect as intended, the amendment is not incorporated and “(md not incorp)” is added to the amendment history.

### Endnote 2—Abbreviation key

| ad = added or inserted | orig = original |
|---|---|
| am = amended | par = paragraph(s)/subparagraph(s) |
| amdt = amendment | /sub‑subparagraph(s) |
| c = clause(s) | pres = present |
| C[x] = Compilation No. x | prev = previous |
| Ch = Chapter(s) | (prev…) = previously |
| def = definition(s) | Pt = Part(s) |
| Dict = Dictionary | r = regulation(s)/rule(s) |
| disallowed = disallowed by Parliament | reloc = relocated |
| Div = Division(s) | renum = renumbered |
| exp = expires/expired or ceases/ceased to have | rep = repealed |
| effect | rs = repealed and substituted |
| F = Federal Register of Legislation | s = section(s)/subsection(s) |
| gaz = gazette | Sch = Schedule(s) |
| LA = *Legislation Act 2003* | Sdiv = Subdivision(s) |
| LIA = *Legislative Instruments Act 2003* | SLI = Select Legislative Instrument |
| (md not incorp) = misdescribed amendment | SR = Statutory Rules |
| cannot be given effect | Sub‑Ch = Sub‑Chapter(s) |
| mod = modified/modification | SubPt = Subpart(s) |
| No. = Number(s) | underlining = whole or part not |
| o = order(s) | commenced or to be commenced |
| Ord = Ordinance |  |

### Endnote 3—Legislation history

| **Name** | **Registration** | **Commencement** | **Application, saving and transitional provisions** |
|---|---|---|---|
| *Customs (Information Technology Requirements) Determination 2021* | 25 March 2021 | 31 March 2021 | — |
| *Customs (Information Technology Requirements) Amendment (Self-Assessed Clearance Declaration) Determination 2024* | 14 June 2024 | 15 June 2024 | — |
| *Customs (Information Technology Requirements) Amendment (Australia Travel Declaration) Determination 2024* | 16 October 2024 | 17 October 2024 | — |
| *Customs (Information Technology Requirements) Amendment (API Project and Other Measures) Determination 2025* | 27 June 2025 | 28 June 2025 (items 1-5, 10, 11)<br>1 July 2025 (items 6-9) | — |

### Endnote 4—Amendment history

| **Provision affected** | **How affected** |
|---|---|
| **Part 1** |  |
| s 2 | rep LA s 48D |
| s 4 | am F2025L00744 |
| **Part 2**<br>s 8B | ad F2025L00744 |
| **Part 2A** |  |
| s 9A<br>s 9B<br>s 9E | am F2025L00744<br>am F2025L00744<br>am F2025L00744 |
| **Part 3**<br>s 11<br>s12A<br>s 13<br>s 14A | rs F2025L00744<br>ad F2025L00744<br>am F2025L00744<br>ad F2025L00744 |
|  |  |
| **Schedule 1** |  |
| Schedule 1 | rep LA s 48C |
