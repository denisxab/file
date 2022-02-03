from abc import abstractmethod
from pprint import pformat
from typing import Any, Callable

from loguru import logger

from ..base_serializer import Efetch
from ..base_sql import BaseSql


class SyncBaseSql(BaseSql):

    def connect_db(self, fun: Callable, *args, **kwargs) -> Any:
        try:
            with self.CONNECT(**self.SETTINGS_DB) as connection:
                return fun(connection, *args, **kwargs)
        except self.ERROR as e:
            logger.error(e)
            raise e

    def rsql(self, execute: str, params: tuple | dict | list = (), tdata: Efetch = Efetch.n, *args,
             **kwargs) -> tuple[str, tuple | dict | list]:
        """
        Чтение из БД
        """
        return self.connect_db(self.read_command, execute=execute, params=params, tdata=tdata)

    def Rsql(self, execute: str, params: tuple | dict | list = (), tdata: Efetch = Efetch.n, *args,
             **kwargs) -> str:
        """
        Чтение из БД с красивым выводом в консоль
        """
        return self.pprint_deco(self.rsql(execute, params, tdata))

    def wsql(self, execute: str, params: tuple | dict | list = ()) -> tuple[str, tuple | dict | list]:
        """
        Внесение изменений в БД
        """
        return self.connect_db(self.mutable_command, execute=execute, params=params)

    @staticmethod
    def pprint_deco(d: Any) -> str:
        """
        Декоратор для красивого вывода результата функции в консоль
        """
        return pformat(d)

    @abstractmethod
    def read_command(self, _connection, execute: str, params: tuple | dict | list = (), tdata: Efetch = Efetch.n,
                     *args,
                     **kwargs):
        """
        Декоратор для выполнения чтения из БД
        """
        return NotImplemented()

    @abstractmethod
    def mutable_command(self, _connection, execute: str, params: tuple | dict | list, *args, **kwargs):
        """
        Декоратор для выполнения изменяемой SQL команды
        """
        return NotImplemented()
