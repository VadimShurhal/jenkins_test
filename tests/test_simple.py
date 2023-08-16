import distutils
import os

import pytest

TEST_UPPER = bool(eval(os.environ.get('TEST_UPPER')))
TEST_ISUPPER = bool(eval(os.environ.get('TEST_ISUPPER')))


class TestClass:

    @pytest.mark.skipif(TEST_UPPER, reason='Bug 543534')
    def test_upper(self):
        assert 'foo'.upper() == 'FOO'

    @pytest.mark.skipif(TEST_ISUPPER, reason='Bug 42342')
    def test_isupper(self):
        assert 'FOO'.isupper()
