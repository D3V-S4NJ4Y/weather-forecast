from flask import Flask, render_template, request
import requests
from datetime import datetime
import webbrowser
from threading import Timer
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    forecast_data = None
    error = None
    
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
            
            current_response = requests.get(current_url)
            forecast_response = requests.get(forecast_url)

            if current_response.status_code == 200 and forecast_response.status_code == 200:
                weather_data = current_response.json()
                forecast_data = forecast_response.json()

                weather_data["sys"]["sunrise"] = datetime.utcfromtimestamp(
                    weather_data["sys"]["sunrise"]).strftime('%H:%M:%S')
                weather_data["sys"]["sunset"] = datetime.utcfromtimestamp(
                    weather_data["sys"]["sunset"]).strftime('%H:%M:%S')
            else:
                error = "City not found. Please try again."
        else:
            error = "Please enter a city name."
    
    return render_template("index.html", weather_data=weather_data, forecast_data=forecast_data, error=error)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True)
