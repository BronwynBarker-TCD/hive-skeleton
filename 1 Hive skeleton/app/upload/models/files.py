from flask import Markup, url_for
from flask_appbuilder.models.mixins import AuditMixin, FileColumn
from sqlalchemy import Column, Integer
from flask_appbuilder import Model
from flask_appbuilder.filemanager import get_file_original_name

"""
You can use the extra Flask-AppBuilder fields and Mixin's
AuditMixin will add automatic timestamp of created and modified by who
"""

class ProjectFiles(AuditMixin,Model):
    __tablename__ = "project_files"
    id = Column(Integer, primary_key=True)
    file = Column(FileColumn, nullable=False)

    def download(self):
        return Markup(
            '<a href="' + url_for('ProjectFilesModelView.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))
        