# coding:utf-8
"""
 *@Projet  Yafinger
 *@Author  yaseng@uauc.net 
 *@Desc    mysql  class 
"""

import MySQLdb
import time
import config
from   lib      import util

       
# mysql
class MySQL:    
    error_code = ''  

    _instance = None 
    _conn = None 
    _cur = None 

    _TIMEOUT = 30 
    _timecount = 0
        
    def __init__(self, dbconfig):
        try:
            self._conn = MySQLdb.connect(host=dbconfig['host'],
                                         port=dbconfig['port'],
                                         user=dbconfig['user'],
                                         passwd=dbconfig['passwd'],
                                         db=dbconfig['db'],
                                         charset=dbconfig['charset'])
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            util.log("MySQL error:%d  %s" % (e.args[0], e.args[1]), 3, "mysql")
            return  

        
        self._cur = self._conn.cursor(MySQLdb.cursors.DictCursor)
        self._instance = MySQLdb

    def execute(self, sql):
    	if config.log_sql == 1 :
    		util.log(sql, 2, 'mysql')
        return  self._cur.execute(sql)

    def query(self, sql):
        try:
            self._cur.execute("SET NAMES utf8") 
            result = self.execute(sql)
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            util.log("Query sql error:%d  %s" % (e.args[0], e.args[1]), 3, "mysql")
            result = False
        return result

    def update(self, sql):
        try:
            self._cur.execute("SET NAMES utf8") 
            result=self.execute(sql)
            self._conn.commit()         
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            util.log("[MySQL]Update sql error:%d  %s" % (e.args[0], e.args[1]), 3, "mysql")
            result = False
        return result
        
    def insert(self, sql):
        try:
            self._cur.execute("SET NAMES utf8")
            self.execute(sql)
            self._conn.commit()
            return   int(self._cur.lastrowid)
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            util.log("[MySQL]Insert sql error:%d  %s" % (e.args[0], e.args[1]), 3, "mysql")
            return False
    
    def fetch_all(self):
        return self._cur.fetchall()

    def fetch_one(self):
        return self._cur.fetchone()
 
    def getRowCount(self):
        return self._cur.rowcount
                          
    def commit(self):
        self._conn.commit()
                        
    def rollback(self):
        self._conn.rollback()
           
    def __del__(self): 
        try:
            self._cur.close() 
            self._conn.close() 
        except:
            pass
        
    def  close(self):
        self.__del__()
