import config

def parse(text):

    for keyword in config.IGNORE_KEYWORDS:
        text = text.replace(keyword, '')
        
    return text.replace('  ', ' ').replace('  ', ' ').strip()
