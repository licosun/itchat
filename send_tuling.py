#coding=utf-8
import requests

import itchat
import time

#coding=utf8
import requests
import itchat

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return

# 实现微信消息的注册
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    return reply or defaultReply

itchat.auto_login(hotReload=True)
#想给谁发信息，先查找到这个朋友
#users = itchat.search_friends(name=u'通讯录备注名')
#找到UserName
#userName = users[0]['UserName']
#然后给他发消息
#itchat.send('hello',toUserName = userName)
#user = itchat.search_friends(name=u'葡萄')[0]
#user.send(u'hello ！我是机器人小晓')
SINCERE_WISH = u'祝国庆节快乐，中秋快乐'
friendList = itchat.get_friends(update=True)[1:]
for friend in friendList:
    # 如果是演示目的，把下面的方法改为print即可
    itchat.send(SINCERE_WISH, friend['UserName'])
    time.sleep(.5)
itchat.run()
