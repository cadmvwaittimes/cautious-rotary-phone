"""Defines the cron job for the cadmv package"""
import crontab


cron = crontab.CronTab(user=True)

py_exc = ('/home/pi/.local/share/virtualenvs/cadmvwaittimes-pg-oxgkURqM/'
          'bin/python')
script = '/home/pi/cadmv/cadmvwaittimes-pg/bin/wait_time_scraper.py'
command = f'{py_exc} {script}'

scraper_job = cron.new(command=command)
# Want to run this 
# - every 5 minutes from 0700 through 1700
# - every day of the week
# - every week of the month
# - every month of the year
# - on Monday through Saturday
schedule = '*/5 7-17 * * 1-6'
scraper_job.setall(schedule)

cron.write()

print(scraper_job.enable())
