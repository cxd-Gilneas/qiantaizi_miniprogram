from apscheduler.schedulers.blocking import BlockingScheduler
import requests

def my_job():
    requests.post('https://ziaode.ren:5000/admin')

sched = BlockingScheduler()
sched.add_job(my_job, 'cron', day_of_week = 'wed', hour = 8, misfire_grace_time = 3600)  # 每周周三的8点自动进行初始化，并给一个缓冲响应时间（这里设置了3600s，其实没必要，60s即可），避免因为响应过晚导致任务不执行
sched.start()
