import streamlit as st
import app.langchain_helper as langchain_helper

st.title("🍽️ Restaurant Name Generator")

# Sidebar input
cuisine = st.sidebar.selectbox(
    "Pick a Cuisine", 
    ("Indian", "Italian", "Mexican", "Arabic", "American")
)

# Run generation
if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    # Display results
    st.header(response["restaurant_name"])
    st.subheader("Menu Items:")
    for item in response["menu_items"]:
        st.write(f"- {item}")