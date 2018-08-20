from apistar import App, Route, http
import configsetup,spotify,contactlist,messenger

class MainDash():
	def __init__(self):
		self.cfg = configsetup.get()
		self.s = spotify.build(self.cfg['SPOTIFY'])
		self.m = messenger.Messenger(self.cfg['MESSENGER']['email'])
	
		
def SpotifyAPI(query_params: http.QueryParams):
	params = dict(query_params)
	action = params['action']
	
	if action == 'play': md.s.play()
	elif action == 'playtrack': md.s.playTrack(params['value'])
	elif action == 'playnext': md.s.playPrevious()
	elif action == 'playprevious': md.s.playNext()
	elif action == 'pause': md.s.pause()
	elif action == 'setvolume': md.s.setVolume(int(params['value']))
	elif action == 'getactivesong': return {'active_song': md.s.getActiveSong()}
	elif action == 'getplaylists': return {'playlists': md.s.getPlaylists()}
	elif action == 'getplaylisttracks': return {'playlist_tracks': md.s.getPlaylistTracks(params['value'])}
	
def ContactListAPI(query_params: http.QueryParams):
	cl = contactlist.ContactList('../data/contacts.csv')
	cl.loadContacts()
	contacts = cl.getContacts()
	out = []
	for c in contacts: out.append(c.toDict())
	return out
	
def MessengerAPI(query_params: http.QueryParams):
	params = dict(query_params)
	if 'messenger_id' in params and 'text_message' in params:
		md.m.send(params['messenger_id'],params['text_message'])
	elif 'pwd' in params:
		md.m.login(params['pwd'])
	else:
		print("No API match")

def indexhtml():
	spotify_html = ''
	with open('spotify.html', 'r') as file: 
		spotify_html += file.read()
	messenger_html = ''
	with open('messenger.html', 'r') as file: 
		messenger_html += file.read()
	settings_html = ''
	with open('settings.html', 'r') as file: 
		settings_html += file.read()
	
	index_content = ''
	with open('web/index.html', 'r') as file: 
		index_content += file.read()
	result = index_content.replace('[spotify_html]',spotify_html)
	result = result.replace('[messenger_html]',messenger_html)
	result = result.replace('[settings_html]',settings_html)
	return result
	
def appjs():
	with open('web/app.js', 'r') as file: return file.read()
	
routes = [
	Route('/index.html', method='GET', handler=indexhtml),
	Route('/app.js', method='GET', handler=appjs),
	Route('/api/spotify/', method='GET', handler=SpotifyAPI),
	Route('/api/contactlist/', method='GET', handler=ContactListAPI),
	Route('/api/messenger/', method='GET', handler=MessengerAPI),
]
web_dir = configsetup.get()['PATHS']['web_dir']
app = App(routes=routes, static_dir=web_dir, static_url='/web/')

if __name__ == '__main__':
	md = MainDash()
	app.serve('127.0.0.1', 80, debug=True)

	