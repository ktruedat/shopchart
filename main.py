import streamlit as st
import pandas as pd

from fetch_data import fetch_sale_trends_data

# Page layout
st.set_page_config(
        page_title="shopChart",
        page_icon="🛒",
        layout="wide"
)

# Header
st.title('Shop Marketing Insights')
st.subheader('Understand the effectiveness of your shop marketing')

df = fetch_sale_trends_data()

print(df)
# Page layout
st.title('Shop Marketing Insights')

# Sidebar menu
menu = st.sidebar.selectbox('Select a section', ['Overview', 'Total Sales', 'Total Quantity Sold', 'Average Sale Amount', 'Total Customers', 'New Customers',
                                                 'RepeatCustomers', 'ProductPopularity', 'CategoryPopularity', 'Sales Growth Percentage', 'Average Purchase Frequency',
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
