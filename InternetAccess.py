from urllib.request import urlopen

with urlopen("https://www.google.com") as content:
    for line in content:
        print (line)