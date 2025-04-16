import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Kalos Price Finder", layout="centered")

# --- PASSWORD PROTECTION ---
PASSWORD = "kalos123"

def password_protect():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        pwd = st.text_input("Enter password:", type="password")
        if pwd == PASSWORD:
            st.session_state["authenticated"] = True
            st.success("Password correct!")
            st.experimental_rerun()
        else:
            if pwd:
                st.error("Incorrect password")
            st.stop()

password_protect()

# --- APP TITLE AND DESCRIPTION ---
st.title("Kalos Price Finder")
st.write("Welcome to Kalos Price Finder! Use the search box to find trending products, compare prices, and save your favorites.")

# --- SEARCH INTERFACE ---
query = st.text_input("Search for a product", "")

# --- MOCK DATA FOR DEMO ---
# In the future, this data will come from live web scraping.
data = [
    {"Product": "Wireless Earbuds", "Price": "$19.99", "Supplier": "AliExpress"},
    {"Product": "LED Strip Lights", "Price": "$12.49", "Supplier": "Amazon"},
    {"Product": "Portable Blender", "Price": "$24.95", "Supplier": "Temu"},
    {"Product": "Phone Tripod", "Price": "$9.99", "Supplier": "eBay"},
    {"Product": "Smart Watch", "Price": "$34.99", "Supplier": "AliExpress"},
]

df = pd.DataFrame(data)

# --- FILTER BASED ON SEARCH ---
if query:
    df = df[df["Product"].str.contains(query, case=False, na=False)]

st.subheader("Results")
st.dataframe(df)

# --- FAVORITE FEATURE ---
favorites = st.multiselect("Select products to favorite", options=df["Product"].tolist())
if favorites:
    st.success("Favorites: " + ", ".join(favorites))

st.write("This is a demo version of Kalos Price Finder. In the future, this app will scrape real trending products and compare prices.")
