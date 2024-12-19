import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape product data from Amazon
def scrape_amazon_data(search_query, num_pages=1):
    base_url = "https://www.amazon.com/s?k="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US, en;q=0.5"
    }
    
    product_data = []

    for page in range(1, num_pages + 1):
        url = f"{base_url}{search_query}&page={page}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            results = soup.find_all("div", {"data-component-type": "s-search-result"})

            for result in results:
                title = result.h2.text if result.h2 else "N/A"
                price = result.find("span", class_="a-price-whole")
                price = price.text if price else "N/A"
                rating = result.find("span", class_="a-icon-alt")
                rating = rating.text.split()[0] if rating else "N/A"
                link = result.h2.a["href"] if result.h2 and result.h2.a else "N/A"

                product_data.append({
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Link": f"https://www.amazon.com{link}"
                })
        else:
            print(f"Failed to retrieve page {page}")
    
    return pd.DataFrame(product_data)

# Function to analyze the data
def analyze_data(df):
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
    avg_price = df["Price"].mean()
    avg_rating = df["Rating"].mean()
    top_products = df.sort_values(by="Rating", ascending=False).head(5)

    print(f"Average Price: ${avg_price:.2f}")
    print(f"Average Rating: {avg_rating:.2f}")
    print("\nTop 5 Products:")
    print(top_products)

# Main execution
if __name__ == "__main__":
    search_term = input("Enter the search term: ")
    num_pages = int(input("Enter the number of pages to scrape: "))

    print("Scraping data...")
    data = scrape_amazon_data(search_term, num_pages)
    
    if not data.empty:
        print(f"Data scraped: {len(data)} products")
        print("Performing analysis...")
        analyze_data(data)
        # Save to CSV
        data.to_csv("amazon_products.csv", index=False)
        print("Data saved to 'amazon_products.csv'")
    else:
        print("No data found!")
