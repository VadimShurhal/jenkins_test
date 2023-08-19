import os
from distutils import util

import pytest


API_TESTS = util.strtobool(os.environ.get('API_TESTS'))


@pytest.mark.skipif(API_TESTS, reason='Bug 543534')
class TestApi:

    def test_api_upper(self):
        assert 'foo'.upper() == 'FOO'

    def test_api_isupper(self):
        assert 'FOO'.isupper()
