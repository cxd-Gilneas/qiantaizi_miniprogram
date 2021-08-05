import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


# 连接数据库
def get_db():
    if 'db' not in g:  # g 是一个特殊对象，对于每个request请求都是唯一的。它用于存储在请求期间可能被多个函数访问的数据。如果get_db在同一request请求的生命周期中第二次调用该连接，则该连接将被存储和重用，而不是创建新连接。
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],  # current_app是另一个特殊对象，指向处理请求的 Flask 应用程序。由于使用了应用程序工厂，因此在编写其余代码时没有应用程序对象。 get_db将在应用程序创建并处理请求时调用，因此current_app可以使用。
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row  # sqlite3.Row告诉连接返回类似于 dicts 的行。这允许按名称访问列。

    return g.db

# 初始化数据库
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:  # open_resource()打开一个与flaskr包相关的sql语句文件。get_db 返回一个数据库连接，用于执行从文件中读取的sql命令。
        db.executescript(f.read().decode('utf8'))  # 执行SQL语句

# 关闭数据库
def close_db(e=None):
    db = g.pop('db', None)  # 删除 g 的 key 为db的值，并返回赋值给 db， 如果没有找到‘db’，则返回None

    if db is not None:  # 如果存在 db，则关闭数据库
        db.close()

@click.command('init-db')  # 使用 @click.command() 装饰下面的函数，使之成为命令行接口，命令名默认为原函数名‘init-db-command’（下划线改为横杠），但此处传递了第一个参数‘init-db’，使得命令名变为‘init-db’
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')  # 可以理解为有更好兼容性的print()

# 注册应用程序
def init_app(app):
    app.teardown_appcontext(close_db)  # 声明了当这个app被销毁的时候需要的动作：关闭数据库连接
    app.cli.add_command(init_db_command)  # 添加了一个可以用flask命令调用的新命令。这样就可以通过命令行>flask init-db来激活数据库的初始化