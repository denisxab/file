import asyncio
from abc import abstractmethod
from pprint import pformat
from typing import Any, Coroutine, Callable

from loguru import logger

from ..base_serializer import Efetch
from ..base_sql import BaseSql


class BaseTasks:
    """
    Базовый класс для списка асинхронных задач.
    Используются как примесь к асинхронному классу `AsyncBaseSql`
    """

    def __init__(self):
        self.__tasks: list[Coroutine] = []

    @property
    def tasks(self) -> Any:  # GET
        """Получить список задач"""
        return self.__tasks

    @staticmethod
    async def _run(tasks: list):
        """Выполнить список задач"""
        return await asyncio.gather(*tasks)

    def executeTasks(self):
        """Запустить выполнения задач"""
        return asyncio.run(self._run(self.__tasks))

    def appendTask(self, coroutine: Coroutine):
        """Добавить здание в список"""
        self.__tasks.append(coroutine)

    def extendTask(self, coroutine: list[Coroutine]):
        """Расширить список задач другим списком список"""
        self.__tasks.extend(coroutine)


class AsyncBaseSql(BaseSql, BaseTasks):
    """
    Базовый асинхронны класс
    """

    def __init__(self, user: str, password: str,
                 host: str = "localhost"):
        super().__init__(user, password, host)
        BaseTasks.__init__(self)

    async def connect_db(self, fun: Callable, *args, **kwargs) -> Any:
        try:
            async with self.CONNECT(self.SETTINGS_DB) as connection:
                return await fun(connection, *args, **kwargs)
        except self.ERROR as e:
            logger.error(e)
            raise e

    async def Rsql(self, execute: str, params: tuple | dict | list = (), tdata: Efetch = Efetch.n, *args,
                   **kwargs) -> str:
        """
        Чтение из БД с красивым выводом в консоль
        """
        return await self.pprint_deco(self.rsql, execute, params, tdata)

    async def rsql(self, execute: str, params: tuple | dict | list = (), tdata: Efetch = Efetch.n, *args,
                   **kwargs) -> str:
        """
        Чтение из БД
        """
        return await self.connect_db(self.read_command, execute=execute, params=params, tdata=tdata)

    @staticmethod
    async def pprint_deco(fun: Callable, execute: str, params: tuple | dict | list = (),
                          tdata: Efetch = Efetch.n, ) -> str:
        """
        Декоратор для красивого вывода результата функции в консоль
        """
        return pformat(await fun(execute, params, tdata))

    @abstractmethod
    async def read_command(self, _connection, execute: str, params: tuple | dict | list = (), tdata: Efetch = Efetch.n,
                           *args,
                           **kwargs):
        """
        Декоратор для выполнения чтения из БД
        """
        return NotImplemented()

    @abstractmethod
    async def mutable_command(self, _connection, execute: str, params: tuple | dict | list, *args, **kwargs):
        """
        Декоратор для выполнения изменяемой SQL команды
        """
        return NotImplemented()
