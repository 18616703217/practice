from flask import Blueprint,request
from service.system_user_info_service import SystemUserInfoService
import json
from common.result import ResultMessage
from conf import test_jar_conf
system_user_info = Blueprint('system_user_info', __name__)

@system_user_info.route('/get/<id>', methods=['GET'])
def get(id):
    result_message = ResultMessage()
    system_user_info_service = SystemUserInfoService()
    result = system_user_info_service.find_user_info_by_id(id)

    result_message.data = result
    result_message.errcode = test_jar_conf.SUCCESS_CODE
    return result_message.result()

@system_user_info.route('/update', methods=['POST'])
def update():
    result_message = ResultMessage()
    user_info = json.loads(request.get_data(as_text=True))

    system_user_info_service = SystemUserInfoService()
    result = system_user_info_service.update_user_info(user_info)

    result_message.data = result
    result_message.errcode = test_jar_conf.SUCCESS_CODE
    return result_message.result()

@system_user_info.route('/delete/<id>', methods=['GET'])
def delete(id):
    result_message = ResultMessage()
    system_user_info_service = SystemUserInfoService()
    result = system_user_info_service.delete_user_info(id)

    result_message.data = result
    result_message.errcode = test_jar_conf.SUCCESS_CODE
    return result_message.result()
