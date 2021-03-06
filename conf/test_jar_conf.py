#coding:utf8
"""
Author : zhangwenqi
Description : testjJar全量配置
CreateTime : 2019-08-05
"""
#外部域名





#成功状态码
SUCCESS_CODE = 0
#参数类型错误状态码
PARAMETER_TYPE_ERROR = 1001
#参数缺失错误
PARAMETER_MISSING_ERROR = 1002
#请求失败
REQUEST_FAILURE_ERROR = 1010

#http请求发送工具配置
#成功
API_REQUESTS_SUCCESS_CODE = 2000
#请求url格式错误
API_REQUESTS_URL_TYPE_ERROR_CODE = 2001
#方法内容错误
API_REQUESTS_METHOD_CONTENT_ERROR_CODE = 2002
#主体内容错误
API_REQUESTS_BODY_CONTENT_ERROR_CODE = 2003
#请求头错误
API_REQUESTS_HEADER_CONTENT_ERROR_CODE = 2004
#主体格式错误
API_REQUESTS_BODY_TYPE_ERROR_CODE = 2005
#QUERY格式错误
API_REQUESTS_QUERY_CONTENT_ERROR_CODE = 2006

#请求主体类型
API_REQUESTS_BODY_TYPE_LIST = ["FORM","JSON",None]

#HTTP请求方法
API_REQUESTS_METHOD_LIST = ["POST","GET","DELETE","PUT","HEAD"]