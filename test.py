def remove_extra_spaces(original_string):
    """Remove extra spaces from a string."""
    return ' '.join(original_string.split())

# Example usage:
original_string = "  This  is   an example  string   with   extra spaces.  "
cleaned_string = remove_extra_spaces(original_string)
print(f"Original string: '{original_string}'")
print(f"Cleaned string: '{cleaned_string}'")