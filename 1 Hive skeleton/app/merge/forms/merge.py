# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 07:05:56 2019

@author: Tanzelle.Oberholster
"""

from wtforms import Form, FileField
from wtforms.validators import InputRequired
from flask import Markup, url_for
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

class MergeFilesForm(DynamicForm):
    file1 = FileField(('File 1'),
                      validators = [InputRequired()])
    file2 = FileField(('File 2'),
                      validators = [InputRequired()])

def download(self):
        return Markup(
            '<a href="' + url_for('MergeFilesFormView.download', filename=str(self.file)) + '">Download</a>')

def file_name(self):
    return get_file(str('Merged.csv'))