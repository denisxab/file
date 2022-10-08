
from pathlib import Path
from pprint import pprint
import sys
import pytest
from logsmal import logger

sys.path.insert(0, Path(sys.path[0]).parent.parent.parent.__str__())
from mg_file.pcos.base_pcos import os_exe_async


def test_os_exe_async():
    res = os_exe_async([
        'ls .', 
        'lsss /', 
        'sleep 9 && echo 1', 
        # 'ls .', 
        # "sleep 8 && echo 2", 
        # 'ls .',
        # "sleep 7 && echo 3"
        # 'ls .', 
        # "sleep 6 && echo 4", 
        # 'ls .',
        # "sleep 5 && echo 5"
    ])
    # for _x in res:
    #     _x.__str__(
    #         logger_info=logger.info,
    #         logger_error=logger.error, flag="CLONES"
    #     )
    # pprint(res)


test_os_exe_async()
