 Weather Map Application 🌦️

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)

A simple yet powerful command-line (CLI) application built with Python to fetch and display real-time weather data for any city in the world using the OpenWeatherMap API. This project demonstrates modular code structure, API integration, and user-friendly error handling.

## 🌟 Features

-   **Real-time Weather Data**: Get up-to-the-minute weather information for any city.
-   **Detailed Information**: Displays key details including temperature, "feels like" temperature, humidity, wind speed, and a general description.
-   **Continuous Search Mode**: Allows users to look up multiple cities consecutively without restarting the application.
-   **Robust Error Handling**: Gracefully handles common errors such as invalid city names or network issues.
-   **Modular & Readable Code**: The project is structured into logical modules (`api_handler`, `ui_manager`, `main`) for clarity, reusability, and easy maintenance.

## 📸 Demo

Here is a quick demonstration of the application in action, showing both a successful query and an invalid city error.

```text
===== Weather Map Application =====
1. Get Weather by City
2. Exit
Enter your choice: 1

Enter city name (or press Enter to return to menu): Hyderabad

--- Current Weather ---
City: Hyderabad, IN
Temperature: 24.0°C (Feels like: 24.58°C)
Humidity: 94%
Wind Speed: 2.57 m/s
Description: Haze
-----------------------

Enter city name (or press Enter to return to menu): InvalidCityName

Error: The city 'InvalidCityName' could not be found. Please check the spelling.
Could not display weather information.

Enter city name (or press Enter to return to menu): 
===== Weather Map Application =====
1. Get Weather by City
2. Exit
Enter your choice: 2
Exiting the application. Goodbye!
📂 Project Structure
The code is organized into three distinct modules to separate concerns:

.
├── api_handler.py      # Handles all communication with the OpenWeatherMap API.
├── ui_manager.py       # Manages all user interaction (menus, display).
├── main.py             # The main entry point of the application.
├── requirements.txt    # Lists the project's dependencies.
└── README.md           # This documentation file.
⚙️ Setup and Installation
Follow these steps to get the application running on your local machine.

1. Clone the Repository
Bash

# Replace 'your-github-username' with your actual username
git clone [https://github.com/your-github-username/weather-map-application.git](https://github.com/your-github-username/weather-map-application.git)
cd weather-map-application
2. Create a requirements.txt File
This file tells Python which external libraries are needed. Create a new file in your project folder named requirements.txt and add the following line to it:

Plaintext

requests
3. Install Dependencies
Install the necessary libraries using pip:

Bash

pip install -r requirements.txt
4. Set Up the API Key
You will need a free API key from OpenWeatherMap.

Sign up and get your API key.

Open the main.py file.

Replace the placeholder text with your actual API key.

▶️ How to Run
Once the setup is complete, you can run the application from your terminal with the following command:

Bash

python main.py
🛠️ Technologies Used
Python 3.8+

Libraries:

requests

APIs:

OpenWeatherMap API