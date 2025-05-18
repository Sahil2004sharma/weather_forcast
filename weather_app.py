import streamlit as st
import requests

# Defining a class to handle weather forecasting
class WeatherData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.weatherapi.com/v1/forecast.json"  

    # Function to fetch weather info
    def fetch_weather(self, city, days=3):  
        url = f"{self.base_url}?key={self.api_key}&q={city}&days={days}&aqi=no&alerts=no"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": {"message": "Invalid API response"}}
        except Exception as e:
            return {"error": {"message": str(e)}}

# Main function for Streamlit app
def run_app():
    st.title(" Weather Forecast Portal")

    api_key = "31cb52e6d9d54f80bea65125251705"  # API key for weather data
    weather = WeatherData(api_key)  # Initializing class object

    city_name = st.text_input("Enter City Name")  # Input field for user
    forecast_days = st.slider("Select Forecast Duration", 1, 7, 3)  

    if st.button("Get Weather"):
        if city_name.strip():  
            weather_info = weather.fetch_weather(city_name, forecast_days)  

            if "error" not in weather_info:  
                st.success(f" Weather forecast for **{city_name}**")

                for daily_data in weather_info["forecast"]["forecastday"]:
                    date = daily_data["date"]
                    temp_avg = daily_data["day"]["avgtemp_c"]
                    climate = daily_data["day"]["condition"]["text"]

                    st.write(f" **Date:** {date}")
                    st.write(f" **Avg Temperature:** {temp_avg}°C")
                    st.write(f"**Condition:** {climate}")
                    st.write("------")

            else:
                st.error(f" Error: {weather_info['error']['message']}")

if __name__ == "__main__":
    run_app()