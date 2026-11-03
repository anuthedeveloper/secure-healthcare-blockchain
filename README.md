# Secure healthcare system blockchain

> :warning: **This project was made for educational purposes only.** It is not intended to be used in production environments.

### Task 2 documentation (theory + explanation)

This project implements a secure healthcare data management prototype using blockchain and cryptographic techniques.

The system demonstrates how patient medical records can be securely created, stored, accessed, and audited using:

- Blockchain with Proof-of-Work (PoW)
- Cryptographic primitives (SHA-256, AES/Fernet, RSA, HMAC)
- A smart-contract-like PatientRecordContract
- Secure access control and integrity verification

The prototype is intended for academic demonstration and aligns with healthcare security requirements such as confidentiality, integrity, auditability, and controlled data sharing.

- System Requirements

  - Python version: Python 3.9 or higher
  - Operating System: Windows, Linux, or macOS

- Required dependencies or modules are installed globally
  Install dependencies using:

```
pip install
```

Built-in Libraries used:

```
- hashlib
- hmac
- json
- time
- os
```

No database or external blockchain framework is required.

How to Run the Prototype
Step 1: Clone or Extract the Project

```
git clone <repos-url>
cd secure-healthcare-blockchain
```

Or extract the submitted ZIP file and naviaget into the project root directory

Step 2: Run the Main Prototype

```
python main.py
```

- Expected Sample JSON/Input (Optional)
  The prototype does not require external JSON or input files. All sample data is embedded directly within the Python scripts to ensure deterministic execution, ease of testing, and reproducibility for assessment purposes.
  - All sample data (e.g. patient records, IDs, users) are defined directly in the Python code (main.py and test_system.py).
  - This ensures the system runs out of the box without additional setup.
- Without Sample JSON file, simply rename the `sample` folder
  - Optional JSON Input Support
  - The system optionally supports loading patient records from a JSON file.
  - This feature demonstrates extensibility and readiness for integration with healthcare data formats.
  - If no JSON file is present, the system automatically falls back to internally defined sample data to ensure deterministic execution and ease of assessment.

```
rm -r sample_data
python main.py
```

- Expected Output
  - A blockchain is initialized with a genesis block
  - A patient record is encrypted and authenticated
  - The encrypted record is stored on the blockchain
  - Blockchain integrity is verified

Example output:
`Blockchain valid: True`

This confirms:

- Proof-of-Work succeeded
- Blocks are correctly linked
- No tampering occurred

#### Sample Usage Explanation

1. Record Creation

- Patient data is encrypted using symmetric encryption (Fernet/AES)
- An HMAC is generated to authenticate the record
- Only encrypted data and metadata are stored on-chain

2. Blockchain Storage

- Each block contains:
  - Encrypted record
  - HMAC for integrity
  - Hash of the previous block
- Proof-of-Work ensures immutability

3. Smart Contract Logic

The `PatientRecordContract` manages access to patienct records

##### State Variables

- records: Stores encrypted patient records indexes by patient ID.
- access_control: Enforces role-based access, Maps patient IDs to a set of authorisez users

##### Functions

- create_record(): Secure creation, creates a new patient record and assigns ownership
- request_access(): Controlled sharing, Allows controlled sharing of records
- get_record(): Authorization-checked retrieval, Retrieves a record only if access is authorised
  Unauthorized access raises a `PermissionError`.

Test Coverage

1. Blockchain integrity

- Detects tampering
- Verifies block linkage

2. Crptography Correctness

- ENcryption/decryption cycle
- Hash consisitency
- HMAC verification

3. Smart Contract Security

- Access control enforcement
- Unauthorized access prevention

How to Run Tests

```
python test_system.py
```

Expected test output
`All tests passed`
This confirms correct functionality and basic security enforcement.

##### Security Considerations

- No plaintext patient data is stored on the blockchain
- Blockchain provides tamper resistance and auditability
- Authorization checks prevent insider abuse
- HMAC prevent record manipulation
- No re-entrancy risk (no external calls)

- Threats & Mitigation

| Threat         | Risk                   | Defence                                 |
| -------------- | ---------------------- | --------------------------------------- |
| Ransomware     | Data encryption attack | Encrypted backups, immutable blockchain |
| Insider Misuse | Unauthorized access    | Smart-contract access control           |
| Phishing       | Credential theft       | Public-key authentication               |
| Data Tampering | Record alteration      | SHA-256 + blockchain immutability       |
