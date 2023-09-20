import streamlit as st

# Set page configuration with a title, icon, and expanded sidebar
st.set_page_config(
    page_title="EcoFind - Discover Eco-Friendly Products",
    page_icon="🌿",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    # Get the current theme and create a button to switch themes
    theme = st.config.get_option("theme.base")
    if theme == "light":
        switch = st.button("🌞")  # Light mode button
    else:
        switch = st.button("🌙")  # Dark mode button

    # Check the button value and toggle the theme, then reload the page to apply the change
    if switch:
        theme = st.config.get_option("theme.base")
        if theme == "light":
            st.config.set_option("theme.base", "dark")
        else:
            st.config.set_option("theme.base", "light")
        st.experimental_rerun()

# Main content
st.title(
    ":rainbow[EcoFind]: Discover :green[Green], :blue[Sustainable], and :orange[Eco-Friendly] :violet[Gems]"
)
st.header("Your Gateway to _Conscious Consumerism_")

st.markdown(
    """
    Welcome to EcoFind, where sustainability meets convenience. We believe that making eco-conscious choices 
    should be effortless and enjoyable. With our curated selection of green, sustainable, and eco-friendly 
    products, you can shop with a clear conscience while making a positive impact on the planet.
    """
)

# Display images and additional content

st.image("./images/1.webp")

st.subheader("Why EcoFind?")
st.markdown(
    """
    At EcoFind, we've harnessed the power of machine learning to bring you the best in environmentally friendly 
    products. Our algorithm tirelessly searches the web to handpick three exceptional products daily. Each 
    product not only meets our stringent eco-friendly criteria but also comes with detailed information, 
    a direct link to the retailer, and a captivating image.
    """
)

st.image("./images/2.png")

st.subheader("Discover the Future of Shopping:")
st.write(
    "🌿 **Green Choices:** Explore products that leave a minimal carbon footprint and promote a healthier planet."
)
st.write(
    "🌱 **Sustainable Living:** Embrace a sustainable lifestyle with products designed to last and reduce waste."
)
st.write(
    "♻️ **Eco-Friendly Delights:** Find joy in guilt-free shopping, knowing your choices support ethical and eco-conscious brands."
)

st.subheader("Join the EcoRevolution:")
st.markdown(
    """
    By choosing EcoFind, you're not just shopping; you're taking a stand for the environment. Every purchase you make 
    through our platform supports businesses that prioritize sustainability and conservation.
    """
)

st.subheader("Stay Informed:")
st.markdown(
    "Don't miss our blog section, where you can stay updated on eco-friendly trends, tips for sustainable living, and stories of inspiring changemakers in the green community."
)

st.subheader("Join Us in Shaping a Greener Tomorrow:")
st.markdown(
    "At EcoFind, we're committed to making sustainable living accessible and exciting. Join us on this journey to transform how we shop and make the planet a better place for future generations."
)
