# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:55:36 2019

@author: Tanzelle.Oberholster
"""
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView
from app.upload.models.files import ProjectFiles
from app import appbuilder, db
from flask_appbuilder.actions import action
from flask import redirect

class ProjectFilesModelView(ModelView):
    datamodel = SQLAInterface(ProjectFiles)

    label_columns = {'created_on': 'Date Upload', 'file_name': 'File Name', 'download': 'Download', 'created_by': 'User'}
    add_columns = ['file']
    edit_columns = ['file']
    list_columns = ['file_name','created_by','created_on', 'download']
    show_columns = ['file_name','created_by','created_on', 'download']

    @action("muldelete", "Delete", "Confirm Multi-Delete?", "fa-times")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())

db.create_all()

appbuilder.add_view(ProjectFilesModelView, "List Files", icon="fa-table", category="Uploads")