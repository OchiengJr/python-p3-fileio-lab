import os
from file_io import write_file, append_file, read_file

def test_write_file(tmp_path):
    """Test write_file()"""
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    write_file(file_name, file_content)
    assert os.path.exists(f'{file_name}.txt'), "File was not created"
    with open(f'{file_name}.txt', 'r') as f:
        file_content_read = f.read()
    assert file_content_read == file_content, "Content mismatch"

def test_append_file(tmp_path):
    """Test append_file()"""
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    append_content = "\nAppended content."
    write_file(file_name, file_content)
    append_file(file_name, append_content)
    with open(f'{file_name}.txt', 'r') as f:
        file_content_read = f.read()
    expected_content = file_content + append_content
    assert file_content_read == expected_content, "Content mismatch"

def test_read_file(tmp_path):
    """Test read_file()"""
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    write_file(file_name, file_content)
    file_content_read = read_file(file_name)
    assert file_content_read == file_content, "Content mismatch"

def test_read_nonexistent_file(tmp_path):
    """Test read_file() with non-existent file"""
    file_name = tmp_path / "nonexistent_file"
    file_content_read = read_file(file_name)
    assert file_content_read == "", "Content should be empty for non-existent file"
