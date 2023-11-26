# import library yang dibutuhkan
import base64
import streamlit as st
from web_functions import load_data
from Tabs import beranda, broiler, visualise

# @st.cache_data
# def get_img_as_base64(file):
#     with open(file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# img = get_img_as_base64("gambar3.jpg")

# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] {{
# background-image: url("data:image/jpg;base64,{img}");
# background-size: 100%;
# background-repeat: no-repeat;
# }}

# [data-testid="stHeader"] {{
#     background:rgba(0,0,0,0);
# }}

# [data-testid="stToolbar"] {{
#     right:2rem;
# }}

# [data-testid="stSidebar"] {{
#     background-image: url("/img/chiken.jpg");
#     background-position: left;
# }}
# </style>
# """

# st.markdown(page_bg_img, unsafe_allow_html=True)

def load_custom_css():
    st.markdown('<style>{}</style>'.format(open('style.css').read()), unsafe_allow_html=True)

load_custom_css()

Tabs = {
    "Beranda" : beranda,
    "Broiler" : broiler,
    "Visualisation" : visualise
}

# membuat sidebar
st.sidebar.title("Navigasi")

# membuat radio option
page = st.sidebar.radio("Page", list(Tabs.keys()))

# load dataset
# df1, df2, x1, y1, x2, y2 = load_data()
df, x, y = load_data()

# kondisi call app function
if page in ["Broiler", "Visualisation"]:
    Tabs[page].app(df, x, y)
else:
    Tabs[page].app()

# kondisi call app function
# if page == "Prediction":
#     df1, x1, y1 = load_data()
#     predict.app(df1, df2, x1, y1, x2, y2)
# elif page == "Visualisation":
#     df2, x2, y2 = load_data()
#     visualise.app(df2, x2, y2)
# else:
#     Tabs[page].app()

# selected = option_menu(
#     menu_title=None,
#     options=["Home", "Prediction", "Visualisation"],
#     icons=["house", "book", "envelope"],
#     menu_icon="cast",
#     default_index=0,
#     orientation="horizontal",
# )

# if page == "Home":
#     home_app()
#     st.title(f"You have selected {selected}")
#     # home_path = os.path.join("Tabs", "home.py")
#     # exec(open(home_path).read())  # Menjalankan file home.py
# if page == "Prediction":
#     st.title(f"You have selected {selected}")
# if selected == "Visualisation":
#     st.title(f"You have selected {selected}")