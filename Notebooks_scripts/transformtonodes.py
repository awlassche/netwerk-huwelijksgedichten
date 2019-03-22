import csv

def writecsv(csvwriter, attribs, d):
    l = []
    for a in attribs:
        l.append(d[a])
    csvwriter.writerow(l)

file_loc = "/Users/alielassche/documents/github/netwerk-huwelijksgedichten/data/gedichtenGGD_STCN_Steur_stripped.csv"
gedichten = csv.DictReader(open(file_loc, newline='', encoding='utf-8'), delimiter=';',
                         quotechar='"')

f = open('/Users/alielassche/documents/github/netwerk-huwelijksgedichten/data/nodes.csv', 'w', newline='', encoding='utf-8')
csvWriter = csv.writer(f, delimiter=';', quotechar='"',
                           quoting=csv.QUOTE_MINIMAL)
attribs = ['id', 'label', 'function', 'year', 'place_print']
csvWriter.writerow(attribs)
rowDict = {}
id = 1
for gedicht in gedichten:
    for item in gedicht:
        writeDict = {}
        if item == 'Drukker' or item == 'Bruidspaar' or 'Auteur' in item:
            if gedicht[item] != '' and gedicht[item] != ' ':
                if 'Auteur' in item:
                    function = 'Auteur'
                else:
                    function = item
                stripped_name = gedicht[item].strip()
                if stripped_name not in rowDict:
                    writeDict['id'] = id
                    id += 1
                    writeDict['label'] = stripped_name
                    writeDict['function'] = function
                    if item == 'Bruidspaar':
                        writeDict['year'] = gedicht['Jaar']
                    else:
                        writeDict['year'] = ''
                    if item == 'Drukker':
                        writeDict['place_print'] = gedicht['Plaats_druk']
                    else:
                        writeDict['place_print'] = ''
                    rowDict[writeDict['label']] = writeDict
                elif stripped_name in rowDict:
                    writeDict = rowDict[stripped_name]
                    if function not in writeDict['function']:
                        if function[0] == 'D':
                            writeDict['function'] += ', ' + function
                        elif function[0] == 'A':
                            writeDict['function'] = function + ', ' + writeDict['function']
                        else:
                            writeDict['function'] += ', ' + function
                    rowDict[stripped_name] = writeDict

for author in rowDict:
    writeDict = rowDict[author]
    writecsv(csvWriter, attribs, writeDict)


