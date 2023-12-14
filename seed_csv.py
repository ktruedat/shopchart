import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Function to generate random date within a given range
def random_date(start_date, end_date):
    return fake.date_between_dates(date_start=start_date, date_end=end_date)

# Function to generate random decimal number
def random_decimal(start, end, precision):
    return round(random.uniform(start, end), precision)

# Function to generate seed data for Categories
def generate_categories_data(num_records):
    categories_data = []
    for _ in range(num_records):
        category_id = fake.random_int(min=1, max=100)
        category_name = fake.word()
        categories_data.append((category_id, category_name))
    return categories_data

# Function to generate seed data for Customers
def generate_customers_data(num_records):
    customers_data = []
    for _ in range(num_records):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        customers_data.append((name, email, phone))
    return customers_data

# Function to generate seed data for Producers
def generate_producers_data(num_records):
    producers_data = []
    for _ in range(num_records):
        producer_name = fake.company()
        producer_location = fake.city()
        producers_data.append((producer_name, producer_location))
    return producers_data

# Function to generate seed data for Products
def generate_products_data(num_records, num_categories, num_producers):
    products_data = []
    for _ in range(num_records):
        name = fake.word()
        category_id = fake.random_int(min=1, max=num_categories)
        price = random_decimal(10, 200, 2)
        producer_id = fake.random_int(min=1, max=num_producers)
        products_data.append((name, category_id, price, producer_id))
    return products_data

# Function to generate seed data for Promotions
def generate_promotions_data(num_records):
    promotions_data = []
    for _ in range(num_records):
        promotion_name = fake.word()
        discount_percentage = random_decimal(0, 50, 2)
        start_date = random_date(datetime(2023, 1, 1), datetime(2023, 12, 31))
        end_date = start_date + timedelta(days=fake.random_int(min=1, max=30))
        promotions_data.append((promotion_name, discount_percentage, start_date, end_date))
    return promotions_data

# Function to generate seed data for Sales
def generate_sales_data(num_records, num_products, num_customers, num_promotions):
    sales_data = []
    for _ in range(num_records):
        product_id = fake.random_int(min=1, max=num_products)
        customer_id = fake.random_int(min=1, max=num_customers)
        quantity = fake.random_int(min=1, max=10)
        amount = random_decimal(10, 200, 2)
        promotion_id = fake.random_int(min=1, max=num_promotions)
        date = random_date(datetime(2023, 1, 1), datetime(2023, 12, 31))
        sales_data.append((product_id, customer_id, quantity, amount, promotion_id, date))
    return sales_data

# Function to generate seed data for SalesTrend
def generate_sales_trend_data(num_records):
    sales_trend_data = []
    for _ in range(num_records):
        date = random_date(datetime(2023, 1, 1), datetime(2023, 12, 31))
        total_sales = random_decimal(1000, 5000, 2)
        total_quantity_sold = fake.random_int(min=100, max=1000)
        average_sale_amount = random_decimal(10, 200, 2)
        total_customers = fake.random_int(min=50, max=200)
        new_customers = fake.random_int(min=10, max=50)
        repeat_customers = total_customers - new_customers
        product_popularity = fake.word()
        category_popularity = fake.word()
        sales_growth_percentage = random_decimal(0, 50, 2)
        average_purchase_frequency = random_decimal(1, 10, 2)
        customer_retention_rate = random_decimal(50, 100, 2)
        seasonal_trends = fake.word()
        promotion_effectiveness = fake.word()

        sales_trend_data.append((
            date, total_sales, total_quantity_sold, average_sale_amount, total_customers, new_customers,
            repeat_customers, product_popularity, category_popularity, sales_growth_percentage,
            average_purchase_frequency, customer_retention_rate, seasonal_trends, promotion_effectiveness
        ))
    return sales_trend_data

# Define the number of records you want for each table
num_categories_records = 50
num_customers_records = 200
num_producers_records = 50
num_products_records = 100
num_promotions_records = 20
num_sales_records = 500
num_sales_trend_records = 365

# Generate seed data
categories_data = generate_categories_data(num_categories_records)
customers_data = generate_customers_data(num_customers_records)
producers_data = generate_producers_data(num_producers_records)
products_data = generate_products_data(num_products_records, num_categories_records, num_producers_records)
promotions_data = generate_promotions_data(num_promotions_records)
sales_data = generate_sales_data(num_sales_records, num_products_records, num_customers_records, num_promotions_records)
sales_trend_data = generate_sales_trend_data(num_sales_trend_records)

# Write data to CSV files
csv_file_mapping = {
    'Categories': categories_data,
    'Customers': customers_data,
    'Producers': producers_data,
    'Products': products_data,
    'Promotions': promotions_data,
    'Sales': sales_data,
    'SalesTrend': sales_trend_data,
}

for table_name, data in csv_file_mapping.items():
    csv_file_path = f'{table_name}.csv'
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)

    print(f'Data for table "{table_name}" written to {csv_file_path}')
