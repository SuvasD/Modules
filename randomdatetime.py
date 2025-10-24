import random
import time
def getrandomdate(startdate, enddate):
    print("The start and end dates are ", startdate, enddate)
    randomGenerator=random.random()
    dateFormat='%m/%d/%Y'
    starttime=time.mktime(time.strptime(startdate, dateFormat))
    endtime=time.mktime(time.strptime(enddate, dateFormat))
    randomTime=starttime+randomGenerator*(endtime-starttime)
    randomDate=time.strft(dateFormat, time.localtime(randomTime))
    return getrandomdate
print("Random Date = ", getrandomdate("1/1/2016", "12/12/2018"))
