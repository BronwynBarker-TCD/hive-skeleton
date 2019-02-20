# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 08:48:34 2019

@author: Tanzelle.Oberholster
"""

import os 
import pandas as pd
from app.merge.controller import UPLOAD_FOLDER

#Merging script

def compute_function(filename1,filename2):
    #Read in files as .csv
    File1 = pd.read_csv(os.path.join(UPLOAD_FOLDER , filename1),
                        header=[0], keep_default_na=False, na_values=[''])
    
    File2 = pd.read_csv(os.path.join(UPLOAD_FOLDER , filename2),
                        header=[0], keep_default_na=False, na_values=[''])
    #Formating & CLeaning

    #File1 = File1.apply(lambda x: x.str.strip() if x.dtyFile1=='object' else x) #remove trailing whitespaces
    #File2 = File2.apply(lambda x: x.str.strip() if x.dtyFile2=='object' else x)

    #Merge datasets

    Merged = pd.merge(File1, File2)
    
    #Write csv file
    
    Merged.to_csv('Merged.csv', sep=',', encoding='utf-8')

     

