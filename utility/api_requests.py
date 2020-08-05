#coding:utf8
"""
Author : zhangwenqi
Description : http请求发送工具
CreateTime : 2019-08-05
"""
import requests
from conf import test_jar_conf
from common.result import ResultMessage
class ObtainRequests():
    def __init__(self,url,method,headers=None,query=None,body=None,body_type=None):
        self.url = url
        self.method = method
        self.headers = headers
        self.query = query
        self.body = body
        self.body_type = body_type

    """
        Description : 发请求实体
        CreateTime : 2019-08-05
    """
    def obtain_requests(self):
        method = self.method.upper()
        if self.body_type is not None and isinstance(self.body_type,str):
            self.body_type = self.body_type.upper()
        code = self._check_requests_parame(self.url,self.method,self.headers,self.query,self.body,self.body_type)
        respons = None
        result_message = ResultMessage()
        if code != test_jar_conf.API_REQUESTS_SUCCESS_CODE:
            result_message.errcode = code
            return result_message.result()
        if method == "GET":
            if self.headers is not None:
                if self.query is not None:
                    respons = requests.get(self.url,headers=self.headers,params=self.query)
            else:
                if self.query is not None:
                    respons = requests.get(self.url,params=self.query)
                else:
                    respons = requests.get(self.url)
        if method == "POST":
            if self.headers is not None:
                if self.query is not None:
                    if self.body is not None:
                        if self.body_type == "JSON":
                            #body = json.dumps(body)
                            respons = requests.post(self.url,headers=self.headers,params=self.query,json=self.body)
                        elif self.body_type == "FORM":
                            respons = requests.post(self.url,headers=self.headers,params=self.query,data=self.body)
                    else:
                        respons = requests.post(self.url, headers=self.headers, params=self.query)
                else:
                    if self.body is not None:
                        if self.body_type == "JSON":
                            #body = json.dumps(body)
                            respons = requests.post(self.url,headers=self.headers,json=self.body)
                        elif self.body_type == "FORM":
                            respons = requests.post(self.url,headers=self.headers,data=self.body)
                    else:
                        respons = requests.post(self.url, headers=self.headers)
            else:
                if self.query is not None:
                    if self.body is not None:
                        if self.body_type == "JSON":
                            # body = json.dumps(body)
                            respons = requests.post(self.url, params=self.query, json=self.body)
                        elif self.body_type == "FORM":
                            respons = requests.post(self.url, params=self.query, data=self.body)
                    else:
                        respons = requests.post(self.url ,params=self.query)
                else:
                    if self.body is not None:
                        if self.body_type == "JSON":
                            # body = json.dumps(body)
                            respons = requests.post(self.url, json=self.body)
                        elif self.body_type == "FORM":
                            respons = requests.post(self.url, data=self.body)
                    else:
                        respons = requests.post(self.url)

        result_message.data = respons
        result_message.errcode = code
        return result_message

    """
    Description : 校验请求参数准确性方法
    CreateTime : 2019-08-05
    """
    @staticmethod
    def _check_requests_parame(url,method,headers=None,query=None,body=None,body_type=None):
        if not isinstance(url,str):
            return test_jar_conf.API_REQUESTS_URL_TYPE_ERROR_CODE
        if not url.startswith("http://") and not url.startswith("https://"):
            return test_jar_conf.API_REQUESTS_URL_TYPE_ERROR_CODE
        if not isinstance(method,str):
            return test_jar_conf.API_REQUESTS_METHOD_CONTENT_ERROR_CODE
        if method not in test_jar_conf.API_REQUESTS_METHOD_LIST:
            return test_jar_conf.API_REQUESTS_METHOD_CONTENT_ERROR_CODE
        if headers is not None:
            if isinstance(headers, str):
                try:
                    headers = eval(headers)
                    if not isinstance(headers,dict):
                        return test_jar_conf.API_REQUESTS_HEADER_CONTENT_ERROR_CODE
                except:
                    return test_jar_conf.API_REQUESTS_HEADER_CONTENT_ERROR_CODE
            elif not isinstance(headers, dict):
                return test_jar_conf.API_REQUESTS_HEADER_CONTENT_ERROR_CODE
        if query is not None:
            if isinstance(query, str):
                try:
                    query = eval(query)
                    if not isinstance(query, dict):
                        return test_jar_conf.API_REQUESTS_QUERY_CONTENT_ERROR_CODE
                except:
                    return test_jar_conf.API_REQUESTS_QUERY_CONTENT_ERROR_CODE
            elif not isinstance(query, dict):
                return test_jar_conf.API_REQUESTS_QUERY_CONTENT_ERROR_CODE
        if body is not None:
            if isinstance(body, str):
                try:
                    body = eval(body)
                    if not isinstance(body, dict):
                        return test_jar_conf.API_REQUESTS_BODY_CONTENT_ERROR_CODE
                except:
                    return test_jar_conf.API_REQUESTS_BODY_CONTENT_ERROR_CODE
            elif not isinstance(body, dict):
                return test_jar_conf.API_REQUESTS_BODY_CONTENT_ERROR_CODE
        if not body_type in test_jar_conf.API_REQUESTS_BODY_TYPE_LIST:
            return test_jar_conf.API_REQUESTS_BODY_TYPE_ERROR_CODE
        return test_jar_conf.API_REQUESTS_SUCCESS_CODE

if __name__ == "__main__":
    o = ObtainRequests("http://www.didi.com","GET")
    print(o.obtain_requests().data.text)