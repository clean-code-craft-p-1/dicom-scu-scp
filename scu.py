from pydicom.dataset import Dataset
from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import Verification, SecondaryCaptureImageStorage, CTImageStorage
from pydicom.uid import ExplicitVRLittleEndian, JPEGLossless

debug_logger()

def send_c_echo():
    ae = AE()
    ae.add_requested_context(Verification)
    ae.add_requested_context(SecondaryCaptureImageStorage, ExplicitVRLittleEndian)
    ae.add_requested_context(CTImageStorage, JPEGLossless)

    assoc = ae.associate('127.0.0.1', 11112)
    if assoc.is_established:
        status = assoc.send_c_echo()
        print(f'C-ECHO response: {status}')
        print('\nNext sending a secondary capture\n')
        ds = Dataset()
        # Add file meta information
        file_meta = Dataset()
        file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
        file_meta.ImplementationClassUID = '1.2.3.4'
        ds.file_meta = file_meta
        ds.is_little_endian = True
        ds.is_implicit_VR = False
        ds.SOPClassUID = '1.2.840.10008.5.1.4.1.1.7'  # Secondary Capture Image Storage
        ds.SOPInstanceUID = '1.2.3'
        ds.PatientName = 'Test^Patient'
        ds.PatientID = '123456'
        ds.Rows = 4
        ds.Columns = 4
        ds.PhotometricInterpretation = 'MONOCHROME2'
        ds.SamplesPerPixel = 1
        ds.BitsAllocated = 8
        ds.BitsStored = 8
        ds.HighBit = 7
        ds.PixelRepresentation = 0
        ds.PixelData = bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        status = assoc.send_c_store(ds)
        print(f'C-STORE response: {status}')
        assoc.release()
    else:
        print('Association failed')

if __name__ == "__main__":
    send_c_echo()