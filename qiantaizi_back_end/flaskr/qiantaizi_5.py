import numpy as np
import pandas as pd
import random
import warnings

# 下面是签五个台子的版本（如需修改，则需要修改time_shuffle中的list1和qiantaizi中每轮第二次签台子的range）

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

list_time_dic = {'Monfirst': '周一8点',
             'Monsecond': '周一12点',
             'Monthird': '周一16点',
             'Monforth': '周一20点',
             'Tuefirst': '周二8点',
             'Tuesecond': '周二12点',
             'Tuethird': '周二16点',
             'Tueforth': '周二20点',
             'Wedfirst': '周三8点',
             'Wedsecond': '周三12点',
             'Wedthird': '周三16点',
             'Wedforth': '周三20点',
             'Thufirst': '周四8点',
             'Thusecond': '周四12点',
             'Thuthird': '周四16点',
             'Thuforth': '周四20点',
             'Frifirst': '周五8点',
             'Frisecond': '周五12点',
             'Frithird': '周五16点',
             'Friforth': '周五20点',
             'Satfirst': '周六8点',
             'Satsecond': '周六12点',
             'Satthird': '周六16点',
             'Satforth': '周六20点',
             'Sunfirst': '周日8点',
             'Sunsecond': '周日12点',
             'Sunthird': '周日16点',
             'Sunforth': '周日20点'}


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
        list1 = [0, 4, 8, 12, 16]
        random.shuffle(list1)
    elif taizi_time[3:] == 'second':
        list1 = [1, 5, 9, 13, 17]
        random.shuffle(list1)
    elif taizi_time[3:] == 'third':
        list1 = [2, 6, 10, 14, 18]
        random.shuffle(list1)
    elif taizi_time[3:] == 'forth':
        list1 = [3, 7, 11, 15, 19]
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
                
                for k in range(0, 20):  # 本轮第二次签不论当日的哪一个台子，反正只要签上一个就行
                    if str(df2[taizi_day][k]) == ' ':  # 如果有空，直接填写名字
                        isSamePersonInSameTime = False  # 定义一个标签，用于看当前空位置的同时间段的其它位置是否被同一个人签了，签了则True，不进行下面的给台子操作，没签则False
                        for l in [-16, -12, -8, -4, 4, 8, 12, 16]:
                            try:
                                if(str(df2[taizi_day][k + l]) == name):
                                    isSamePersonInSameTime = True
                            except:
                                continue
                        if isSamePersonInSameTime == False:
                            df2[taizi_day][k] = name
                            df1[j][i] = -1  # 将已经填入的进行记录
                            cuowei.append(str(name + list_time_dic[j] + '第' + str(lunshu - 1) + '轮' + '错位'))
                            break
                if df1[j][i] == lunshu - 1:  # 真的签不上的情况下
                    sign_failed.append(str(name + list_time_dic[j] + '第' + str(lunshu - 1) + '轮' + '无'))

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
                    
                    for k in range(0, 20):  # 本轮第二次签不论当日的哪一个台子，反正只要签上一个就行,给其略差的台子
                        if str(df2[taizi_day][k]) == ' ':  # 如果有空，直接填写名字
                            isSamePersonInSameTime = False  # 定义一个标签，用于看当前空位置的同时间段的其它位置是否被同一个人签了，签了则True，不进行下面的给台子操作，没签则False
                            for l in [-16, -12, -8, -4, 4, 8, 12, 16]:
                                try:
                                    if(str(df2[taizi_day][k + l]) == name):
                                        isSamePersonInSameTime = True
                                except:
                                    continue
                            if isSamePersonInSameTime == False:
                                df2[taizi_day][k] = name
                                df1[j][i] = -1  # 将已经填入的进行记录
                                cuowei.append(str(name + list_time_dic[j] + '第' + str(lunshu) + '轮' + '错位'))
                                break
                    if df1[j][i] == lunshu - 1:  # 真的签不上的情况下
                        sign_failed.append(str(name + list_time_dic[j] + '第' + str(lunshu) + '轮' + '无'))





def polish(df):  # 把需要连台的同学的位置拼到一起 注意：该函数目前只能处理二连台，当遇见需要三连台或更多时，很可能出各种bug
    date = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i in range (0, 7):
        for m in [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14]:  # 首先查看某一时间点的后一个时间点是否有签台子（最后一个时间点被排除）
            flag = 0  # 定义一个标签，用于确定需要往后查看几个台子
            if m < 3:  
                flag = 4  # 当在为第一个台子拼接时，查看后面四个台子
            elif  m < 7:
                flag = 3  # 当在为第二个台子拼接时，查看后面三个台子
            elif  m < 11:
                flag = 2  # 当在为第三个台子拼接时，查看后面两个台子
            elif  m < 15:
                flag = 1  # 当在为第四个台子拼接时，查看后面一个台子
            if str(df[date[i]][m]) != ' ':  # 当该位置有人签时
                #region 避免打乱已有的连台region
                if m in set([0, 1, 4, 5, 8, 9, 12, 13]):  # 只有当想要换的隔壁时间段的台子可以组成连台时才进行下面的判断（即想要换的隔壁时间段的台子的下一个时间段是连续的）
                    if df[date[i]][m + 1] == df[date[i]][m + 2]:  # 如果想要换的隔壁时间段的台子本身是连台情况，则不换
                        continue
                #endregion 避免打乱已有的连台end
                for k in range(0, flag):  # 查看该时间点的后四（或三或二或一）个台子是否有可以拼接的连台
                    if df[date[i]][m] == df[date[i]][m + 5 + k*4]:  # 如果该时间点的后一个时间点有签台子，则将后一个时间点的两个台子名字交换
                        temp = df[date[i]][m + 1]
                        df[date[i]][m + 1] = df[date[i]][m + 5 + k*4]
                        df[date[i]][m + 5 + k*4] = temp
        for n in [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15]:  # 再查看某一时间点的前一个时间点是否有签台子（最前一个时间点被排除）
            flag = 0  # 定义一个标签，用于确定需要往后查看几个台子
            if n < 4:  
                flag = 4  # 当在为第一个台子拼接时，查看后面四个台子
            elif  n < 8:
                flag = 3  # 当在为第二个台子拼接时，查看后面三个台子
            elif  n < 12:
                flag = 2  # 当在为第三个台子拼接时，查看后面两个台子
            elif  n < 16:
                flag = 1  # 当在为第四个台子拼接时，查看后面一个台子
            if str(df[date[i]][n]) != ' ':  # 当该位置有人签时
                #region 避免打乱已有的连台region
                if n in set([2, 3, 6, 7, 10, 11, 14, 15]):  # 只有当想要换的隔壁时间段的台子可以组成连台时（即想要换的隔壁时间段的台子的上一个时间段是连续的）
                    if df[date[i]][n - 1] == df[date[i]][n - 2]:  # 如果想要换的目标台子本身是连台情况，则不换
                        continue
                #endregion 避免打乱已有的连台end
                for k in range(0, flag):  # 查看该时间点的后四（或三或二或一）个台子是否有可以拼接的连台
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

