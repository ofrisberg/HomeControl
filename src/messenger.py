from fbchat import Client
from fbchat.models import *

## Messenger wrapper
#  https://fbchat.readthedocs.io/en/master/

class Messenger(object):
	def __init__(self,email,pwd=None):
		self.email = email
		self.pwd = pwd
		self.client = None
		if pwd is not None:
			self.client = Client(email, pwd)
	
	def isOnline(self): return self.client.isLoggedIn()
	
	def login(self,pwd=None): 
		if pwd is None:
			self.client.login(self.email,self.pwd)
		else:
			self.pwd = pwd
			self.client = Client(self.email,self.pwd)
			
	def searchUsers(self,search_query): return self.client.searchForUsers(search_query,limit=5)
	
	def send(self,messenger_id,message): return self.client.send(Message(text=message), thread_id=messenger_id, thread_type=ThreadType.USER)
	
	def getLast(self,th): return self.client.fetchThreadMessages(thread_id=th, limit=1)[0]
	
	def logout(self):self.client.logout()
	
	def __str__(self):return "Messenger<uid:"+str(self.client.uid)+">"
	
if __name__ == '__main__':
	email = input("Email: ")
	pwd = input("Password: ")
	m = Messenger(email,pwd)
	
	m_id = input("Receiver: ")
	msg = input("Message: ")
	m.send(m_id,msg)