"""

"""

from typing import Any, Callable

from mg_file.sql_raw.base_deco import BaseSql, Efetch


class Config(BaseSql):
    def __init__(self, user: str, password: str, database: str | None = None,
                 port: int = 5432,
                 host: str = "localhost"):
        from psycopg2 import connect, OperationalError
        self.SETTINGS_DB = {"host": host,
                            "port": port,
                            "user": user,
                            "database": database,
                            "password": password}
        self.CONNECT = connect
        self.ERROR = OperationalError

    def mutable_command(self, _connection, execute: str, params: tuple | dict | list, *args, **kwargs):
        """
        Декоратор для выполнения изменяемой SQL команды
        """
        with _connection.cursor() as cursor:
            cursor.execute(execute, params)
            _connection.commit()
        return cursor.statusmessage

    def read_command(self, _connection, execute: str, params: tuple | dict | list = (), tdata: Callable = Efetch.n,
                     *args,
                     **kwargs) -> Any:
        """
        Декоратор для выполнения чтения из БД
        """
        with _connection.cursor() as cursor:
            cursor.execute(execute, params)
            return tdata(cursor)
