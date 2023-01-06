import unittest

from huge import main


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertIsNone(main.important())


if __name__ == "__main__":
    unittest.main()
