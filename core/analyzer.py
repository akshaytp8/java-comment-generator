import re

def extract_functions(code: str):
    """Extract method names from Java code."""
    pattern = r"(public|private|protected)?\s+[\w<>]+\s+(\w+)\s*\([^)]*\)\s*\{"
    matches = re.findall(pattern, code)
    return [m[1] for m in matches]

def analyze_code_structure(code: str):
    """Basic structural metrics: line count, classes, methods."""
    lines = code.splitlines()
    num_classes = len(re.findall(r"class\s+\w+", code))
    functions = extract_functions(code)
    return {
        "lines": len(lines),
        "num_classes": num_classes,
        "num_functions": len(functions),
        "function_names": functions,
    }
