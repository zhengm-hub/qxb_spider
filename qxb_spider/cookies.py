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
    cookie = "tencentSig=8738658304; aliyungf_tc=AQAAAAv/8B0MMQgAzr1a2tzv8oApiQ0f; sid=s%3Aml66Mj8nAyPnfZawL66dxs1ZQ9cBwbiY.nq9n4b%2B7ZpJSxnvN5Ok2G63smtG6pXPjRlTuuOOCsEk; _qddamta_800809556=3-0; responseTimeline=14; _qddac=3-1.2lc9gi.ioj5l3.j457kezm; _zg=%7B%22uuid%22%3A%20%2215caad30d41afb-0b5a4fdaf26b42-30637509-13c680-15caad30d42296%22%2C%22sid%22%3A%201497941291.948%2C%22updated%22%3A%201497950668.778%2C%22info%22%3A%201497514577227%2C%22cuid%22%3A%20%221b121b06-d0fa-4b23-86e9-a8b271b511be%22%7D; Hm_lvt_52d64b8d3f6d42a2e416d59635df3f71=1497693087,1497700731,1497847415,1497935371; Hm_lpvt_52d64b8d3f6d42a2e416d59635df3f71=1497950669; _qddaz=QD.plzkcz.co2edw.j3y5ij7b; _qdda=3-1.2lc9gi; _qddab=3-ioj5l3.j457kezm"
    trans = transCookie(cookie)
    print(trans.stringToDict())
