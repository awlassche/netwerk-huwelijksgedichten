import csv

def writecsv(csvwriter, attribs, d):
    l = []
    for a in attribs:
        l.append(d[a])
    csvwriter.writerow(l)

def loadrowdict(nodescsv):
    rowDict = {}
    for node in nodescsv:
        rowDict[node['label']] = node
    return rowDict

def removeBrackets(name):
    result = name
    start = name.find('(')
    end = name.find(')')
    if start != -1 and end != -1:
        result = name[:start - 1] + name[end + 1:]
    return result


file_loc = "/Users/alielassche/dropbox/student-assistentschap/netwerken_huwelijksgedichten/gedichtenGGD_STCN.csv"
gedichten = csv.DictReader(open(file_loc, newline='', encoding='utf-8'), delimiter=';',
                         quotechar='"')


nodesloc = '/Users/alielassche/dropbox/student-assistentschap/netwerken_huwelijksgedichten/nodes.csv'
nodescsv = csv.DictReader(open(nodesloc, newline='', encoding='utf-8'), delimiter=';',
                         quotechar='"')

edgesfile = '/Users/alielassche/dropbox/student-assistentschap/netwerken_huwelijksgedichten/edges.csv'
f = open(edgesfile, 'w', newline='', encoding='utf-8')
csvWriter = csv.writer(f, delimiter=';', quotechar='"',
                           quoting=csv.QUOTE_MINIMAL)
attribs = ['source', 'target', 'weight']
csvWriter.writerow(attribs)

tupleDict = {}
if __name__ == '__main__':
    rowDict = loadrowdict(nodescsv)
    for gedicht in gedichten:
        connectionlist = []
        for item in gedicht:
            if item == 'Drukker' or item == 'Bruidspaar' or 'Auteur' in item:
                if gedicht[item] != '' and gedicht[item] != ' ':
                    stripped_name = gedicht[item].strip()
                    at_id = rowDict[stripped_name]['id']
                    connectionlist.append(at_id)
        resultlist = []
        for connection in connectionlist:
            myindex = connectionlist.index(connection)
            newlist = connectionlist[:myindex] + connectionlist[myindex + 1:]
            for item in newlist:
                mytuple = (connection, item)
                backtuple = (item, connection)
                if backtuple not in resultlist:
                    resultlist.append(mytuple)
        for tuple in resultlist:
            item, connection = tuple
            backtuple = (connection, item)
            if tuple not in tupleDict and backtuple not in tupleDict:
                tupleDict[tuple] = 1
            else:
                if tuple in tupleDict:
                    tupleDict[tuple] += 1
                if backtuple in tupleDict:
                    tupleDict[backtuple] += 1

for tuple in tupleDict:
    writeDict = {}
    writeDict['source'] = tuple[0]
    writeDict['target'] = tuple[1]
    writeDict['weight'] = tupleDict[tuple]
    writecsv(csvWriter, attribs, writeDict)


f.close()

####VANAF HIER: ACHTERNAMEN
f = open(edgesfile, 'a', newline='', encoding='utf-8')
csvWriter = csv.writer(f, delimiter=';', quotechar='"',
                           quoting=csv.QUOTE_MINIMAL)
gedichten = csv.DictReader(open(file_loc, newline='', encoding='utf-8'), delimiter=';',
                         quotechar='"')
nodesloc = '/Users/alielassche/dropbox/student-assistentschap/netwerken_huwelijksgedichten/nodes.csv'
nodescsv = csv.DictReader(open(nodesloc, newline='', encoding='utf-8'), delimiter=';',
                         quotechar='"')

rowDict = loadrowdict(nodescsv)
tupledict = {}
for gedicht in gedichten:
    bruidspaar = gedicht['Bruidspaar']
    names = bruidspaar.split('&')
    for name in names:
        name = removeBrackets(name)
        while '(' in name:
            name = removeBrackets(name)
        strip_name = name.strip()
        alln = strip_name.split(' ')
        bruidspaar_stripped = bruidspaar.strip()
        if alln[-1] not in tupledict:
            tupledict[alln[-1]] = [rowDict[bruidspaar_stripped]['id']]
        elif alln[-1] in tupledict:
            alist = tupledict[alln[-1]]
            alist.append(rowDict[bruidspaar_stripped]['id'])
            tupledict[alln[-1]] = alist
resultlist = []
for lastname in tupledict:
    if len(tupledict[lastname]) > 1:
        connectionlist = tupledict[lastname]
        for connection in connectionlist:
            myindex = connectionlist.index(connection)
            newlist = connectionlist[:myindex] + connectionlist[myindex + 1:]
            for item in newlist:
                mytuple = (connection, item)
                backtuple = (item, connection)
                if backtuple not in resultlist:
                    resultlist.append(mytuple)
for tuple in resultlist:
    appendDict = {}
    appendDict['source'] = tuple[0]
    appendDict['target'] = tuple[1]
    appendDict['weight'] = '1'
    writecsv(csvWriter, attribs, appendDict)