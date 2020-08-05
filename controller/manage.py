from flask import Flask
from dao.base_dao import BaseDao
from conf import config
from controller.system_user_info import system_user_info
from controller.target_cycle_summary import target_cycle_summary
from controller.obtain_target_summary import obtain_target_summary

app = Flask(__name__)
# 引入配置文件中的相关配置
app.config.from_object(config.config["testing"])
# 配置db
BaseDao.init(app)
# 注册蓝图，并指定其对应的前缀（url_prefix）
app.register_blueprint(system_user_info, url_prefix="/system_user_info")
app.register_blueprint(target_cycle_summary, url_prefix="/target_cycle_summary")
app.register_blueprint(obtain_target_summary, url_prefix="/obtain_target_summary")



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
