# Part Database Management System

This program provides a command-line interface for managing a parts database stored in a tab-separated file (`part.tbl`). Users can perform CRUD (Create, Read, Update, Delete) operations on the parts data.

## Features

1. **Insert New Data Item**: Add a new part to the database.
2. **Search Data Items**: Search for parts based on attributes like `PARTKEY`, `NAME`, `BRAND`, or `TYPE`.
3. **Update Data Item**: Update an existing part's details by providing its `PARTKEY`.
4. **Delete Data Item**: Remove a part from the database using its `PARTKEY`.
5. **Exit Program**: Exit the interactive session.

## Program Design

### Functional Components
1. **File Handling**:
   - The program reads and writes data from/to a tab-separated file (`part.tbl`).
   - `read_part_file(filename)` and `save_part_file(parts, filename)` handle file operations.
   
2. **CRUD Operations**:
   - `insert_part(parts, part_details)`: Appends a new part to the dataset and saves it.
   - `search_parts(parts, search_by, search_value)`: Searches for parts based on the given attribute and value.
   - `update_part(parts, partkey, updated_details)`: Updates an existing part based on its `PARTKEY`.
   - `delete_part(parts, partkey)`: Deletes a part based on its `PARTKEY`.

3. **Interactive Menu**:
   - A user-friendly menu guides users through the available operations.

### Architectural Design
- The system follows a modular structure:
  - **Data Layer**: File operations for reading and saving data.
  - **Logic Layer**: CRUD operations for manipulating data.
  - **Interface Layer**: Command-line menu for user interaction.
- Error handling ensures smooth operation and provides user feedback on issues (e.g., missing file, invalid inputs).

## Installation

1. Clone the repository or download the script file.
2. Ensure you have Python installed (version 3.6 or later is recommended).

## Compilation and Execution

1. Place your parts data file (`part.tbl`) in the same directory as the script, or ensure the script can locate it.
2. Run the program from the command line:
   ```bash
   python part_management.py
