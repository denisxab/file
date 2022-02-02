"""

"""

from typing import Callable

from mg_file.sql_raw.base_deco import BaseSql, Efetch


class Config(BaseSql):
    def __init__(self, user: str, password: str, dbname: str | None = None,
                 port: int = 3306,
                 host: str = "localhost"):
        from mysql.connector import connect, Error

        self.SETTINGS_DB = {"host": host,
                            "port": port,
                            "user": user,
                            "dbname": dbname,
                            "password": password}

        self.CONNECT = connect
        self.ERROR = Error

    def mutable_command(self, _connection, execute: str, params: tuple | dict | list, *args,
                        **kwargs):
        """
        Декоратор для выполнения изменяемой SQL команды
        """
        with _connection.cursor() as cursor:
            cursor.execute(execute, params, multi=kwargs["multi"])
            _connection.commit()
        return cursor.statement

    def read_command(self, _connection, execute: str, params: tuple | dict | list = (),
                     tdata: Callable = Efetch.n,
                     *args,
                     **kwargs):
        """
        Декоратор для выполнения чтения из БД
        """
        with _connection.cursor() as cursor:
            cursor.execute(execute, params, multi=kwargs["multi"])
            return tdata(cursor)
