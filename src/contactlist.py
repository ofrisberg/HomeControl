import os,sys,csv,fire
from contact import Contact

## The contact list class
#  manages Contact-objects

class ContactList():
	def __init__(self,csv_file):
		self.csv_file = csv_file
		self.contacts = []
		
	def loadContacts(self):
		filereader = csv.reader(open(self.csv_file,newline=''), delimiter=",")
		header = next(filereader)
		for nick_name,full_name,phone_nr,email,messenger_id in filereader:
			contact = Contact(nick_name,full_name,phone_nr,email,messenger_id)
			self.contacts.append(contact)
	
	def getContacts(self):
		return self.contacts
		
	def getContactByNickName(self,nick_name):
		for contact in self.contacts:
			if nick_name == contact.getNickName():
				return contact
		return None
		
	
	
if __name__ == '__main__':
	cl = ContactList('../data/contacts.csv')
	cl.loadContacts()
	fire.Fire(cl)