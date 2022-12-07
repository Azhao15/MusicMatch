import string
import random

from flask import (
    Blueprint, flash, redirect, render_template, request, session
)
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
from musicproject.database import db_session

from sqlalchemy import update

from musicproject.auth import login_required
from musicproject.helpers import find_song, find_song_with_artist, find_image_from_song

from csv import DictReader

bp = Blueprint('application', __name__, url_prefix='/', static_url_path='')
extensions = ['.jpg', '.png', '.gif', '.jpeg']


# open file in read mode
with open("musicproject/input/data.csv", 'r') as f:
    dict_reader = DictReader(f)
    data = list(dict_reader)


@bp.route("/home", methods = ["GET"])
@login_required
def home():
    """ Render home page """

    return render_template("home.html")


@bp.route("/profile", methods = ["GET"])
@login_required
def profile():
    """ Render profile page """

    # query for user data
    user = db_session.execute("SELECT * FROM users WHERE id = :id", {'id':session['user_id']}).first()

    return render_template("profile.html", user=user)


@bp.route("/recommender", methods = ["GET", "POST"])
@login_required
def recomender():
    """ Recommend a song """

    if request.method == "GET":
        return render_template("recommender.html")

    else:
        # store user input
        name = request.form.get("song")
        artist = request.form.get("artist")

        # check that all fields are filled
        if not name:
            flash("Must submit song name.")
            return render_template("recommender.html")
        elif not artist:
            flash("Must submit artist name.")
            return render_template("recommender.html")
        
        # query song data from song name and artist
        song_info = find_song_with_artist(name, artist)
        
        # check if song exists:
        if song_info == None:
            flash("Sorry, couldn't find that song! Please try another")
            return render_template("recommender.html")

        # query for song attributes
        danceability = float(song_info['danceability'])
        energy = float(song_info['energy'])
        key = int(song_info['key'])
        loudness = float(song_info['loudness'])
        acousticness = float(song_info['acousticness'])
        valence = float(song_info['valence'])
        tempo = float(song_info['tempo'])

        
        # set range variables
        sensitivity = .25
        tempo_range = 10

        recommendation_list = []

        # add song to recommendation list if the attributes are within the range
        for song in data:
            if (
                abs(float(song['danceability']) - danceability) < sensitivity and
                abs(float(song['energy']) - energy) < sensitivity and 
                int(song['key']) == key and
                abs(float(song['loudness']) - loudness) < sensitivity and
                abs(float(song['acousticness']) - acousticness) < sensitivity and
                abs(float(song['valence']) - valence) < sensitivity and 
                abs(float(song['tempo']) - tempo) < tempo_range and
                song['name'] != song_info['name']
                ):
                    recommendation_list.append(song)

        # choose a random song in the recommendation list
        n = len(recommendation_list) - 1
        rand = random.randint(0, n)
        recommended_song = recommendation_list[rand]

        # get artists from recommended song
        artists = list(recommended_song['artists'].replace("[","").replace("]","").replace("'","").split(","))

        # get the image url for the song
        img_url = find_image_from_song(recommended_song['name'], artists[0])

        # render recommendation page
        return render_template("recommendation.html", recommended_song=recommended_song, artists=artists, img_url=img_url)


@bp.route("/sentencer", methods = ["GET", "POST"])
@login_required
def sentencer():
    """ Find songs for each word """

    if request.method == "GET":
        return render_template("sentencer.html")
    
    else:
        # get sentence input from user
        sentence = request.form.get("sentence")

        # check that user entered sentence
        if not sentence:
            flash("Must provide sentence.")
            return redirect("/sentencer")
        
        # input each word of the sentence into a list
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        sentenceList = sentence.split(" ")

        # input the song data from the word's song into a list
        songList = []
        for word in sentenceList:
            if find_song(word) == None:
                flash("Sorry, couldn't find a song for a word! Please try another sentence!")
                return render_template("sentencer.html")
            else:
                songList.append(find_song(word))


        # render results page
        return render_template("results.html", songList = songList)
