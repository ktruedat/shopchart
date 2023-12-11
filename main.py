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
