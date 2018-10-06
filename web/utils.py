# -*- coding: utf-8 -*-

import logging
import os
import requests
import shutil
def download_util(url, epi_folder, idx, FilenameExtension):
    try:
        if not os.path.exists('./img/' + epi_folder):
            os.makedirs('./img/' + epi_folder)
        myPath = os.path.abspath('./img/' + epi_folder)
        fullfilename = os.path.join(myPath, idx)
        fullfilename+=FilenameExtension
        #url="S"
        #logging.debug("FFF: ",fullfilename)

        #================================================================= todo Connection problem
        headers = {
            'Connection': 'close'
        }

        #response = requests.get(url, stream=True, headers=headers)
        #response = requests.get(url, headers=headers)
        #response = requests.get(url, stream=True)
        #=================================================================

        with requests.get(url, stream=True) as response:
            with open(fullfilename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)

        return url+"download ok!\n"+"To "+fullfilename

        #urllib.request.urlretrieve(url, fullfilename)
    except Exception as e:
        errMsg="Exception: " + str(e) + " at " + url
        logging.debug(errMsg)
        global running
        running = False

        return errMsg
