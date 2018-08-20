import os,sys

## The contact class
#  

class Contact():
	def __init__(self,nick_name,full_name,phone_nr,email,messenger_id):
		self.nick_name = nick_name
		self.full_name = full_name
		self.phone_nr = phone_nr
		self.email = email
		self.messenger_id = messenger_id
		
	def __str__(self):
		return "Contact-object ("+self.getNickName()+")"
		
	def getNickName(self): return self.nick_name
	def getFullName(self): return self.full_name
	def getPhoneNr(self): return self.phone_nr
	def getEmail(self): return self.email
	def getMessengerId(self): return self.messenger_id
	
	def toDict(self):
		return {
			'nick_name':self.getNickName(),
			'full_name':self.getFullName(),
			'phone_nr':self.getPhoneNr(),
			'email':self.getEmail(),
			'messenger_id':self.getMessengerId(),
		}
	
if __name__ == '__main__':
	c = Contact('john','john doe','','john@doe.se','')
	print(c)
	print(c.toDict())