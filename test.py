#!/usr/bin/env python
# coding: utf-8

from wxbot import *


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.send_msg_by_uid(u'hi', msg['user']['id'])
            self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])

    def schedule(self):
        useridKedou = self.get_user_id('小蝌蚪');
        
        userid = self.get_user_id('毛哥');
        
        print  'userid ' + userid
        
  
        
        #self.send_msg(u'小蝌蚪', u'测试')
  
        #self.send_msg('毛哥', 'mao哥你好')
  
       # self.send_msg('怀化人在上海微信群', '111')
  
  #@@08807a0121684fc46ceb038dfefeee230e9a0f688ada84df8800a2c3cbbd7491
        
        
        self.send_msg_by_uid('呼叫毛哥！！！！毛哥是否尚在????????',userid)
        
        #self.send_img_msg_by_uid("img/1.png", userid)
        self.send_img_msg_by_uid("e:/test.png", userid)
       
        self.send_img_msg_by_uid("e:/test.png", useridKedou)
       
        
        time.sleep(20)



def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
