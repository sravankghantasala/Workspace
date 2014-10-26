import random

def getMeAQuote():
	with open('Home/python_scripts/Quotes') as fh:
		quotes = [ line.strip() for line in fh.readlines() if not line.isspace()]
		quote_no = random.randint(0,len(quotes))
		if quotes[quote_no].startswith('('):
			quote = quotes[quote_no + 1]
			auth = quotes[quote_no +2].strip('()')
		else :
			quote = quotes[quote_no]
			auth = quotes[quote_no + 1].strip('()')

	return {'Author': auth, 'Quote': quote}

if __name__ == '__main__':
	getMeAQuote()