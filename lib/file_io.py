def write_file(file_name, file_content):
    """Write content to a file."""
    try:
        with open(file_name, 'w') as f:
            f.write(file_content)
    except Exception as e:
        print(f"Error writing to {file_name}: {e}")

def append_file(file_name, append_content):
    """Append content to a file."""
    try:
        with open(file_name, 'a') as f:
            f.write(append_content)
    except Exception as e:
        print(f"Error appending to {file_name}: {e}")

def read_file(file_name):
    """Read content from a file."""
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error reading from {file_name}: {e}")
        return ""
