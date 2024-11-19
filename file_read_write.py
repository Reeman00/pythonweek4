def file_read_write():
    try:
        # Ask the user for the filename
        input_filename = input("Enter the filename to read from: ")

        # Attempt to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (for demonstration, we'll convert to uppercase)
        modified_content = content.upper()

        # Ask for the new file name to write the modified content
        output_filename = input("Enter the filename to write the modified content to: ")
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Content successfully written to {output_filename}.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file could not be read. Please check the file permissions or try another file.")

# Run the function
file_read_write()
