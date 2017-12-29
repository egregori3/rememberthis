# https://blog.pythonanywhere.com/121/
# https://blog.pythonanywhere.com/158/


from flask import Flask, redirect, render_template, request, url_for
from GoogleDatastore import GoogleDatastore


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    db = GoogleDatastore()
    if request.method == "GET":
        titles = [record['title'] for record in db.query('paper')]
        return render_template("main_page.html", comments=titles)

    # POST of index page
#    content=request.form["contents"]

    # Force GET of index page
    return redirect(url_for('index'))
