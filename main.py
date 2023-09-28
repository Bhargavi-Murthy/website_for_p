import streamlit as st

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
