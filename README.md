[![Codacy Badge](https://api.codacy.com/project/badge/grade/515c6e91d147465f97181e44aef7f803)](https://www.codacy.com/app/shubhamoy/justdialscraper)
# Just Dial Scraper

It takes the search term and location as input. After successful scraping, it writes down to a CSV file. Feel free to share and modify.

#### Initial Configuration

```
virtualenv -p /usr/local/bin/python3 py3env 
(Your python path may be different, check using which python3)
source py3env/bin/activate
pip install beautifulsoup4
pip install requests
```



#### Usage
```
python3 justdialscraper.py
=========================
Just Dial Scraper
=========================
Enter your Query: Electrical Shops
Enter the City: Agra
Scraping Page 1
.
.
.
Scraping Finished
```
