<h1> Movie lookup web application </h1>
<h3> Easily find information on movies in one simple search </h3>

<h4>Setup</h4>
There are 2 main components that add need to be running in order to bring movie checker online. The REACT server (Front end), and the Flask server (API/Backend

See steps below for setup.

<h3>First setup your environment/installs</h3>
<h4>This project was built in a linux environment</h4>
<h4>Python packages required (installed with pip3)</h4>
<li>requests</li>
<li>tinydb</li>
<li>Flask</li>

Ensure you have nodejs installed so you can run the REACTjs server with 'npm start'

<h3>Front end (REACTjs server setup</h3>
On a separate terminal, navigate into the 'movie_lookup_react' folder and run the command 'npm start'. This creates the REACTjs web server and runs it locally on 0.0.0.0:3000

<code>
$: cd movie_lookup_react
$: npm start
</code>

<h3>API (Flask server setup)</h3>
Navigate into the 'api_movie_lookup' folder and run the command 'python3 movie_lookup_api.py'. This creates a flask server running on port 6000 (Note that the react server is proxied to this port so changing it may cause issues between the two services)

<h3>Database</h3>
For the database it is a lightweight json based python package called 'tinydb', there is no server or service required to run it. Just ensure you have it installed.
