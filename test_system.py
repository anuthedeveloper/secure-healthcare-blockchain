# Unit & security tests

import unittest
from blockchain import Blockchain
from crypto_utils import *
from smart_contract import PatientRecordContract

class TestSecureHealthcareSystem(unittest.TestCase):

    def test_blockchain_integrity(self):
        bc = Blockchain()
        bc.add_block("Test")
        self.assertTrue(bc.is_chain_valid())

    def test_encryption_cycle(self):
        key = generate_symmetric_key()
        data = b"Medical Data"
        encrypted = encrypt_data(key, data)
        decrypted = decrypt_data(key, encrypted)
        self.assertEqual(decrypted, data)

    def test_access_control(self):
        contract = PatientRecordContract()
        contract.create_record("P1", b"enc", "owner")

        with self.assertRaises(PermissionError):
            contract.get_record("P1", "attacker")



if __name__ == "__main__":
    unittest.main()

