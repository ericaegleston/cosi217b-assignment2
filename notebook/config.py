import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = ('99ffb6903f691d6b3aa9d205a9684b7'
                  '875a39883c37e27a03bcaad6cf82b8aaf')
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or
                               'sqlite:///' + os.path.join(basedir, 'app.db'))
