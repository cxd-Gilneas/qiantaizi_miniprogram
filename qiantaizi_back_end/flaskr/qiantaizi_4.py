import numpy as np
import pandas as pd
import random
import warnings

# 下面是签四个台子的版本（如需修改，则需要修改time_shuffle中的list1和qiantaizi中每轮第二次签台子的range）

warnings.filterwarnings("ignore")  # 忽略警告信息

global list_time
list_time = ['Monfirst',
             'Monsecond',
             'Monthird',
             'Monforth',
             'Tuefirst',
             'Tuesecond',
             'Tuethird',
             'Tueforth',
             'Wedfirst',
             'Wedsecond',
             'Wedthird',
             'Wedforth',
             'Thufirst',
             'Thusecond',
             'Thuthird',
             'Thuforth',
             'Frifirst',
             'Frisecond',
             'Frithird',
             'Friforth',
             'Satfirst',
             'Satsecond',
             'Satthird',
             'Satforth',
             'Sunfirst',
             'Sunsecond',
             'Sunthird',
             'Sunforth']


def make_dict(dataf):  # 预先准备一个字典，将姓名作为key，是否有一天多个台子的情况作为value存入
    global dict_isMultiple
    dict_isMultiple = {}
    for i in range(0, dataf.shape[0] - 1):  
        a = str(dataf.loc[i, 'Name'])
        dict_isMultiple[a] = False  # 每个人的value用于记录是否存在一天签多个台子的情况，True为存在，False不存在
        date = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for j in range(0, 7):
            list_isMultiple = [dataf.loc[i, f'{date[j]}first'], dataf.loc[i, f'{date[j]}second'], dataf.loc[i, f'{date[j]}third'], dataf.loc[i, f'{date[j]}forth']]
            set_isMultiple=list(set(list_isMultiple))
            if 0 in set_isMultiple:
                set_isMultiple.remove(0)
            if len(set_isMultiple) >= 2:  # 存在一天多个台子的情况
                dict_isMultiple[a] = True
                break


def time_shuffle(taizi_time):  # 打乱台子排序，保证随机性
    global list1
    if taizi_time[3:] == 'first':
        list1 = [0, 4, 8, 12]
        random.shuffle(list1)
    elif taizi_time[3:] == 'second':
        list1 = [1, 5, 9, 13]
        random.shuffle(list1)
    elif taizi_time[3:] == 'third':
        list1 = [2, 6, 10, 14]
        random.shuffle(list1)
    elif taizi_time[3:] == 'forth':
        list1 = [3, 7, 11, 15]
        random.shuffle(list1)


def qiantaizi(lunshu):

    for i in range(0, df1.shape[0] - 1):  # 本轮首次签，给每个人确定的位置
        for j in list_time:  # 遍历28个时间点
            if df1.loc[i, j] == lunshu:
                taizi_day = j[0:3]  # taizi_day = 'Mon'/'Tue'……
                time_shuffle(j)
                name = str(df1.loc[i, 'Name'])

                isSigned = False  # 如果已经签了当天的台子，则利用isSigned=True的continue跳过
                for k in range(0, df2.shape[0]):  # 遍历查看当天的所有台子
                    if dict_isMultiple[name] == True:  # 如果标明了需要一天签多个台子，则不进行该检定
                        break
                    if str(df2.loc[k, taizi_day]) == name:
                        isSigned = True
                        break
                if isSigned == True:  # 已经签了当天的台子，跳过
                    continue

                for k in list1:  # 有空台子的情况
                    if str(df2[taizi_day][k]) == ' ':  # 如果有空，直接填写名字
                        df2[taizi_day][k] = name
                        df1[j][i] = -1  # 将已经填入的进行记录
                        break

    for i in range(0, df1.shape[0] - 1):  # 本轮第二次签，给上一轮没有签上的人一个同日的任意位置
        for j in list_time:
            if df1.loc[i, j] == lunshu - 1 and df1.loc[i, j] != 0:
                taizi_day = j[0:3]  # taizi_day = 'Mon'/'Tue'……
                time_shuffle(j)
                name = str(df1.loc[i, 'Name'])

                isSigned = False  # 如果已经签了当天的台子，则利用isSigned=True的continue跳过
                for k in range(0, df2.shape[0]):  # 遍历查看当天的所有台子
                    if dict_isMultiple[name] == True:  # 如果标明了需要一天签多个台子，则不进行该检定
                        break
                    if str(df2.loc[k, taizi_day]) == name:
                        df1[j][i] = -1  # 保险起见，将之前已经填入的再次进行记录
                        isSigned = True
                        break
                if isSigned == True:  # 已经签了当天的台子，跳过
                    continue
                
                for k in range(15, -1, -1):  # 本轮第二次签不论当日的哪一个台子，反正只要签上一个就行,给其略差的台子
                    if str(df2[taizi_day][k]) == ' ':  # 如果有空，直接填写名字
                        df2[taizi_day][k] = name
                        df1[j][i] = -1  # 将已经填入的进行记录
                        cuowei.append(str(name + j + '第' + str(lunshu - 1) + '轮' + '错位'))
                        break
                if df1[j][i] == lunshu:  # 真的签不上的情况下
                    sign_failed.append(str(name + j + '第' + str(lunshu - 1) + '轮' + '无'))

    if lunshu == 6:  # 最后一轮的第二次签（上一个循环中的第二次签是倒数第二轮的，所以这里要补一个最后一轮的第二次签）
        for i in range(0, df1.shape[0] - 1):  # 最后一轮第二次签，给上一轮没有签上的人一个同日的任意位置
            for j in list_time:
                if df1.loc[i, j] == lunshu:  # 最后一轮第二次签，给最后一轮没有签上的人一个同日的任意位置
                    taizi_day = j[0:3]  # taizi_day = 'Mon'/'Tue'……
                    time_shuffle(j)
                    name = str(df1.loc[i, 'Name'])

                    isSigned = False  # 如果已经签了当天的台子，则利用isSigned=True的continue跳过
                    for k in range(0, df2.shape[0]):  # 遍历查看当天的所有台子
                        if dict_isMultiple[name] == True:  # 如果标明了需要一天签多个台子，则不进行该检定
                            break
                        if str(df2.loc[k, taizi_day]) == name:
                            df1[j][i] = -1  # 保险起见，将之前已经填入的再次进行记录
                            isSigned = True
                            break
                    if isSigned == True:  # 已经签了当天的台子，跳过
                        continue
                    
                    for k in range(15, -1, -1):  # 本轮第二次签不论当日的哪一个台子，反正只要签上一个就行,给其略差的台子
                        if str(df2[taizi_day][k]) == ' ':  # 如果有空，直接填写名字
                            df2[taizi_day][k] = name
                            df1[j][i] = -1  # 将已经填入的进行记录
                            cuowei.append(str(name + j + '第' + str(lunshu) + '轮' + '错位'))
                            break
                    if df1[j][i] == lunshu:  # 真的签不上的情况下
                        sign_failed.append(str(name + j + '第' + str(lunshu) + '轮' + '无'))


def polish(df):  # 把需要连台的同学的位置拼到一起 注意：该函数目前只能处理二连台，当遇见需要三连台或更多时，很可能出各种bug
    date = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i in range (0, 7):
        for m in [0, 1, 2, 4, 5, 6, 8, 9, 10]:  # 首先查看某一时间点的后一个时间点是否有签台子（最后一个时间点被排除）
            flag = 0  # 定义一个标签，用于确定需要往后查看几个台子
            if m < 3:  
                flag = 3  # 当在为第一个台子拼接时，查看后面三个台子
            elif  m < 7:
                flag = 2  # 当在为第二个台子拼接时，查看后面两个台子
            elif  m < 11:
                flag = 1  # 当在为第三个台子拼接时，查看后面一个台子
            if str(df[date[i]][m]) != ' ':  # 当该位置有人签时
                for k in range(0, flag):  # 查看该时间点的后三（或二或一）个台子是否有可以拼接的连台
                    if df[date[i]][m] == df[date[i]][m + 5 + k*4]:  # 如果该时间点的后一个时间点有签台子，则将后一个时间点的两个台子名字交换
                        temp = df[date[i]][m + 1]
                        df[date[i]][m + 1] = df[date[i]][m + 5 + k*4]
                        df[date[i]][m + 5 + k*4] = temp
        for n in [1, 2, 3, 5, 6, 7, 9, 10, 11]:  # 再查看某一时间点的前一个时间点是否有签台子（最前一个时间点被排除）
            flag = 0  # 定义一个标签，用于确定需要往后查看几个台子
            if n < 4:  
                flag = 3  # 当在为第一个台子拼接时，查看后面三个台子
            elif  n < 8:
                flag = 2  # 当在为第二个台子拼接时，查看后面两个台子
            elif  n < 12:
                flag = 1  # 当在为第三个台子拼接时，查看后面一个台子
            if str(df[date[i]][n]) != ' ':  # 当该位置有人签时
                for k in range(0, flag):  # 查看该时间点的后三（或二或一）个台子是否有可以拼接的连台
                    if df[date[i]][n] == df[date[i]][n + 3 + k*4]:  # 如果该时间点的前一个时间点有签台子，则将前一个时间点的两个台子名字交换
                        temp = df[date[i]][n - 1]
                        df[date[i]][n - 1] = df[date[i]][n + 3 + k*4]
                        df[date[i]][n + 3 + k*4] = temp
            

# -------------------------
def QIANTAIZI(connection):
    dataresult = []
    error_number = []

    DF1 = pd.read_sql_query("SELECT * FROM qiantaizi ORDER BY Money ASC", connection)
    DF2 = pd.read_sql_query("SELECT * FROM qiantaizi_template", connection)
    global cuowei
    global sign_failed
    cuowei = []
    sign_failed = []

    global df1
    df1 = DF1.copy()
    global df2
    df2 = DF2.copy()

    make_dict(df1)  # 记录相关信息存入字典

    for j in range(1, 7):  # 签6轮台子(小程序设置了一个人最多签6个台子，所以最多六轮)
        qiantaizi(j)

    print(df2)
    
    polish(df2)  # 为可以二连台的同学调整为连台

    result_df = df2.copy()
    print(result_df)
    print(cuowei)
    print(sign_failed)

    return result_df, cuowei, sign_failed

# -------------------------

