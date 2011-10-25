from firemark import Compiler
import unittest

class TestCompiler(unittest.TestCase):

    def setUp(self):
        self.test_data = "mark" 
    
    def testEntity(self):

        self.assertEqual(self.test_exists, True, 'Test does not exists')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
