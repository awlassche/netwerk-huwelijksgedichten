import csv

def writecsv(csvwriter, attribs, d):
    l = []
    for a in attribs:
        l.append(d[a])
    csvwriter.writerow(l)

file_loc = "/Users/alielassche/Dropbox/Student-assistentschap/Netwerken_huwelijksgedichten/gedichtenGGD_STCN.csv"
gedichten = csv.DictReader(open(file_loc, newline='', encoding='utf-8'), delimiter=';',
                         quotechar='"')

f = open('/Users/alielassche/Dropbox/Student-assistentschap/Netwerken_huwelijksgedichten/nodes.csv', 'w', newline='', encoding='utf-8')
csvWriter = csv.writer(f, delimiter=';', quotechar='"',
                           quoting=csv.QUOTE_MINIMAL)
attribs = ['id', 'label', 'function', 'date', 'place']
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
                        writeDict['date'] = gedicht['Datum']
                    else:
                        writeDict['date'] = ''
                    if item == 'Drukker':
                        writeDict['place'] = gedicht['Plaats']
                    else:
                        writeDict['place'] = ''
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


