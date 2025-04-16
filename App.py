import streamlit as st
import requests
from bs4 import BeautifulSoup

# Load password from Streamlit secrets
PASSWORD = st.secrets["password"]

# Simple password protection
def check_password():
    def password_entered():
        if st.session_state["password"] == PASSWORD:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Remove it from memory
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter Password:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter Password:", type="password", on_change=password_entered, key="password")
        st.error("Incorrect password.")
        return False
    else:
        return True

# App logic only runs if password is correct
if check_password():
    st.title("Kalos Price Finder")

    query = st.text_input("Search for a product")

    if query:
        st.write(f"Searching for **{query}**...")

        # Simple scraping logic (placeholder - you can upgrade it later)
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        urls = [
            f"https://www.ebay.com/sch/i.html?_nkw={query}",
            f"https://www.amazon.com/s?k={query.replace(' ', '+')}",
        ]

        for url in urls:
            try:
                res = requests.get(url, headers=headers)
                soup = BeautifulSoup(res.text, 'html.parser')
                st.write(f"Results from [{url}]({url}):")
                st.code(soup.title.string if soup.title else "No title found")
            except Exception as e:
                st.warning(f"Failed to scrape {url}: {e}")
