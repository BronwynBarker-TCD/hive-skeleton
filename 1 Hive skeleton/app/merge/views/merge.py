# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 07:06:46 2019

@author: Tanzelle.Oberholster
"""
from app import appbuilder
from flask import request, send_from_directory, send_file
from flask_appbuilder import SimpleFormView
from flask_babel import lazy_gettext as _
import os
from werkzeug import secure_filename

from app.merge.forms.merge import MergeFilesForm
from app.merge.controller import allowed_file, UPLOAD_FOLDER
from app.merge.script import compute_function

class MergeFilesFormView(SimpleFormView):
    form = MergeFilesForm
    form_title = 'Select 2 Files to Merge'
    filename = None

    def form_get(self, form):
        form.file1.data = 'file1'
        form.file2.data = 'file2'

    def form_post(self, form):
        # Save uploaded file on server if it exists and is valid
        #if request.method == 'POST':
            file1 = request.files['file1']
            file2 = request.files['file2']
                # Make a valid version of filename for any file ystem
            if file1 and allowed_file(file1.filename):
                    filename1 = secure_filename(file1.filename)
                    file1.save(os.path.join(UPLOAD_FOLDER , filename1))

            if file2 and allowed_file(file2.filename):
                    filename2 = secure_filename(file2.filename)
                    file2.save(os.path.join(UPLOAD_FOLDER , filename2))

            result = compute_function(filename1,filename2)
            return send_from_directory(UPLOAD_FOLDER,filename='Merged.csv')
            return send_file(UPLOAD_FOLDER, attachment_filename='Merged.csv')
          
appbuilder.add_view(MergeFilesFormView, "Select Files", icon="fa-plus", label=_('Select Files'),
                     category="Merge")