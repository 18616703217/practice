"""

"""

from dao.system_user_info_dao import UserInfo
from common.result import ResultMessage
from conf import test_jar_conf
import json

class SystemUserInfoService:
    result_message = ResultMessage()

    def __init__(self):
        self.user_info = UserInfo()

    def find_user_info_by_id(self,id):
        result = self.user_info.find_by_id(id)
        self.result_message.data = result
        self.result_message.errcode = test_jar_conf.SUCCESS_CODE
        return self.result_message.result()

    def update_user_info(self,user_info):
        result = None
        if not user_info.get("id"):
            result = self.user_info.insert_user(user_info)
        else:
            update_user_info = self.user_info.find_by_id(user_info["id"])
            if update_user_info:
                result = self.user_info.update_user_by_id(user_info)

        self.result_message.data = result
        self.result_message.errcode = test_jar_conf.SUCCESS_CODE
        return self.result_message.result()

    def delete_user_info(self,id):
        user_info = {"delete_status":1,"id":id}
        result = self.user_info.update_user_by_id(user_info)
        self.result_message.data = result
        self.result_message.errcode = test_jar_conf.SUCCESS_CODE
        return self.result_message.result()



if __name__ == "__main__":
    pass
    # SystemUserInfoService.find_user_info_by_id(1)