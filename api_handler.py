# api_handler.py
# This module is responsible for all communication with the OpenWeatherMap API.

import requests

def get_weather(city: str, api_key: str) -> dict | None:
    """
    Fetches and processes weather data for a given city from the API.

    Args:
        city (str): The name of the city to get weather for.
        api_key (str): The API key for authenticating with the service.

    Returns:
        dict | None: A dictionary containing the processed weather information
                      if the request was successful, otherwise None.
    """
    # The API URL, constructed with the city name and API key.
    # The 'units=metric' parameter ensures we get temperature in Celsius.
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Send a GET request to the API endpoint.
        response = requests.get(base_url)
        # This will raise an exception if the response has a 4xx or 5xx status code (e.g., 401 Unauthorized, 404 Not Found).
        response.raise_for_status()
        
        # Parse the JSON response from the API into a Python dictionary.
        data = response.json()
        
        # Extract only the necessary information from the large API response.
        weather_info = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title(),
            "wind_speed": data["wind"]["speed"]
        }
        # Return the clean, organized dictionary.
        return weather_info

    except requests.exceptions.HTTPError:
        # Handle cases where the city is not found (404 error) or other HTTP errors.
        if response.status_code == 404:
            print(f"Error: The city '{city}' could not be found. Please check the spelling.")
        else:
            print(f"An HTTP error occurred (Code: {response.status_code}). Please check your API key.")
        return None
    except requests.exceptions.RequestException:
        # Handle network-related errors, like no internet connection.
        print("A network error occurred. Please check your internet connection.")
        return None
    except KeyError:
        # Handle cases where the API response is missing expected data.
        print("Error: Could not parse the weather data. The API response format may have changed.")
        return None