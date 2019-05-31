# OMDB Parser Tool

This repo contains the source code files required to access the Online Movie Databas website http://www.omdbapi.com through API calls and return the movie **rating** if the movie name is found in the database.  

**Pre-requisites:**  

**1. RHEL/CentOS 6.x**  
**2. Python 3.x**  
**3. Docker engine (needs RHEL/CentOS 7)**  
**4. omdb API access**;  
please register on the webpage ('http://omdbapi.com/') and get the API key after download: plase replace 'xxxxxx' with the actual api key in the file: omdbapi_keys.json  
```
[bash@localhost omdbapi]$ cat omdbapi_keys.json
{"api":"xxxxxx"}
```

**NOTE**: Tested the code under Centos 6.10, python 3.6.8, it may work with latest python versions.

## Docker Installation and Setup
RHEL 7 or Centos 7 is required.  
Please refer to the document here: https://docs.docker.com/install/linux/docker-ce/centos/  
After installation, make sure that docker is running correctly  
```
$ sudo docker run hello-world
```
if the above command runs correctly, docker is running correctly.  

### Docker Setup for OMDB API Tool
```
This directory contains a docker file called Dockerfile: 
$ cat Dockerfile 
FROM python:3
ADD omdbapi_keys.json /
ADD omdb.py /
CMD [ "python", "./omdb.py", "-m 'independence day'" ]
--
You can change the arguments as necessary later.

$ sudo docker build -t python-omdb -f ./Dockerfile  .

If the above command is successful, it would have created a docker image called: python-omdb. You can simply run the docker image as:

$ sudo docker run python-omdb

Output:
[bash@osboxes docker]$ sudo docker build -t python-omdb -f ./Dockerfile  . 
Sending build context to Docker daemon  6.656kB
Step 1/4 : FROM python:3
 ---> a4cc999cf2aa
Step 2/4 : ADD omdbapi_keys.json /
 ---> Using cache
 ---> db1fbe73540f
Step 3/4 : ADD omdb.py /
 ---> Using cache
 ---> 52b877d8fc58
Step 4/4 : CMD [ "python", "./omdb.py", "-m 'independence day'" ]
 ---> Running in 3330e66e84a8
Removing intermediate container 3330e66e84a8
 ---> f26415dad7ec
Successfully built f26415dad7ec
Successfully tagged python-omdb:latest
[bash@osboxes docker]$ sudo docker run python-omdb
movie name =   'independence day'
Retrieving the movie data of " 'independence day'" now… 
Rating is 7.0 
```
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
