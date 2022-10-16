from apscheduler.schedulers.blocking import BlockingScheduler
import requests

def my_job():
    requests.post('https://ziaode.ren:5000/admin')

sched = BlockingScheduler()
sched.add_job(my_job, 'cron', day_of_week = 'wed', hour = 8)  # 每周周三的8点自动进行初始化
sched.start()
