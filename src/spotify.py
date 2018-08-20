import sys,spotipy,configsetup
import spotipy.util as util
import fire

## Spotify wrapper
#  https://spotipy.readthedocs.io/en/latest/
#  https://stackoverflow.com/questions/47028093/attributeerror-spotify-object-has-no-attribute-current-user-saved-tracks

class Spotify():
	def __init__(self):
		self.username = None
		self.token = None
		self.sp = None
		
	def login(self,username,id,secret,redirect_url,permissions):
		self.username = username
		self.token = util.prompt_for_user_token(username,permissions,client_id=id,client_secret=secret,redirect_uri=redirect_url)
		self.sp = spotipy.Spotify(auth=self.token)
		
	def getActiveSong(self):
		resp = self.sp.currently_playing()
		if resp is not None: return resp['item']['name']
		else: return "No active song"
		
	def pause(self): self.sp.pause_playback()
	
	def play(self): self.sp.start_playback()
	
	def playPrevious(self): self.sp.previous_track()
	
	def playNext(self): self.sp.next_track()
	
	def setVolume(self,val): self.sp.volume(val)
	
	def showToplist(self):
		resp = self.sp.current_user_top_tracks()
		for item in resp['items']: print(item['name'])
		
	def playTrack(self,track_id):
		uri = "spotify:track:"+track_id
		self.sp.start_playback(uris=[uri])
		
	def searchTrack(self,search_query):
		resp = self.sp.search(search_query, limit=1, offset=0, type='track')
		if resp['tracks']['total'] == 1: return resp['tracks']['items'][0]
		else: return None
	
	def getDevices(self): return self.sp.devices()['devices']
		
	def changeDevice(self,device_id): self.sp.transfer_playback(device_id, force_play=True)
	
	def getPlaylists(self):
		playlists = self.sp.user_playlists(self.username)
		res = []
		for playlist in playlists['items']:
			if playlist['owner']['id'] == self.username:
				res.append({'id':playlist['id'],'name':playlist['name'],'nr_tracks':playlist['tracks']['total']})
		return res
		
	def getPlaylistTracks(self,playlist_id):
		results = self.sp.user_playlist(self.username, playlist_id,fields="tracks,next")
		tracks = results['tracks']
		res = []
		firstIter = True
		while tracks['next'] or firstIter:
			firstIter = False
			if tracks['next']: tracks = sp.next(tracks)
			for i, item in enumerate(tracks['items']):
				track = item['track']
				if track['id'] is not None:
					res.append({
						'id':track['id'],
						'name':track['name'],
						'artist':track['artists'][0]['name'],
						'album':track['album']['name'],
						'duration':track['duration_ms']
					})
		print(str(len(res)) + " - "+playlist_id)
		return res
		
def build(cfg):
	s = Spotify()
	s.login(cfg['username'],cfg['id'],cfg['secret'],cfg['redirect_url'],cfg['permissions'])
	"""
	sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=cfg['id'],client_secret=cfg['secret'],redirect_uri=cfg['redirect_url'],scope=cfg['permissions'])
	token_info = sp_oauth.get_cached_token() 
	if not token_info:
		auth_url = sp_oauth.get_authorize_url(show_dialog=True)
		print(auth_url)
		response = input('Paste the above link into your browser, then paste the redirect url here: ')

		code = sp_oauth.parse_response_code(response)
		token_info = sp_oauth.get_access_token(code)

		token = token_info['access_token']

	sp = spotipy.Spotify(auth=token)
	s.sp = sp
	s.login(cfg['username'],cfg['id'],cfg['secret'],cfg['redirect_url'],cfg['permissions'])
	"""
	
	return s
		
if __name__ == '__main__':
	cfg = configsetup.get()['SPOTIFY']
	s = build(cfg)
	fire.Fire(s)
	
	
	
	
	
	
	