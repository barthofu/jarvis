import config

def parse(text):

    for keyword in config.IGNORE_KEYWORDS:
        str = str.replace(keyword, '')
        
    return str.replace('  ', ' ').replace('  ', ' ').strip()
