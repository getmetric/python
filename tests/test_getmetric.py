import time

from getmetric.getmetric import Getmetric
from tests import *


class TestGetmetric(unittest.TestCase):

    def test_good_values(self):
        errors = []
        gm = Getmetric(async_dump=False)
        if not gm.push_measure("dummy", 1):
            errors.append("int push fail")
        if not gm.push_measure("dummy", 1.1):
            errors.append("float push fail")
        if not gm.push_measures("dummy", {"f1": 1, "f2": 1.1}):
            errors.append("multiple fields push fail")
        self.assert_(len(errors) < 1, "test_good_values: errors occurred:\n{}".format("\n".join(errors)))

    def test_bad_values(self):
        errors = []
        gm = Getmetric(async_dump=False)
        if gm.push_measure("dummy", "way to fail"):
            errors.append("string push is not failed")
        if gm.push_measure("dummy", ""):
            errors.append("empty string push is not failed")
        if gm.push_measure("dummy", None):
            errors.append("None push is not failed")
        if gm.push_measures("dummy", ""):
            errors.append("measures empty string push is not failed")
        if gm.push_measures("dummy", None):
            errors.append("measures None push is not failed")
        if gm.push_measures("dummy", {}):
            errors.append("measures empty dict push is not failed")
        if gm.push_measures("dummy", {"f1": ""}):
            errors.append("measures empty string value push is not failed")
        if gm.push_measures("dummy", {"f1": None}):
            errors.append("measures Nona value push is not failed")
        self.assert_(len(errors) < 1, "test_bad_values: errors occurred:\n{}".format("\n".join(errors)))

    def test_good_per_sec_values(self):
        errors = []
        gm = Getmetric(async_dump=False)
        if not gm.push_per_second_measure("BD6aRuuLA4SEFZ8dCfkAmXn6gAHeeHfrMWJ", 1):
            errors.append("push int failed")
        if not gm.push_per_second_measure("BD6aRuuLA4SEFZ8dCfkAmXn6gAHeeHfrMWJ", 1.1):
            errors.append("push float failed")
        self.assert_(len(errors) < 1, "test_good_per_sec_values: errors occurred:\n{}".format("\n".join(errors)))

    def test_bad_per_sec_values(self):
        errors = []
        gm = Getmetric(async_dump=False)
        if gm.push_per_second_measure("BD6aRuuLA4SEFZ8dCfkAmXn6gAHeeHfrMWJ", None):
            errors.append("push None is not failed")
        if gm.push_per_second_measure("BD6aRuuLA4SEFZ8dCfkAmXn6gAHeeHfrMWJ", ""):
            errors.append("push string is not failed")
        if gm.push_per_second_measures("BD6aRuuLA4SEFZ8dCfkAmXn6gAHeeHfrMWJ", []):
            errors.append("push empty array is not failed")
        if gm.push_per_second_measures("BD6aRuuLA4SEFZ8dCfkAmXn6gAHeeHfrMWJ", {}):
            errors.append("push empty dict is not failed")
        self.assert_(len(errors) < 1, "test_bad_per_sec_values: errors occurred:\n{}".format("\n".join(errors)))

    @pytest.mark.xfail
    def test_overflow(self):
        gm = Getmetric(async_dump=False, max_queue_len=10)
        for x in range(10):
            gm.push_measure("dummy", x)

        self.assertEqual(True, gm.push_measure("dummy", 11))

    def test_fake_send(self):
        gm = Getmetric(async_dump=True, send_period_sec=1, send_debug=True)
        gm.push_measure("dummy", 11)
        time.sleep(1.5)
        gm.stop()
        self.assertEqual(gm.get_sent_count(), 1)
