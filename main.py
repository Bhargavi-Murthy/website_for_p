import streamlit as st

# Define custom HTML and CSS
custom_html = """
<!DOCTYPE html>
<html>
<head>
    <title>My Streamlit App</title>
    <style>
        /* CSS styles go here */

        /* Style the body */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
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
    </style>
</head>
<body>
    <header>
        <h1>Welcome to My Streamlit App</h1>
    </header>

    <div class="content">
        <p>This is a sample paragraph with <a href="#">a link</a>.</p>
    </div>
</body>
</html>
"""

# Render custom HTML in Streamlit
st.markdown(custom_html, unsafe_allow_html=True)

# Streamlit content
st.title("Streamlit Integration Example")
st.write("You can mix custom HTML and CSS with Streamlit content.")
