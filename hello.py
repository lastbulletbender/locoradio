import player
import songs
import picontrol

from flask import Flask,url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def indexpage():
	return render_template('hello.html')

@app.route('/start/<song>')
def startradio(song):
	player.start(song)
	return render_template('start.html')

@app.route('/stop/')
def stopradio():
	player.stop()
	return render_template('hello.html')

@app.route('/shutdown/')
def shutdown():
	picontrol.shutdown()

@app.route('/songs/')
def printdir():
	song_list = songs.get_songs_list()
	return render_template('songs.html',music = song_list)

