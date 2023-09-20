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
st.title(":rainbow: Eco Insights")
st.header("Discover, Learn, and Embrace _Eco-Friendly Living_")


# Text description
st.markdown(
    """
Click on each topic below to expand and read the full blog article. Explore a range of environmental topics and discover how you can embrace eco-friendly living. We invite you to dive into these insightful articles and learn more about making sustainable choices in your daily life.
"""
)


# Blog post 1
with st.expander("The Impact of Plastic Pollution on Our Oceans"):
    st.subheader("The Impact of Plastic Pollution on Our Oceans")
    st.image(
        "https://images.unsplash.com/flagged/photo-1572213426852-0e4ed8f41ff6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2074&q=80"
    )
    st.markdown(
        """
    Plastic pollution is a global crisis that's causing irreparable damage to our oceans. It's estimated that over eight million tons of plastic end up in our seas every year. This not only threatens marine life but also poses risks to human health.

    Plastic debris, from single-use bottles to microplastics, finds its way into the stomachs of marine animals, often with fatal consequences. It disrupts ecosystems, damages coral reefs, and contributes to the acidification of our oceans.

    To combat this crisis, we must reduce our plastic consumption. EcoFind can assist in this journey by recommending eco-friendly alternatives to everyday plastic products. By making sustainable choices, we can help protect our oceans for future generations.
    """
    )

# Blog post 2
with st.expander("Climate Change and Sustainable Energy Solutions"):
    st.subheader("Climate Change and Sustainable Energy Solutions")
    st.image("https://unece.org/sites/default/files/user_upload/renewable_energy.jpg")
    st.markdown(
        """
    Climate change is one of the most critical challenges of our time, largely driven by the use of fossil fuels. Transitioning to sustainable energy sources is crucial to mitigating its effects.

    Renewable energy, such as solar and wind power, offers a clean and sustainable alternative. EcoFind can guide you in selecting energy-efficient appliances and renewable energy solutions, making it easier to reduce your carbon footprint and combat climate change.

    By choosing sustainable energy options, we contribute to a healthier planet and a more sustainable future for all.
    """
    )

# Blog post 3
with st.expander("The Beauty of Biodiversity: Protecting Endangered Species"):
    st.subheader("The Beauty of Biodiversity: Protecting Endangered Species")
    st.image(
        "https://www.drishtiias.com/images/blogs/The-Urgency-of-Protecting-Endangered-Species-from-Extinction-02.jpg"
    )
    st.markdown(
        """
    Our planet's biodiversity is a treasure trove of life forms, but many species are on the brink of extinction due to habitat destruction and other human activities.

    EcoFind encourages a sustainable lifestyle by highlighting eco-friendly products that support wildlife conservation efforts. By choosing these products, you contribute to the preservation of endangered species and the protection of our planet's rich biodiversity.

    Let's celebrate and protect the beauty of the natural world by making conscious choices that support wildlife conservation.
    """
    )

# Blog post 4
with st.expander("Eco-Friendly Gardening: Growing a Sustainable Oasis"):
    st.subheader("Eco-Friendly Gardening: Growing a Sustainable Oasis")
    st.image(
        "https://images.herzindagi.info/image/2022/May/Ideas-To-Create-An-Eco-Friendly-Garden.jpg"
    )
    st.markdown(
        """
    Gardening is a wonderful way to connect with nature, but traditional gardening practices can harm the environment. Embracing eco-friendly gardening methods can help you create a sustainable oasis in your backyard.

    EcoFind recommends organic gardening supplies and eco-conscious gardening tools that enable you to cultivate a garden that's in harmony with nature. With these sustainable choices, you can nurture a thriving garden while minimizing your environmental impact.

    Join the movement of eco-conscious gardeners and let your garden bloom sustainably!
    """
    )

# Blog post 5
with st.expander("The Food-Waste Dilemma: How Small Changes Can Make a Big Impact"):
    st.subheader("The Food-Waste Dilemma: How Small Changes Can Make a Big Impact")
    st.image(
        "https://media.istockphoto.com/id/1425232352/photo/expired-organic-bio-waste-mix-vegetables-and-fruits-in-a-huge-container-in-a-rubbish-bin-heap.jpg?s=612x612&w=0&k=20&c=_hIv18ePoswfw6BTJK9j7JMC4mhgXU-GX8rpIEbIJ5s="
    )
    st.markdown(
        """
    Food waste is a global issue with serious environmental consequences. Each year, tons of food end up in landfills, producing methane, a potent greenhouse gas.

    EcoFind can help you reduce food waste by recommending kitchen gadgets and storage solutions that extend the shelf life of your groceries. By minimizing food waste, you not only save money but also reduce your carbon footprint and contribute to a more sustainable food system.

    Small changes in the kitchen can make a significant impact on the environment.
    """
    )

# Blog post 6
with st.expander("EcoFind: Your Guide to a Greener Lifestyle"):
    st.subheader("EcoFind: Your Guide to a Greener Lifestyle")
    st.image(
        "https://www.fultonbank.com/-/media/Feature/Teaser/Education-Center/Trending/Go-green_TN.ashx"
    )
    st.markdown(
        """
    EcoFind is your one-stop destination for embracing a greener lifestyle. Our platform offers a wealth of resources and recommendations to help you make eco-conscious choices in your daily life.

    From suggesting eco-friendly products to providing sustainability ratings and informative articles in our blog section, EcoFind empowers you to lead a more sustainable life.

    Join us on this journey toward a greener, more eco-friendly future. Let's make a positive impact together.
    """
    )
