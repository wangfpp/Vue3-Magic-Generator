from flask import Flask
from flask_cors import CORS

from web.config import UPLOAD_FOLDER

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///test.db'  # 更换为您的数据库路径
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)


