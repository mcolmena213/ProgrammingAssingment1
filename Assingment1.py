import csv

# Function to read parts from the file
def read_part_file(filename='part.tbl'):
    try:
        parts = []
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='\t')
            for row in reader:
                parts.append(row)
        return parts
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to save parts to the file
def save_part_file(parts, filename='part.tbl'):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter='\t')
            for part in parts:
                writer.writerow(part)
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

# Function to search parts based on an attribute
def search_parts(parts, search_by, search_value):
    results = []
    for part in parts:
        if search_by.upper() in ['PARTKEY', 'NAME', 'BRAND', 'TYPE']:
            index = ['PARTKEY', 'NAME', 'MFGR', 'BRAND', 'TYPE', 'SIZE', 'CONTAINER', 'RETAILPRICE', 'COMMENT'].index(search_by.upper())
            if part[index].lower() == search_value.lower():  # case insensitive search
                results.append(part)
    return results

# Function to insert a new part into the dataset
def insert_part(parts, part_details):
    parts.append(part_details)
    save_part_file(parts)  # Save to file after inserting

# Function to update a part by PARTKEY
def update_part(parts, partkey, updated_details):
    for i, part in enumerate(parts):
        if part[0] == partkey:  # Match the PARTKEY
            parts[i] = updated_details
            save_part_file(parts)  # Save to file after updating
            return True
    return False

# Function to delete a part by PARTKEY
def delete_part(parts, partkey):
    for i, part in enumerate(parts):
        if part[0] == partkey:  # Match the PARTKEY
            parts.pop(i)
            save_part_file(parts)  # Save to file after deleting
            return True
    return False

# Main program that offers user interaction
def main():
    filename = 'part.tbl'
    parts = read_part_file(filename)
    
    if not parts:
        print("No data found.")
        return

    print("\nPart Database Menu")
    print("1. Insert New Data Item")
    print("2. Search Data Items")
    print("3. Update Data Item")
    print("4. Delete Data Item")
    print("5. Exit")
    
    while True:
        choice = input("Select an option (1-5): ")

        if choice == '1':  # Insert New Data Item
            partkey = input("Enter PARTKEY: ")
            name = input("Enter NAME: ")
            mfgr = input("Enter MFGR: ")
            brand = input("Enter BRAND: ")
            type_ = input("Enter TYPE: ")
            size = input("Enter SIZE: ")
            container = input("Enter CONTAINER: ")
            retailprice = input("Enter RETAILPRICE: ")
            comment = input("Enter COMMENT: ")
            new_part = [partkey, name, mfgr, brand, type_, size, container, retailprice, comment]
            insert_part(parts, new_part)
            print("Part added successfully.")

        elif choice == '2':  # Search Data Items
            search_by = input("Search by PARTKEY, NAME, BRAND, TYPE: ").strip()
            if search_by.upper() not in ['PARTKEY', 'NAME', 'BRAND', 'TYPE']:
                print("Invalid attribute. Please choose from PARTKEY, NAME, BRAND, or TYPE.")
                continue
            search_value = input(f"Enter the value for {search_by}: ").strip()
            results = search_parts(parts, search_by, search_value)

            if results:
                print(f"\nFound {len(results)} matching part(s):")
                for result in results:
                    print(result)  # Print the matching parts
            else:
                print("No matching parts found.")
                
        elif choice == '3':  # Update Data Item
            partkey = input("Enter PARTKEY of the item to update: ").strip()
            updated_details = []
            updated_details.append(partkey)
            updated_details.append(input("Enter updated NAME: ").strip())
            updated_details.append(input("Enter updated MFGR: ").strip())
            updated_details.append(input("Enter updated BRAND: ").strip())
            updated_details.append(input("Enter updated TYPE: ").strip())
            updated_details.append(input("Enter updated SIZE: ").strip())
            updated_details.append(input("Enter updated CONTAINER: ").strip())
            updated_details.append(input("Enter updated RETAILPRICE: ").strip())
            updated_details.append(input("Enter updated COMMENT: ").strip())

            if update_part(parts, partkey, updated_details):
                print("Part updated successfully.")
            else:
                print("Part with given PARTKEY not found.")

        elif choice == '4':  # Delete Data Item
            partkey = input("Enter PARTKEY of the item to delete: ").strip()
            if delete_part(parts, partkey):
                print("Part deleted successfully.")
            else:
                print("Part with given PARTKEY not found.")

        elif choice == '5':  # Exit
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose 1-5.")

if __name__ == '__main__':
    main()
