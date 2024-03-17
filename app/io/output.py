def print_to_console(*args, **kwargs):
    """
        Function to print text to the console.

        Accepts any number of positional and keyword arguments and prints them to the console.

        Args:
            *args: Positional arguments to be printed to the console.
            **kwargs: Keyword arguments that can be used to configure the printing.
    """
    print(*args, **kwargs)


def write_to_file(file_path, data):
    """
        Function to write data to a file.

        Writes the provided data to a file using Python's built-in capabilities.

        Args:
            file_path (str): The path to the file where the data will be written.
            data (str): The data to be written to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        print("Successfully written to file.")
    except IOError:
        print("Failure.")
