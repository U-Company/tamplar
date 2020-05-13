import os

import pytest

from tamplar import tests
from tamplar.api import methods
from tamplar.tests import utils


def test_run_full():
    methods.init(src_path=tests.src_path, dst_path=tests.dst_path)
    methods.run(src_path=tests.src_path)
    methods.run(src_path=tests.src_path)
