from firemark import Compiler
import unittest
import os

class TestCompiler(unittest.TestCase):

    # Tuple of all possible Markdown syntaxi

    marks = ('# First-level heading #####\n','## Second-level heading\n',
                    '### Third-level heading\n','#### Forth-level heading\n',
                    '##### Fifth-level heading\n','###### Sixth-level heading\n',
                    '*emphasis*', '_emphasis_')

    def setUp(self):
        """Write a file with all syntax"""
        f = open('test.txt', 'w')
        
        for mark in self.marks:
            f.write(mark)
        f.close()
    
    def testRemoveHash(self):
        c = Compiler()
        test = c.strip_end(self.marks[0])
        self.assertEqual(test,"# First-level heading", "Line not stripped correctly")

    def testConvertH1Hash(self):
        c = Compiler()
        test = c.atx_headers(self.marks[0])
        self.assertEqual(test,"<h1> First-level heading </h1>", 
                                "\nLine not converted correctly\nInput: %s\nOutput: %s" % 
                                (self.marks[0], test))
    def testConvertH2Hash(self):
        c = Compiler()
        test = c.atx_headers(self.marks[1])
        self.assertEqual(test,"<h2> Second-level heading </h2>", 
                                "\nLine not converted correctly\nInput: %s\nOutput: %s" % 
                                (self.marks[1], test))
 
    def testConvertH3Hash(self):
        c = Compiler()
        test = c.atx_headers(self.marks[2])
        self.assertEqual(test,"<h3> Third-level heading </h3>", 
                                "\nLine not converted correctly\nInput: %s\nOutput: %s" % 
                                (self.marks[2], test))
    
    def testConvertH4Hash(self):
        c = Compiler()
        test = c.atx_headers(self.marks[3])
        self.assertEqual(test,"<h4> Forth-level heading </h4>", 
                                "\nLine not converted correctly\nInput: %s\nOutput: %s" % 
                                (self.marks[3], test))
 
    def testConvertH5Hash(self):
        c = Compiler()
        test = c.atx_headers(self.marks[4])
        self.assertEqual(test,"<h5> Fifth-level heading </h5>", 
                                "\nLine not converted correctly\nInput: %s\nOutput: %s" % 
                                (self.marks[4], test))
 
    def testConvertH6Hash(self):
        c = Compiler()
        test = c.atx_headers(self.marks[5])
        self.assertEqual(test,"<h6> Sixth-level heading </h6>", 
                                "\nLine not converted correctly\nInput: %s\nOutput: %s" % 
                                (self.marks[5], test))
 
    def testEmphasisAsk(self):
        c = Compiler()
        test = c.emphasis(self.marks[6])
        self.assertEqual(test,"<em>emphasis</em>", "Line not converted correctly")

    def testEmphasisUnder(self):
        c = Compiler()
        test = c.emphasis(self.marks[7])
        self.assertEqual(test,"<em>emphasis</em>", "Line not converted correctly")

    def tearDown(self):
        os.remove('test.txt')

if __name__ == "__main__":
    unittest.main()
