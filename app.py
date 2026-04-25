from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "f0a03d15b43f2f8397063cbacf521368"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None
    icon = None   # ✅ add this

    if request.method == 'POST':
        city = request.form['city']

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            description = data["weather"][0]["description"]   # ✅ extract first

            # 🔥 ICON LOGIC (correct place)
            if "cloud" in description.lower():
                icon = "☁️"
            elif "rain" in description.lower():
                icon = "🌧️"
            elif "clear" in description.lower():
                icon = "☀️"
            elif "snow" in description.lower():
                icon = "❄️"
            else:
                icon = "🌡️"

            # ✅ now dictionary
            weather = {
                "city": city,
                "temp": data["main"]["temp"],
                "description": description
            }

        else:
            error = "City not found or API issue!"

    return render_template('index.html', weather=weather, error=error, icon=icon)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# trigger pipeline