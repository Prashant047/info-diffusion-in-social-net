import csv
import re

with open('MeToo.csv') as input_file:
    csv_reader = csv.reader(input_file, delimiter=",")
    for i, row in enumerate(csv_reader):
        if i is 23:
            break

        text = row[1][1:]
        url_regex = 'https://t.co/[\w]*'
        tag_regex = '@[\w]*'
        b_code = '[\w]*(\\x[\w]{2})[\w]*'

        urls = re.findall(url_regex, text)
        tags = re.findall(tag_regex, text)
       

        for url in urls:
            text = text.replace(url, '')
        for tag in tags:
            text = text.replace(tag, '')
        text = text.replace('RT : ', '')
        text = text.replace("\\n", '')

        print(text)
