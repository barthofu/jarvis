import config
from difflib import SequenceMatcher

class Task:
    
    def __init__(self, phrases = [], stopPriority = False):
        
        self.phrases = phrases

        # if phrases:
        #     p = r'.*\b('
        #     p += str(words)[1:-1].replace('\'', '').replace(', ', '|')
        #     p += r')\b.*'
        #     patterns.append(p)

        # self.patterns = patterns
            
            
    def match(self, text):

        matched = []
        
        for phrase in self.phrases:

            comparison = SequenceMatcher(None, phrase, text)
            matched.append(comparison.ratio())

        return matched
        