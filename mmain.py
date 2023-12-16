import streamlit as st
from PIL import Image
from st_clickable_images import clickable_images


# Main page
def main_page():
    st.markdown("<h1 style='text-align: center;'>Main Page</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        crud_image = Image.open("static/crud.png")
        st.button("", st.image(crud_image))
        # clicked = clickable_images(["/home/ktruedat/Projects/PycharmProjects/shopchart/static/crud.png"])
        # st.header("CRUD Functionality")
        # if clicked:
        #     crud_page()

    # with col2:
    #     st.header("Data Analytics")
    #     if st.button(st.image("static/analysis.png"), key="analytics_button", help="Data Analytics", on_click=analytics_page):
    #         st.experimental_rerun()


# CRUD page
def crud_page():
    st.title("CRUD Functionality")
    # Add CRUD functionality components here

# Analytics page
def analytics_page():
    st.title("Analytics Menu")
    # Add analytics menu components here

# App entry point
def main():
    st.sidebar.title("Navigation")
    pages = ["Main Page", "CRUD Functionality", "Analytics Menu"]
    page = st.sidebar.radio("Go to", pages)

    if page == "Main Page":
        main_page()
    elif page == "CRUD Functionality":
        crud_page()
    elif page == "Analytics Menu":
        analytics_page()

if __name__ == "__main__":
    main()
