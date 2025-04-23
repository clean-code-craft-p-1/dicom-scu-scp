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
