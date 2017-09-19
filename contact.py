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

    def deleteContact(self, del_email):
        for contact in self.contacts:
            if contact.email == del_email:
                self.contacts.remove(contact)
                print("Deletion Successful!\nThese are your remaining contacts:")
                my_manager.displayContacts()
        else:
            return "Sorry that contact does not exist!!"

    def searchContact(self, search_name):
        print("Your search matched the following:")
        for contact in self.contacts:
            if search_name in contact.name:
                print(contact)
        else:
            print("Sorry that contact does not exist!!")

    def displayContacts(self):
        for contact in self.contacts:
            print(contact)

    def readFromFile(self, filename):
        with open(filename) as read_file:
            header = read_file.readline()

            for line in read_file.readlines():
                values = line.strip().split(",")
                self.contacts.append(Contact(*values))
        return self.displayContacts()

    def writeToFile(self, filename):
        with open(filename, "w") as write_file:
            write_file.write("name,email,cell_phone,work_phone\n")

            for contact in self.contacts:
                contact_dict = contact.__dict__
                write_file.write(
                    "{name},{email},{cell_phone},{work_phone}\n".format(
                        **contact_dict))
        self.displayContacts()

if __name__ == "__main__":
    my_manager = ContactManager()


while True:
    print("""Welcome, How may I help?
    0: Read Contacts from file
	1: Add Contact
	2: Search Contact
	3: Delete Contact
	4: Write Contacts to file
	5: Exit
	""")
    response = int(input("Enter Response: "))
    if response in [0, 1, 2, 3, 4]:
        if response == 0:
            filename = input("Enter Filename to read from: ")
            my_manager.readFromFile(filename)
        elif response == 1:
            # User input for new Contact
            print("New Contact")
            c_name = input("Enter name: ")
            c_email = input("Enter email: ")
            cell = input("Enter cell phone number: ")
            work = input("Enter work phone number: ")
            my_manager.addContact(Contact(c_name, c_email, cell, work))
        elif response == 2:
            search_name = input("Enter Contact Name: ")
            my_manager.searchContact(search_name)
        elif response == 3:
            del_email = input("Enter Contact Email: ")
            print(my_manager.deleteContact(del_email))
        elif response == 4:
            filename = input("Enter Filename to write to: ")
            my_manager.writeToFile(filename)
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
