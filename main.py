import requests
from flask import Flask, render_template
app = Flask(__name__)

Info= requests.get("https://api.open-meteo.com/v1/gfs?latitude=40.7312&longitude=-74.2735&hourly=temperature_2m&temperature_unit=fahrenheit&wind_speed_unit=mph")

print(Info.json()["hourly"]["time"][0],Info.json()["hourly"]["temperature_2m"][0])
Time=Info.json()["hourly"]["time"][0]
Temp=Info.json()["hourly"]["temperature_2m"][0]

@app.route("/")
def home():
	return render_template('index.html',Time=Time,Temp=Temp)

if __name__ == "__main__":
	app.run(debug=True)