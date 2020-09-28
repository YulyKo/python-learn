# # Створити додаток Телефонна книга. 
# # Необхідно зберігати дані про абонента 
# # ( ПІП, тел. Персональний, тел.моб., дод.інфа про абонента) 
# # в середині відповідного класу. 
# # Наповнити клас конструкторами.. деструкторaми..

# class Contact():
#     def _init_(self, contactName, phoneNumber):
#         self.contactName = contactName
#         self.phoneNumber = phoneNumber
#     pass
    
#     def get_name(self):
#         return self.contactName
#     pass

#     def get_phone(self):
#         return self.phoneNumber
#     pass

#     def set_name(self, name):
#         self.contactName = name
#     pass
    
#     def set_phone(self, number):
#         self.phoneNumber = number
#     pass
# pass


# class ContactBook:
#     def __init__(self):
#         self.contactBook = []
#     pass

#     def showMenu(self):
#         print("Select what do you want to do: \n
#         1. Add Contact \n")
#         pass

#     def setNewContactName(self):
#         print("Print name for contact:  ")
#         name = input()
#         return name

#     def setNewContactPhone(self):
#         print("Print phone of contact:  ")
#         phone = input()
#         return phone

#     def appendContact(self, contact):
#         self.contactBook.append(contact)
#         # print(self.contactBook[0].get_name())
#         # print(self.contactBook[0].get_phone())
#         pass

#     def showContactsFromBook(self):
#         for contactId in self.contactBook:
#             print("name:  " + self.contactBook[contactId].get_name())
#             print("phone:  " + self.contactBook[contactId].get_phone())
#             pass
#         pass
# pass

# cb = ContactBook()
# contact = Contact()

# name = cb.setNewContactName()
# contact.set_name(name)

# phone = cb.setNewContactPhone()
# contact.set_phone(phone)

# cb.appendContact(contact)
