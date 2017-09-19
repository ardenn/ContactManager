class Contact:
    """docstring for Contact"""

    def __init__(self, name, email, cell_phone, work_phone):
        self.name = name
        self.email = email
        self.cell_phone = cell_phone
        self.work_phone = work_phone

    def __repr__(self):
        return """
    	Contact Details
    	Name: {}
    	Email: {}
    	Cell Phone: {}
    	Work Phone: {}
    	""".format(self.name, self.email, self.cell_phone, self.work_phone)


class ContactManager:

    def __init__(self, contacts=[]):
        self.contacts = contacts

    def addContact(self, contact):
        self.contacts.append(contact)
        my_manager.displayContacts()

    def deleteContact(self):
        del_email = input("Enter Contact Email: ")
        for contact in self.contacts:
            if contact.email == del_email:
                self.contacts.remove(contact)
                print("Deletion Successful!\nThese are your remaining contacts:")
                my_manager.displayContacts()
        else:
            return "Sorry that contact does not exist!!"

    def searchContact(self):
        search_name = input("Enter Contact Name: ")
        print("Your search matched the following:")
        for contact in self.contacts:
            if search_name in contact.name:
                return contact
        else:
            return "Sorry that contact does not exist!!"

    def displayContacts(self):
        for contact in self.contacts:
            print(contact)


if __name__ == "__main__":
    my_manager = ContactManager()


while True:
    print("""Welcome, How may I help?
				1: Add Contact
				2: Search Contact
				3: Delete Contact
				4: Exit
		""")
    response = int(input("Enter Response: "))
    if response in [1, 2, 3, 4]:
        if response == 1:

                # User input for new Contact
            print("New Contact")
            c_name = input("Enter name: ")
            c_email = input("Enter email: ")
            cell = input("Enter cell phone number: ")
            work = input("Enter work phone number: ")

            my_manager.addContact(Contact(c_name, c_email, cell, work))
        elif response == 2:
            print(my_manager.searchContact())
        elif response == 3:
            print(my_manager.deleteContact())
        else:
            print("Exiting...")
            break
        print("""Do you wish to do something else?
         				1. Yes
         				2. No
         		""")
        response = int(input("Enter Response: "))
        if response == 1:
            continue
        else:
            break
    else:
        print("Please Enter a valid choice!!")
        continue
