# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


if __name__ == "__main__":
    cookie = "tencentSig=8738658304; aliyungf_tc=AQAAAKM4x1S36AcA3jhQcFvEfqrqMBmh; _qddamta_800809556=3-0; sid=s%3A4XkcDKBl4abaabmk_rPM3W8ADzIzhG3s.g%2FbWXDMhJ8Hl4Nwwn5ngaLsp1Gg4EnA2IqFyjeh8ak8; responseTimeline=21; _qddac=3-1.jaciv.pwv8mc.j43noehj; _zg=%7B%22uuid%22%3A%20%2215caad30d41afb-0b5a4fdaf26b42-30637509-13c680-15caad30d42296%22%2C%22sid%22%3A%201497847415.114%2C%22updated%22%3A%201497860553.15%2C%22info%22%3A%201497514577227%2C%22cuid%22%3A%20%221b121b06-d0fa-4b23-86e9-a8b271b511be%22%7D; Hm_lvt_52d64b8d3f6d42a2e416d59635df3f71=1497671575,1497693087,1497700731,1497847415; Hm_lpvt_52d64b8d3f6d42a2e416d59635df3f71=1497860553; _qddaz=QD.plzkcz.co2edw.j3y5ij7b; _qdda=3-1.jaciv; _qddab=3-pwv8mc.j43noehj"
    trans = transCookie(cookie)
    print(trans.stringToDict())
