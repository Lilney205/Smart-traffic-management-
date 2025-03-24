from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    car_count = random.randint(0, 10)
    traffic_light = "GREEN" if car_count > 5 else "RED"
    return render_template("index.html", car_count=car_count, traffic_light=traffic_light)

if __name__ == "__main__":
    app.run(debug=True)
