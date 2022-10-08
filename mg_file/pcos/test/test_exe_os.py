
import pytest
from pcos.base_pcos import os_exe_async


def test_os_exe_async():
    os_exe_async([
        """curl \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: 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" \
        "https://api.github.com/users/denisxab"
        """
    ])
    assert 1 == 1
