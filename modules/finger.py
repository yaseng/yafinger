# coding:utf-8
"""
 *@Projet  Yafinger
 *@Author  yaseng@uauc.net
 *@Desc    playweb finger modules
"""
import ast,time
import config
from   lib                import util

def get_web_app(url):
    rsp_index = util.http_get(url)
    str_index = ""
    if rsp_index == None :
        return None
    list_app=[]
    fingers=config.get('fingers');
    for  finger  in   fingers :
        rule = ast.literal_eval(finger['finger'])
        if finger['type'] == 'web_index_contain': 
            # limit header and  body and code  exp : {'header':'jsessionid=','code': 200, 'grep': '.action'}
            if rule.has_key('header') and  rule['header'] not in   str(rsp_index['headers']).lower()  : 
                continue
            if rsp_index['code'] == rule['code'] and  rule['grep']  in rsp_index['data'] :
                list_app.append({'app_id':finger['id'], 'url':url})
                util.log("url:%s app:%s" % (url, finger['app_name']))
    
        elif finger['type'] == 'web_url_contain' :
             rsp_tmp = util.http_get(url + rule['url'])
             if rsp_tmp == None :
                 continue
             if rsp_tmp['code'] == rule['code'] and  rule['grep']  in rsp_tmp['data'] :
                 list_app.append({'app_id':finger['id'], 'url':url})
                 util.log("url:%s app:%s" % (url + rule['url'], finger['app_name']))
        elif  finger['type'] == 'web_header_contain' :

            if  rule['grep']  in  str(rsp_index['headers']).lower() :
                list_app.append({'app_id':finger['id'], 'url':url})
                util.log("url:%s app:%s" % (url , finger['app_name']))
                        
            
        time.sleep(0.01)
    return  list_app