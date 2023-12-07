import pandas as pd
import streamlit as st

from api.controller.customer import CustomerController
from api.controller.product import ProductController
from api.repository.customer import CustomerRepository
from api.repository.product import ProductRepository


# Dependencies init
# Product
product_repository = ProductRepository()
product_controller = ProductController(product_repository)

# Customer
customer_repository = CustomerRepository()
customer_controller = CustomerController(customer_repository)

###############################################################

# Page Config
st.set_page_config(
    page_title="shopChart",
    page_icon="📑️",
    layout="wide"
)

st.title('Shop Marketing Insights')
st.subheader('Understand the effectiveness of your shop marketing')
st.title('Shop Marketing Insights')

################################################################

df = None

print(df)


# CRUD Menu
crud_menu = st.sidebar.selectbox('Select a section', ['Add Product', 'Get All Products', 'Update Product', 'Delete Product'])

if crud_menu == 'Add Product':
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


# Sidebar menu
menu = st.sidebar.selectbox('Select a section',
                            ['Overview', 'Total Sales', 'Total Quantity Sold', 'Average Sale Amount', 'Total Customers',
                             'New Customers',
                             'RepeatCustomers', 'ProductPopularity', 'CategoryPopularity', 'Sales Growth Percentage',
                             'Average Purchase Frequency',
                             'Customer Retention Rate', 'Seasonal Trends', 'Promotion Effectiveness'])

# Sections
if menu == 'Overview':
    st.subheader('Overview Section')
    # Display overall insights, summary charts, etc.

elif menu == 'Total Sales':
    st.subheader('Total Sales Section')
    st.line_chart(df.set_index('Date')['TotalSales'])

elif menu == 'Total Quantity Sold':
    st.subheader('Total Quantity Sold Section')
    st.line_chart(df.set_index('Date')['TotalQuantitySold'])

elif menu == 'Average Sale Amount':
    st.subheader('Average Sale Amount Section')
    st.line_chart(df.set_index('Date')['AverageSaleAmount'])

elif menu == 'Total Customers':
    st.subheader('Total Customers Section')
    st.line_chart(df.set_index('Date')['TotalCustomers'])

elif menu == 'New Customers':
    st.subheader('New Customers Section')
    st.line_chart(df.set_index('Date')['NewCustomers'])

elif menu == 'Repeat Customers':
    st.subheader('Repeat Customers Section')
    st.line_chart(df.set_index('Date')['RepeatCustomers'])

elif menu == 'Product Popularity':
    st.subheader('Product Popularity Section')
    st.line_chart(df.set_index('Date')['ProductPopularity'])

elif menu == 'Category Popularity':
    st.subheader('Category Popularity Section')
    st.line_chart(df.set_index('Date')['CategoryPopularity'])

elif menu == 'Sales Growth Percentage':
    st.subheader('Sales Growth Section')
    st.line_chart(df.set_index('Date')['SalesGrowthPercentage'])

elif menu == 'Average Purchase Frequency':
    st.subheader('Average Purchase Frequency Section')
    st.line_chart(df.set_index('Date')['AveragePurchaseFrequency'])

elif menu == 'Customer Retention Rate':
    st.subheader('Customer Retention Rate Section')
    st.line_chart(df.set_index('Date')['CustomerRetentionRate'])

elif menu == 'Seasonal Trends':
    st.subheader('Seasonal Trends Section')
    st.line_chart(df.set_index('Date')['SeasonalTrends'])

elif menu == 'Promotion Effectiveness':
    st.subheader('Promotion Effectiveness Section')
    st.line_chart(df.set_index('Date')['PromotionEffectiveness'])

# Footer
st.markdown('ktruedat shopChart')

# Custom styling
st.markdown(
    """
        <style>
            .css-17xpkmf {
                background-color: #f0f0f0;
            }
            .css-1aumxhk {
                background-color: #ffffff;
                border: 1px solid #d1d1d1;
                border-radius: 5px;
            }
            .css-17xpkmf, .css-1aumxhk {
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .css-vunfms {
                background-color: #e0e0e0;
            }
        </style>
        """,
    unsafe_allow_html=True
)
