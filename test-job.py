"""Defines the cron job for the cadmv package"""
import crontab


cron = crontab.CronTab(user=True)

py_exc = '/home/pi/.local/share/virtualenvs/cronjobs-UootRD-S/bin/python'
script = '/home/pi/python/cronjobs/test.py'
command = f'{py_exc} {script}'

test_job = cron.new(command=command)
# Want to run this 
# - every 5 minutes from 0700 through 1700
# - every day of the week
# - every week of the month
# - every month of the year
# - on Monday through Saturday
test_job.minute.during(

cron.write()

print(scraper_job.enable())
