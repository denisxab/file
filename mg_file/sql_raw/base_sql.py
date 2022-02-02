from typing import Callable, Any

# Необходимо переопределить
CONNECT: Callable | object | None = None
ERROR: BaseException | None = None
MUTABLE_COMMAND_A: Callable[[Any, str, tuple | dict | list], Any] | None = None
READ_COMMAND_A: Callable[[Any, str, tuple | dict | list], Any] | None = None
# Переопределится в функции `Config`
SETTINGS_DB: dict | None = None
