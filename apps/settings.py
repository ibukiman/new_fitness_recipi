import os

basedir = os.path.dirname(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.sqlite')

SECRET_KEY = os.urandom(10)

from pathlib import Path

UPLOAD_FOLDER = str(Path(basedir,'apps','images'))