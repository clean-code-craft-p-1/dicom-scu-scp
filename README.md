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

Send a C-ECHO request using the SCU (Service Class User):

```bash
python scu.py
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
