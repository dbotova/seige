#!/usr/bin/python

import urllib2
import string
import getpass
import time
import threading
import numpy
import os

def make_req(url, status, elapsed):
    try:
        req = urllib2.Request(url)
        f = urllib2.urlopen(req)
        start = float(time.time())
        page = f.read()
        end = float(time.time())
        elapsed.append(float(end - start))
        status.append(f.getcode())
        f.close()
    except IOError, e:
        print "Failed to open", url
        if hasattr(e, 'code'):
            print "Error code:", e.code
    return

if __name__ == "__main__":
    os.system('clear')
    url = raw_input("URL: ")
    users = int(raw_input("Number of users: "))
    threads = []
    status = []
    elapsed = []
    start = time.time()
    for n in range (users):
        t = threading.Thread(target=make_req(url, status, elapsed))
        threads.append(t)
        t.start()
    end = time.time()
    os.system('clear')
    print("Statistic for URL: %s" % url)
    print("Number of users: %s" % users)
    print("Elapsed time: %ss" % float(end - start))
    print ("Average respond time: %fs" % numpy.mean(elapsed))
    print("Status code 200: %s" % status.count(200))
    print("Failed transactions: %d" % (users - status.count(200)))

