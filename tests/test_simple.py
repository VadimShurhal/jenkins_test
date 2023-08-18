import os
from distutils import util

import pytest

TEST_UPPER = util.strtobool(os.environ.get('TEST_UPPER'))
TEST_ISUPPER = util.strtobool(os.environ.get('TEST_ISUPPER'))


class TestClass:

    @pytest.mark.skipif(TEST_UPPER, reason='Bug 543534')
    def test_upper(self):
        assert 'foo'.upper() == 'FOO'

    @pytest.mark.skipif(TEST_ISUPPER, reason='Bug 42342')
    def test_isupper(self):
        assert 'FOO'.isupper()
