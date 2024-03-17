from app.io.input import input_text, read_from_file, read_with_pandas
from app.io.output import print_to_console, write_to_file


def main():
    # Using the console's input and output functions
    text = input_text()
    print_to_console("Entered text:", text)

    # Using functions for reading data from a file and writing data to a file
    file_path = "data/example.txt"  # Change this value to the one that is suitable for you
    data_to_write = "Hello World!"
    write_to_file(file_path, data_to_write)
    data_from_file = read_from_file(file_path)
    print_to_console("Data read from file:", data_from_file)

    # Using function for reading data from a file using the pandas library.
    file_path_csv = "data/example.csv"  # Change this value to the one that is suitable for you
    data_from_csv = read_with_pandas(file_path_csv)
    print_to_console("Data read from CSV file using pandas:")
    print_to_console(data_from_csv)


if __name__ == "__main__":
    main()
