import os
import argparse
from string import Template
import json


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--template", required=True,
					help="path to the template xml file")
parser.add_argument("-d", "--data", required=True,
					help="path to the data json file")
parser.add_argument("-o", "--out", required=True,
					help="path to the generated xml file")
args = parser.parse_args()


template = None
with open(args.template, 'r') as f:
	template = Template(f.read())
assert template is not None


data = None
with open(args.data) as f:
	data = json.load(f)
assert data is not None


generated = template.substitute(data)
with open(args.out, 'w') as f:
	f.write(generated)
	print(f"✅ {os.path.abspath(f.name)}")

