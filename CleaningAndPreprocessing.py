# Importing required libraries
import pandas as pd
import numpy as np

# Load Customer Table
customer_df = pd.read_excel("customer_data.xlsx")
# Load Product Table
product_df = pd.read_excel("product_data.xlsx")
# Load Sale Table
sale_df = pd.read_excel("sales_data.xlsx")
# Load Trending Product Table
trending_df = pd.read_excel("trendingproduct_data.xlsx")
# Load Website Access Table
website_df = pd.read_excel("webaccess_data.xlsx")

# Cleaning Customer Table
customer_df = customer_df.dropna()  # Drop rows with null values
customer_df = customer_df.drop_duplicates()  # Remove duplicate rows
# Remove leading/trailing whitespaces
customer_df = customer_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  
# Reset index after cleaning
customer_df.reset_index(drop=True, inplace=True)  # Reset index after cleaning

# Cleaning Product Table
product_df = product_df.dropna()  # Drop rows with null values
product_df = product_df.drop_duplicates()  # Remove duplicate rows
# Remove leading/trailing whitespaces
product_df = product_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  

# Convert Product_Price to numeric, remove '$' and handle wrong format cases
product_df['Product_Price'] = pd.to_numeric(product_df['Product_Price'].replace(r'[\$,]', '', regex=True),
                                             errors='coerce')
product_df.reset_index(drop=True, inplace=True)  # Reset index after cleaning

# Cleaning Sale Table
sale_df = sale_df.dropna()  # Drop rows with null values
sale_df = sale_df.drop_duplicates()  # Remove duplicate rows

 # Remove leading/trailing whitespaces
sale_df = sale_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  

# Convert Sale_Date to datetime and handle wrong format cases
sale_df['Sale_Date'] = pd.to_datetime(sale_df['Sale_Date'], errors='coerce')  
sale_df.reset_index(drop=True, inplace=True)  # Reset index after cleaning

# Cleaning Trending Product Table
trending_df = trending_df.dropna()  # Drop rows with null values
trending_df = trending_df.drop_duplicates()  # Remove duplicate rows

# Remove leading/trailing whitespaces
trending_df = trending_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x) 

trending_df.reset_index(drop=True, inplace=True)  # Reset index after cleaning

# Cleaning Website Access Table
website_df = website_df.dropna()  # Drop rows with null values
website_df = website_df.drop_duplicates()  # Remove duplicate rows

# Remove leading/trailing whitespaces
website_df = website_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  

 # Convert Access_Date to datetime and handle wrong format cases
website_df['Access_Date'] = pd.to_datetime(website_df['Access_Date'], errors='coerce') 
website_df.reset_index(drop=True, inplace=True)  # Reset index after cleaning

#tables after cleaning and preprocessed
print("Cleaned and Preprocessed Customer Table:")
print(customer_df)
print("\nCleaned and Preprocessed Product Table:")
print(product_df)
print("\nCleaned and Preprocessed Sale Table:")
print(sale_df)
print("\nCleaned and Preprocessed Trending Product Table:")
print(trending_df)
print("\nCleaned and Preprocessed Website Access Table:")
print(website_df)