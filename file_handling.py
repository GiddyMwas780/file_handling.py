def file_read_write():
    try:
        # 🧪 Ask user for the filename
        filename = input("Enter the name of the file to read: ")

        # 📖 Open and read file content
        with open(filename, "r") as file:
            content = file.read()

        # 🖋️ Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # ✍️ Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"🎉 Success! Modified file saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
file_read_write()
