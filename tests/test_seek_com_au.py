import os
import sys
import pytest

from seek_com_au import SeekComAu


def test_constructor():
    api = SeekComAu()
    assert api
