
# -*- coding: utf-8 -*-
 
import itchat
import requests
import json
itchat.auto_login(hotReload=True)
 
friends = itchat.get_friends()
 
def getResponse(msg):
    url = "http://openapi.tuling123.com/openapi/api/v2"
    data = {
    	"reqType":0,
        "perception": {
            "inputText": {
                "text": msg
            },
            "inputImage": {
                "url": "imageUrl"
            }
        },
        "userInfo": {
            "apiKey": "81a0447221504656bff04b47d1a8c868",
            "userId": "Geclipse"
        }
    }
    data = json.dumps(data)
    r = requests.post(url,data).json()
    return r['results'][0]['values']['text']
 
 
@itchat.msg_register(itchat.content.TEXT)    #读取接受到的消息的TEXT部分内容,存储进默认的msg
 
def auto_reply(msg):
    friends_message = msg['Text']
    name = msg['FromUserName']
    reply = getResponse(friends_message)
    itchat.send(reply,toUserName=name)
 
itchat.run()