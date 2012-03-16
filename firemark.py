class Parser: 

    stack = []
    
    stack_ct = 0
 
    def build_block(self, block, line, stack_ct):
        block = self.stack[stack_ct]
                        
        self.stack_ct += 1

    def strip_end(self, line):
        """Strip spaces from lines and remove hashes from the end"""
        
        line = line.strip()
        
        if line[-1] == "#":
            while line[-1] == "#":
                line = line[0:-1]
        line = line.strip()
        
        return line
    
    def atx_headers(self, line):
        """ Convert hashes to <h?> tags """

        line = self.strip_end(line)

        if line.startswith('###### '):
            line = line.replace("###### ","<h6> ")      
            line = line + " </h6>"
            return line 
        elif line.startswith('##### '):
            line = line.replace("##### ","<h5> ")      
            line = line + " </h5>"
            return line 
        elif line.startswith('#### '):
            line = line.replace("#### ","<h4> ")      
            line = line + " </h4>"
            return line 
        elif line.startswith('### '):
            line = line.replace("### ","<h3> ")      
            line = line + " </h3>"
            return line 
        elif line.startswith('## '):
            line = line.replace("## ","<h2> ")      
            line = line + " </h2>"
            return line 
        elif line.startswith('# '):
            line = line.replace("# ","<h1> ")      
            line = line + " </h1>"
            return line 
        else:  
            pass

    def emphasis(self, line):
        """ Convert * and _ to <em> """
        line = self.strip_end(line)
        ct = 0

        while '**' in line:
            if ct == 0: 
                line = line.replace("**", "<em>", 1)
                ct += 1
            else:
                line = line.replace("**", "</em>", 1)
                ct = 0
        
        while '__' in line:
            if ct == 0: 
                line = line.replace("__", "<em>", 1)
                ct += 1
            else:
                line = line.replace("__", "</em>", 1)
                ct = 0

        while '*' in line:
            if ct == 0: 
                line = line.replace("*", "<em>", 1)
                ct += 1
            else:
                line = line.replace("*", "</em>", 1)
                ct = 0
        
        while '_' in line:
            if ct == 0: 
                line = line.replace("_", "<em>", 1)
                ct += 1
            else:
                line = line.replace("_", "</em>", 1)
                ct = 0
            
        return line


    def process_block(self):
        pass
 
if __name__ == '__main__':
    c = Compiler()
    test = open('input.txt', 'r')
    for line in test:
        c.strip_end(line)
        print c.headers(line)
    test.close()


