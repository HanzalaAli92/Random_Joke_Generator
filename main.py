import streamlit as st  # For creating the web app
import requests  # For making HTTP requests to the API

def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        # Make GET request to joke API
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            joke_data = response.json()
            # Return formatted joke with setup and punchline (dictionary keys)
            return f"🎭 {joke_data['setup']} \n\n 😂 {joke_data['punchline']}"
        else:
            # Return error message if API call fails
            return "⚠️ Failed to fetch a joke. Please try again later."
    except:
        # Return fallback joke if exception occurs like internet issues
        return "💻 Why did the programmer quit his job? \n\n 😂 Because he didn't get array!"

def main():
    """Main function to run the Streamlit app"""
    # Set page title with emoji
    st.title("🤣 Random Joke Generator 🎭")
    
    # Add instruction text with emoji
    st.write("👉 Click the button below to generate a random joke! 😆")
    
    # Create button and handle click
    if st.button("🎲 Generate Joke 😂"):
        # Get random joke when button clicked
        joke = get_random_joke()
        # Display joke with success styling
        st.success(joke)

    # Add horizontal line
    st.divider()
    
    # Footer using HTML, displaying text in the center with heart emoji
    st.markdown(
        """
        <div style='text-align:center;'>
            <p>🃏 Joke from Official Joke API</p>
            <p>❤️ Built with love by <b>Muhammad Hanzala Ali</b> using Streamlit ❤️</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Run main function when script is executed directly
if __name__ == "__main__":
    main()