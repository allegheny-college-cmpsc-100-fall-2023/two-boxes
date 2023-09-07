import re
import requests
import json
import sys

trinket_type = "glowscript"
try: 
    #get url from LINK.md
    file = open('LINK.md', 'r')
    file = file.read()
    #get all urls from file
    url = re.search('trinket.io/.*', file).group(0)
    #if url contains paren, remove it and all characters after it
    if ')' in url:
        url = url[:url.index(')')]

    #if url contains ], remove it and all characters after it
    if ']' in url:
        url = url[:url.index(']')]

    #if url format is https://trinket.io/library/trinkets/*, cnage it to https://trinket.io/python/*
    if 'library/trinkets' in url:
        url = url.replace('library/trinkets', trinket_type)


    #if last character in url is not alphanumeric, remove it
    if not url[-1].isalnum():
        url = url[:-1]

    #format url to embed link so python from editor can be scraped
    #insert "embed/" between "trinket.io/" and "python /"
    url = 'https://' + url[:11] + "embed/" + url[11:]
    print(url)

    #get the html from the url
    html = requests.get(url).text

    #get trinketObject.content from html 
    trinketObject = re.search('trinketObject = (.*);', html).group(1)
    trinketObject = json.loads(trinketObject)
    python = trinketObject['code']

    #write python from editor to file
    f = open("main.py", "w")
    f.write(str(python))
    f.close()
except:
    print("link unavailable or invalid")

