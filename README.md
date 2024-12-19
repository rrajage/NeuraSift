1. What the Code Does
An AI bot to extract product data from Amazon website and do a basic analysis on the extracted data is created by the given Python code. However,
It relies on web scraping techniques to collect information product titles, prices, ratings and product urls for a given search query.
The pages where the data is collected are all pulled together and organized in a structured manner for researching.
Furthermore, we calculate average prices and ratings and find the highest rated products. We show these results in the console and save them in a CSV file for a future use.
This script demonstrates collecting, and analyzing your data to derive actionable insights.

2. Structure of the Code
The code is structured into four main sections:

Library Imports: Starting at the beginning they import key libraries such as requests (HTTP requests), Beautiful Soup (HTML parsing), and pandas (data manipulation and analysis).
Data Scraping Function (scrape_amazon_data): This function receives a query to search and the amount of pages to scrape. It makes HTTP requests to Amazon's search results page and loads
HTML using BeautifulSoup and pulls out product details relevant to you. This data is stored in a pandas DataFrame.
Data Analysis Function (analyze_data): The scraped data passed to this function. It computes average product prices and ratings, identifies top rated products 
and displays these insights. Here you will see data cleaning and conversions (for example, going from a price to a numerical value representation).
Main Execution Block: It takes inputs (search term and the number of pages) through the script then it runs the scraping and the analysis function and saves the result in a CSV file, amazon products CSV.

3. How to Prepare to Run
To prepare the script for execution:

Python Environment: In case you don’t have Python 3.6 or above installed on your system, make sure you have installed it.
Install Required Libraries: To install the needed libraries run:
You can install it with: 
pip install requests beautifulsoup4 pandas
Check Website Terms: Always review Amazon’s terms of service to make sure you fit their guidelines. If your scraping is heavy, 
you might want to use an Amazon API (if available) or enhance your script to use proxy.
Save the Script: Store the code in a file with a .py extension e.g amazon_scraper.py.

4. How to Run
Run the Script: If the script is in a directory you can open the terminal or command prompt in that directory and execute:
python amazon_scraper.py
Provide User Inputs: When prompted, enter:
Here the search term that we’re looking for (e.g. laptops).
2: number of pages to scrape (e.g.).
View Outputs:
Total number of scraped products and their analysis will be displayed to the console from the script.
The scraped product data will be contained in a CSV file (amazon_products.csv) put it the same directory.
Inspect and Analyze: To analyse or visualize further, open the CSV file in tools like Excel or Python.
