from subprocess import check_output, CalledProcessError, STDOUT
from threading import Lock, Thread

# poetry add tqdm
from tqdm import tqdm

from ..logsmal import loglevel


def os_exe_thread(
        label_command: str,
        command_list: list[str],
        call_log_info: loglevel = lambda _x, flag: ...,
        call_log_error: loglevel = lambda _x, flag: ...,
):
    """
    Выполнить команды системы в нескольких потоках

    :param label_command: Общее название команд
    :param command_list: Список команд
    :param call_log_info: Функция для логов информации
    :param call_log_error: Функция для логов ошибок
    """

    lock = Lock()

    def self_(_command: str):
        """

        :param _command:
        """
        try:
            res = check_output(
                _command,
                shell=True,
                stderr=STDOUT,
            )
            with lock:
                call_log_info(f"{_command}:{res.decode('utf-8')}", flag=label_command)

        except CalledProcessError as e:
            with lock:
                call_log_error(f"{_command}:{e.output.decode('utf-8')}", flag=str(e.returncode))

        with lock:
            pbar.update()
            pbar.set_description(f"{_command}")

    list_thread: list[Thread] = []
    with tqdm(total=len(command_list)) as pbar:
        for _command in command_list:
            th = Thread(
                target=self_, args=(_command,),
                name=f"th_{_command}", daemon=True,
            )
            list_thread.append(th)
            th.start()

        for th in list_thread:
            th.join()
