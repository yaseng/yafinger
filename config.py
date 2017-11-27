# coding:utf-8
"""
 *@Projet  Yafinger
 *@Author  yaseng@uauc.net
 *@Desc    global config 
"""
import  os
from    lib.db        import *

#init project
def init():
	pass

#debug model on:  show  info alert error succeed  message
#            off: error & alert succeed  message  log file & database 
debug=1
#log_type  0:log to screen   1:log  to file  
log_type=1 

#db_config
log_sql=1
db_config={"host":"127.0.0.1","port":3306, "user":"root", "passwd":"", "db":"playweb","charset":'utf8'}


#path config
pw_path='./'
path={'log':pw_path+"/data/log/",'data':pw_path+'data/'}


#global option
o={}  

def  set(key,value):
    global o
    o[key]=value

def  get(key):
    global o
    return o[key]






