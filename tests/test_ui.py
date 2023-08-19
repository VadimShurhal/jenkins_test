import os
from distutils import util

import pytest


UI_TESTS = util.strtobool(os.environ.get('UI_TESTS'))


@pytest.mark.skipif(UI_TESTS, reason='Bug 543534')
class TestUI:

    def test_ui_upper(self):
        assert 'foo'.upper() == 'FOO'

    def test_ui_isupper(self):
        assert 'FOO'.isupper()
