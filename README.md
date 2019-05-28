# OMDB Parser Package

This repo contains the source code files required to access the Online Movie Database 
website http://www.omdbapi.com through API call and returns the movie rating if the movie name is found in the database. 
Pre-Requisites:
<br>
CentOS 6.x
<br>
python 3.x
<br>omdb API access, please register on the webpage ('http://omdbapi.com/') and get the API key
after download: plase replace 'xxxxxx' with the actual api key in the file: omdbapi_keys.json
<br>[bash@localhost omdbapi]$ cat omdbapi_keys.json 
<br>{"api":"xxxxxx"}
<br>
<br>NOTE: Tested the code under Centos 6.10, python 3.6.8, it may work with latest python versions.
<br>
Sample Usage
<br>bash$ git clone <repo>
<br>
<br>bash$ cd omdb_api
<br>[bash@localhost omdbapi]$ python omdb.py  
<br>missing movie argument
<br>$ python  omdb.py [-h] <-m movie-name>
<br>for example: $ python  omdb.py -m "Independence day"
<br>for example: $ python  omdb.py -m Matrix
<br>[bash@localhost omdbapi]$ python omdb.py  -h
<br>Usage: $ python  omdb.py [-h] <-m movie-name>
<br>[bash@localhost omdbapi]$ python omdb.py  -m joy
<br>movie name =  joy
<br>Retrieving the movie data of "joy" now… 
<br>Rating is 6.6 
<br>[bash@localhost omdbapi]$ python omdb.py  -m 'the mathematician'
<br>movie name =  the mathematician
<br>Retrieving the movie data of "the mathematician" now… 
<br>Rating is N/A 
<br>---
<br>NOTE: If your API key is invalid, you may get an error as follows:
<br>$ python omdb.py -m test
<br>movie name =  test
<br>Retrieving the movie data of "test" now… 
<br>ERROR: Unauthorized
