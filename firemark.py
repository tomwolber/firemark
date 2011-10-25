
class Compiler:
    
    def filterHeaders(self, dirty):
        if '### ' in dirty:
            dirty = dirty.replace("### ","<h3>").strip()      
            dirty = dirty + "</h3>"
            print dirty 
        elif '## ' in dirty:
            dirty = dirty.replace("## ","<h2>").strip()      
            dirty = dirty + "</h2>"
            print dirty 
        elif '# ' in dirty:
            dirty = dirty.replace("# ","<h1>").strip()      
            dirty = dirty + "</h1>"
            print dirty 
            
        else:  
            pass
 
if __name__ == '__main__':
    c = Compiler()
    test = open('input.txt', 'r')
    for line in test:
        c.filterHeaders(line)
    test.close()


