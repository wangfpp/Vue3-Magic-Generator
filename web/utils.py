from sqlalchemy import inspect

from web.config import ALLOWED_EXTENSIONS


def get_foreign_keys_for_model(model):
    foreign_keys = []
    # 遍历所有列
    for column in model.__table__.columns:
        # 检查列是否有外键
        if column.foreign_keys:
            # 添加外键信息到列表
            foreign_keys.append(column)
    return foreign_keys


def get_primary_key_for_model(model):
    # 遍历所有列
    for column in model.__table__.columns:
        # 检查列是否有外键
        if column.primary_key:
            # 添加外键信息到列表
            return column


def serialize_model(model_instance):
    """
    自动化序列化 SQLAlchemy 模型实例到字典
    """
    if isinstance(model_instance, (set, list)):
        return [serialize_model(i) for i in model_instance]
    return {c.key: getattr(model_instance, c.key) for c in inspect(model_instance).mapper.column_attrs}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_primary_key_value_for_model(model):
    field_name = get_primary_key_for_model(model)
    if field_name is None:
        return None
    return field_name, model.__dict__[field_name]
