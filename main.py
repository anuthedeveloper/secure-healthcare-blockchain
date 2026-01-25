# System prototype demo
import os
import json
from blockchain import Blockchain
from crypto_utils import *
from smart_contract import PatientRecordContract
from utils.json_loader import load_patient_record

# Initialize system
blockchain = Blockchain()
contract = PatientRecordContract()

# Keys
sym_key = generate_symmetric_key()
hmac_key = os.urandom(32)

try:
    data = load_patient_record('sample/patient_record.json')
    patient_id = data['patient_id']
    owner_id = data['owner_id']
    record_bytes = json.dumps(data["record"]).encode('utf-8')

except FileNotFoundError:
    # Fallback to hardcoded sample (default behavior)
    # Patient record
    patient_id = "PAT001"
    owner_id = "patient"
    record_bytes = b"Blood Test: Normal"
    
# ---------- ENCRYPT & STORE ----------
encrypted_record = encrypt_data(sym_key, record_bytes)
record_hmac = generate_hmac(hmac_key, encrypted_record)

# Store on blockchain
blockchain.add_block({
    "patient_id": patient_id,
    "record": encrypted_record.decode(),
    "hmac": record_hmac.hex()
})

# Smart contract logic
contract.create_record(patient_id, encrypted_record, owner_id)

print("Blockchain valid:", blockchain.is_chain_valid())
