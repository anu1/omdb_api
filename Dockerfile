FROM python:3
ADD omdbapi_keys.json /
ADD omdb.py /
CMD [ "python", "./omdb.py", "-m 'independence day'" ]
