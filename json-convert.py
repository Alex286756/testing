import json
import os

with open('./coverage/coverage-temp.json') as json_file:
    old_data = json.load(json_file)
os.remove('./coverage/coverage-temp.json')
total = int(float(old_data["totals"]["percent_covered_display"]))
data = {}
lines = {'pct': total}
data_total = {'lines': lines, 'statements': lines, 'functions': lines, 'branches': lines}
data['total'] = data_total
with open('./coverage/coverage-summary.json', 'w') as outfile:
    json.dump(data, outfile)
