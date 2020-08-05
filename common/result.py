#coding:utf8
"""
Author : zhangwenqi
Description : 定义统一返回结果
CreateTime : 2019-08-21
"""

import json

class ResultMessage:
    def __init__(self):
        #响应状态码
        self.__errcode = None

        #响应结果
        self.__message = None

        #传输数据
        self.__data = None

    @property
    def errcode(self):
        return self.__errcode

    @property
    def message(self):
        return self.__message

    @property
    def data(self):
        return self.__data

    @errcode.setter
    def errcode(self,errcode):
        if isinstance(errcode,int):
            self.__errcode = errcode
        else:
            raise TypeError("需要传入整型")

    @message.setter
    def message(self,message):
        if isinstance(message,str):
            self.__message = message
        else:
            raise TypeError("需要传入字符串")

    @data.setter
    def data(self,data):
        self.__data = data

    def result(self):
        dict_result = {"errcode":self.__errcode,"message":self.__message,"data":self.__data}
        return json.dumps(dict_result)