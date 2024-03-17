from app.io.input import read_from_file, read_with_pandas
import pandas as pd


# Tests for read_from_file
def test_read_from_file_exists():
    assert callable(read_from_file), "read_from_file function does not exist"


def test_read_from_file_returns_string():
    file_path = "tests/test_io/test_data/test_example.txt"  # Directory with test examples
    assert isinstance(read_from_file(file_path), str), "read_from_file should return a string"


def test_read_from_file_content():
    file_path = "tests/test_io/test_data/test_example.txt"  # Directory with test examples
    expected_content = "Hello World!"
    assert read_from_file(file_path) == expected_content, "read_from_file should read the correct content from the file"


# Tests for read_with_pandas
def test_read_with_pandas_exists():
    assert callable(read_with_pandas), "read_with_pandas function does not exist"


def test_read_with_pandas_returns_dataframe():
    file_path = "tests/test_io/test_data/test_example.csv"  # Directory with test examples
    assert isinstance(read_with_pandas(file_path), pd.DataFrame), "read_with_pandas should return a pandas DataFrame"
