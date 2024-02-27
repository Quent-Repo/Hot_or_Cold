import requests
from flask import Flask, render_template, requests
app = Flask(__name__)

Info= requests.get("https://api.open-meteo.com/v1/gfs?latitude=40.7312&longitude=-74.2735&hourly=temperature_2m&temperature_unit=fahrenheit&wind_speed_unit=mph")

print(Info.json()["hourly"]["time"][2],Info.json()["hourly"]["temperature_2m"][2])
Time,Temp=Info.json()["hourly"]["time"][2],Info.json()["hourly"]["temperature_2m"][2]

@app.route("/")
def home():
	return render_template('index.html',Date=Time[:10],Time=Time[11:],Temp=Temp)

if __name__ == "__main__":
	app.run(debug=True)