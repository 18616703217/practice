from flask import Blueprint
target_cycle_summary = Blueprint('target_cycle_summary', __name__)

# 查询目标库
@target_cycle_summary.route('/query_name/<user_name>', methods=['GET'])
def query_by_name(user_name):
    return "hello1"