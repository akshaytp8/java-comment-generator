def load_code(file_path: str) -> str:
    """Reads Java code from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def save_code(file_path: str, code: str):
    """Writes commented code to a file."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
