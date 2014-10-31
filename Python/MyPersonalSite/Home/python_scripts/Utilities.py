import random
import os

def getMeAQuote():
    with open(os.path.join(os.path.dirname(__file__), 'Quotes'), 'r', encoding='utf-8') as fh:
        quotes = [ line.strip() for line in fh.readlines() if not line.isspace()]
        quote_no = random.randint(0, len(quotes))
        if quotes[quote_no].startswith('('):
            quote = quotes[quote_no + 1]
            auth = quotes[quote_no + 2].strip('()')
        else :
            quote = quotes[quote_no]
            auth = quotes[quote_no + 1].strip('()')

    return {'Author': auth, 'Quote': quote}

if __name__ == '__main__':
    getMeAQuote()
