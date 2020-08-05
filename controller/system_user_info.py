from flask import Blueprint,request
from service.system_user_info_service import SystemUserInfoService
import json
system_user_info = Blueprint('system_user_info', __name__)



@system_user_info.route('/get/<id>', methods=['GET'])
def get(id):
    system_user_info_service = SystemUserInfoService()
    return system_user_info_service.find_user_info_by_id(id)

@system_user_info.route('/update', methods=['POST'])
def update():
    user_info = json.loads(request.get_data(as_text=True))
    system_user_info_service = SystemUserInfoService()
    return system_user_info_service.update_user_info(user_info)

@system_user_info.route('/delete/<id>', methods=['GET'])
def delete(id):
    system_user_info_service = SystemUserInfoService()
    return system_user_info_service.delete_user_info(id)
