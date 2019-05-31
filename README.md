# OMDB Parser Tool

This repo contains the source code files required to access the Online Movie Databas website http://www.omdbapi.com through API calls and return the movie **rating** if the movie name is found in the database.  

**Pre-requisites:**  

**1. RHEL/CentOS 6.x**  
**2. Python 3.x**  
**3. omdb API access**;  
please register on the webpage ('http://omdbapi.com/') and get the API key after download: plase replace 'xxxxxx' with the actual api key in the file: omdbapi_keys.json  
```
[bash@localhost omdbapi]$ cat omdbapi_keys.json
{"api":"xxxxxx"}
```

**NOTE**: Tested the code under Centos 6.10, python 3.6.8, it may work with latest python versions.
## Sample Usage

```
bash$ git clone git@github.com:anu1/omdb_api.git
bash$ cd omdb_api

[bash@localhost omdbapi]$ python omdb.py  
missing movie argument
$ python  omdb.py [-h] <-m movie-name>
for example: $ python  omdb.py -m "Independence day"
for example: $ python  omdb.py -m Matrix

[bash@localhost omdbapi]$ python omdb.py  -h
Usage: $ python  omdb.py [-h] <-m movie-name>

[bash@localhost omdbapi]$ python omdb.py  -m joy
movie name =  joy
Retrieving the movie data of "joy" now… 
Rating is 6.6 

[bash@localhost omdbapi]$ python omdb.py  -m 'the mathematician'
movie name =  the mathematician
Retrieving the movie data of "the mathematician" now… 
Rating is N/A 

### NOTE: If your API key is invalid, you may get an error as follows:
$ python omdb.py -m test
movie name =  test
Retrieving the movie data of "test" now… 
ERROR: Unauthorized
