# Import necessary libraries
import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

# Load product data and similarity matrix from pickle files
product_list = pickle.load(open("../trained_model/products.pkl", "rb"))
products = pd.DataFrame(product_list)
similarity = pickle.load(open("../trained_model/similarity.pkl", "rb"))

recommended_products = []


# Function to recommend similar products based on user input
def recommend(product):
    product_index = products[products["name"] == product].index[0]
    distances = similarity[product_index]
    product_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        :5
    ]
    for i in product_list:
        product = [
            products.get("name")[i[0]],
            products.get("url")[i[0]],
            products.get("Classification")[i[0]],
            products.get("ratings")[i[0]],
            products.get("no_of_ratings")[i[0]],
            products.get("image")[i[0]],
        ]
        recommended_products.append(product)
    return recommended_products


# Function to check if an image URL is valid
def is_image_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        return True
    except Exception as e:
        return False


# Function to display star ratings based on a numeric rating
def stars_in_ratings(rating):
    full_stars = "⭐" * int(rating)
    if rating == int(rating):
        return full_stars
    half_star = "⭐" if rating % 1 >= 0.5 else "🌗"
    return full_stars + half_star


# Configure Streamlit page settings and theme toggle button
st.set_page_config(
    page_title="EcoFind - Discover Eco-Friendly Products",
    page_icon="🌿",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    theme = st.config.get_option("theme.base")

    # Create a button to switch themes (light/dark)
    if theme == "light":
        switch = st.button("🌞")
    else:
        switch = st.button("🌙")

    # Check the button value and toggle the theme, then reload the page to apply the change
    if switch:
        theme = st.config.get_option("theme.base")
        if theme == "light":
            st.config.set_option("theme.base", "dark")
        else:
            st.config.set_option("theme.base", "light")
        st.experimental_rerun()

# Set the main title and header for the Streamlit app
st.title(
    ":rainbow[EcoFind]: 🔍Search :green[Green], :blue[Sustainable], and :orange[Eco-Friendly] :violet[Products]"
)
st.header("Your Gateway to _Conscious Consumerism_ 😊😀")

# Allow the user to select a product from the dropdown
selected_product = st.selectbox(
    "Enter product name and category", products["name"].values
)
st.text("Please wait for some time while we curate your personalized product list!⏳⌛")

# Button to initiate the product curation process
if st.button("Curate Personalised Product List"):
    message = st.text("Running the operation...")
    recommendations = recommend(selected_product)

    # Display recommended products with details and images
    for i in recommendations:
        if i[5] == "0":
            # Use the Pexels API to fetch an image if the image URL is not available
            url = "https://api.pexels.com/v1/search"
            query = i[0]
            per_page = 1
            headers = {
                "Authorization": "tN5RuIJaOdUZYQBBhCybr0ZziUE0zZ95N8u5mNyKPpnDJsB1ek3MUO22"
            }
            params = {"query": query, "per_page": per_page}
            response = requests.get(url, headers=headers, params=params)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                global data
                data = response.json()
            else:
                print(f"Error shown through terminal: {response.status_code}")
            original_image_url = data["photos"][0]["src"]["original"]
        else:
            original_image_url = str(i[5])

        # Display product information and image in two columns
        colx1, colx2 = st.columns(spec=[5, 3])
        colx1.subheader(i[0], divider="rainbow")
        col12, col22 = colx1.columns(2)
        col12.caption("Category: " + i[2])
        if i[3] == "No ratings available":
            col12.caption("Ratings: " + str(i[3]))
        else:
            num = float("".join(str(i[3]).split()))
            col12.caption("Ratings: " + str(i[3]) + stars_in_ratings(num))
        col22.caption("[Go to Website](" + i[1] + ")")
        col12.caption("No. of ratings: " + str(i[4]))
        if is_image_url(original_image_url):
            # Display the image
            colx2.image(original_image_url, width=200)
        else:
            # Display "Image not available" message
            colx2.write("Image not available")
