#!/bin/python

# jeb grabber
# it grabs jebs emails
# whats it to ya
# 
# beepz paulz 


import httplib, urllib, json
from datetime import date, timedelta
from pymongo import MongoClient

"""
 workflow here:
 getEmails(date) - give me a date, I return data to you
 some sort of data function
 some sort of file structure
 some sort of put me in the mongodb thing

 i created a mongodb instance with a database jebgrabber
 and collection emails..

"""
client = MongoClient()
db = client.jebgrabber

def insert(data):
    db.emails.insert(data)

"""
Need to catch when there is no data in this function, and alert the range
"""    
def getEmails(_date):
    jebme = httplib.HTTPConnection("www.jebbushemails.com")
    params = urllib.urlencode({'year':_date.year,'month':_date.month,'day':_date.day,'locale':'en-us'})
    headers = {"Content-Type": "application/x-www-form-urlencoded", 
               "Accept": "application/json"}
    jebme.request("POST", "/api/email.py/", params, headers )
    response = jebme.getresponse()
    data = json.loads(response.read())
    json.dumps(data, sort_keys=True, indent=4)
    return data

def getEmailsRange(start_date, end_date):
    for _date in date_range(start_date, end_date):
        data = getEmails(_date)
        insert(data)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

