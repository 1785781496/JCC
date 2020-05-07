import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text


def main():
    itchat.auto_login()
    print(itchat.check_login())
    itchat.run()


if __name__ == '__main__':
    main()
