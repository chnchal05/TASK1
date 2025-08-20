import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Ask user to enter a city name
city = input("Enter your city name: ")

# Your OpenWeatherMap API key
API_KEY = 'a45089aafcb2ab5d10e15dfab890f721'

# API URL for 5-day forecast (data every 3 hours)
url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'

# Make the API request
response = requests.get(url)
data = response.json()

# Check if the response is valid
if response.status_code != 200 or "list" not in data:
    print("Error fetching data. Please check the city name or API key.")
    exit()

# Extract dates and temperatures (first 10 entries)
dates = []
temperatures = []

for entry in data['list'][:10]:
    dates.append(entry['dt_txt'])  # e.g., "2025-06-28 12:00:00"
    temperatures.append(entry['main']['temp'])  # Temperature in °C

# Set Seaborn style
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temperatures, color='blue', linewidth=2)
plt.scatter(dates, temperatures, color='red')  # Add points for visibility

# Add titles and labels
plt.title(f'Temperature Forecast for {city}', fontsize=16)
plt.xlabel('Date and Time', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.xticks(rotation=45)

# Final layout and display
plt.tight_layout()
plt.show()