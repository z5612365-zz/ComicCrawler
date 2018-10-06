# -*- coding: utf-8 -*-

import logging
import requests
import shutil
from bs4 import BeautifulSoup
import os
import time
import json

from utils import *


from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


# ------------------------------------------ api ------------------------------------------
#post url:https://www.cartoonmad.com/comic/1221.html to 192.168.99.100:5000/api/detect_EPISODE_num
@app.route("/api/detect_EPISODE_num", methods=['POST'])
def detect_EPISODE_num():

    if request.method == 'POST':
        url=request.form.get('url')

        r = requests.get(url)
        r.encoding = 'big5'

        #search table
        soup = BeautifulSoup(r.text, 'html.parser')
        result = soup.find_all('table', attrs={"width":800})
        result_list = []
        result_list.append(str(result[1]))
        r2=''.join(result_list)

        #search somthing has <a> tag and href, and that's our EPISODE num
        soup2 = BeautifulSoup(r2, 'html.parser')
        result2=soup2.find_all('a', href=True)

        result_list2 = []
        for x in result2:
            result_list2.append( {str(x.getText()):x['href'] }  )

        #return render_template('detect_EPISODE_num.html', result_list=result_list2)
        json_str = json.dumps(result_list2, ensure_ascii=False).encode('utf8')
        return json_str

#post url:https://www.cartoonmad.com/comic/122100002035001.html to 192.168.99.100:5000/api/get_EPISODE_head_img
@app.route("/api/get_EPISODE_head_img", methods=['POST'])
def get_EPISODE_img():

    if request.method == 'POST':
        url=request.form.get('url')

        r = requests.get(url)
        r.encoding = 'big5'

        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img', attrs={"oncontextmenu":'return false'})

        result_list = []
        for image in images:
            #print image source
            print( image['src'] )

            result_list.append(image['src'])

        json_str = json.dumps(result_list)
        #return render_template('get_EPISODE_head_img.html', result_list=json_str)
        return json_str


"""
@app.route("/api/get_EPISODE_head_img", methods=['GET', 'POST'])
def get_EPISODE_img():

    url = "https://www.cartoonmad.com/comic/122100002035001.html"

    r = requests.get(url)
    r.encoding = 'big5'

    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img', attrs={"oncontextmenu":'return false'})

    result_list = []
    for image in images:
        #print image source
        print( image['src'] )

        result_list.append(image['src'])

    json_str = json.dumps(result_list)
    #return render_template('get_EPISODE_head_img.html', result_list=json_str)
    return json_str

"""

#from_EPISODE = '1',end_EPISODE = '2'from_EPISODE
'''
@app.route("/api/download/<imgUrl>/<from_EPISODE>/<end_EPISODE>", methods=['GET', 'POST'])
def download(imgUrl, from_EPISODE, end_EPISODE):

    download_util(url=imgUrl, epi_folder=EPISODE, idx=img_string)

    return render_template('download.html')
'''

@app.route("/api/download", methods=['GET', 'POST'])
def download():
    EPISODE='001'
    img_string='001'
    FilenameExtension=".jpg"
    imgUrl = "http://web1.cartoonmad.com/c37sn562e81/1221/" + EPISODE + "/" + img_string + FilenameExtension

    Msg=download_util(url=imgUrl, epi_folder=EPISODE, idx=img_string, FilenameExtension=FilenameExtension)

    #return render_template('download.html')
    return Msg


"""
    for EPISODE_int in range(int(from_EPISODE), int(end_EPISODE) + 1):

        EPISODE = fix_int_to_string(EPISODE_int)
        print('--- EPISODE:' + EPISODE + ' ---')

        running = True
        for x in one_to_infinity():
            if running == False:
                break

            img_string = fix_int_to_string(x)
            imgUrl = "http://web1.cartoonmad.com/c26vn522e83/1221/" + EPISODE + "/" + img_string + ".jpg"
            print('--- EPISODE:' + EPISODE + ' --- IMAGE:' + img_string)
            download(url=imgUrl, epi_folder=EPISODE, idx=img_string)
            time.sleep(0.2)

"""


# time.sleep( 0.2 )

    # ===========================================

def one_to_infinity():
    i = 1
    while True:
        yield i
        i += 1

# have bug when return str
# TypeError: can only concatenate str (not "NoneType") to str
def fix_int_to_string(x):
    if len(str(x)) == 1:
        fix_str = '00' + str(x)
        return fix_str

    elif len(str(x)) == 2:
        fix_str = '0' + str(x)
        return fix_str



#===========================================

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    app.run(debug=True,host='0.0.0.0')