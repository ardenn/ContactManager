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

print("New Contact")
c_name = input("Enter name: ")
c_email = input("Enter email: ")
cell = input("Enter cell phone number: ")
work = input("Enter work phone number: ")

new_contact = Contact(c_name, c_email, cell, work)
print(new_contact)
