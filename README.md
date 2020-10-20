
<img src="https://github.com/cherkesky/Rev2CSV/blob/master/logo.png" height="200" width="800">

### by Guy Cherkesky | [LinkedIn](http://linkedin.com/in/cherkesky) | [Website](http://cherkesky.com) 

Can't get Google Places API to return a review list? 
{
    "html_attributions": [],
    "status": "NOT_FOUND"
}

## Details
Rev2CSV is a simple command line tool that accept a Google Place ID (PID) and scrape your business listing for published review (latest 10) and generate a CSV file that can be imported by many WordPress review plugins

<img src="https://github.com/cherkesky/Rev2CSV/blob/master/scraper.gif" height="400" width="800">
<img src="https://github.com/cherkesky/Rev2CSV/blob/master/csv.png" height="400" width="800">

#### Technology Stack: 
- Python
- Selenium Web Driver
- CSV Library

## Run It Locally

### `python -m venv env`
### `source env/bin/activate`
### `pip install -r requirements.txt`
### `python get_review.py`


Happy Scraping!
