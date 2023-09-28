import streamlit as st

# Custom HTML and CSS for the music recommendation system website
custom_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Music Recommendation System</title>
    <style>
        /* CSS styles go here */

        /* Style the body */
        body {
            font-family: Arial, sans-serif;
            background-color: #f9dada; /* Light pink background */
            margin: 0;
            padding: 0;
        }

        /* Style the header */
        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px;
        }

        /* Style the h1 header */
        h1 {
            color: #ff6600; /* Orange text color */
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

        /* Style the music recommendation container */
        .recommendation-container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        /* Style the recommended music list */
        .recommended-music {
            list-style-type: none;
            padding: 0;
        }

        .recommended-music li {
            margin-bottom: 10px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <header>
        <h1>Music Recommendation System</h1>
    </header>

    <div class="recommendation-container">
        <h2>Enter your mood or preference:</h2>
        <form method="POST">
            <input type="text" id="user_input" name="user_input" required>
            <input type="submit" value="Recommend Music">
        </form>
        
        {% if user_input %}
            <h2>Recommended Music:</h2>
            <ul class="recommended-music">
                {% for song in recommended_music %}
                    <li>{{ song }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    </div>
</body>
</html>
"""

# Render custom HTML in Streamlit
st.markdown(custom_html, unsafe_allow_html=True)

# Streamlit content
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
