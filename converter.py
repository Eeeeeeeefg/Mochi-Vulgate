import json
import csv

from pprint import pprint

testament = input('Testament')
booknum = input('Book Num')

if testament == "old":
    f = open('old_testament.json', 'r')
    data = json.load(f)
elif testament == 'new':
    f = open('new_testament.json', 'r')
    data = json.load(f)
else:
    print('nah fam')
    exit()


book = data[int(booknum)]
#print(book)


#for chapter in book['chapters']:
#    print(chapter['chapterNumber'])

with open(book['title'], 'w') as file:
     writer = csv.DictWriter(file, delimiter=' ', fieldnames=['textLatin', 'text'], extrasaction='ignore')
     cnt = 1
     writer.writeheader()
     for chapter in book['chapters']:
        for verse in chapter['verses']:
            pprint(verse)
            print(verse.values())
            writer.writerows(verse)

            
        

f.close()