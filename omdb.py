#!/usr/bin/python

# python code to extract movie rating info from omdb.com webserver
# include all the libraries
import urllib.parse
import urllib.request
import json
import pprint
import sys
import getopt

# main function to begin the execution
def main(argv):
    moviename = ''
    
    # check/process the arguments
    if len(argv) == 0:
        print("missing movie argument")
        print("$ python  %s [-h] <-m movie-name>" %sys.argv[0])
        print("for example: $ python  %s -m \"Independence day\"" %sys.argv[0])
        print("for example: $ python  %s -m Matrix" %sys.argv[0])
        sys.exit(2)
    try:
       opts, args = getopt.getopt(argv,"hm:",["movie="])
    except getopt.GetoptError:
        print("Incorrect arguments")
        print("Usage: $ python  %s [-h] <-m movie-name>" %sys.argv[0])
        print("for example: $ python  %s -m \"Independence day\"" %sys.argv[0])
        print("for example: $ python  %s -m Matrix" %sys.argv[0])
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: $ python  %s [-h] <-m movie-name>" %sys.argv[0])
            sys.exit()
        elif opt in ("-m", "--movie"):
            moviename = arg
        else:
            print("Incorrect arguments")
            print("Usage: $ python  %s [-h] <-m movie-name>" %sys.argv[0])
            sys.exit()
    print(f"movie name =  {moviename}")

    # get the API key value
    with open('omdbapi_keys.json') as fp:
        keys = json.load(fp)
        omdbapi = keys['api']

    omdburl = 'http://www.omdbapi.com/?'
    apikey = '&apikey='+omdbapi

    # get the movie details
    get_movie_details(omdburl,apikey,moviename)
    sys.exit(0)

# function to extract the movie details from omdbapi.com website
def get_movie_details(omdburl,apikey,title):
    if len(title) < 1 or title=='quit': 
        print("exiting...")
        return None
    try:
        url = omdburl + urllib.parse.urlencode({'t': title})+apikey
        print(f'Retrieving the movie data of "{title}" now… ')
        uh = urllib.request.urlopen(url)
        data = uh.read()
        json_data=json.loads(data)
 
        if json_data['Response']=='True':
            #pprint.pprint(json_data)
            print("Rating is %s " %json_data['imdbRating'])
            #pprint.pprint(json_data)
            #print(json.dumps(json_data, sort_keys=True))

        else:
            print(f"Movie \'{title}\' is NOT FOUND, please try again")

    except urllib.error.URLError as e:
        print(f"ERROR: {e.reason}")

if __name__ == "__main__": main(sys.argv[1:])

exit(0)
