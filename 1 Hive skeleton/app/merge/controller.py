# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 07:51:34 2019

@author: Tanzelle.Oberholster
"""
import os
from config import UPLOAD_FOLDER

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

# Allowed file types for file upload
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

def allowed_file(filename):
    """Does filename have the right extension?"""
    return '.' in filename
    filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS