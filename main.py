import streamlit as st

from menu import product_crud_menu, customer_crud_menu, producer_crud_menu, promotion_crud_menu, sale_crud_menu, analytics_menu

# Page Config
st.set_page_config(
    page_title="shopChart",
    page_icon="📑️",
    layout="wide"
)

st.title('Shop Marketing Insights')
st.subheader('Understand the effectiveness of your shop marketing')

###################
product_crud_menu()
customer_crud_menu()
producer_crud_menu()
promotion_crud_menu()
sale_crud_menu()
analytics_menu()
###################


# Footer
st.markdown('ktruedat shopChart')