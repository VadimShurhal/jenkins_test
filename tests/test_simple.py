import os

import pytest

TEST_UPPER = os.environ.get('TEST_UPPER')
TEST_ISUPPER = os.environ.get('TEST_ISUPPER')


class TestClass:

    @pytest.mark.skipif(bool(TEST_UPPER), reason='Bug 543534')
    def test_upper(self):
        assert 'foo'.upper() == 'FOO'

    @pytest.mark.skipif(bool(TEST_ISUPPER), reason='Bug 42342')
    def test_isupper(self):
        assert 'FOO'.isupper()
