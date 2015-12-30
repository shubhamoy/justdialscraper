#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==========================================================================
# Just Dial Scraper
# Original Author: Rushi Agrawal(rushi.agr@gmail.com)
# Source: http://www.rushiagr.com/blog/2015/09/14/quick-justdial-scraper/
# Modified by Shubhamoy (me@shubhamoy.com)
# ==========================================================================
import csv
import json
import requests
from bs4 import BeautifulSoup

print(25*"=")
print("Just Dial Scraper")
print(25*"=")

url = 'http://www.justdial.com/functions/ajxsearch.php?national_search=0&act'\
'=pagination&city={0}&search={1}&page={2}'
what = input("Enter your Query: ")
what = what.replace(' ', '+')
where = input("Enter the Location: ")

with open(what+"_"+where+'.csv', 'w') as f:
    f.write('company, address, phone\n')
    page = 1
    while True:
        print('Scraping Page', page)
        resp = requests.get(url.format(where, what, page))
        
        if not resp.json()['paidDocIds']:
            print(25*"-")
            print('Scraping Finished')
            print(25*"-")
            break

        markup = resp.json()['markup'].replace('\/', '/')
        soup = BeautifulSoup(markup, 'html.parser')

        for thing in soup.find_all('section'):
            csv_list = []
            if thing.get('class') == ['jcar']:
                # Company name
                for a_tag in thing.find_all('a'):
                    if a_tag.get('onclick') == "_ct('clntnm', 'lspg');":
                        csv_list.append(a_tag.get('title'))

                # Address
                for span_tag in thing.find_all('span'):
                    if span_tag.get('class') == ['mrehover', 'dn']:
                        csv_list.append(span_tag.get_text().strip())

                # Phone number
                for a_tag in thing.find_all('a'):
                    if a_tag.get('href').startswith('tel:'):
                        csv_list.append(a_tag.get('href').split(':')[-1])

                csv_list = ['"'+item+'"' for item in csv_list]
                writeline = ','.join(csv_list)+'\n'
                f.write(','.join(csv_list)+'\n')
        page += 1
