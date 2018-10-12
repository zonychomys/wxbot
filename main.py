#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itchat
from turing import get_turing_reply
from itchat.content import TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO


@itchat.msg_register([TEXT])
def reply_friend_message(msg):
    from_username = itchat.originInstance.storageClass.userName
    turing_reply = get_turing_reply(msg.text)
    turing_reply = turing_reply.replace('图灵', '力宝宝')
    if (hasattr(msg.user, 'RemarkName')
            and msg.user.RemarkName.startswith('__')
            and msg.FromUserName != from_username
            or msg.user.UserName == 'filehelper'):
        msg.user.send(turing_reply)


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    from_username = itchat.originInstance.storageClass.userName
    if (hasattr(msg.user, 'RemarkName')
            and msg.user.RemarkName.startswith('__')
            and msg.FromUserName != from_username
            or msg.user.UserName == 'filehelper'):
        greeting = '暂不支持图片、语音、附件以及视频等信息类型'
        msg.user.send(greeting)


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()