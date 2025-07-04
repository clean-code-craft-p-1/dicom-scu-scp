# DICOM SCU and SCP

This project demonstrates a simple implementation of a DICOM Service Class User (SCU) and Service Class Provider (SCP) using Python.

## Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the SCP

Start the SCP (Service Class Provider) to listen for incoming DICOM requests:

```bash
python scp.py
```

## Running the SCU

Send a C-ECHO followed by a C-STORE as SCU (Service Class User):

```bash
python scu.py
```

## Send a DICOM file to the scp

```bash
python -m pynetdicom storescu 127.0.0.1 11112 "samples\ctslice" -v -cx
```

## DICOM as a chat analogy

DICOM Term | Chat Analogy
-----|-----
AE Title | Username
Association | Starting a chat
Abstract Syntax | Chat topic (e.g. images, queries)
Transfer Syntax | Language/format of messages
DIMSE Services | Actions like send/print
SOP Class | Topic + Action combo
Implementation Class UID | The vendor/app ID (e.g., WhatsApp)
Implementation Version | App version (e.g., v2.23)

---

DICOM content | Photo Analogy
-----|-----
Modality (CT, MR, US, CR) | Type of camera (Phone camera, IR camera)
DICOM tags (0x00200010) | Information in a photo (location, timestamp)
PACS | Google photos (store, tag, search, retrieve)
Worklist (MWL) | Photography schedule (morning housewarming, evening reception)
Study Instance UID | Unique ID of the photo album of a tour
Series Instance UID | Unique ID of a collection in the album (e.g. at a location)
SOP Instance UID | A unique ID for an individual photo inside a collection

## References

DICOM viewer: https://www.microdicom.com/

DICOM in python: https://pydicom.github.io

DICOM standard: https://www.dicomstandard.org/

DICOM-web cheatsheet: https://www.dicomstandard.org/using/dicomweb/dicomweb-cheatsheet

Easy browsing of DICOM standard: https://dicom.innolitics.com

OHIF DICOM-web viewer: https://ohif.org/
