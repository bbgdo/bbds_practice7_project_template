import pandas as pd


def input_text():
    """Function for inputting text from the console.

        Returns:
            str: The string entered by the user from the console.
    """
    text = input("text input: ")
    return text


def read_from_file(file_path):
    """Function for reading data from a file.

        Args:
            file_path (str): The path to the file from which to read data.

        Returns:
            str: A string with the read data or None if the file is not found.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print("File not found.")
        return None


def read_with_pandas(file_path):
    """Function for reading data from a file using the pandas library.

        Args:
            file_path (str): The path to the file from which to read data.

        Returns:
            pandas.DataFrame: A pandas DataFrame object or None if the file is not found.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found.")
        return None
