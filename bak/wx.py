#!/usr/bin/python3
# -*- coding: utf-8 -*-

from wxpy import *
import random

bot = Bot()
tuling = Tuling(api_key='743d0c5f987c4e1e93db7f253db60a4f')
dir(Tuling)


@bot.register([User,Group],TEXT)  
def reply_my_friend(msg):
    rad=random.randint(1,10)
    if isinstance(msg.chat,Group) and not msg.is_at:
        return
    else:
        if  rad <2:
            return
        else:
            tuling.do_reply(msg)


embed()  
