from abc import abstractmethod
from pprint import pformat
from typing import Any

from loguru import logger

from sql_raw.base_serializer import Efetch


class BaseSql:

    def connect_db(self, *args, **kwargs) -> Any:
        try:
            with self.CONNECT(**self.SETTINGS_DB) as connection:
                return connection
        except self.ERROR as e:
            logger.error(e)
            raise e

    @abstractmethod
    def mutable_command(self, _connection, execute: str, params: tuple | dict | list, *args, **kwargs):
        """
        Декоратор для выполнения изменяемой SQL команды
        """
        return NotImplemented()

    @abstractmethod
    def read_command(self, _connection, execute: str, params: tuple | dict | list = (), tdata: Efetch = Efetch.n, *args,
                     **kwargs):
        """
        Декоратор для выполнения чтения из БД
        """
        return NotImplemented()

    @staticmethod
    def pprint_deco(d: Any) -> str:
        """
        Декоратор для красивого вывода результата функции в консоль
        """
        return pformat(d)

    def rsql(self, execute: str, params: tuple | dict | list = (), tdata: Efetch = Efetch.n, *args,
             **kwargs) -> tuple[str, tuple | dict | list]:
        """
        Чтение из БД
        """
        return self.read_command(self.connect_db(), execute, params, tdata)

    def Rsql(self, execute: str, params: tuple | dict | list = (), tdata: Efetch = Efetch.n, *args,
             **kwargs) -> str:
        """
        Чтение из БД с красивым выводом в консоль
        """
        return self.pprint_deco(self.read_command(self.connect_db(), execute, params, tdata))

    def wsql(self, execute: str, params: tuple | dict | list = ()) -> tuple[str, tuple | dict | list]:
        """
        Внесение изменений в БД
        """
        return self.mutable_command(self.connect_db(), execute, params)

###########################################
