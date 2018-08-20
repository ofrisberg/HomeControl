import os,sys,configparser

"""
Generate and get config file
https://docs.python.org/3/library/configparser.html
"""
def generate():
	cfg = configparser.ConfigParser()
	
	cfg['GENERAL'] = {}
	
	cfg['PATHS'] = {
		'ROOT_DIR' : os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')),
		'DATA_DIR' : os.path.join('${root_dir}','data'),
		'SRC_DIR' : os.path.join('${root_dir}','src'),
		'WEB_DIR' : os.path.join('${src_dir}','web'),
	}
	
	cfg['MODES'] = {
		'STRICT' : 'off',
		'QUIET' : 'off',
		'VERBOSE' : 'off'
	}
	
	cfg['SPOTIFY'] = {
		'USERNAME' : '',
		'ID' : '',
		'SECRET' : '',
		'REDIRECT_URL' : '',
		'PERMISSIONS' : "user-library-read playlist-read-private user-read-playback-state user-modify-playback-state user-top-read"
	}
	
	cfg['CONTACTS'] = {
		'CSV_FILE' : os.path.join('${data_dir}','contacts.csv'),
	}
	
	cfg['MESSENGER'] = {
		'EMAIL' : '',
	}
	
	
	filename = getFilename()
	with open(filename, 'w') as configfile:
		cfg.write(configfile)
	
def get():
	cfg = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
	filename = getFilename()
	if os.path.isfile(filename): 
		cfg.read(filename)
		return cfg
	print("Error: Could not find config file '"+ filename +"'")
	sys.exit()

def getFilename():
	return os.path.join(os.path.dirname( __file__ ), '..', 'config.ini')
	
if __name__ == '__main__':
	input("Press enter if you want to overwrite old config file")
	generate()
	
	
	
	
	