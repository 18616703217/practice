from flask import Blueprint
obtain_target_summary = Blueprint('obtain_target_summary', __name__)

# 查询目标库
@obtain_target_summary.route('/query_name/<name>', methods=['GET'])
def query_by_name(name):
    return "hello3"+name