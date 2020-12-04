#!/usr/bin/python3

from tinydb import TinyDB, Query
from flask import Flask, jsonify, request
import requests

"""
    I was originally going to use some database server like MySQL or MongoDB but tinyDB is cool
    and is simple enough to just be integrated directly into the API script

    it also makes setup really simple for someone testing this out locally
"""
# initialize the app and also our 'database'
db = TinyDB('ratings.json')
app = Flask(__name__)


@app.route('/ratings', methods=['POST'], strict_slashes=False)
def get_ratings():
    """ get_ratings
         this route is used to populate each movie entry with
         the pre-existing ratings data

         for updating and changing like count, see routes 'dislike' and 'like'
    """
    q_id = Query()
    response = request.json['imdb_id']

    # IF it doesnt exist, create a blank one (Makes things easier on front end)
    if (db.search(q_id.imdb_id == response) == []):
        db.insert({'imdb_id': response, 'likes': 0, 'dislikes': 0})

    # Search and return the first entry under that ID
    return db.search(q_id.imdb_id == response)[0]


@app.route('/like', methods=['POST'], strict_slashes=False)
def like_movie():
    """ like
         This route updates the number of likes on an IMDB_ID entry
         if the entry does not exist or has no rating, it creates
         its own
    """
    q_id = Query()
    response = request.json['imdb_id']

    # If the value does not exist, create an entry for it
    if (db.search(q_id.imdb_id == response) == []):
        db.insert({'imdb_id': response, 'likes': 0, 'dislikes': 0})

    # Increase the number of likes by 1
    db.update({'likes': db.search(q_id.imdb_id == response)[0]['likes'] + 1}, q_id.imdb_id == response)

    # Return the entry we just updated
    return db.search(q_id.imdb_id == response)[0]

@app.route('/dislike', methods=['POST'], strict_slashes=False)
def dislike_movie():
    """ dislike
         This route updates the number of dislikes on an IMDB_ID entry
         if the entry does not exist or has no rating, it creates
         its own
    """
    q_id = Query()
    response = request.json['imdb_id']

    # If the value does not exist, create an entry for it
    if (db.search(q_id.imdb_id == response) == []):
        db.insert({'imdb_id': response, 'likes': 0, 'dislikes': 0})

    # Increase the number of dislikes by 1
    db.update({'dislikes': db.search(q_id.imdb_id == response)[0]['dislikes'] + 1}, q_id.imdb_id == response)

    # Return the entry we just updated
    return db.search(q_id.imdb_id == response)[0]

@app.route('/search_movie', methods=['POST'], strict_slashes=False)
def search_movies():
    """
        search_movies
        This interacts with the IMDB api to find the 10 most relevent
        movie titles, then using those IDs it gathers more information
        for the front end to use. This is possible in REACTjs but its easier
        in python to organize all the data and simplify to one API call on the
        front end
    """

    url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
    querystring = {"title": request.json['movie'],"type":"get-movies-by-title"}

    headers = {
        'x-rapidapi-key': "0221aebcd3msh363781e70cd07ebp148bb9jsn9a8731204b28",
        'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
    }
    """
        First search for all related titles, unfortunately the data from this search
        is missing some information. To solve this we can search each movie by its 
        IMDB id, which contains info about a movie such as director, description, etc
    """
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()

    """
        this api is limited to only 500 calls a month before they begin charging by call
        so i need to limit the amount of calls. Rather than searching for more info on all
        50 movies im going to limit that number to just the top 10.

        first loop just creates a list of IDs we can lookup
    """
    movie_ids = {}
    for idx in range(0, 10):
        if (idx < len(response['movie_results'])):
            movie_ids[response['movie_results'][idx]['title']] = response['movie_results'][idx]


    movie_info = {}
    data = []
    """
        Search up information on each ID and include it in a dictionary
        key it by name
    """
    for m_id in movie_ids.values():
        querystring = {"imdb":m_id['imdb_id'],"type":"get-movie-details"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()
        data.append(response)

    movie_info['data'] = data
    return movie_info

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='6000', threaded=True)
