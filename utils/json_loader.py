import json
from pathlib import Path


def load_patient_record(json_path: str) -> dict:
    """
    Loads a patient record from a JSON file.

    Raises:
        FileNotFoundError: if file does not exist
        ValueError: if JSON is invalid
    """
    path = Path(json_path)

    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
