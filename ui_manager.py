# ui_manager.py
# This module manages all user interface components, like menus and formatted output.

# We need to import the get_weather function from our other module.
from api_handler import get_weather

def view_weather(weather_data: dict):
    """
    Displays the formatted weather information to the user.

    Args:
        weather_data (dict): A dictionary containing the processed weather details.
    """
    # Check if the weather_data dictionary exists before trying to print it.
    if not weather_data:
        # This message is shown if get_weather returned None due to an error.
        print("Could not display weather information.")
        return
        
    # Print the weather data in a clean, readable format.
    print("\n--- Current Weather ---")
    print(f"City: {weather_data['city']}, {weather_data['country']}")
    print(f"Temperature: {weather_data['temperature']}°C (Feels like: {weather_data['feels_like']}°C)")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Wind Speed: {weather_data['wind_speed']} m/s")
    print(f"Description: {weather_data['description']}")
    print("-----------------------")


def menu(api_key: str):
    """
    The main menu and application loop.

    Args:
        api_key (str): The API key needed to make calls to the weather service.
    """
    # This loop keeps the menu running until the user chooses to exit.
    while True:
        print("\n===== Weather Map Application =====")
        print("1. Get Weather by City")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # This inner loop allows the user to check multiple cities without returning to the main menu.
            while True:
                city = input("\nEnter city name (or press Enter to return to menu): ")
                
                if not city:
                    # If the user just presses Enter, break out of this inner loop.
                    break
                
                # Call the get_weather function from the api_handler module.
                weather_details = get_weather(city, api_key)
                # Call the local view_weather function to display the results.
                view_weather(weather_details)
                
        elif choice == '2':
            # If the user chooses to exit, print a goodbye message and break the main loop.
            print("Exiting the application. Goodbye!")
            break
        else:
            # Handle invalid menu choices.
            print("Invalid choice. Please enter 1 or 2.")