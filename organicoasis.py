import streamlit as st

# Website Title
st.title("Organic Oasis🥗")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Menu", "Contact"])

# Home Page
if page == "Home":
    st.header("Welcome to Organic Oasis")
    st.write("Your favorite food, made organically and fresh.")
    

# Menu Page
elif page == "Menu":
    st.header("Our Menu")
    menu_items = [
        {
            "name": "Margherita Pizza",
            "price": "$10",
            "description": "Classic pizza with tomato, mozzarella, and basil.",
        },
        {
            "name": "Veggie Burger",
            "price": "$8",
            "description": "Grilled veggie patty with lettuce, tomato, and aioli.",
        },
        {
            "name": "Caesar Salad",
            "price": "$7",
            "description": "Crisp romaine, parmesan, croutons, and Caesar dressing.",
        },
    ]
    for item in menu_items:
        st.subheader(f"{item['name']} - {item['price']}")
        st.write(item["description"])

# Contact Page
elif page == "Contact":
    st.header("Contact Us")
    st.write("📞 Phone: +91 9307946976")
    st.write("📧 Email:organicoasis127@gmail.com")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Thank you for contacting us! We'll get back to you soon.")
