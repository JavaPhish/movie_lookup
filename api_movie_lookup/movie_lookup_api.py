#!/usr/bin/python3


from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/search_movie', methods=['POST'], strict_slashes=False)
def search_movies():

    url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
    querystring = {"title": request.json['movie'],"type":"get-movies-by-title"}

    headers = {
        'x-rapidapi-key': "YOU NEED TO GET YOUR OWN API KEY.",
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
