# -*- coding: utf-8 -*-

import logging
import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


# ------------------------------------------ api ------------------------------------------
@app.route("/api/detect_EPISODE_num", methods=['GET', 'POST'])
def overview():
    url="https://www.cartoonmad.com/comic/1221.html"
    r = requests.get(url)
    r.encoding = 'big5'

    soup = BeautifulSoup(r.text, 'html.parser')


    #str = soup.find_all('table').prettify()
    result = soup.find_all('table', attrs={"width":800})
    #logging.debug(str)
    #logging.debug(type(result) )

    result_list = []
    #for x in result:
    #    result_list.append(str(x))

    result_list.append(str(result[1]))
    r2=''.join(result_list)
#=========================

    soup2 = BeautifulSoup(r2, 'html.parser')
    result2=soup2.find_all('a', href=True)


    result_list2 = []
    for x in result2:
        result_list2.append(str(x.getText()))
        #result_list2.append('<br>')




    #return ''.join(result_list2)

    return render_template('detect_EPISODE_num.html', result_list=result_list2)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True,host='0.0.0.0')