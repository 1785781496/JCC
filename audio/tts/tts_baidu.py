# -*- coding: utf-8 -*-
from aip import AipSpeech
""" 你的 APPID AK SK 可在AI服务控制台中的应用列表中查看"""
APP_ID = '16815394'     #常量APP_ID在百度云控制台中创建，
API_KEY = 'jM4b8GIG9gzrzySTRq3szK2E'    #常量API_KEY与SECRET_KEY是在创建完毕应用后，
SECRET_KEY = 'iE626cEpjT1iAVwh24XV5h1QFuR8FPD2' #系统分配给用户的，均为字符串，用于标识用户，为访问做签名验证，

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)



def main():
    # text = '你好，这里是CGTeamwork！'#文字内容自定义
    text = "Hello, This is from beijing."
    result = client.synthesis(text, 'zh', 1, {      #'zh'表示中文，1表示区分机器号（非必须参数）
        'spd':5,    #语速，0-9默认为5
        'pit':5,    #音调，0-9默认为5
        'vol': 5,   #音量，0-9默认为5
        'per':1,    #发音人，0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)

'''
// 成功返回二进制文件流
// 失败返回
{
    "err_no":500,
    "err_msg":"notsupport.",
    "sn":"abcdefgh",
    "idx":1
}

'''
if __name__ == '__main__':
    main()