"""Check what jobs are running"""
import crontabs


for cron in crontabs.CronTabs():
    # print(repr(cron))
    print(cron)
