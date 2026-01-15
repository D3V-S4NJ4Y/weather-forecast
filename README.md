# Weather Forecast Application

A Flask-based web application that displays current weather and 5-day forecast for any city using the OpenWeatherMap API.

## Features

- Current weather information (temperature, humidity, wind speed, etc.)
- 5-day weather forecast
- Sunrise and sunset times
- Automatic browser launch
- Clean and responsive interface

## Prerequisites

- Python 3.7 or higher
- OpenWeatherMap API key (free tier available at [openweathermap.org](https://openweathermap.org/api))

## Installation

1. Clone the repository or download the project files

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your OpenWeatherMap API key to the `.env` file:
     ```
     API_KEY=your_api_key_here
     ```

## Usage

1. Run the application:
```bash
python Weather.py
```

2. The application will automatically open in your default browser at `http://127.0.0.1:5000/`

3. Enter a city name to get the current weather and forecast

## Project Structure

```
weather-forecast/
├── Weather.py          # Main Flask application
├── templates/          # HTML templates
│   └── index.html
├── static/            # CSS, JS, images (if any)
├── .env               # Environment variables (not in git)
├── .env.example       # Example environment file
├── requirements.txt   # Python dependencies
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## API Reference

This application uses the OpenWeatherMap API:
- Current Weather: `api.openweathermap.org/data/2.5/weather`
- 5-Day Forecast: `api.openweathermap.org/data/2.5/forecast`

## License

This project is open source and available for personal and educational use.
