from flask import Flask, render_template


app = Flask(__name__)
numberOrViews = 0


@app.route("/")
def welcome():
    return render_template("welcome.html",
                           message="something to display")




@app.route("/views")
def views():
    global numberOrViews
    numberOrViews = numberOrViews + 1
    return "Views number " + str(numberOrViews)
