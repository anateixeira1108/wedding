from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/schedule")
def schedule():
    return render_template('schedule.html')


@main.route("/wedding-party")
def wedding_party():
    return render_template('wedding_party.html')
