

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import argparse
import datetime
from outputs import output_json, output_csv
import pandas as pd
import os

iso_codes = pd.read_json('iso-lang-codes.json')['Code'].tolist()

def parse_args():
	parser = argparse.ArgumentParser(description='Google News Scraper')
	parser.add_argument('-k', '--keyword', required=True, help='Enter Keyword')
	parser.add_argument('-l', '--location', required=True, help='ISO_639-1 code representation for desired location')
	parser.add_argument('-o', '--output', required=True, help='Output format: csv or json')
	args = vars(parser.parse_args())

	if args['output'].strip() not in ['csv','json']:
		print(f'Output must be csv or json. You\'ve declared: {args["output"].strip()}')
		return

	if args['location'].strip() not in iso_codes:
		print(f'''"{args["location"].strip()}" ISO code is not on the list.
Check iso-lang-codes.json file for all the available codes of locations. ''')
		return

	return get_news(args)

def get_news(args):
	all_data = []

	keyword = quote_plus(args['keyword'].strip())
	output = args['output'].strip()
	loc = quote_plus(args['location'].strip())
	r = f'https://news.google.com/rss/search?q={keyword}&hl={loc}'

	resp = requests.get(r)
	soup = BeautifulSoup(resp.text, 'lxml')
	data = soup.select('item')

	for i in data:

		x = {
		'title': ''.join([x.text for x in i.select('title')]),
		'link': ''.join([x.text.split()[1][6:].replace('"', '') for x in i.select('description')]),
		'publication_date': ''.join([str(datetime.datetime.strptime(x.text[5:-13], '%d %b %Y')).split()[0] for x in i.select('pubDate')])
		
		}

		all_data.append(x)

	if output == 'csv':
		print('''Finished scraping for keyword: %s
Results Gathered: %s
File Location: %s''' %
		(args["keyword"].strip(), len(all_data), os.path.join(os.getcwd(), output, keyword.replace("+", "-") + (".csv" if output.endswith("csv") else ".json"))))
		return output_csv(all_data, keyword)

	elif output == 'json':
		print('''Finished scraping for keyword: %s
Results Gathered: %s
File Location: %s''' %
		(args["keyword"].strip(), len(all_data), os.path.join(os.getcwd(), output, keyword.replace("+", "-") + (".csv" if output.endswith("csv") else ".json"))))
		return output_json(all_data, keyword)

if __name__ == '__main__':
	parse_args()






