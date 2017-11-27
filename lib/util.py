# coding:utf-8
"""
 *@Projet  Yafinger
 *@Author  yaseng@uauc.net 
 *@Desc    util library  
"""


import   time, re
import   config
import   urllib2,cookielib,itertools,os

import socket  
socket.setdefaulttimeout(10)


"""
*@desc log function 
*@param text: log text
*@param type: log type  0=info([*])  1=succeed [+]  2=alert [!] 3=error [x]  8=yamsg [y]
*@param module : log module  exp:mysql redis  
"""
def log(text, type=1, module=""):
    str_time = time.strftime('%Y-%m-%d %X', time.localtime())
    str_pre = '[*]'
    if type == 1 :
        str_pre = '[+]'
    elif type == 2:
        str_pre = '[!]'
    elif type == 3:
        str_pre = '[x]'
    if len(module) > 0:
        module = "[%s]" % module
    str_log = str_pre + module + text
    if config.debug == 1 :
        print str_log

    else :
        if type == 0:
            return
        else :
            file_path = config.path['log'] + time.strftime('%Y-%m-%d', time.localtime()) + ".log"
            file_log = open(file_path, "a")
            file_log.writelines(str_time + " " + str_log + "\n")
            file_log.close()

def msg(text, type=0):
    str_pre = ""
    if type > 0 :
        for i in range(0, type) :
            str_pre = str_pre + "   " 
    print  str_pre + text
    return  


def find_text(text, start, end):
    regex = '%s([\s\S]*)%s' % (start, end)
    text_re = re.search(regex, text)
    if text_re is None :
        return  None
    return text_re.group(1)

def addslashes(s):
    return  s.replace("'", "")


def  get_http_headers():
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
                'Referer'    : 'http://www.baidu.com',
                'X-FORWARDED-FOR' : '216.239.53.53'
              
              }
    return headers


def  http_get(url, headers=None, time=5):
    if headers == None :
        headers=get_http_headers()
    ret = {}
    req = urllib2.Request(url, None, headers)
 
    try:
        r = urllib2.urlopen(req,timeout=time)
        ret = {"data":r.read(), "code":200, "headers":r.headers}
    except urllib2.HTTPError, e:
        ret = {"data":e.read(), "code":e.code, "headers":e.headers}
    except urllib2.URLError, e:
        return None
    except :
        return None 
    return  ret


def  http_post(url, data, headers=None, time=10):
    ret = {}
    try:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.LWPCookieJar())) 
        req = urllib2.Request(url, data, get_http_headers())
        r = opener.open(req,None,time)
        ret = {"data":r.read(), "code":200, "headers":r.headers}
    except urllib2.HTTPError, e:
        ret = {"data":e.read(), "code":e.code, "headers":e.headers}
    except urllib2.URLError, e:
        return None
    except :
        return None 
    return  ret

def process_exit(name):
    return len(os.popen('ps aux | grep %s | grep -v grep' % name ).readlines())

 






