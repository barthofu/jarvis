from difflib import SequenceMatcher

class Task:
    
    def __init__(self, phrases = [], stopPriority = False, enabled = True):
        
        self.phrases = phrases
        self.stopPriority = stopPriority
        self.enabled = enabled

            
    def match(self, text):

        matched = []
        
        for phrase in self.phrases:

            comparison = SequenceMatcher(None, phrase, text)
            matched.append(comparison.ratio())

        return matched