# -*- coding: utf-8 -*-
from gtts import gTTS

if __name__ == '__main__':
    # with open('test.txt', 'r', encoding='utf-8') as f:
    #     audio = gTTS(text=f.read(),lang="zh-cn")
    #     audio.save("test.mp3")
    text = u"今日之我昨日之我"
    audio = gTTS(text, lang="zh-cn")
    audio.save("test.mp3")

