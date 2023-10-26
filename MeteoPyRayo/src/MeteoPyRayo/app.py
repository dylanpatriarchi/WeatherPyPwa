"""
API Weather for searching weather in python for an android app
"""
def main():
    # This should start and launch your app!
    pass
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Funzione per ottenere la previsione del tempo da wttr.in
def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    return response.text

@app.route('/', methods=['GET', 'POST'])
def weather():
    city = request.form.get('city', 'New York')  # Impostazione predefinita su New York
    weather_data = get_weather(city)
    return render_template('weather.html', city=city, weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)

