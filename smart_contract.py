# PatientRecordContract

class PatientRecordContract:
    def __init__(self):
        self.records = {}          # patient_id -> stores encrypted patient record
        self.access_control = {}   # patient_id -> set(authorized_users) enforces role-based access

    # ---------- MODIFIERS ----------
    
    # Check if user is authorized to access the record
    def _is_authorized(self, patient_id, user_id):
        return user_id in self.access_control.get(patient_id, set())

    # ---------- FUNCTIONS ----------

    # Create a new patient record
    def create_record(self, patient_id, encrypted_record, owner_id):
        self.records[patient_id] = encrypted_record
        self.access_control[patient_id] = {owner_id}

    # Request access to a patient record
    def request_access(self, patient_id, user_id, owner_id):
        if owner_id in self.access_control.get(patient_id, set()):
            self.access_control[patient_id].add(user_id)

    # Retrieve a patient record with access control
    def get_record(self, patient_id, user_id):
        if not self._is_authorized(patient_id, user_id):
            raise PermissionError("Access denied")
        return self.records[patient_id]
