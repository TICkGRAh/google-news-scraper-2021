
import pandas as pd
import os 	
import json

def output_json(all_data, keyword):
	if 'json' not in os.listdir():
		os.mkdir('json')
	with open(f'json/{keyword.replace("+", "-")}.json', 'w') as f:
		json.dump(all_data, f, indent=4)


def output_csv(all_data, keyword):
	if 'csv' not in os.listdir():
		os.mkdir('csv')
	df = pd.DataFrame(all_data)
	df.to_csv(f'csv/{keyword.replace("+", "-")}.csv', index=False)
