from pynetdicom import AE, debug_logger, evt
from pynetdicom.sop_class import Verification, SecondaryCaptureImageStorage
from pydicom.uid import ExplicitVRLittleEndian

debug_logger()

def handle_store(event):
    ds = event.dataset
    ds.file_meta = event.file_meta
    print(f"Received C-STORE request from: {event.assoc.requestor.address}")
    print(f"SOP Class UID: {ds.SOPClassUID}")
    print(f"Transfer Syntax UID: {event.context.transfer_syntax}")
    return 0x0000

handlers = [(evt.EVT_C_STORE, handle_store)]


def start_scp():
    ae = AE(ae_title='tryout_scp')
    ae.add_supported_context(Verification)
    ae.add_supported_context(SecondaryCaptureImageStorage, ExplicitVRLittleEndian)

    ae.start_server(('127.0.0.1', 11112), block=True, evt_handlers=handlers)

if __name__ == "__main__":
    start_scp()
