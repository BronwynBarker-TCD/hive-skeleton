import datetime
from flask import Markup, url_for
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, DateTime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from flask_appbuilder.filemanager import get_file_original_name

"""
You can use the extra Flask-AppBuilder fields and Mixin's
AuditMixin will add automatic timestamp of created and modified by who
"""

class Project(AuditMixin, Model):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)


class ProjectFiles(AuditMixin,Model):
    __tablename__ = "project_files"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship("Project")
    #user_name = Column(Integer, ForeignKey('ab_user.id'), default=id, nullable=True)
    file = Column(FileColumn, nullable=False)
    #date_upload = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    description = Column(String(150))

    def download(self):
        return Markup(
            '<a href="' + url_for('ProjectFilesModelView.download', filename=str(self.file)) + '">Download</a>')

    def file_name(self):
        return get_file_original_name(str(self.file))
        