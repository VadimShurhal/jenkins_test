import os
from distutils import util

import pytest

DB_TESTS = util.strtobool(os.environ.get('DB_TESTS'))


@pytest.mark.skipif(DB_TESTS, reason='Bug 543534')
class TestDB:

    def test_db_upper(self):
        assert 'foo'.upper() == 'FOOd'

    def test_db_isupper(self):
        assert 'FOO'.isupper()
