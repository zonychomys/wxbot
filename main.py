#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itchat
from turing import get_turing_reply


@itchat.msg_register([itchat.content.TEXT])
def reply_message(msg):
    from_username = itchat.originInstance.storageClass.userName
    turing_reply = get_turing_reply(msg.text)
    if (hasattr(msg.user, 'RemarkName')
            and msg.user.RemarkName.startswith('__')
            and msg.FromUserName != from_username
            or msg.user.UserName == 'filehelper'):
        msg.user.send(turing_reply)


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()