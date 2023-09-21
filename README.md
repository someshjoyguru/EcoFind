# EcoFind - Discover Eco-Friendly Products Web App

Welcome to EcoFind, your gateway to conscious consumerism! EcoFind is a web application that empowers users to discover, learn, and embrace eco-friendly living. With a curated selection of green, sustainable, and eco-friendly products, EcoFind makes it easy for users to shop with a clear conscience while making a positive impact on the planet.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation

To get started with EcoFind, follow these installation steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/someshjoyguru/EcoFind.git

2. Navigate to the project directory:

   ```bash
   cd ecofind

4. Create "trained_model" folder

5. Go to following 3 Google Colab notebooks:
   1. dataset1
   2. dataset2
   3. merged

6. Upload the datasets and eco_friendly_products.py python file given in Google Drive link[https://drive.google.com/open?id=1_GpwRRvMy_1OaaxXJTvljowe0f8gLU8o&usp=drive_copy] to respective Google Colab notebook.
   ###OR
   You can upload this[https://drive.google.com/drive/folders/1psgLlyUpobtDOYbfd4aT-B4WgGt6Auw6?usp=sharing] folder in the root directory of your Google Drive. Ensure that the folder name is EcoTech while you       save too.
   
8. Run the 3 Google Colab notebooks in following order:
   1. dataset1
   2. dataset2
   3. merged
   
   (Note: After performing dataset1 and dataset2, upload the products1 and products2 pickle files to the "merged" notebook and run it.)

9. Upload the "products" and "similarity" pickle file to the trained_model folder

10. Install dependencies:

   ```bash
   pip install -r requirements.txt

11. Run the application:

   ```bash
   streamlit run _Home.py
   ```

https://drive.google.com/file/d/1k0L-AkoTgH0A0bSZTTb_g9yWUKMvet6i/view?usp=sharing
## Usage

EcoFind is designed to provide users with a seamless experience in discovering eco-friendly products. Here's how to use it:

1. Launch the application as described in the installation steps.

2. Select a product category and enter the name of the product you're interested in.

3. Click the "Curate Personalised Product List" button to receive personalized product recommendations.

4. Explore the recommended products, including their ratings, descriptions, and direct purchase links.
