import sys
sys.path.append('../../AndroidCOM/src')
import androidcom

class Android(androidcom.AndroidCOM):

	def __init__(self):
		super().__init__()
		
		
if __name__ == '__main__':
	a = Android()
	print(a.statusPower())