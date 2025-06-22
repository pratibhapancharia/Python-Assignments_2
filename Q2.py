'''2.Write a function that reads a text file and returns its
lines.
Use with open(...) as f: 
Catch and handle FileNotFoundError with a user-friendly message.
From main(), prompt user for file name, call read_lines, then print line
count'''
def read_lines(filepath: str) -> list[str]:
    try:
        with open(filepath, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found. Please check the file name and try again.")
        return []

def main() -> None:
    """
    Prompt the user for a filename, read its lines, and print the line count.
    """
    filename = input("Enter the file name: ")
    lines = read_lines(filename)
    if lines:
        print(f"The file '{filename}' has {len(lines)} lines.")
    else:
        print("No lines to display.")

if __name__ == "__main__":
    main()
