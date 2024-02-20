import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from web.flaskapp import app
from web.utils import get_primary_key_value_for_model, get_primary_key_for_model

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    created_by = db.Column(db.String)
    created_at = db.Column(db.Text, default=db.func.datetime('now', 'localtime'))
    updated_by = db.Column(db.String)
    updated_at = db.Column(db.Text, default=db.func.datetime('now', 'localtime'))
    status = db.Column(db.Integer, default=1)


class ImageCollection(db.Model):
    __tablename__ = 'image_collections'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    is_top = db.Column(db.Integer)
    created_by = db.Column(db.String)
    created_at = db.Column(db.Text, default=db.func.datetime('now', 'localtime'))
    updated_by = db.Column(db.String)
    updated_at = db.Column(db.Text, default=db.func.datetime('now', 'localtime'))


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_by = db.Column(db.String)
    created_at = db.Column(db.Text, default=db.func.datetime('now', 'localtime'))
    updated_by = db.Column(db.String)
    updated_at = db.Column(db.Text, default=db.func.datetime('now', 'localtime'))


class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    bio = db.Column(db.Text)
    artists_url = db.Column(db.String)
    created_by = db.Column(db.String)
    created_at = db.Column(db.Text, default=db.func.datetime('now', 'localtime'))
    updated_by = db.Column(db.String)
    updated_at = db.Column(db.Text, default=db.func.datetime('now', 'localtime'))


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    image_collection_id = db.Column(db.Integer, db.ForeignKey('image_collections.id'))
    url = db.Column(db.String, nullable=False)
    created_by = db.Column(db.String)
    created_at = db.Column(db.Text, default=db.func.datetime('now', 'localtime'))
    updated_by = db.Column(db.String)
    updated_at = db.Column(db.Text, default=db.func.datetime('now', 'localtime'))


class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    filename = db.Column(db.String(120), nullable=False)
    date_uploaded = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"File('{self.uuid}', '{self.filename}')"


models = {
    'user': User,
    'image_collection': ImageCollection,
    'category': Category,
    'artist': Artist,
    'image': Image,
}

models_translate = {
    'image_collection': [
        {"table": "image", "dst": "images"},
        {"table": "artist", "dst": "artists"},
    ],
}


def save_or_update(item: db.Model):
    pk = get_primary_key_for_model(item)
    if pk is not None and pk.name in item.__dict__:
        d = item.__dict__
        val = d.get(pk.name)
        d.pop('_sa_instance_state', None)
        item.query.filter_by(**{pk.name: val}).update(d)
    else:
        db.session.add(item)


def clear_not_in_table_filed(table, form: dict):
    col = [i.name for i in models[table].__table__.columns]
    [form.pop(i) for i in [k for k in form.keys() if k not in col]]


def save_form_config(form_config):
    '''
    c = {"table": "image_collection", "form": {"title": "1"},
         "children": [{"table": "image", "form": {"url": "cccccccccc"}}]}
    :param form_config:
    :return:
    '''
    try:
        clear_not_in_table_filed(form_config["table"], form_config["form"])
        item = models[form_config["table"]](**form_config["form"])
        save_or_update(item)
        db.session.commit()
        cid = item.id
        for i in form_config['children']:
            i["form"][form_config["table"] + '_id'] = str(cid)
            clear_not_in_table_filed(i["table"], i["form"])
            item = models[i["table"]](**i["form"])
            save_or_update(item)
        return cid
    except Exception as e:
        db.session.rollback()
        raise e
