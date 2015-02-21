from pymongo import MongoClient
from collections import Counter
from bson.json_util import dumps
import json, jebgrabber, re

db = jebgrabber.db.emails
"""
Need to remove articles and other useless words
check the length - just assuming 3 letters is sufficient
"""
def getCounter(text):
    counter = Counter()
    for word in text.split():
        counter[word] += 1
    return counter
    
def dateCounter(start_date, end_date):
    counter = Counter()
    for _date in jebgrabber.daterange(start_date, end_date):
        emails = db.find({'dateCentral': re.compile(_date.strftime("%Y-%m-%d"))})
        for email in emails:
            counter = counter + getCounter(email['message'])
    return counter

def getEmails(_date):
    emails = db.find({'dateCentral': re.compile(_date.strftime("%Y-%m-%d"))})
    return emails

def getEmailsFrom(start_date, end_date):
    for _date in jebgrabber.daterange(start_date, end_date):
        emails = db.find({'dateCentral': re.compile(_date.strftime("%Y-%m-%d"))})
    return emails

def getEmailsThatContain(text):
    text = "\\s*"+text+"\\s*"
    emails = db.find({'message': re.compile(text, re.IGNORECASE)}) 
    return emails

