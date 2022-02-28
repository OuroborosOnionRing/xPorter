from flask import Flask, render_template, request, flash
##Youtube imports
from pytube import YouTube
import os
import pafy
import regex
import tkinter as tk
from tkinter import filedialog
from tkinter import *
##instagram imports

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

import instaloader

###tiktok imports
from pathlib import Path
from TikTokApi import TikTokApi




app = Flask(__name__)
app.secret_key = "123456789"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/how')
def how():
    return render_template("how.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/socials')
def socials():
    return render_template('socials.html')


@app.route('/start')
def start():
    return render_template("start.html")


@app.route('/downloaded',methods=["GET","POST"])
def downloaded():
    root = tk.Tk()
    root.withdraw()


    if request.method=="GET":
        return render_template("no.html")

    #root = tk.Tk()
    #root.withdraw()
    ###code for form actions here
    types= request.form.get('type') ##type(mp3 or mp4)
    links=str(request.form.get('link')) ##this is the link given by the user
    print(regex)
    ######code to run the download here
    
    #for mp4
    if types =="YouVid" :
        
        yt=YouTube(links)
        ys = yt.streams.get_highest_resolution()
        path="downloads"
        #path = filedialog.askdirectory()
        ys.download(output_path = path, filename = yt.title + " .mp4 ")
        display = yt.title 
    

    #for mp3
    elif types=="YouAu":
        
        yt = YouTube(links)
        video=pafy.new(links)
        #path = filedialog.askdirectory()
        path="downloads"
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        display = yt.title 


    ########################################################################workspace for selenium cus i drivers has issues
    elif types=="insta":
        username = links
        instaloader.Instaloader().download_profile(username,profile_pic_only=False)
        display = links + "'s profile" 


    '''
  
    elif types =="tiktok":
        Path("videos").mkdir(exist_ok=True)
        api = TikTokApi.get_instance()
        results = 3
        trending = api.trending(count=results, custom_verifyFp="")
        for tiktok in trending:
	        video_url = 'https://www.tiktok.com/@%s/video/%s' % (tiktok['author']['uniqueId'], tiktok['id'])
	        data = api.get_video_no_watermark(video_url, return_bytes=1, language='en', proxy=None, custom_verifyFp="")
	        with open("videos/%s.mp4" % tiktok['id'], 'wb') as output:
		        output.write(data)
    


    '''
    
    return render_template("downloaded.html",headline = display)

app.run(debug=True,port=5000)


'''  
Note:if you still get an error to due to me forgetting what to install do drop me a message


$ pip install Flask
pip install TikTokApi
python -m playwright install
pip install beautifulsoup
pip install selenium
pip install tk
$ pip install pytube

'''