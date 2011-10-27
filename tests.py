from firemark import Parser
import unittest
import os

class TestParser(unittest.TestCase):

    # Tuple of all possible Markdown syntaxi

    marks = ('# First-level heading #####\n','## Second-level heading\n',
                    '### Third-level heading\n','#### Forth-level heading\n',
                    '##### Fifth-level heading\n','###### Sixth-level heading\n',
                    '*emphasis*', '_emphasis_')
    
    stack = ['one', 'two', 'three']

    def setUp(self):
        """Write a file with all syntax"""
        f = open('test.txt', 'w')
        
        for mark in self.marks:
            f.write(mark)
        f.close()

    def testAddToStack(self):
        c = Parser()
        c.push_stack(self.stack, 'four')
        self.assertEqual(self.stack,['one', 'two', 'three', 'four'],self.stack)
 
    def testClearStack(self):
        c = Parser()
        test = c.clear_stack(self.stack) 
        self.assertEqual(test,[],"Stack not cleared correctly")
            
    def testRemoveHash(self):
        c = Parser()
        test = c.strip_end(self.marks[0])
        self.assertEqual(test,"# First-level heading", "Line not stripped correctly")

    def testConvertH1Hash(self):
        c = Parser()
        test = c.atx_headers(self.marks[0])
        self.assertEqual(test,"<h1> First-level heading </h1>", 
                                "\nLine not converted correctly\nInput: %s\nOutput: %s" % 
                                (self.marks[0], test))
    def testConvertH2Hash(self):
        c = Parser()
        test = c.atx_headers(self.marks[1])
        self.assertEqual(test,"<h2> Second-level heading </h2>", 
                                "\nLine not converted correctly\nInput: %s\nOutput: %s" % 
                                (self.marks[1], test))
 
    def testConvertH3Hash(self):
        c = Parser()
        test = c.atx_headers(self.marks[2])
        self.assertEqual(test,"<h3> Third-level heading </h3>", 
                                "\nLine not converted correctly\nInput: %s\nOutput: %s" % 
                                (self.marks[2], test))
    
    def testConvertH4Hash(self):
        c = Parser()
        test = c.atx_headers(self.marks[3])
        self.assertEqual(test,"<h4> Forth-level heading </h4>", 
                                "\nLine not converted correctly\nInput: %s\nOutput: %s" % 
                                (self.marks[3], test))
 
    def testConvertH5Hash(self):
        c = Parser()
        test = c.atx_headers(self.marks[4])
        self.assertEqual(test,"<h5> Fifth-level heading </h5>", 
                                "\nLine not converted correctly\nInput: %s\nOutput: %s" % 
                                (self.marks[4], test))
 
    def testConvertH6Hash(self):
        c = Parser()
        test = c.atx_headers(self.marks[5])
        self.assertEqual(test,"<h6> Sixth-level heading </h6>", 
                                "\nLine not converted correctly\nInput: %s\nOutput: %s" % 
                                (self.marks[5], test))
 
    def testEmphasisAsk(self):
        c = Parser()
        test = c.emphasis(self.marks[6])
        self.assertEqual(test,"<em>emphasis</em>", "Line not converted correctly")

    def testEmphasisUnder(self):
        c = Parser()
        test = c.emphasis(self.marks[7])
        self.assertEqual(test,"<em>emphasis</em>", "Line not converted correctly")

    def tearDown(self):
        os.remove('test.txt')
        
if __name__ == "__main__":
    unittest.main()
