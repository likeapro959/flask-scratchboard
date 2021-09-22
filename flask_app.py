
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

comments = []

@app.route('/', methods=["GET", "POST"])
def index():
    global comments
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    if len(comments) > 50:
        comments = []
    comments.append(request.form["contents"])
    return redirect(url_for("index"))
