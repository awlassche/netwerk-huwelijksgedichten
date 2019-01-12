from csv import DictReader, writer
csvfile = open("/Users/alielassche/Dropbox/Student-assistentschap/Netwerken_huwelijksgedichten/Gephi/kopie300records.csv")
huwged = DictReader(csvfile, delimiter=';')
print(huwged)

# for row in huwged:
#     for cell in row:
#         print(cell)


for row in huwged:
    print(row['Auteur2'])