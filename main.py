import streamlit as st
from streamlit_option_menu import option_menu

from menu import product_crud_menu, customer_crud_menu, producer_crud_menu, promotion_crud_menu, sale_crud_menu, \
    analytics_menu

# Main page

# Page Config
st.set_page_config(
    page_title="shopChart",
    page_icon="static/statistics.png",
    layout="wide"
)

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Home", "Edit Data", "Analytics"],
    icons=["house", "database", "bar-chart-fill"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)


def main_page():
    with st.container(border=True):
        st.markdown("<h1 style='text-align: center;'>shopChart</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Understand the effectiveness of your shop marketing</h2>",
                    unsafe_allow_html=True)
        style = "<style>h2 {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)
        st.columns(3)[1].image("static/statistics.png")


def crud_page():
    st.title("CRUD Functionality")
    st.write(
        "Welcome to the CRUD Functionality page. This page allows you to perform Create, Read, Update, and Delete ("
        "CRUD) operations on various entities. Explore the following features:")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col5:
        st.subheader("Product CRUD:")
        st.write("- Add, edit, and delete products in your inventory.")
        st.write("- View detailed information about each product.")
        st.image("static/product.png")
    # Customer CRUD Card
    with col1:
        st.subheader("Customer CRUD:")
        st.write("- Manage customer data, including adding new customers and updating their details.")
        st.write("- Keep track of customer interactions and purchases.")
        st.image("static/customer.png")

    # Producer CRUD Card
    with col2:
        st.subheader("Producer CRUD:")
        st.write("- Maintain a list of producers and their information.")
        st.write("- Easily update and delete producer details.")
        st.image("static/producer.png")

    # Promotion CRUD Card
    with col3:
        st.subheader("Promotion CRUD:")
        st.write("- Create and manage promotional offers.")
        st.write("- Track the performance of promotions over time.")
        st.image("static/promotion.png")

    # Sale CRUD Card
    with col4:
        st.subheader("Sale CRUD:")
        st.write("- Record and manage sales transactions.")
        st.write("- Monitor sales performance and generate reports.")
        st.image("static/sale.png")

    product_crud_menu()
    customer_crud_menu()
    producer_crud_menu()
    promotion_crud_menu()
    sale_crud_menu()


# Analytics page
def analytics_page():
    st.title("Analytics Menu")
    st.write("Explore insightful analytics on this page. Gain valuable insights and visualize data to make informed "
             "decisions. Key features include:")

    col1, col2 = st.columns(2)

    # Data Visualization Card
    with col1:
        st.subheader("Data Visualization:")
        st.write("- Utilize interactive charts and graphs to visualize trends.")
        st.write("- Compare data points to identify patterns and outliers.")

    # Statistical Analysis Card
    with col2:
        st.subheader("Statistical Analysis:")
        st.write("- Perform statistical analyses on your data.")
        st.write("- Uncover correlations and dependencies within your dataset.")

    analytics_menu()


if selected == "Home":
    main_page()
elif selected == "Edit Data":
    crud_page()
elif selected == "Analytics":
    analytics_page()
