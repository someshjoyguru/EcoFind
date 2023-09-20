import streamlit as st

# Configure Streamlit page settings and theme toggle button
st.set_page_config(
    page_title="EcoFind - Discover Eco-Friendly Products",
    page_icon="🌿",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    theme = st.config.get_option("theme.base")

    # Create a button to switch themes
    if theme == "light":
        switch = st.button("🌞")
    else:
        switch = st.button("🌙")

    # Check the button value and toggle the theme
    if switch:
        theme = st.config.get_option("theme.base")
        if theme == "light":
            st.config.set_option("theme.base", "dark")
        else:
            st.config.set_option("theme.base", "light")

        # Reload the page to apply the theme change
        st.experimental_rerun()

# Title and header
st.title("Coming Soon...")

# Define the headings and bullet points
features = [
    (
        "Sustainable Ratings and Reviews:",
        [
            "User-Generated Ratings",
            "Environmental Impact Ratings",
            "User Reviews",
            "Product Insights",
        ],
    ),
    (
        "Product Comparisons:",
        [
            "Side-by-Side Product Comparison",
            "Price Comparison",
            "Environmental Impact Comparison",
            "Feature Comparison",
        ],
    ),
    (
        "Local and Ethical Sourcing:",
        [
            "Highlight Local and Ethically Sourced Products",
            "Fair Trade and Local Community Support",
        ],
    ),
    (
        "Carbon Footprint Calculator:",
        [
            "Calculate Carbon Footprint of Purchases",
            "Provide Eco-Friendly Alternatives",
            "Environmental Impact Tracking",
        ],
    ),
    (
        "User Forums and Community:",
        [
            "Discussion Forums",
            "Sustainable Living Tips Exchange",
            "Like-Minded Community",
        ],
    ),
    (
        "Green Deals and Discounts:",
        [
            "Exclusive Eco-Friendly Product Deals",
            "Discounts on Sustainable Choices",
            "Promote Affordable Eco-Friendly Shopping",
        ],
    ),
    (
        "Interactive Sustainability Challenges:",
        [
            "Monthly/Quarterly Challenges",
            "Encourage Sustainable Actions",
            "Rewards and Recognition",
        ],
    ),
    (
        "Eco-Friendly Brands Directory:",
        [
            "Curated List of Eco-Conscious Brands",
            "Brand Values and Certifications",
            "Support Ethical Businesses",
        ],
    ),
    (
        "Product Certification Information:",
        [
            "Detailed Information on Eco-Certifications",
            "Educate Users on Product Standards",
        ],
    ),
    (
        "Green Events Calendar:",
        [
            "Upcoming Environmental Events",
            "Workshops and Sustainability Activities",
            "Stay Informed and Engaged",
        ],
    ),
    (
        "Personalized Sustainability Reports:",
        [
            "User-Specific Reports",
            "Tracking Sustainable Shopping Habits",
            "Suggest Areas for Improvement",
        ],
    ),
    (
        "Mobile App:",
        [
            "On-the-Go Access",
            "Product Scanning for Eco-Friendliness",
            "Eco-Tips and Shopping Assistance",
        ],
    ),
]

# Display the headings and bullet points
st.title(":rainbow[EcoFind's Upcoming Features]")
for heading, points in features:
    st.markdown(f"### :blue[{heading}]")
    for point in points:
        st.markdown(f"- :s[{point}]")
