import os

from dotenv import load_dotenv
from flask import Flask

from models import db


load_dotenv()

app = Flask(__name__)
# SQLAlchemy 설정

# 내가 사용 할 DB URI
database_url = os.getenv('SQLALCHEMY_DATABASE_URI')
database_port = os.getenv('SQLALCHEMY_DATABASE_PORT')
database_schema = os.getenv('SQLALCHEMY_DATABASE_SCHEMA')
database_user = os.getenv('SQLALCHEMY_DATABASE_USERNAME')
database_password = os.getenv('SQLALCHEMY_DATABASE_PASSWORD')
database_uri = f"mysql+pymysql://{database_user}:{database_password}@{database_url}:{database_port}/{database_schema}"
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
# 비지니스 로직이 끝날때 Commit 실행(DB반영)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 수정사항에 대한 TRACK
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
db.app = app

with app.app_context():
    from models.static import *
    from models.dynamic import *
    db.create_all()

app.register_blueprint(api_blueprint)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
