# Import necessary libraries
import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

# Load product data and similarity matrix from pickle files
product_list = pickle.load(open("products.pkl", "rb"))
products = pd.DataFrame(product_list)
similarity = pickle.load(open("similarity.pkl", "rb"))

recommended_products = []


# Function to recommend similar products based on user input
def recommend(product):
    # Find the index of the selected product in the products DataFrame
    product_index = products[products["name"] == product].index[0]
    
    # Get the category (Classification) of the input product
    category = products.loc[product_index, "Classification"]
    
    # Get the similarity scores between the selected product and all other products
    distances = similarity[product_index]
    
    # Initialize an empty list to store the recommended products
    # recommended_products = []
    
    # Loop through all products and check if they belong to the same category
    for i, dist in enumerate(distances):
        # Skip the current product (the one we're comparing to itself)
        if i == product_index:
            continue
        
        # Check if the product belongs to the same category as the input product
        if products.loc[i, "Classification"] == category:
            product_details = [
                products.loc[i, "name"],
                products.loc[i, "url"],
                products.loc[i, "Classification"],
                products.loc[i, "ratings"],
                products.loc[i, "no_of_ratings"],
                products.loc[i, "image"],
            ]
            
            # Append the product details to the recommended_products list
            recommended_products.append(product_details)
            
            # Break the loop when we have found 5 similar items from the same category
            if len(recommended_products) == 5:
                break
    
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
st.caption("Please be patient while we curate your personalized product list.")
st.caption("This may take a moment or two.⏳⌛")


# Button to initiate the product curation process
if st.button("Curate Personalised Product List"):
    message = st.text("Running the operation...")
    recommendations = recommend(selected_product)

    # Display recommended products with details and images
    for i in recommendations:
        original_image_url = str(i[5])

        # Display product information and image in two columns
        colx1, colx2 = st.columns(spec=[5, 3])
        colx1.subheader(i[0], divider="rainbow")
        col12, col22 = colx1.columns(2)
        col12.caption("Category: " + i[2])

        # Check if ratings are available and display them
        if i[3] == "No ratings available":
            col12.caption("Ratings: " + str(i[3]))
        else:
            num = float("".join(str(i[3]).split()))
            col12.caption("Ratings: " + str(i[3]) + stars_in_ratings(num))

        col22.caption("[Go to Website](" + i[1] + ")")
        col12.caption("No. of ratings: " + str(i[4]))

        # Check if the image URL is available
        if is_image_url(original_image_url):
            # Display the image
            colx2.image(original_image_url, width=200)
        else:
            # Fetch an image from the Pexels API
            url = "https://api.pexels.com/v1/search"
            query = i[0]
            per_page = 1
            headers = {
                "Authorization": st.secrets["Authorization_token"]
            }
            params = {"query": query, "per_page": per_page}
            response = requests.get(url, headers=headers, params=params)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                data = response.json()
                original_image_url = data["photos"][0]["src"]["original"]
                colx2.caption("Image retrieved from Pexels API")
                colx2.caption("Please note that this image may not be related to the product")
                colx2.image(original_image_url, width=200)
            else:
                colx2.write("Image not available")
            
