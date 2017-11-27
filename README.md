# yafinger
yet another  web fingerprinter

 
     __    __            ___                                         
    /\ \  /\ \         /'___\  __                                    
    \ `\`\\/'/   __   /\ \__/ /\_\     ___       __       __   _ __  
     `\ `\ /'  /'__`\ \ \ ,__\\/\ \  /' _ `\   /'_ `\   /'__`\/\`'__\
       `\ \ \ /\ \L\.\_\ \ \_/ \ \ \ /\ \/\ \ /\ \L\ \ /\  __/\ \ \/ 
         \ \_\\ \__/.\_\\ \_\   \ \_\\ \_\ \_\\ \____ \\ \____\\ \_\ 
          \/_/ \/__/\/_/ \/_/    \/_/ \/_/\/_/ \/___L\ \\/____/ \/_/ 
                                                 /\____/             
                                                 \_/__/ 
 

## 安装
导入数据库，修改配置config.py即可。

## 使用 

```
➜  yafinger python  yafinger.py
Usage: yafinger.py --host  host --port  port --finger  <all|app_name>
Example:yafinger.py  --url  http://127.0.0.1    --finger phpmyadmin

Options:
  -h, --help            show this help message and exit
  -u URL, --url=URL     target url
  -f FINGER, --finger=FINGER
                        finger_db app_name,default all
➜  yafinger python   yafinger.py  --url  http://www.discuz.net
[!][mysql]SELECT  * from  pw_finger_db  where  `enable`=1
[+][finger]load fingers count 41
[+]url:http://www.discuz.net app:discuz
```

## 整合
本项目可以快速作为模块集成到扫描器或者其他项目中。输入url  ，线程池识别指纹，结果输出到数据库。

## 文章
《浅谈现代化指纹识别及工具编写》


