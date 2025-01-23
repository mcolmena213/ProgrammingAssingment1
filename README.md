
# README.md

## Description

This program provides functionality for managing a dataset stored in a `.tbl` file. It allows users to perform various operations such as:

- Loading and viewing the data
- Inserting new data
- Searching for data
- Updating existing data
- Deleting data entries
- Saving changes back to the file

The dataset is structured into columns such as PARTKEY, NAME, MANUFACTURER, BRAND, TYPE, QUANTITY, SIZE, PRICE, DESCRIPTION, and optionally EXTRA (if the dataset has 10 columns).

### Design Overview

The program is designed to interact with a dataset, allowing users to perform CRUD (Create, Read, Update, Delete) operations. It is divided into several modular functions to handle different operations and ensures smooth handling of data through validation and input checks. The key components of the design include:

- **Data Handling:** The program uses `pandas` to load, manipulate, and save data in a DataFrame format. The data is separated by a pipe (`|`) delimiter and contains various attributes for each part (e.g., part key, name, manufacturer, etc.).
  
- **CRUD Operations:**
  - **Create:** Users can insert new data by specifying attributes such as name, manufacturer, quantity, etc. New data entries are validated for proper data types.
  - **Read:** Users can search for data by specifying a column (e.g., PARTKEY, NAME, etc.) and a search value. The program displays matching results.
  - **Update:** Users can update existing data by specifying the PARTKEY and entering new values for any attribute.
  - **Delete:** Users can delete a specific entry based on PARTKEY after confirming the action.

- **Input Validation:** The program ensures proper data types are entered for fields like QUANTITY (integer) and PRICE (float). It handles incorrect or missing input gracefully and prompts the user to correct it.

- **File Handling:** Data is loaded from a `.tbl` file and saved back after modifications. The program uses `pandas` to save the dataset with pipe-delimited values.

### Architectural Design

1. **File I/O:** The `load_data` function reads the dataset from a `.tbl` file, and the `save_data` function writes any changes back to the file. The file is assumed to be in the same directory or can be specified in the code.

2. **Modular Functions:**
   - **Insert Data:** The `insert_data` function collects user input for each attribute and inserts the new row into the dataset. It automatically assigns the next available PARTKEY and checks for duplicates.
   - **Search Data:** The `search_data` function allows searching for values in a specific column. It uses string matching and handles case insensitivity.
   - **Update Data:** The `update_data` function allows users to modify existing data for a given PARTKEY. It provides an interactive prompt for each attribute with the current value pre-filled.
   - **Delete Data:** The `delete_data` function deletes a row with a specified PARTKEY after confirming the user's intent.

3. **Main Program Loop:** The `main()` function provides a simple menu for users to select actions, repeatedly offering the CRUD options until the user opts to exit.

4. **Error Handling:** The program incorporates error handling to manage issues such as invalid input or missing columns. It ensures that only valid data is added or modified in the dataset.

5. **Interactive User Interface:** The program is designed to run in a console, providing a simple, text-based interface for interacting with the data.

## Features

- Load data from a pipe-delimited `.tbl` file into a pandas DataFrame.
- View the first few rows and the shape of the dataset.
- Insert, update, delete, or search for data in the dataset.
- Save modified data back to the file.
- Provides validation for user input (numerical values for QUANTITY and PRICE).
- Handles errors gracefully and provides clear instructions.

## Requirements

- Python 3.x
- pandas library (Install via `pip install pandas`)

## How to Compile and Run the Program

1. **Install Dependencies:**
   Make sure you have Python installed on your machine. You can install the required libraries with the following command:
   ```bash
   pip install pandas
   ```

2. **Download or Clone the Repository:**
   Download or clone the repository containing the Python script.

3. **Run the Program:**
   Open a terminal or command prompt and navigate to the directory containing the Python script. Run the program with:
   ```bash
   python your_script_name.py
   ```
   Replace `your_script_name.py` with the actual name of your Python file.

4. **Interact with the Program:**
   Once the program starts, you will see the main menu where you can select an action by entering a number (1-6). The program will guide you through each option step-by-step.

   - **Insert new data**: Adds a new row to the dataset by prompting you for values.
   - **Search data**: Allows you to search for records based on specific attributes.
   - **Update data**: Lets you modify an existing record by entering the PARTKEY.
   - **Delete data**: Allows you to delete a record based on PARTKEY.
   - **Save data**: Saves any changes to the file.
   - **Exit**: Exits the program.

5. **File Handling:**
   The program expects the dataset file (`part.tbl`) to be in the same directory. If the file does not exist or is incorrectly formatted, the program will provide error messages.

## Example Usage

```bash
Please provide the following details for the new data entry:
Enter NAME (Text): Widget
Enter MANUFACTURER (Text): ABC Corp
Enter BRAND (Text): SuperBrand
Enter TYPE (Text): Electronics
Enter QUANTITY (Integer): 100
Enter PRICE (Decimal number, e.g., 99.99): 19.99
Enter SIZE (Text, e.g., 'SM', 'LG', etc.): Medium
Enter DESCRIPTION (Text): High-quality widget for everyday use
New data inserted successfully.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
