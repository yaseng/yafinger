# coding:utf-8
"""
 *@Projet  Yafinger
 *@Author  yaseng@uauc.net
 *@Desc    yafinger test 
     __    __            ___                                         
    /\ \  /\ \         /'___\  __                                    
    \ `\`\\/'/   __   /\ \__/ /\_\     ___       __       __   _ __  
     `\ `\ /'  /'__`\ \ \ ,__\\/\ \  /' _ `\   /'_ `\   /'__`\/\`'__\
       `\ \ \ /\ \L\.\_\ \ \_/ \ \ \ /\ \/\ \ /\ \L\ \ /\  __/\ \ \/ 
         \ \_\\ \__/.\_\\ \_\   \ \_\\ \_\ \_\\ \____ \\ \____\\ \_\ 
          \/_/ \/__/\/_/ \/_/    \/_/ \/_/\/_/ \/___L\ \\/____/ \/_/ 
                                                 /\____/             
                                                 \_/__/ 
"""
import   os, time, sys, Queue, threading, ast
import config
from   lib                import util
from   lib.db             import *
from   optparse           import OptionParser
from   modules            import finger

if __name__ == "__main__":
    usage= '''%prog --host  host --port  port --finger  <all|app_name>   \r\nExample:%prog  --url  http://127.0.0.1    --finger phpmyadmin  '''
    parser = OptionParser(usage=usage)
    parser.add_option("-u", "--url", dest="url", help="target url")
    parser.add_option("-f", "--finger", dest="finger", help="finger_db app_name,default all ", default="all")
    options, arguments = parser.parse_args()
    if options.url == None :
        parser.print_help() 
        exit(0)
    db = MySQL(config.db_config)
    sql_finger_where=' '  if options.finger == 'all' else "  and  app_name='%s' "  % options.finger
    db.query("SELECT  * from  pw_finger_db  where  `enable`=1   %s "  % sql_finger_where)
    fingers = db.fetch_all()
    if len(fingers) == 0 :
        util.log('finger app_name %s not found' % options.finger ,3,'finger') 
    config.set("fingers",fingers)
    util.log("load fingers count %d" % len(fingers),1,'finger')
    finger.get_web_app(options.url)
