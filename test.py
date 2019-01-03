"""Test script for cron jobs"""
import datetime

text = open('test.txt', 'w')

# Write the time
now = datetime.datetime.utcnow()
text.write(now)
text.close()
