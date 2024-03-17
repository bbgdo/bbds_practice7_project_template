from tests.test_io.test_input import (test_read_from_file_exists, test_read_from_file_returns_string,
                                      test_read_from_file_content, test_read_with_pandas_exists,
                                      test_read_with_pandas_returns_dataframe)


def main():
    pass


if __name__ == "__main__":
    main()
else:
    try:
        test_read_from_file_exists()
        print("Test 'test_read_from_file_exists' passed")
    except AssertionError as e:
        print("Test 'test_read_from_file_exists' failed:", e)

    try:
        test_read_from_file_returns_string()
        print("Test 'test_read_from_file_returns_string' passed")
    except AssertionError as e:
        print("Test 'test_read_from_file_returns_string' failed:", e)

    try:
        test_read_from_file_content()
        print("Test 'test_read_from_file_content' passed")
    except AssertionError as e:
        print("Test 'test_read_from_file_content' failed:", e)

    try:
        test_read_with_pandas_exists()
        print("Test 'test_read_with_pandas_exists' passed")
    except AssertionError as e:
        print("Test 'test_read_with_pandas_exists' failed:", e)

    try:
        test_read_with_pandas_returns_dataframe()
        print("Test 'test_read_with_pandas_returns_dataframe' passed")
    except AssertionError as e:
        print("Test 'test_read_with_pandas_returns_dataframe' failed:", e)
