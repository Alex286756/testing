import json
import os

with open('./coverage/coverage-temp.json') as json_file:
    old_data = json.load(json_file)
os.remove('./coverage/coverage-temp.json')
total = int(float(old_data["totals"]["percent_covered_display"]))
# data = {}
# lines = {'pct': total}
# data_total = {'lines': lines, 'statements': lines, 'functions': lines, 'branches': lines}
# data['total'] = data_total
# with open('./coverage/coverage-summary.json', 'w') as outfile:
#     json.dump(data, outfile)
with open('./.github/workflows/coverage.svg', 'w') as svg_file:
    svg_file.write(f'<svg width="96.3" height="20" viewBox="0 0 963 200" xmlns="http://www.w3.org/2000/svg" '
                   f'role="img" aria-label="coverage: {total}%">\n')
    svg_file.write(f'  <title>coverage: {total}%</title>\n')
    svg_file.write('  <linearGradient id="iASfb" x2="0" y2="100%">\n')
    svg_file.write('    <stop offset="0" stop-opacity=".1" stop-color="#EEE"/>\n')
    svg_file.write('    <stop offset="1" stop-opacity=".1"/>\n')
    svg_file.write('  </linearGradient>\n')
    svg_file.write('  <mask id="MAnTh"><rect width="963" height="200" rx="30" fill="#FFF"/></mask>\n')
    svg_file.write('  <g mask="url(#MAnTh)">\n')
    svg_file.write('    <rect width="603" height="200" fill="#555"/>\n')
    svg_file.write('    <rect width="360" height="200" fill="#F73" x="603"/>\n')
    svg_file.write('    <rect width="963" height="200" fill="url(#iASfb)"/>\n')
    svg_file.write('  </g>\n')
    svg_file.write('  <g aria-hidden="true" fill="#fff" text-anchor="start" font-family="Verdana,DejaVu Sans,'
                   'sans-serif" font-size="110">\n')
    svg_file.write('    <text x="60" y="148" textLength="503" fill="#000" opacity="0.25">coverage</text>\n')
    svg_file.write('    <text x="50" y="138" textLength="503">coverage</text>\n')
    svg_file.write(f'    <text x="658" y="148" textLength="260" fill="#000" opacity="0.25">{total}%</text>\n')
    svg_file.write(f'    <text x="648" y="138" textLength="260">{total}%</text>\n')
    svg_file.write('  </g>\n')
    svg_file.write('</svg>\n')
