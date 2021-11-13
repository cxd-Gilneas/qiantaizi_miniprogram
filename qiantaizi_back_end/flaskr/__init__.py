import os

from flask import Flask
from flask import request
from flask import send_file

# 应用工厂模式，在函数内部创建实例，而不是全局创建
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)  # 告诉应用程序配置文件是相对于 实例文件夹 的。实例文件夹位于flaskr包外部，可以保存本地数据，例如配置机密和数据库文件。
    app.config.from_mapping(  # 设置应用程序将使用的一些默认配置
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),  # 设置 SQLite 数据库文件的路径
    )

    from . import db  # 导入db.py
    db.init_app(app)  # 调用db.py中的init_app方法，可以完成数据库的初始化

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # 确保 app.instance_path存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    # 用户资料endpoint
    # R READ读取数据 /GET
    # C CREATE 创建数据 /POST
    # U UPDATE 更新数据 /PUT
    # D DELETE 删除数据 /DELETE

    @app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])  # 返回字典格式的数据，查看其自动转换为JSON格式
    def userprofile():
        taizi_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        taizi_time = ['first', 'second', 'third', 'forth']
        if request.method == 'GET':  # 用于获取实时台子量信息
            # 1 获取数据库连接
            connection = db.get_db()
            # 2 执行获取台子量信息的sql操作
            cursor = connection.cursor()
            monitoring_result = []

            for i in range(0, 7):
                result_dict = {"day": "", "first": "", "second": "", "third": "", "forth": ""}
                result_dict['day'] = taizi_day[i]
                for j in range(0, 4):
                    query = f"SELECT * FROM qiantaizi WHERE {taizi_day[i]}{taizi_time[j]} > 0"
                    cursor.execute(query)
                    results = cursor.fetchall()
                    if len(results) < 4:
                        result_dict[f'{taizi_time[j]}'] = 'success'
                    elif len(results) == 4:
                        result_dict[f'{taizi_time[j]}'] = 'info_circle'
                    elif len(results) > 4:
                        result_dict[f'{taizi_time[j]}'] = 'cancel'
                monitoring_result.append(result_dict)
            cursor.close()
            if len(monitoring_result) == 7:
                print("成功获取了一次实时台子量信息")
                return dict(success = True, message = "成功刷新", data = monitoring_result)
            else:
                return dict(success = False, message = "未知错误")


        elif request.method == 'POST':  # 用于录入个人姓名学号信息
            # 1 获取前端POST body中的数据  
            studentID = request.json.get('studentID')
            Name = request.json.get('Name')
            # 2 获取数据库连接
            connection = db.get_db()
            # 3 执行查询学号和姓名的相关的sql操作
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM qiantaizi WHERE studentID = '{studentID}' AND Name = '{Name}'")
            row = cursor.fetchone()  # 找到学号和姓名都匹配的第一个项目
            cursor.close()
            if row:
                return dict(success = False, message = "学号或姓名已存在")
            else:
                connection.execute(f'''INSERT INTO qiantaizi (studentID, Name) VALUES ('{studentID}', '{Name}')''')
                connection.commit()
                print(f"成功录入了{studentID}的个人信息")
                return dict(success = True, message = "信息提交成功")


        elif request.method == 'PUT':  # 用于提交个人签台子信息
            # 1 获取前端PUT body中的数据
            studentID = request.json.get('studentID')
            Name = request.json.get('Name')
            Money = request.json.get('Money')
            dict_day_time = {}
            for i in range (1, 7):
                dict_day_time[f'multiIndex{i}'] = request.json.get(f'multiIndex{i}')         
            # 2 获取数据库连接
            connection = db.get_db()
            # 3 执行查询学号和姓名的相关的sql操作
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM qiantaizi WHERE studentID = '{studentID}' AND Name = '{Name}'")
            row = cursor.fetchone()  # 找到学号和姓名都匹配的第一个项目
            cursor.close()
            if row:
                connection.execute(f'''UPDATE qiantaizi SET Money = 99.99, 
                                    Monfirst = 0,
                                    Monsecond = 0,
                                    Monthird = 0,
                                    Monforth = 0,
                                    Tuefirst = 0,
                                    Tuesecond = 0,
                                    Tuethird = 0,
                                    Tueforth = 0,
                                    Wedfirst = 0,
                                    Wedsecond = 0,
                                    Wedthird = 0,
                                    Wedforth = 0,
                                    Thufirst = 0,
                                    Thusecond = 0,
                                    Thuthird = 0,
                                    Thuforth = 0,
                                    Frifirst = 0,
                                    Frisecond = 0,
                                    Frithird = 0,
                                    Friforth = 0,
                                    Satfirst = 0,
                                    Satsecond = 0,
                                    Satthird = 0,
                                    Satforth = 0,
                                    Sunfirst = 0,
                                    Sunsecond = 0,
                                    Sunthird = 0,
                                    Sunforth = 0
                                    WHERE studentID = '{studentID}' ''')  # 对当前提交人的数据初始化
                connection.execute(f'''UPDATE qiantaizi SET Money = {Money} WHERE studentID = '{studentID}' ''')

                for i in range(1, 7):  # 遍历六个picker框的数据
                    if dict_day_time[f'multiIndex{i}'][0] != 0:  # 如果第i轮(第i个picker框)有签台子
                        if dict_day_time[f'multiIndex{i}'][0] == 1:  # 如果签的周一的台子
                            if dict_day_time[f'multiIndex{i}'][1] == 0:  # 如果签的8:00~10:30的台子
                                query_init = f'Monfirst = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 1:  # 如果签的12:00~14:30的台子
                                query_init = f'Monsecond = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 2:  # 如果签的16:00~18:30的台子
                                query_init = f'Monthird = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 3:  # 如果签的20:00~22:30的台子
                                query_init = f'Monforth = {i}'
                            
                        elif dict_day_time[f'multiIndex{i}'][0] == 2:  # 如果签的周二的台子
                            if dict_day_time[f'multiIndex{i}'][1] == 0:  # 如果签的8:00~10:30的台子
                                query_init = f'Tuefirst = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 1:  # 如果签的12:00~14:30的台子
                                query_init = f'Tuesecond = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 2:  # 如果签的16:00~18:30的台子
                                query_init = f'Tuethird = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 3:  # 如果签的20:00~22:30的台子
                                query_init = f'Tueforth = {i}'
                            
                        elif dict_day_time[f'multiIndex{i}'][0] == 3:  # 如果签的周三的台子
                            if dict_day_time[f'multiIndex{i}'][1] == 0:  # 如果签的8:00~10:30的台子
                                query_init = f'Wedfirst = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 1:  # 如果签的12:00~14:30的台子
                                query_init = f'Wedsecond = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 2:  # 如果签的16:00~18:30的台子
                                query_init = f'Wedthird = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 3:  # 如果签的20:00~22:30的台子
                                query_init = f'Wedforth = {i}'

                        elif dict_day_time[f'multiIndex{i}'][0] == 4:  # 如果签的周四的台子
                            if dict_day_time[f'multiIndex{i}'][1] == 0:  # 如果签的8:00~10:30的台子
                                query_init = f'Thufirst = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 1:  # 如果签的12:00~14:30的台子
                                query_init = f'Thusecond = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 2:  # 如果签的16:00~18:30的台子
                                query_init = f'Thuthird = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 3:  # 如果签的20:00~22:30的台子
                                query_init = f'Thuforth = {i}'

                        elif dict_day_time[f'multiIndex{i}'][0] == 5:  # 如果签的周五的台子
                            if dict_day_time[f'multiIndex{i}'][1] == 0:  # 如果签的8:00~10:30的台子
                                query_init = f'Frifirst = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 1:  # 如果签的12:00~14:30的台子
                                query_init = f'Frisecond = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 2:  # 如果签的16:00~18:30的台子
                                query_init = f'Frithird = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 3:  # 如果签的20:00~22:30的台子
                                query_init = f'Friforth = {i}'
                        
                        elif dict_day_time[f'multiIndex{i}'][0] == 6:  # 如果签的周六的台子
                            if dict_day_time[f'multiIndex{i}'][1] == 0:  # 如果签的8:00~10:30的台子
                                query_init = f'Satfirst = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 1:  # 如果签的12:00~14:30的台子
                                query_init = f'Satsecond = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 2:  # 如果签的16:00~18:30的台子
                                query_init = f'Satthird = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 3:  # 如果签的20:00~22:30的台子
                                query_init = f'Satforth = {i}'

                        elif dict_day_time[f'multiIndex{i}'][0] == 7:  # 如果签的周日的台子
                            if dict_day_time[f'multiIndex{i}'][1] == 0:  # 如果签的8:00~10:30的台子
                                query_init = f'Sunfirst = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 1:  # 如果签的12:00~14:30的台子
                                query_init = f'Sunsecond = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 2:  # 如果签的16:00~18:30的台子
                                query_init = f'Sunthird = {i}'
                            elif dict_day_time[f'multiIndex{i}'][1] == 3:  # 如果签的20:00~22:30的台子
                                query_init = f'Sunforth = {i}'

                        connection.execute(f'''UPDATE qiantaizi SET {query_init} WHERE studentID = '{studentID}' ''')
                        print(f'''UPDATE qiantaizi SET {query_init} WHERE Name = '{Name}' ''')
                        connection.commit()

                    else:  # 如果第i轮没有签台子
                        continue
                os.system("@copy instance\\flaskr.sqlite backup")
                print(f"成功录入了{studentID}的一次签台子信息")
                return dict(success = True, message = "信息提交成功")

            else:
                return dict(success = False, message = "学号或姓名不存在或不匹配")

    
    @app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])  # 管理员页面的登陆操作
    def login():
        if request.method == 'PUT':
            password = request.json.get('password')
            print(password)
            if password == '这里是你自己设置的密码':
                print("成功登录管理员界面")
                return dict(success = True)
            else:
                return dict(success = False)


    @app.route('/admin', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def admin():
        if request.method == 'POST':  # 管理员页面的数据初始化操作
            # 1 获取数据库连接
            connection = db.get_db()
            # 2 写初始化数据库的sql语句
            try:
                connection.execute('''UPDATE qiantaizi SET Money = 99.99, 
                                    Monfirst = 0,
                                    Monsecond = 0,
                                    Monthird = 0,
                                    Monforth = 0,
                                    Tuefirst = 0,
                                    Tuesecond = 0,
                                    Tuethird = 0,
                                    Tueforth = 0,
                                    Wedfirst = 0,
                                    Wedsecond = 0,
                                    Wedthird = 0,
                                    Wedforth = 0,
                                    Thufirst = 0,
                                    Thusecond = 0,
                                    Thuthird = 0,
                                    Thuforth = 0,
                                    Frifirst = 0,
                                    Frisecond = 0,
                                    Frithird = 0,
                                    Friforth = 0,
                                    Satfirst = 0,
                                    Satsecond = 0,
                                    Satthird = 0,
                                    Satforth = 0,
                                    Sunfirst = 0,
                                    Sunsecond = 0,
                                    Sunthird = 0,
                                    Sunforth = 0
                                    ''')
                connection.commit()
                print("成功进行了数据初始化")
                return dict(success = True)
            except:
                return dict(success = False)

        elif request.method == 'GET':  # 管理员页面的获取未签台子人员名单操作
            uncommitted = []
            # 1 获取数据库连接
            connection = db.get_db()
            # 2 写获得未签人员姓名的sql语句
            cursor = connection.cursor()
            cursor.execute('''SELECT Name FROM qiantaizi WHERE 
                            Monfirst = 0 AND
                            Monsecond = 0 AND
                            Monthird = 0 AND
                            Monforth = 0 AND
                            Tuefirst = 0 AND
                            Tuesecond = 0 AND
                            Tuethird = 0 AND
                            Tueforth = 0 AND
                            Wedfirst = 0 AND
                            Wedsecond = 0 AND
                            Wedthird = 0 AND
                            Wedforth = 0 AND
                            Thufirst = 0 AND
                            Thusecond = 0 AND
                            Thuthird = 0 AND
                            Thuforth = 0 AND
                            Frifirst = 0 AND
                            Frisecond = 0 AND
                            Frithird = 0 AND
                            Friforth = 0 AND
                            Satfirst = 0 AND
                            Satsecond = 0 AND
                            Satthird = 0 AND
                            Satforth = 0 AND
                            Sunfirst = 0 AND
                            Sunsecond = 0 AND
                            Sunthird = 0 AND
                            Sunforth = 0
                            ''')
            results = cursor.fetchall()
            try:
                for i in range(len(results)):
                    uncommitted.append(results[i][0])
                print("成功获取了未签台子人员名单")
                return dict(success = True, data = uncommitted)
            except:
                return dict(success = False)
        
        elif request.method == 'PUT':  # 管理员页面的获取签台子结果情况
            taizi_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            taizi_time = ['first', 'second', 'third', 'forth']
            # 1 获取数据库连接
            connection = db.get_db()
            cursor = connection.cursor()
            # 2 统计表格数据赋值给1024统计行
            for i in range(0, 7):
                for j in range(0, 4):
                    query = f"SELECT * FROM qiantaizi WHERE {taizi_day[i]}{taizi_time[j]} > 0 AND studentID is not 1024"
                    cursor.execute(query)
                    results = cursor.fetchall()
                    count = len(results)
                    connection.execute(f"UPDATE qiantaizi SET Money = 1024, {taizi_day[i]}{taizi_time[j]} = {count} WHERE studentID = 1024")  # 给每个时间点的台子数计数                    
            cursor.close()
            connection.commit()
            # 3 输出签台子结果
            import qiantaizi_4
            try:
                result_df, result_cuowei, result_sign_failed = qiantaizi_4.QIANTAIZI(connection)
                result_df.to_excel("qiantaizi_result.xlsx")
                print("成功输出了签台子的结果")
                return dict(success = True, data = [result_cuowei, result_sign_failed])
            except:
                return dict(success = False)

    @app.route('/check', methods=['PUT'])  # 首页获取本人当前签台子情况
    def check():
        # 1 获取前端PUT body中的数据
        studentID = request.json.get('studentID')
        Name = request.json.get('Name')
        # 2 获取数据库连接
        connection = db.get_db()
        # 3 执行查询学号和姓名的相关的sql操作
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM qiantaizi WHERE studentID = '{studentID}' AND Name = '{Name}'")
        row = cursor.fetchone()  # 找到学号和姓名都匹配的第一个项目
        cursor.close()
        taizi_day = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        taizi_time = ['8:00~10:30', '12:00~14:30', '16:00~18:30', '20:00~22:30']
        result = []                   
        if row:
            for i in range(0, 7):
                for j in range(0, 4):
                    if row[i*4+j+3] != 0:
                        result.append(f'第{row[i*4+j+3]}个台子：{taizi_day[i]}{taizi_time[j]}')
            print(f"成功输出了{studentID}的当前签台子情况")
            return dict(success = True, data = result)
        else:
            return dict(success = False, data = '姓名或学号不正确或不匹配')

            
    @app.route('/download', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def download():
        return send_file('C:\Program Files\website_qiantaizi\qiantaizi_result.xlsx', as_attachment=True)

    return app
