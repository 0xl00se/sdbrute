#!/usr/bin/env python
# -*- encoding: utf8 -*-

'''
    program: sdbrute
    author: 0xl00se
    time: 2017.5.1

'''
import linecache
import threading
import sys
import optparse
import requests

def fileBlock(filename, num):
    lc = linecache.getlines(filename)
    lcLen = len(lc)
    step = lcLen / num
    threads = []
    for i in range(num):
        prex = i * step
        sufx = (i+1) * step
        t = threading.Thread(target=validate, args=(lc[prex:sufx]))
        threads.append(t)
    lt = threading.Thread(target=validate, args=(lc[num * step:]))
    threads.append(lt)
    for l in threads:
        l.start()
    for l in threads:
        l.join()

def validate(*list):
    for l in list:
        url = "http://" + l.strip() + "." + options.domain
        try:
            res = requests.head(url)
            if res.status_code == 200:
                print url[7:]
        except:
            pass

if __name__ == "__main__":
    parser = optparse.OptionParser('Usage: %prog [options] domain', version='%prog 1.0.0\nauthor: 0xl00se\ntime: 2017.5.1')
    parser.add_option('-t', '--target', dest='domain', help='specify a target')
    parser.add_option('-f', '--file', dest='filename', default='dict/dict.txt', help='specify a file')
    parser.add_option('-n', dest='threads', type=int, default=200, help='set a threads nums')
    (options, args) = parser.parse_args()
    if not sys.argv[1:]:
        parser.print_help()
        sys.exit(0)
    fileBlock(options.filename, options.threads)