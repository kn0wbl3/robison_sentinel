from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    # grab data
    oil_data = pd.read_csv("data/oil_levels.csv")
    # Creating Figure
    p = figure(
        title="Oil Levels", 
        x_axis_label="Date",
        y_axis_label="Oil (Gallons)",
        height=350, 
        sizing_mode="stretch_both"
    )
 
    # Defining figure to be line
    p.line(
        pd.to_datetime(oil_data.date),
        oil_data.oil_level,
        color="navy",
        line_width=2
    )

    p.xaxis[0].formatter = DatetimeTickFormatter(days="%D")
 
    # Get Chart Components
    script, div = components(p)
    return render_template("index.html", script=script, div=div)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5001")
