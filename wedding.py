from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/schedule")
def schedule():
    return render_template('schedule.html')


@app.route("/wedding-party")
def weddingparty():
    return render_template('wedding-party.html')


@app.route("/registry")
def registry():
    return render_template('registry.html')


@app.route("/rsvp")
def rsvp():
    return render_template('rsvp.html')


if __name__ == '__main__':
    app.run(debug=True)