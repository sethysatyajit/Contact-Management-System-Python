import json
import os

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        """Load contacts from JSON file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return {}
        return {}
    
    def save_contacts(self):
        """Save contacts to JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)
    
    def add_contact(self, name, phone, email=None, address=None):
        """Add a new contact"""
        if name in self.contacts:
            print(f"Contact '{name}' already exists. Use update to modify.")
            return False
        
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        self.save_contacts()
        print(f"Contact '{name}' added successfully.")
        return True
    
    def view_contact(self, name):
        """View a specific contact"""
        contact = self.contacts.get(name)
        if contact:
            print(f"\nName: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact.get('email', 'Not provided')}")
            print(f"Address: {contact.get('address', 'Not provided')}")
        else:
            print(f"Contact '{name}' not found.")
    
    def view_all_contacts(self):
        """View all contacts"""
        if not self.contacts:
            print("No contacts found.")
            return
        
        print("\n--- All Contacts ---")
        for name, details in self.contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details.get('email', 'Not provided')}")
            print(f"Address: {details.get('address', 'Not provided')}")
        print("\n--- End of Contacts ---")
    
    def update_contact(self, name, phone=None, email=None, address=None):
        """Update an existing contact"""
        if name not in self.contacts:
            print(f"Contact '{name}' not found.")
            return False
        
        contact = self.contacts[name]
        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email
        if address:
            contact['address'] = address
        
        self.save_contacts()
        print(f"Contact '{name}' updated successfully.")
        return True
    
    def delete_contact(self, name):
        """Delete a contact"""
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact '{name}' deleted successfully.")
            return True
        else:
            print(f"Contact '{name}' not found.")
            return False
    
    def search_contacts(self, search_term):
        """Search contacts by name or phone number"""
        results = {}
        for name, details in self.contacts.items():
            if (search_term.lower() in name.lower() or 
                search_term in details['phone']):
                results[name] = details
        
        if results:
            print("\n--- Search Results ---")
            for name, details in results.items():
                print(f"\nName: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details.get('email', 'Not provided')}")
                print(f"Address: {details.get('address', 'Not provided')}")
            print("\n--- End of Results ---")
        else:
            print("No matching contacts found.")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. View All Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Search Contacts")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email (optional): ").strip() or None
            address = input("Enter address (optional): ").strip() or None
            contact_book.add_contact(name, phone, email, address)
        
        elif choice == '2':
            name = input("Enter name to view: ").strip()
            contact_book.view_contact(name)
        
        elif choice == '3':
            contact_book.view_all_contacts()
        
        elif choice == '4':
            name = input("Enter name to update: ").strip()
            phone = input("Enter new phone number (leave blank to keep current): ").strip() or None
            email = input("Enter new email (leave blank to keep current): ").strip() or None
            address = input("Enter new address (leave blank to keep current): ").strip() or None
            contact_book.update_contact(name, phone, email, address)
        
        elif choice == '5':
            name = input("Enter name to delete: ").strip()
            contact_book.delete_contact(name)
        
        elif choice == '6':
            search_term = input("Enter name or phone number to search: ").strip()
            contact_book.search_contacts(search_term)
        
        elif choice == '7':
            print("Exiting Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()