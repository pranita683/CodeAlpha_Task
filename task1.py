import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&cnt=7&appid={api_key}"
    
    # Make the API request and check if the request is successful
    response = requests.get(url)
    
    # Check for errors in the response
    if response.status_code != 200:
        print(f"Error: Unable to fetch data. HTTP Status Code: {response.status_code}")
        return None
    
    # Print the raw response to understand the issue
    print(f"Response from API: {response.json()}")
    
    data = response.json()
    
    # Check if the API returns the expected 'list' key
    if "list" not in data:
        print(f"Error: The 'list' key is missing in the API response.")
        print(f"API Response: {data}")
        return None
    
    # Extract necessary information
    dates = []
    temperatures = []
    humidities = []
    
    for forecast in data['list']:
        dates.append(forecast['dt_txt'])
        temperatures.append(forecast['main']['temp'])
        humidities.append(forecast['main']['humidity'])
    
    # Create a DataFrame
    weather_df = pd.DataFrame({
        'Date': pd.to_datetime(dates),
        'Temperature (°C)': temperatures,
        'Humidity (%)': humidities
    })
    
    return weather_df

# Set your API key here (make sure it's the correct one)
API_KEY = '01865941e9a70db44cb80529d0a629e6'  # Replace with your actual API key

# Get weather data for a city (example: London)
city = 'India'
weather_data = fetch_weather_data(city, API_KEY)

# Check if data was fetched successfully before proceeding with visualization
if weather_data is not None:
    # Show the fetched data
    print(weather_data)

    # Visualize the data using Seaborn and Matplotlib

    # Plot temperature
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=weather_data, x='Date', y='Temperature (°C)', marker='o', label="Temperature (°C)")
    plt.title(f'7-Day Weather Forecast for {city}')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot humidity
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=weather_data, x='Date', y='Humidity (%)', marker='o', label="Humidity (%)", color='orange')
    plt.title(f'7-Day Weather Forecast for {city} - Humidity')
    plt.xlabel('Date')
    plt.ylabel('Humidity (%)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("No data to visualize due to an error in fetching data.")
