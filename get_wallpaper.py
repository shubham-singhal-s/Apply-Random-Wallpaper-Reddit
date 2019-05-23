import praw
import urllib
from random import randint
import ctypes, os

subReddit = "multiwall"
tag = "Dual"

reddit = praw.Reddit(client_id='vXbBf3rtaMrYtw', client_secret='tczE75Ap7PxjR_kio5NBALDhiI4', user_agent='wallpaper_dual')
hot_posts = reddit.subreddit(subReddit).top(limit=400)
arr = []
for x in hot_posts:
    if ('png' in x.url or 'jpg' in x.url) and x.link_flair_text==tag:
        arr.append(x)

x = arr[randint(0, len(arr) - 1)]
try:
        fName = x.url.split('/')[-1]
        if fName not in os.listdir('.'):
                f = open(fName,'wb')
                print("Downloading Wallpaper")
                f.write(urllib.request.urlopen(x.url).read())
                path = f.name
                f.close()
        else:
                print("Using previous file")
                path = "./"+fName
except Exception as e:
        print("error: "+str(e))

ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(path), 3)
