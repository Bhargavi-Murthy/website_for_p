import streamlit as st
import base64

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "About", "More"])

# Streamlit content based on navigation
if page == "Home":
    st.image("Taylor_Swift_(6966830273).jpg", use_column_width=True)
    st.title("Bha and Sheb's Auditory Recommendation System")
    st.write("Enter your mood or preference, and we'll recommend some music for you!")

    # Dummy music recommendation function
    def recommend_music(user_input):
        # Replace this with your music recommendation logic
        recommended_music = ["Song 1", "Song 2", "Song 3"]
        return recommended_music

    # Input for user's mood or preference
    user_input = st.text_input("Enter your mood or preference:")

    # Button to trigger music recommendation
    if st.button("Recommend Music"):
        recommended_music = recommend_music(user_input)
        st.subheader("Recommended Music:")
        for song in recommended_music:
            st.write(song)

elif page == "About":
    st.image("Taylor_Swift_(6966830273).jpg", use_column_width=True)
    st.title("About Us")
    st.write("This is the About Us page. We are passionate about music!")

elif page == "More":
    st.image("Taylor_Swift_(6966830273).jpg", use_column_width=True)
    st.title("More Information")
    st.write("Here you can find more information about our music recommendation system.")

# Custom CSS styles with background and text color changes
st.markdown(
    f"""
    <style>
        /* CSS styles go here */

        /* Style the body */
        body {{
            font-family: Arial, sans-serif;
            background-color: thistle; /* Thistle purple background */
            color: #8C0044; /* Hallmark purple text color */
            text-align: center;
            padding: 0;
            margin: 0;
            background-image: url('Taylor_Swift_(6966830273).jpg'); /* Specify the image path */
            background-size: cover; /* Cover the entire screen */
            background-repeat: no-repeat; /* No image repetition */
        }}

        /* Style the header */
        header {{
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px;
        }}

        /* Style the h1 header */
        h1 {{
            color: ##D8BFD8; /* Orange text color */
            font-size: 36px;
        }}

        /* Style paragraphs */
        p {{
            font-size: 18px;
            line-height: 1.5;
        }}

        /* Style links */
        a {{
            text-decoration: none;
            color: #0073e6; /* Blue link color */
        }}

        /* Change link color on hover */
        a:hover {{
            color: #00468c; /* Darker blue on hover */
        }}
    </style>
    """,
    
    unsafe_allow_html=True
)


@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("Taylor_Swift_(6966830273).jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("Taylor_Swift_(6966830273).jpg");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:Taylor_Swift_(6966830273)/jpg;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""



