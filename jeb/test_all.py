import jebgrabber
from datetime import date

#def test_counter():
#    text = "this should equal 4"
#    counter = jebalytics.getCounter(text)
#    assert len(counter) == 4


def test_db():
    jebgrabber.connect_db()
    print jebgrabber.cur

#def test_getEmails(): 
#    _date = date(2001,01,01)
#    emails = jebalytics.getEmails(_date)
#    print emails[0]

#def test_getEmailsThatContain():
#    text = "republican"
#    emails = jebalytics.getEmailsThatContain(text)
#    print emails[0]
    
#def test_dateCounter():
#    sd = date(2001,01,01)
#    ed = date(2001,01,07)
#    counter = jebalytics.dateCounter(sd, ed)

def test_daterange():
    d1 = date(2001,01,01)
    d2 = date(2001,01,07)
    date_set = []
    for _date in jebgrabber.daterange(d1,d2):
        date_set.append(_date)
    assert len(date_set) == 7 
    assert date_set[0] == d1
    assert date_set[6] == d2

def test_parseEmail():
    before = "I AM TEXT\n-----Original Message-----\n I SHOULDN'T BE HERE"
    after = "I AM TEXT"
    assert jebgrabber.parseEmail(before) == after
