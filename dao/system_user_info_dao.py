from dao.base_dao import BaseDao
import copy

class UserInfo(BaseDao):

    __user_dict = {"id":None,"user_name":None,"group_id":None,"email":None,"password":None,"delete_status":None}
    _table_name = "system_user"

    def find_by_id(self,id = None):
        user_data = BaseDao.first(self,{"id":id,"delete_status":0})
        return self.__set_user(user_data)


    def find_by_condition(self,ft = None):
        user_list = []
        user_data = BaseDao.all(self,ft)
        for i in user_data:
            user = self.__set_user(i)
            user_list.append(copy.copy(user))
        return user_list

    def all(self):
        user_list = []
        user_data = BaseDao.all(self)
        for i in user_data:
            user = self.__set_user(i)
            user_list.append(copy.copy(user))
        return user_list

    def insert_users(self,user_list):
        for user_info in user_list:
            self.insert_user(user_info)

    def insert_user(self,user_info):
        sql_str = "INSERT INTO system_user (user_name,group_id,email,password) VALUES ('{user_name}','{group_id}','{email}','{password}');"
        return self.execute_sql(sql_str,user_info)

    def update_user_by_id(self,modify):
        condition = {"id":modify.pop("id")}
        return self.update_users(modify,condition)

    def update_users(self,modify,condition):
        sql_str = "UPDATE system_user SET "
        for i in modify.keys():
            sql_str += "%s = '%s'," % (i,modify[i])
        sql_str = sql_str[:-1] + " where "
        for i in condition.keys():
            sql_str += "%s = '%s' AND" % (i,condition[i])
        sql_str = sql_str[:-3]+";"
        print(sql_str)
        return self.execute_sql(sql_str)

    def __set_user(self,user_data,type=BaseDao._SET_TYPE_TABLE):
        if not user_data:
            return
        if type == BaseDao._SET_TYPE_TABLE:
            UserInfo.__user_dict["id"] = user_data.id
            UserInfo.__user_dict["user_name"] = user_data.user_name
            UserInfo.__user_dict["group_id"] = user_data.group_id
            UserInfo.__user_dict["email"] = user_data.email
            UserInfo.__user_dict["password"] = user_data.password
            UserInfo.__user_dict["delete_status"] = user_data.delete_status
            return UserInfo.__user_dict
        else:
            UserInfo.__user_dict["user_name"] = user_data.user_name
            UserInfo.__user_dict["group_id"] = user_data.group_id
            UserInfo.__user_dict["email"] = user_data.email
            UserInfo.__user_dict["password"] = user_data.password
            UserInfo.__user_dict["delete_status"] = user_data.delete_status
            return UserInfo.__user_dict




if __name__ == "__main__":
    m = "mysql+pymysql://root:123@localhost:3306/atlantis?charset=utf8mb4"
    UserInfo.db_conf = m
    u = UserInfo()
    print(u.find_by_id(1))
    u.update_users({"name":"ztb1","email":"test1"},{"id":2})
    # print(u.find_by_condition({"name":"2"}))
    # u.insert_users([{"id1":2,"name":"2","business_id":2,"email":"2","pwd":1,"status":1,"company_name":1},{"id":3,"name":"3","business_id":'3',"email":'3',"pwd":'3',"status":'3',"company_name":'3'}])
    # print(l)
