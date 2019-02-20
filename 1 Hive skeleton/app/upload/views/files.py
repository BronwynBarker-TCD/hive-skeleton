# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:55:36 2019

@author: Tanzelle.Oberholster
"""
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView, CompactCRUDMixin
from app.upload.models.files import Project, ProjectFiles
from app import appbuilder, db

class ProjectFilesModelView(ModelView):
    datamodel = SQLAInterface(ProjectFiles)

    label_columns = {'created_on': 'Date Upload', 'file_name': 'File Name', 'download': 'Download', 'created_by': 'User'}
    add_columns = ['file','description']
    edit_columns = ['file','description']
    list_columns = ['file_name','created_by','created_on', 'download']
    show_columns = ['file_name','created_by','created_on', 'download']


class ProjectModelView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(Project)
    related_views = [ProjectFilesModelView]

    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'

    add_columns = ['name']
    edit_columns = ['name']
    list_columns = ['name', 'created_by', 'created_on', 'changed_by', 'changed_on']
    show_fieldsets = [
        ('Info', {'fields': ['name']}),
        ('Audit', {'fields': ['created_by', 'created_on', 'changed_by', 'changed_on'], 'expanded': False})
    ]


db.create_all()

appbuilder.add_view(ProjectModelView, "List Folders", icon="fa-table", category="Uploads")
appbuilder.add_view(ProjectFilesModelView, "List Files", icon="fa-table", category="Uploads")