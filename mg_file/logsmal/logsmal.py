from typing import Optional, Final, Any

from mg_file import LogFile


class MetaLogger:
    """
    Мета данные логгера
    """
    reset_: Final[str] = "\x1b[0m"
    blue: Final[str] = "\x1b[96m"
    yellow: Final[str] = "\x1b[93m"
    read: Final[str] = "\x1b[91m"
    green: Final[str] = "\x1b[92m"


class loglevel:
    """
    Создание логгера
    """
    __slots__ = [
        "level",
        "fileout",
        "console_out",
        "color_flag",
        "color_loglevel",
    ]

    def __init__(self, level: str,
                 fileout: Optional[str] = None,
                 console_out: bool = True,
                 color_flag: Optional[str] = None,
                 color_loglevel: Optional[str] = None,
                 ):
        """

        :param level:
        :param fileout:
        :param console_out:
        """
        self.level: str = level
        self.fileout: Optional[str] = fileout
        self.console_out: bool = console_out
        self.color_flag: str = color_flag
        self.color_loglevel: str = color_loglevel

    def __call__(self, data: str, flag: str = ""):
        """
        Вызвать логгер

        :param data:
        :param flag:
        :return:
        """

        self._base(data, flag)

    def _base(self, data: Any, flag: str):
        """
        Логика работы логера

        :param data:
        :param flag:
        :return:
        """
        if self.fileout:
            log_formatted = "{level}[{flag}]:{data}\n".format(
                level=self.level,
                flag=flag,
                data=data,
            )
            LogFile(self.fileout).appendFile(log_formatted)
        if self.console_out:
            log_formatted = "{color_loglevel}{level}{reset}{color_flag}[{flag}]{reset}:".format(
                level=self.level,
                color_loglevel=self.color_loglevel,
                reset=MetaLogger.reset_,
                flag=flag,
                color_flag=self.color_flag
            )
            print(f"{log_formatted}{data}", end="")


class logger:
    """
    Стандартные логгеры
    """

    info = loglevel(
        "[INFO]",
        color_loglevel=MetaLogger.blue,
        color_flag=MetaLogger.yellow,
    )
    error = loglevel(
        "[ERROR]",
        color_loglevel=MetaLogger.read,
        color_flag=MetaLogger.yellow,
    )
