from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Create a new Chrome browser window
driver = webdriver.Chrome()

# Navigate to the women's section of the H&M website
driver.get("https://eg.hm.com/en/shop-women/")

# Wait for the page to load
time.sleep(5)

# Use BeautifulSoup to extract the data
soup = BeautifulSoup(driver.page_source, 'html.parser')
data = soup.find_all('aside', {'class': 'c-sidebar-first'})

# Extract links to all product categories
categories = []
info = []
for item in data:
    for link in item.find_all('a'):
        href_value = link.get('href')
        if href_value and href_value.startswith("/en/"):
            # Add https://eg.hm.com/
            href_value = 'https://eg.hm.com' + href_value
            title_name = link.get_text()
            tempList = [title_name,href_value]
            categories.append(tempList)

# Extract the price of the first item on each category page
for category in categories:
    if len(category) > 1:
        driver.get(category[1])
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        data = soup.find_all('div', {'class': 'c-products__item views-row'})
        if len(data) > 0:
            for item in data:
                price = item.find('span', {'class': 'price-amount'})
                Name = item.find('div', {'class': 'aa-suggestion'})
                URL_image = item.find('img')
                price = price.get_text()
                Name = Name.get_text()
                URL_image = URL_image.get('src')
                # Clean the data
                price = price.replace('EGP','').strip()
                Name = Name.strip()
                tempList= [category[0],Name,price,URL_image]
                info.append(tempList)

# Close the browser window
driver.quit()

# Write the data to a CSV file
with open('data.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Category', 'Name', 'Price', 'Image URL'])
    for i in info:
        writer.writerow(i)
# Create a pandas dataframe from the CSV file
df = pd.read_csv('data.csv', encoding='ISO-8859-1')

# Clean the 'Price' column
df['Price'] = df['Price'].str.replace(',', '').astype(float)

# Convert the 'Price' column to numeric
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Drop any rows with NaN values in the 'Price' column
df = df.dropna(subset=['Price'])

# Create a bar chart of the average price by category
avg_price = df.groupby('Category')['Price'].mean()
plt.bar(avg_price.index, avg_price.values)
plt.xticks(rotation=90)
plt.title('Average Price by Category')
plt.xlabel('Category')
plt.ylabel('Price (EGP)')
plt.show()
