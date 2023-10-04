#newsletters/tasks.py

from apscheduler.schedulers.background import BackgroundScheduler
from .models import process_newsletters

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(process_newsletters, 'interval', minutes=1)
    scheduler.start()
