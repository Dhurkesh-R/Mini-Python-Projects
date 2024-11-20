import json

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added.")

def view_contacts():
    if contacts:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts found.")

def search_contact():
    name = input("Enter the name of the contact to search: ")
    contact = contacts.get(name)
    if contact:
        print(f"Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def save_contacts_to_file(filename):
    """Save contacts to file if it already exists, else create it."""
    try:
        with open(filename, 'w') as file:
            json.dump(contacts, file)
        print("Contacts saved to file.")
    except Exception as e:
        print(f"Error saving to file: {e}")

def load_contacts_from_file(filename):
    """Load contacts from an existing file."""
    try:
        with open(filename, 'r') as file:
            global contacts
            contacts = json.load(file)
        print("Contacts loaded from file.")
    except FileNotFoundError:
        print("File not found. Starting with an empty contact book.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Starting with an empty contact book.")

def main():
    filename = "contacts.json"
    load_contacts_from_file(filename)  # Load existing contacts at start

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Save Contacts")
        print("6. Exit")
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            save_contacts_to_file(filename)
        elif choice == '6':
            save_contacts_to_file(filename)  # Save before exiting
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
