import json

inputfilename = input('Inform input json filename: ')

with open(inputfilename, 'r') as f:
    data = json.load(f)

# Replace the json extension by xml
outputfilename = inputfilename[0:-5] + '.xml'
with open(outputfilename, 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<graphml xmlns="http://graphml.graphdrawing.org/xmlns"')
    f.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
    f.write(' xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns')
    f.write(' http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">')
    f.write(' <graph id="G" edgedefault="undirected">\n')

    for node in data['nodes']:
        f.write(''' <node id="%s" label="%s" size="%d" 
                    group="%d" main_line="%s" main_area="%s"/>\n''' % (node['id'], node['id'], node['size'], node['group'], node['main_line'], node['main_area']))

    for edge in data['links']:
        f.write(''' <edge source="%s" target="%s" type="%d"
                    value="%d" interarea="%s" interline="%s"/>\n
                ''' % (edge['source'], edge['target'], edge['type'], edge['value'], str(edge['interarea']), str(edge['interline'])))

    f.write(' </graph>\n')
    f.write('</graphml>\n')
