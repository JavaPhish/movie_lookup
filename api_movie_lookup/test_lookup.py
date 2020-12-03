import requests

url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"

querystring = {"type":"get-boxoffice-movies","page":"1"}

headers = {
    'x-rapidapi-key': "0221aebcd3msh363781e70cd07ebp148bb9jsn9a8731204b28",
    'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)