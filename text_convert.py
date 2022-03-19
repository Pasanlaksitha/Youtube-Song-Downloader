import csv

#title artist
def csv_to_txt():
    count = 1
    txt = open('export.txt', 'w',encoding='utf8')
    with open('shazamlibrary.csv', 'r',encoding='utf8') as file:
        reader = csv.reader(file)
        for row in reader:
            title = row[2]
            artist = row[3]
            txt.write(f'{title} - {artist}\n')
            print(count)
            count += 1
    txt.close()

csv_to_txt()