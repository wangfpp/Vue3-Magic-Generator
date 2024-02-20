create_table_to_models = '''
请将建表语句转换为python模型
建表语句
```
{{create_table}}
```

回答样例
```
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# 必须与您的数据模型匹配
models = {
    'user': User,
    # 在这里添加更多表模型
}
```

你的回答
'''