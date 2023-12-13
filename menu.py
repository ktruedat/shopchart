from datetime import datetime

import pandas as pd
import streamlit as st

from api.controller.customer import CustomerController
from api.controller.producer import ProducerController
from api.controller.product import ProductController
from api.controller.promotion import PromotionController
from api.controller.sale import SaleController
from api.repository.customer import CustomerRepository
from api.repository.producer import ProducerRepository
from api.repository.product import ProductRepository
from api.repository.promotion import PromotionRepository
from api.repository.sale import SaleRepository
from api.repository.trend import TrendsRepository

# Product
product_repository = ProductRepository()
product_controller = ProductController(product_repository)

# Customer
customer_repository = CustomerRepository()
customer_controller = CustomerController(customer_repository)

# Producer
producer_repository = ProducerRepository()
producer_controller = ProducerController(producer_repository)

# Promotion
promotion_repository = PromotionRepository()
promotion_controller = PromotionController(promotion_repository)

# Sale
sale_repository = SaleRepository()
sale_controller = SaleController(sale_repository)

# Trends
trends_repository = TrendsRepository()


def product_crud_menu():
    crud_menu = st.sidebar.selectbox('Products',
                                     ['Product Overview', 'Add Product', 'Get All Products', 'Update Product',
                                      'Delete Product'])

    if crud_menu == 'Product Overview':
        print()

    elif crud_menu == 'Add Product':
        st.subheader('Add Product Section')

        product_name = st.text_input('Enter Product Name:')
        product_price = st.number_input('Enter Product Price:')

        categories = {1: 'Category 1', 2: 'Category 2', 3: 'Category 3'}
        selected_category_id = st.selectbox('Select Category:', list(categories.values()))
        producers = {1: 'Producer 1', 2: 'Producer 2', 3: 'Producer 3'}
        selected_producer_id = st.selectbox('Select Producer:', list(producers.values()))

        if st.button('Add Product'):
            product_data = {
                'Name': product_name,
                'CategoryID': selected_category_id,
                'Price': product_price,
                'ProducerID': selected_producer_id
            }
            print(product_data)
            product_id = product_controller.add_product(product_data)
            st.success(f"Product added successfully with ID: {product_id}")

    elif crud_menu == 'Update Product':
        st.subheader('Update Product Section')

        product_id = st.number_input('Enter Product ID to update:')
        updated_product_name = st.text_input('Enter Updated Product Name:')
        updated_product_price = st.number_input('Enter Updated Product Price:')

        categories = {1: 'Category 1', 2: 'Category 2', 3: 'Category 3'}
        selected_category_id = st.selectbox('Select Category:', list(categories.values()))
        producers = {1: 'Producer 1', 2: 'Producer 2', 3: 'Producer 3'}
        selected_producer_id = st.selectbox('Select Producer:', list(producers.values()))
        if st.button('Update Product'):
            product_data = {
                'Name': updated_product_name,
                'CategoryID': selected_category_id,
                'Price': updated_product_price,
                'ProducerID': selected_producer_id
            }
            print(product_data)
            result = product_controller.update_product(product_id, product_data)
            st.success(result)

    elif crud_menu == 'Delete Product':
        st.subheader('Delete Product Section')
        product_id_to_delete = st.number_input('Enter Product ID to delete:')
        if st.button('Delete Product'):
            result = product_controller.delete_product(product_id_to_delete)
            st.success(result)

    elif crud_menu == 'Get All Products':
        st.subheader('Get All Products Section')

        all_products = product_controller.get_all_products()
        print(all_products)
        if all_products:
            products_df = pd.DataFrame([vars(product) for product in all_products])
            st.table(products_df)
        else:
            st.info("No products found.")

    ###############################################################################


def customer_crud_menu():
    # CRUD Menu
    crud_menu_customer = st.sidebar.selectbox('Customers',
                                              ['Customer Overview', 'Add Customer', 'Get All Customers',
                                               'Update Customer',
                                               'Delete Customer'])

    if crud_menu_customer == 'Customer Overview':
        print()

    elif crud_menu_customer == 'Add Customer':
        st.subheader('Add Customer Section')

        customer_name = st.text_input('Enter Customer Name:')
        customer_email = st.text_input('Enter Customer Email:')
        customer_phone = st.number_input('Enter Customer Phone:')

        if st.button('Add Customer'):
            customer_data = {
                'Name': customer_name,
                'Email': customer_email,
                'Phone': customer_phone,
            }
            print(customer_data)
            customer_id = customer_controller.add_customer(customer_data)
            st.success(f"Product added successfully with ID: {customer_id}")

    elif crud_menu_customer == 'Update Customer':
        st.subheader('Update Customer Section')

        customer_id = st.number_input('Enter Customer ID to update:')
        updated_customer_name = st.text_input('Enter Updated Customer Name:')
        updated_customer_email = st.text_input('Enter Updated Customer Email:')
        updated_customer_phone = st.number_input('Enter Updated Customer Phone:')

        if st.button('Update Customer'):
            customer_data = {
                'Name': updated_customer_name,
                'Email': updated_customer_email,
                'Phone': updated_customer_phone,
            }
            print(customer_data)
            result = customer_controller.update_customer(customer_id, customer_data)
            st.success(result)

    elif crud_menu_customer == 'Delete Customer':
        st.subheader('Delete Customer Section')
        customer_id_to_delete = st.number_input('Enter Customer ID to delete:')
        if st.button('Delete Customer'):
            result = customer_controller.delete_customer(customer_id_to_delete)
            st.success(result)

    elif crud_menu_customer == 'Get All Customers':
        st.subheader('Get All Customers Section')

        all_customers = customer_controller.get_customers()
        print(all_customers)
        if all_customers:
            customer_df = pd.DataFrame([vars(customer) for customer in all_customers])
            st.table(customer_df)
        else:
            st.info("No customers found.")

    ###############################################################################


def producer_crud_menu():
    # CRUD Menu
    crud_menu_producer = st.sidebar.selectbox('Producers',
                                              ['Producer Overview', 'Add Producer', 'Get All Producers',
                                               'Update Producer',
                                               'Delete Producer'])

    if crud_menu_producer == 'Producer Overview':
        print()

    elif crud_menu_producer == 'Add Producer':
        st.subheader('Add Producer Section')

        producer_name = st.text_input('Enter Producer Name:')
        producer_location = st.text_input('Enter Producer Location:')

        if st.button('Add Producer'):
            producer_data = {
                'Name': producer_name,
                'Location': producer_location,
            }
            print(producer_data)
            producer_id = producer_controller.producer_repository.add_producer(producer_data)
            st.success(f"Producer added successfully with ID: {producer_id}")

    elif crud_menu_producer == 'Update Producer':
        st.subheader('Update Producer Section')

        producer_id = st.number_input('Enter Producer ID to update:')
        producer_name = st.text_input('Enter Producer Name to update:')
        producer_location = st.text_input('Enter Producer Location to update:')

        if st.button('Update Producer'):
            producer_data = {
                'Name': producer_name,
                'Location': producer_location,
            }
            print(producer_data)
            result = producer_controller.update_producer(producer_id, producer_data)
            st.success(result)

    elif crud_menu_producer == 'Delete Producer':
        st.subheader('Delete Producer Section')
        producer_id_to_delete = st.number_input('Enter Producer ID to delete:')
        if st.button('Delete Producer'):
            result = producer_controller.delete_producer(producer_id_to_delete)
            st.success(result)

    elif crud_menu_producer == 'Get All Producers':
        st.subheader('Get All Producers Section')

        all_producers = producer_controller.get_producers()
        print(all_producers)
        if all_producers:
            producer_df = pd.DataFrame([vars(producer) for producer in all_producers])
            st.table(producer_df)
        else:
            st.info("No producers found.")

    ###############################################################################


def promotion_crud_menu():
    crud_menu_promotion = st.sidebar.selectbox('Promotions',
                                               ['Promotion Overview', 'Add Promotion', 'Get All Promotions',
                                                'Update Promotion',
                                                'Delete Promotion'])

    if crud_menu_promotion == 'Promotion Overview':
        print()

    elif crud_menu_promotion == 'Add Promotion':
        st.subheader('Add Promotion Section')

        promotion_name = st.text_input('Enter Promotion Name:')
        promotion_discount_percentage = st.number_input('Enter Promotion Discount Percentage:')
        promotion_start_date = st.date_input('Enter Promotion Start Date:')
        promotion_end_date = st.date_input('Enter Promotion End Date:')

        if st.button('Add Promotion'):
            promotion_data = {
                'Name': promotion_name,
                'DiscountPercentage': promotion_discount_percentage,
                'StartDate': promotion_start_date,
                'EndDate': promotion_end_date,
            }
            print(promotion_data)
            promotion_id = promotion_controller.add_promotion(promotion_data)
            st.success(f"Promotion added successfully: {promotion_id}")

    elif crud_menu_promotion == 'Update Promotion':
        st.subheader('Update Promotion Section')

        promotion_id = st.number_input('Enter Promotion ID to update:')
        promotion_name = st.text_input('Enter Promotion Name to update:')
        promotion_discount_percentage = st.number_input('Enter Promotion Discount Percentage to update:')
        promotion_start_date = st.date_input('Enter Promotion Start Date to update:')
        promotion_end_date = st.date_input('Enter Promotion End Date to update:')

        if st.button('Update Promotion'):
            promotion_data = {
                'Name': promotion_name,
                'DiscountPercentage': promotion_discount_percentage,
                'StartDate': promotion_start_date,
                'EndDate': promotion_end_date,
            }
            print(promotion_data)
            result = promotion_controller.update_promotion(promotion_id, promotion_data)
            st.success(result)

    elif crud_menu_promotion == 'Delete Promotion':
        st.subheader('Delete Promotion Section')
        promotion_id_to_delete = st.number_input('Enter Promotion ID to delete:')
        if st.button('Delete Promotion'):
            result = promotion_controller.delete_promotion(promotion_id_to_delete)
            st.success(result)

    elif crud_menu_promotion == 'Get All Promotion':
        st.subheader('Get All Promotions Section')

        all_promotions = promotion_controller.get_promotions()
        print(all_promotions)
        if all_promotions:
            promotion_df = pd.DataFrame([vars(promotion) for promotion in all_promotions])
            st.table(promotion_df)
        else:
            st.info("No promotions found.")

    ###############################################################################


def sale_crud_menu():
    crud_menu_sale = st.sidebar.selectbox('Sales',
                                          ['Sale Overview', 'Add Sale', 'Get All Sales', 'Update Sale',
                                           'Delete Sale'])

    if crud_menu_sale == 'Sale Overview':
        print()

    if crud_menu_sale == 'Add Sale':
        st.subheader('Add Sale Section')

        sale_product_id = st.number_input('Enter Product ID:')
        sale_customer_id = st.number_input('Enter Customer ID:')
        sale_quantity = st.number_input('Enter Sale Product Quantity:')
        sale_amount = st.number_input('Enter Sale Amount:')
        sale_promotion_id = st.number_input('Enter Promotion ID if exists:')
        sale_date = st.date_input('Enter Sale Date:')

        if st.button('Add Sale'):
            sale_data = {
                'ProductID': sale_product_id,
                'CustomerID': sale_customer_id,
                'Quantity': sale_quantity,
                'Amount': sale_amount,
                'PromotionID': sale_promotion_id,
                'Date': sale_date,
            }
            print(sale_data)
            sale_id = sale_controller.add_sale(sale_data)
            st.success(f"Sale added successfully: {sale_id}")

    elif crud_menu_sale == 'Update Sale':
        st.subheader('Update Sale Section')

        sale_id = st.number_input('Enter Sale ID to update')
        sale_product_id = st.number_input('Enter Product ID to update:')
        sale_customer_id = st.number_input('Enter Customer ID to update:')
        sale_quantity = st.number_input('Enter Sale Product Quantity to update:')
        sale_amount = st.number_input('Enter Sale Amount to update :')
        sale_promotion_id = st.number_input('Enter Promotion ID to update if exists:')
        sale_date = st.date_input('Enter Sale Date to update:')

        if st.button('Update Sale'):
            sale_data = {
                'ProductID': sale_product_id,
                'CustomerID': sale_customer_id,
                'Quantity': sale_quantity,
                'Amount': sale_amount,
                'PromotionID': sale_promotion_id,
                'Date': sale_date,
            }
            print(sale_data)
            result = sale_controller.update_sale(sale_id, sale_data)
            st.success(result)

    elif crud_menu_sale == 'Delete Sale':
        st.subheader('Delete Sale Section')
        sale_id_to_delete = st.number_input('Enter Sale ID to delete:')
        if st.button('Delete Sale'):
            result = sale_controller.delete_sale(sale_id_to_delete)
            st.success(result)

    elif crud_menu_sale == 'Get All Sales':
        st.subheader('Get All Sales Section')

        all_sales = sale_controller.get_sales()
        print(all_sales)
        if all_sales:
            sales_df = pd.DataFrame([vars(sale) for sale in all_sales])
            st.table(sales_df)
        else:
            st.info("No sales found.")

    ###############################################################################


def analytics_menu():
    menu = st.sidebar.selectbox('Analytics',
                                ['Overview', 'Total Sales', 'Total Quantity Sold',
                                 # 'Average Sale Amount',
                                 'Total Customers',
                                 'New Customers',
                                 'Repeat Customers', 'Product Popularity', 'Category Popularity',
                                 'Sales Growth Percentage',
                                 'Average Purchase Frequency',
                                 'Customer Retention Rate', 'Seasonal Trends', 'Promotion Effectiveness'])

    start_date = st.date_input('Select Start Date', datetime.today())
    end_date = st.date_input('Select End Date', datetime.today())

    if menu == 'Overview':
        # st.subheader('Overview Section')
        print()

    elif menu == 'Total Sales':
        st.subheader('Total Sales Section')
        total_sales_data = trends_repository.get_total_sales(start_date, end_date)

        if total_sales_data:
            total_sales_df = pd.DataFrame(total_sales_data, columns=['Date', 'TotalSales'])
            total_sales_df.set_index('Date', inplace=True)
            st.line_chart(total_sales_df['TotalSales'])
        else:
            st.info("No sales data found.")

    elif menu == 'Total Quantity Sold':
        st.subheader('Total Quantity Sold Section')
        total_quantity_sold_data = trends_repository.get_total_quantity_sold(start_date, end_date)
        # print(f"HERE{total_quantity_sold_data}")

        if total_quantity_sold_data:
            total_quantity_sold_df = pd.DataFrame(total_quantity_sold_data, columns=['Date', 'TotalQuantitySold'])

            total_quantity_sold_df['TotalQuantitySold'] = total_quantity_sold_df['TotalQuantitySold'].astype(float)

            total_quantity_sold_df.set_index('Date', inplace=True)
            st.line_chart(total_quantity_sold_df['TotalQuantitySold'])
        else:
            st.info("No quantity sold data found.")

    # elif menu == 'Average Sale Amount':
    #     st.subheader('Average Sale Amount Section')
    #     st.line_chart(df.set_index('Date')['AverageSaleAmount'])

    elif menu == 'Total Customers':
        st.subheader('Total Customers Section')
        total_customers_data = trends_repository.get_total_customers(start_date, end_date)

        if total_customers_data:
            total_customers_df = pd.DataFrame(total_customers_data, columns=['Date', 'TotalCustomers'])
            total_customers_df.set_index('Date', inplace=True)
            st.line_chart(total_customers_df['TotalCustomers'])
        else:
            st.info("No customer data found.")

    elif menu == 'New Customers':
        st.subheader('New Customers Section')
        new_customers_data = trends_repository.get_total_new_customers(start_date, end_date)

        if new_customers_data:
            new_customers_df = pd.DataFrame(new_customers_data, columns=['Date', 'TotalNewCustomers'])
            new_customers_df.set_index('Date', inplace=True)
            st.line_chart(new_customers_df['TotalNewCustomers'])
        else:
            st.info("No new customer data found.")

    elif menu == 'Repeat Customers':
        st.subheader('Repeat Customers Section')
        repeat_customers_data = trends_repository.get_total_repeat_customers(start_date, end_date)
        print(f"repeat_customers_data{repeat_customers_data}")

        if repeat_customers_data:
            repeat_customers_df = pd.DataFrame(repeat_customers_data, columns=['Date', 'TotalRepeatCustomers'])
            repeat_customers_df.set_index('Date', inplace=True)
            st.line_chart(repeat_customers_df['TotalRepeatCustomers'])
        else:
            st.info("No repeat customer data found.")

    elif menu == 'Product Popularity':
        st.subheader('Product Popularity Section')
        product_popularity_data = trends_repository.get_product_popularity(start_date, end_date)
        print(f"product_popularity_data{product_popularity_data}")

        if product_popularity_data:
            product_popularity_df = pd.DataFrame(product_popularity_data,
                                                 columns=['Date', 'ProductName', 'TotalQuantitySold'])
            product_popularity_df['TotalQuantitySold'] = pd.to_numeric(product_popularity_df['TotalQuantitySold'])
            product_popularity_df.set_index('Date', inplace=True)
            st.bar_chart(product_popularity_df, x='ProductName', y='TotalQuantitySold', use_container_width=True)
        else:
            st.info("No product popularity data found.")

    elif menu == 'Category Popularity':
        st.subheader('Category Popularity Section')
        category_popularity_data = trends_repository.get_category_popularity(start_date, end_date)
        print(f"category_popularity_data{category_popularity_data}")

        if category_popularity_data:
            category_popularity_df = pd.DataFrame(category_popularity_data,
                                                  columns=['Date', 'CategoryName', 'TotalQuantitySold'])
            category_popularity_df['TotalQuantitySold'] = pd.to_numeric(category_popularity_df['TotalQuantitySold'])
            category_popularity_df.set_index('Date', inplace=True)

            st.bar_chart(category_popularity_df, x='CategoryName', y='TotalQuantitySold', use_container_width=True)
        else:
            st.info("No category popularity data found.")

    elif menu == 'Sales Growth Percentage':
        st.subheader('Sales Growth Section')
        sales_growth_percentage_data = trends_repository.get_sales_growth_percentage(start_date, end_date)
        print(f"sales_growth_percentage_data{sales_growth_percentage_data}")

        if sales_growth_percentage_data:
            sales_growth_percentage_df = pd.DataFrame(sales_growth_percentage_data,
                                                      columns=['Date', 'SalesGrowthPercentage'])
            sales_growth_percentage_df.set_index('Date', inplace=True)
            st.line_chart(sales_growth_percentage_df['SalesGrowthPercentage'])
        else:
            st.info("No sales growth percentage data found.")

    elif menu == 'Average Purchase Frequency':
        st.subheader('Average Purchase Frequency Section')
        average_purchase_frequency_data = trends_repository.get_average_purchase_frequency(start_date, end_date)
        print(f"average_purchase_frequency_data{average_purchase_frequency_data}")

        if average_purchase_frequency_data:
            # Assuming average_purchase_frequency_data is a dictionary with keys 'Date' and 'AveragePurchaseFrequency'
            st.write(f"Average Purchase Frequency on {average_purchase_frequency_data['Date']} is {average_purchase_frequency_data['AveragePurchaseFrequency']}")
        else:
            st.info("No average purchase frequency data found.")

    elif menu == 'Customer Retention Rate':
        st.subheader('Customer Retention Rate Section')
        customer_retention_rate_data = trends_repository.get_customer_retention_rate(start_date, end_date)
        print(f"customer_retention_rate_data{customer_retention_rate_data}")

        if customer_retention_rate_data:
            customer_retention_rate_df = pd.DataFrame(customer_retention_rate_data,
                                                      columns=['Date', 'CustomerRetentionRate'])
            customer_retention_rate_df.set_index('Date', inplace=True)
            st.line_chart(customer_retention_rate_df['CustomerRetentionRate'])
        else:
            st.info("No customer retention rate data found.")

    elif menu == 'Seasonal Trends':
        st.subheader('Seasonal Trends Section')
        seasonal_trends_data = trends_repository.get_seasonal_trends(start_date, end_date)
        print(f"seasonal_trends_data{seasonal_trends_data}")

        if seasonal_trends_data:
            seasonal_trends_df = pd.DataFrame(seasonal_trends_data, columns=['Month', 'TotalSales'])
            seasonal_trends_df['Date'] = pd.to_datetime(seasonal_trends_df['Month'], format='%m').dt.strftime('%B')
            seasonal_trends_df.set_index('Date', inplace=True)
            st.line_chart(seasonal_trends_df['TotalSales'])
        else:
            st.info("No seasonal trends data found.")

    elif menu == 'Promotion Effectiveness':
        st.subheader('Promotion Effectiveness Section')
        promotion_id = st.number_input('Enter Promotion ID:')
        promotion_effectiveness_data = trends_repository.get_promotion_effectiveness(promotion_id)
        print(f"promotion_effectiveness_data{promotion_effectiveness_data}")

        if promotion_effectiveness_data is not None:
            st.success(f"The effectiveness of Promotion {promotion_id} is ${promotion_effectiveness_data:.2f}")
        else:
            st.info("No promotion effectiveness data found.")


##################################################################################
