import itertools
import os

from flask import request, jsonify
from flask import send_from_directory
from werkzeug.utils import secure_filename

from web.flaskapp import app
from web.model import File, models, db, save_form_config, models_translate
from web.utils import serialize_model, get_primary_key_for_model


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # 创建文件记录
        new_file = File(filename=filename)
        db.session.add(new_file)
        db.session.commit()

        return jsonify({'message': 'File uploaded successfully', 'uuid': new_file.uuid}), 201


@app.route('/download/<uuid>')
def download_file(uuid):
    file_record = db.session.query(File).filter_by(uuid=uuid).first()
    if file_record is None:
        return jsonify({'error': 'File not found'}), 404

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_record.filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File does not exist'}), 404

    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], path=file_record.filename, as_attachment=True)


@app.route('/common/<table>/<method>', methods=['POST'])
def api(table, method):
    model = models.get(table.lower())

    if not model:
        return jsonify({'error': 'Table not found'}), 404

    data = request.json

    orderby = data.pop('orderby', [])

    if method == 'add':
        item = model(**data)
        db.session.add(item)
        try:
            db.session.commit()
            return jsonify({'success': True, 'id': item.id})
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400

    elif method == 'delete':
        item = model.query.filter_by(**data).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'Item not found'}), 404

    elif method == 'update':
        conditions = data.pop('conditions', None)
        res = get_primary_key_for_model(model)
        if res is not None:
            conditions = conditions if conditions else {}
            conditions = {**conditions, res: data[res]}
        if not conditions:
            return jsonify({'error': 'No conditions provided'}), 400
        item = model.query.filter_by(**conditions).first()
        if item:
            for key, value in data.items():
                setattr(item, key, value)
            db.session.commit()
            return jsonify({'success': True, 'id': item.id})
        else:
            return jsonify({'error': 'Item not found'}), 404

    elif method == 'query':
        query = model.query.filter_by(**data)
        for i in orderby:
            query = query.order_by(getattr(getattr(model, i['column']), i.get('sort', 'asc'))())
        items = query.all()
        res = serialize_model(items)
        translate_dict(table, res)
        return jsonify({'success': True, 'data': res})
    elif method == 'page':
        page = data.pop('page', 1)
        query = model.query.filter_by(**data)
        for i in orderby:
            query = query.order_by(getattr(getattr(model, i['column']), i.get('sort', 'asc'))())
        pages = query.paginate(page=page)
        res = serialize_model(pages.items)
        translate_dict(table, res)
        return jsonify({'success': True,
                        'data': {"items": res, "total": pages.total, "page": pages.page}})
    else:
        return jsonify({'error': 'Invalid method'}), 400


def translate_dict(table_name, items: list[dict]):
    if table_name not in models_translate:
        return
    ids = [i['id'] for i in items]
    main_model = models[table_name]
    for i in models_translate[table_name]:
        model = models.get(i['table'])
        if hasattr(model, table_name + '_id'):
            li = model.query.filter(getattr(model, table_name + '_id').in_(ids)).all()
            grouped = itertools.groupby(li, key=lambda x: getattr(x, table_name + '_id'))
            d = {g[0]: serialize_model(list(g[1])) for g in grouped}
            for j in items:
                j[i['dst']] = d.get(j['id'])
        if hasattr(main_model, i['table'] + "_id"):
            li = model.query.filter(getattr(model, 'id').in_([j[i['table'] + "_id"] for j in items])).all()
            d = {getattr(j, 'id'): serialize_model(j) for j in li}
            for j in items:
                j[i['dst']] = d.get(j[i['table'] + "_id"])


@app.route('/save_form_config', methods=['POST'])
def save_form_by_config():
    id = save_form_config(request.json)
    try:
        db.session.commit()
        return jsonify({'success': True, 'id': id})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 确保所有表都创建了
        app.run(debug=True)
