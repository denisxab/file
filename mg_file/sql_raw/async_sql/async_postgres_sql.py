"""

"""

from typing import Any, Callable

from .base_asycn_sql import AsyncBaseSql
from ..base_serializer import Efetch


class Config(AsyncBaseSql):
    def __init__(self, user: str,
                 password: str,
                 database: str | None = None,
                 port: int = 5432,
                 host: str = "localhost"):
        from psycopg2 import OperationalError
        import aiopg
        super().__init__(user, password, host)
        self.SETTINGS_DB.update({
            "port": port,
            "dbname": database,
        })
        self.SETTINGS_DB = ' '.join([f"{_k}={_v}" for _k, _v in self.SETTINGS_DB.items()])
        self.CONNECT = aiopg.connect
        self.ERROR = OperationalError

    async def read_command(self, _connection, execute: str, params: tuple | dict | list = (),
                           tdata: Callable = Efetch.n,
                           *args,
                           **kwargs) -> Any:
        """
        Декоратор для выполнения чтения из БД
        """
        async with _connection.cursor() as _cur:
            await _cur.execute(execute, params)
            ret = await _cur.fetchall()
            return ret
