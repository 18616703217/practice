# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

class BaseDao(object):

    #数据库表对象
    __base_class = None
    #数据库表名
    _table_name = None
    #数据库配置
    _db_conf = None

    @staticmethod
    def init(app):
        print(app)
        BaseDao._db_conf = app

    def __init__(self,encoding='utf-8', echo=False):
        self._engine = create_engine(BaseDao._db_conf.config.get("SQLALCHEMY_DATABASE_URI"), encoding=encoding, echo=echo)
        session_class = sessionmaker(self._engine)
        self._session = session_class()

    def _table_query(self, table_name):
        """ 避免重复加载，同时只是用execute时，不加载以下内容 """
        if self.__base_class is None:
            self.__base_class = automap_base()
            self.__base_class.prepare(self._engine, reflect=True)
        if hasattr(self.__base_class.classes, table_name):
            table = getattr(self.__base_class.classes, table_name)
            return self._session.query(table)
        else:
            raise KeyError(f"未搜寻到表: {table_name}")

    def execute_sql(self, sql_str, ft = {}):
        """
        执行sql语句，区分查询跟修改操作
        cursor支持fetchall(),fetchone(),fetchmany(),rowcount
        """
        sql_str = sql_str.format(**ft).strip().replace("\n", "").replace("\t", "")
        if sql_str.startswith("select"):
            cursor = self._engine.execute(sql_str)
            return cursor
        try:
            affect_row = self._engine.execute(sql_str).rowcount
            self._session.commit()
            return affect_row
        except Exception as e:
            self._session.rollback()
            self.close()
            raise e

    def execute_many_sql(self, many_sql, ft,separator=";"):
        """ 执行多条sql, sql语句之间使用；号分割，方便执行多条修改语句 """
        sql_list = many_sql.format(**ft).strip().replace("\n", "").replace("\t", "").split(separator)
        sql_list = [sql for sql in sql_list if sql.strip() != ""]
        for sql_str in sql_list:
            self.execute_sql(sql_str,ft)

    def delete(self, ft=None):
        """ 表名 + dict(key=word), 根据ft条件删除数据 """
        ft = {} if ft is None else ft
        delete_row = self._table_query(self._table_name).filter_by(**ft).delete()
        self._session.commit()
        return delete_row

    def first(self, ft=None):
        """ 一行数据 """
        ft = {} if ft is None else ft
        first_row = self._table_query(self._table_name).filter_by(**ft).first()
        return first_row

    def all(self, ft=None):
        """ 所有数据 """
        ft = {} if ft is None else ft
        all_row = self._table_query(self._table_name).filter_by(**ft).all()
        return all_row

    def count(self, ft=None):
        """ 行数 """
        ft = {} if ft is None else ft
        rowcount = self._table_query(self._table_name).filter_by(**ft).count()
        return rowcount

    def close(self):
        self._session.close()

    # def param_check(self,data,type = BaseDao._CHECKOUT_TYPE_TABLES):
    #     if type == BaseDao._CHECKOUT_TYPE_TABLES:
    #         for j in data:
    #             for i in self.__user_dict.keys():
    #                 if i not in j.keys():
    #                     return False
    #     elif type == BaseDao._CHECKOUT_TYPE_TABLE:
    #         for i in data.keys():
    #             if i not in self.__user_dict.keys():
    #                 return False
    #     return True

    # #校验单条数据
    # _CHECKOUT_TYPE_TABLE = "table"
    # #校验多条数据
    # _CHECKOUT_TYPE_TABLES = "tables"
    #设置表对象
    _SET_TYPE_TABLE = "table"
    #设置现成数据
    _SET_TYPE_TABLE_DATA = "table_data"

if __name__ == '__main__':
    pass



