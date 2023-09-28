import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "About", "More"])

# Streamlit content based on navigation
if page == "Home":
    st.title("Music Recommendation System")
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
    st.title("About Us")
    st.write("This is the About Us page. We are passionate about music!")

elif page == "More":
    st.title("More Information")
    st.write("Here you can find more information about our music recommendation system.")

# Custom CSS styles
st.markdown(
    """
    <style>
        /* CSS styles go here */

        /* Style the body */
        body {
            font-family: Arial, sans-serif;
            background-image: url('/Taylor_Swift_(6966830273).jpg'); /* Specify the image path */
            background-size: cover; /* Cover the entire screen */
            background-repeat: no-repeat; /* No image repetition */
            margin: 0;
            padding: 0;
        }

        /* Style the header */
        header {
            background-color: #567;
            color: #fff;
            text-align: center;
            padding: 20px;
        }

        /* Style the h1 header */
        h1 {
            color: #87CEFA; /* Orange text color */
            font-size: 36px;
        }

        /* Style paragraphs */
        p {
            font-size: 18px;
            line-height: 1.5;
        }

        /* Style links */
        a {
            text-decoration: none;
            color: #0073e6; /* Blue link color */
        }

        /* Change link color on hover */
        a:hover {
            color: #00468c; /* Darker blue on hover */
        }
    </style>
    """,
    unsafe_allow_html=True,
)
