# main.py
# This is the main entry point for the Weather Map Application.

# Import the menu function from the user interface module.
from ui_manager import menu

# --- Configuration ---
# Place your API key here. This is the only place you need to edit.
API_KEY = "74a577a8d457ff7e00576ebd392ea2eb"


if __name__ == "__main__":
    """
    This special block ensures that the code inside it only runs when this script
    is executed directly (not when it's imported by another script).
    """
    # First, perform a safety check to ensure the user has replaced the placeholder API key.
    if API_KEY == "YOUR_API_KEY_HERE" or not API_KEY:
        print("ERROR: API_KEY is not set.")
        print("Please open the 'main.py' file and replace 'YOUR_API_KEY_HERE' with your actual OpenWeatherMap API key.")
    else:
        # If the key is set, start the application by calling the menu function.
        # We pass the API_KEY to the menu so it can be used for API calls.
        menu(API_KEY)