class Main:
    
    def __init__(self, 
                 words = [], 
                 patterns = [], 
                 ):
        
        if words:
            p = r'.*\b('
            p += str(words)[1:-1].replace('\'', '').replace(', ', '|')
            p += r')\b.*'
            patterns.append(p)

        self.patterns = patterns
            
            
    def match(self, text):
        
        for pattern in self.patterns:
            if pattern.match(text):
                return True
        return False
    
    
    def run(self):
        print('YES')