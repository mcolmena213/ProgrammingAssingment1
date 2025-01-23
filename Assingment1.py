import pandas as pd

def load_data(file_path):
    try:
        # Load the data from the .tbl file into a DataFrame
        data = pd.read_csv(file_path, delimiter='|', header=None)
        
        # Print the first few rows to check how many columns we have
        print("Data preview:\n", data.head())
        
        # Print the shape of the dataframe to check columns
        print("Data shape: ", data.shape)
        
        # Adjust the columns based on the number of columns in the file
        if data.shape[1] == 9:
            data.columns = ['PARTKEY', 'NAME', 'MANUFACTURER', 'BRAND', 'TYPE', 'QUANTITY', 'SIZE', 'PRICE', 'DESCRIPTION']
        elif data.shape[1] == 10:
            data.columns = ['PARTKEY', 'NAME', 'MANUFACTURER', 'BRAND', 'TYPE', 'QUANTITY', 'SIZE', 'PRICE', 'DESCRIPTION', 'EXTRA']
        else:
            print("Unexpected number of columns. Please check your file.")
        
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()


def insert_data(data):
    # Get current PARTKEY for the next entry (assuming PARTKEY is sequential)
    next_partkey = data['PARTKEY'].max() + 1
    
    # Prompt user for each attribute with clear instructions on expected input types
    print("\nPlease provide the following details for the new data entry:")
    
    name = input("Enter NAME (Text): ")
    manufacturer = input("Enter MANUFACTURER (Text): ")
    brand = input("Enter BRAND (Text): ")
    type_ = input("Enter TYPE (Text): ")
    
    # Input for numerical fields with type validation
    try:
        quantity = int(input("Enter QUANTITY (Integer): "))  # Expecting an integer
        price = float(input("Enter PRICE (Decimal number, e.g., 99.99): "))  # Expecting a float
    except ValueError:
        print("Error: QUANTITY and PRICE must be numeric values.")
        return data
    
    size = input("Enter SIZE (Text, e.g., 'SM', 'LG', etc.): ")
    description = input("Enter DESCRIPTION (Text): ")

    # Create the new data list
    new_data = [name, manufacturer, brand, type_, quantity, size, price, description, None]  # Adding None for the EXTRA column

    # Ensure new_data is correctly populated with 9 elements
    if len(new_data) != 9:
        print("Error: The number of fields does not match the number of columns.")
        return data

    # Create the new row with PARTKEY included as the first element
    new_row = pd.Series([next_partkey] + new_data, index=data.columns)
    
    # Check for duplicates by PARTKEY
    if next_partkey in data['PARTKEY'].values:
        print(f"Error: A row with PARTKEY {next_partkey} already exists.")
        return data
    
    # Use pd.concat to append the new row
    data = pd.concat([data, new_row.to_frame().T], ignore_index=True)
    print("New data inserted successfully.")

    return data



def search_data(data, column, value):
    try:
        # Ensure the column is treated as a string, filling NaN with an empty string
        data[column] = data[column].astype(str).fillna('')
        
        # Search for rows where the specified column contains the search value
        result = data[data[column].str.contains(value, case=False, na=False)]
        return result
    except KeyError:
        print(f"Error: Column '{column}' not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error searching data: {e}")
        return pd.DataFrame()

def update_data(data, partkey):
    # Prompt the user for each attribute
    print(f"Enter the new data for the part with PARTKEY: {partkey}")
    
    # Get current values for the part with the specified PARTKEY
    current_data = data.loc[data['PARTKEY'] == partkey].iloc[0]

    # Ask for each value individually
    name = input(f"Enter new NAME (current: {current_data['NAME']}): ")
    if not name:
        name = current_data['NAME']  # Keep current value if input is blank

    manufacturer = input(f"Enter new MANUFACTURER (current: {current_data['MANUFACTURER']}): ")
    if not manufacturer:
        manufacturer = current_data['MANUFACTURER']  # Keep current value if input is blank

    brand = input(f"Enter new BRAND (current: {current_data['BRAND']}): ")
    if not brand:
        brand = current_data['BRAND']  # Keep current value if input is blank

    type_ = input(f"Enter new TYPE (current: {current_data['TYPE']}): ")
    if not type_:
        type_ = current_data['TYPE']  # Keep current value if input is blank

    # Input for numerical fields, allowing for blank input
    try:
        quantity = input(f"Enter new QUANTITY (current: {current_data['QUANTITY']}): ")
        if quantity:
            quantity = int(quantity)  # Convert to int if input is provided
        else:
            quantity = current_data['QUANTITY']  # Keep current value if input is blank

        price = input(f"Enter new PRICE (current: {current_data['PRICE']}): ")
        if price:
            price = float(price)  # Convert to float if input is provided
        else:
            price = current_data['PRICE']  # Keep current value if input is blank
    except ValueError:
        print("Error: QUANTITY and PRICE must be numeric values.")
        return data

    size = input(f"Enter new SIZE (current: {current_data['SIZE']}): ")
    if not size:
        size = current_data['SIZE']  # Keep current value if input is blank

    description = input(f"Enter new DESCRIPTION (current: {current_data['DESCRIPTION']}): ")
    if not description:
        description = current_data['DESCRIPTION']  # Keep current value if input is blank

    # Create a list of the new data
    new_data = [name, manufacturer, brand, type_, quantity, size, price, description]

    # Ensure new_data is correctly populated with 8 elements (no missing fields)
    if len(new_data) != 8:
        print("Error: The number of fields does not match the number of columns.")
        return data

    # Locate the row with the matching PARTKEY and update it
    data.loc[data['PARTKEY'] == partkey, ['NAME', 'MANUFACTURER', 'BRAND', 'TYPE', 'QUANTITY', 'SIZE', 'PRICE', 'DESCRIPTION']] = new_data
    print(f"Data for PARTKEY {partkey} has been updated.")
    return data


def delete_data(data, partkey):
    # Check if the PARTKEY exists in the dataset
    if partkey not in data['PARTKEY'].values:
        print(f"Error: PARTKEY {partkey} not found.")
        return data
    
    # Ask the user for confirmation before deleting
    confirm = input(f"Are you sure you want to delete the data with PARTKEY {partkey}? (y/n): ").strip().lower()
    if confirm == 'y':
        # Remove the row with the matching PARTKEY
        data = data[data['PARTKEY'] != partkey]
        print(f"Data with PARTKEY {partkey} has been deleted.")
    else:
        print(f"Deletion of PARTKEY {partkey} was canceled.")
    
    return data


def save_data(data, file_path):
    try:
        data.to_csv(file_path, index=False, sep='|', header=False)
        print(f"Data saved successfully to {file_path}")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    # Load the data from the file
    file_path = 'part.tbl'
    data = load_data(file_path)

    while True:
        print("\nData preview:")
        print(data.head())  # Show first few rows as a preview
        print(f"Data shape: {data.shape}")

        # Provide options to the user
        print("\nSelect an action:")
        print("1. Insert new data")
        print("2. Search data")
        print("3. Update data")
        print("4. Delete data")
        print("5. Save data")
        print("6. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            # Insert new data (using the updated insert_data method)
            data = insert_data(data)
        
        elif choice == '2':
            # Search data
            column = input("Enter the column name to search (PARTKEY, NAME, BRAND, TYPE): ").upper()
            value = input("Enter the value to search for: ")
            result = search_data(data, column, value)
            print("Search Results:")
            print(result)
        
        elif choice == '3':
            # Update data
            try:
                partkey = int(input("Enter the PARTKEY of the item to update: "))
                data = update_data(data, partkey)
            except ValueError:
                print("Error: PARTKEY should be an integer.")
        
        elif choice == '4':
            # Delete data
            try:
                partkey = int(input("Enter the PARTKEY of the item to delete: "))
                data = delete_data(data, partkey)
                print(f"Data with PARTKEY {partkey} has been deleted.")
            except ValueError:
                print("Error: PARTKEY should be an integer.")
        
        elif choice == '5':
            # Save data
            save_data(data, file_path)
        
        elif choice == '6':
            # Exit the program
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
