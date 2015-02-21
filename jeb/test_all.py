import jebgrabber, jebalytics
from datetime import date

def test_counter():
    text = "this should equal 4"
    counter = jebalytics.getCounter(text)
    assert len(counter) == 4


def test_db():
    db = jebgrabber.db.emails
    x = db.find_one()
    print x

def test_getEmails(): 
    _date = date(2001,01,01)
    emails = jebalytics.getEmails(_date)
    print emails[0]

def test_getEmailsThatContain():
    text = "republican"
    emails = jebalytics.getEmailsThatContain(text)
    print emails[0]
    
def test_dateCounter():
    sd = date(2001,01,01)
    ed = date(2001,01,07)
    counter = jebalytics.dateCounter(sd, ed)

