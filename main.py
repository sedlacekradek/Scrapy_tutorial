from flask import Flask, render_template
import requests
import json
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
import secrets


### FORMS ###
class LocationForm(FlaskForm):
    site = SelectField('Lokalita', validators=[DataRequired()],
                       choices=[('stodulky', 'Praha - Stodůlky (https://www.bydleni-stodulky.cz/stodulky/cenik/)'),
                                ('skvrnany', 'Plzeň - Skvrňany (https://www.byty-skvrnany.cz/skvrnany/cenik/)'),
                                ('knoviz', 'Knovíz - vilová čtvrť (https://www.knoviz22.cz/)')]
                       )
    submit = SubmitField('Scrape')


### FLASK INI ###
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


### MAIN ###
@app.route("/", methods=["GET", "POST"])
def home():
    form = LocationForm()
    if form.validate_on_submit():
        params = {
            'spider_name': f'{form.site.data}',
            'start_requests': True,
        }
        # scrapyrt - needs to be started from the terminal
        # You send a request to ScrapyRT with spider name and URL,
        # and in response, you get items collected by a spider visiting this URL.
        response = requests.get("http://localhost:9080/crawl.json", params)
        data = json.loads(response.text)
        return render_template("index.html", form=form, data=data["items"])
    return render_template("index.html", form=form, data=None)


### TO TEST LOCALLY ###
if __name__ == "__main__":
    app.run(debug=True)