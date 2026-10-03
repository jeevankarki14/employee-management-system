from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "EMS File"

boss_path = str(DATA_DIR / "boss.txt")
manager_path = str(DATA_DIR / "manager.txt")
employee_path = str(DATA_DIR / "employee.txt")
enquiry_path = str(DATA_DIR / "enquiry.txt")
suggestion_path = str(DATA_DIR / "suggestion.txt")

DEFAULT_DATA = {
    boss_path: "B1|Boss User|CEO|Kathmandu|100000|boss@example.com|boss123",
    manager_path: "M1|Manager User|Manager|Kathmandu|50000|manager@example.com|manager123",
    employee_path: "E1|Employee User|Developer|25|Kathmandu|40000|employee@example.com|employee123",
    enquiry_path: "",
    suggestion_path: "",
}


def setup_system():
    """Create the local data directory and starter files when missing."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for file_path, default_content in DEFAULT_DATA.items():
        path = Path(file_path)
        if not path.exists():
            path.write_text(default_content, encoding="utf-8")
