def insert_comments(original_code: str, commented_output: str) -> str:
    """
    Merge the model-generated comments into the original code.
    If the output already includes full code, return as-is.
    """
    # If the generated output contains class or method signatures, assume it's complete code
    if "class " in commented_output or "public" in commented_output or "void" in commented_output:
        return commented_output.strip()

    # Otherwise, just prepend comments
    merged = f"// Auto-generated comments:\n{commented_output.strip()}\n\n{original_code}"
    return merged
