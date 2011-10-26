class Compiler:

    def strip_end(self, line):
        """Strip spaces from lines and remove hashes from the end"""
        
        line = line.strip()
        
        if line[-1] == "#":
            while line[-1] == "#":
                line = line[0:-1]
        line = line.strip()
        
        return line
    
    def headers(self, line):
        """ Convert hashes to <h?> tags """

        line = self.strip_end(line)

        if '###### ' in line:
            line = line.replace("###### ","<h6> ")      
            line = line + " </h6>"
            return line 
        elif '##### ' in line:
            line = line.replace("##### ","<h5> ")      
            line = line + " </h5>"
            return line 
        elif '#### ' in line:
            line = line.replace("#### ","<h4> ")      
            line = line + " </h4>"
            return line 
        elif '### ' in line:
            line = line.replace("### ","<h3> ")      
            line = line + " </h3>"
            return line 
        elif '## ' in line:
            line = line.replace("## ","<h2> ")      
            line = line + " </h2>"
            return line 
        elif '# ' in line:
            line = line.replace("# ","<h1> ")      
            line = line + " </h1>"
            return line 
        else:  
            pass
 
if __name__ == '__main__':
    c = Compiler()
    test = open('input.txt', 'r')
    for line in test:
        c.strip_end(line)
        print c.headers(line)
    test.close()


