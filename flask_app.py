# https://blog.pythonanywhere.com/121/
# https://blog.pythonanywhere.com/158/


from flask import Flask, redirect, render_template, request, url_for
from GoogleDatastore import GoogleDatastore
from ObjectTypes import CreateObject


app = Flask(__name__)
app.config["DEBUG"] = True


def get(page_type):
    db = GoogleDatastore()
    data = []
    pagetype = ""
    if page_type == 'papers':
        data = [record['title'] for record in db.query('paper')]
        pagetype = "Papers"
    elif page_type == 'bookmarks':
        data = [record['url'] for record in db.query('bookmark')]
        pagetype = "Bookmarks"
    elif page_type == 'notes':
        data = [record['note'] for record in db.query('note')]
        pagetype = "Notes"
    return render_template("main_page.html", records=data, pagetype=pagetype)


def post():
    db = GoogleDatastore()
    print(request.form)
    button = request.form['bsubmit']
    data=request.form['data']
    record = {}
    if button == 'paper': record = CreateObject.PaperRecord('','',data,'','')
    if button == 'bookmark': record = CreateObject.BookmarkRecord('','',data)
    if button == 'note': record = CreateObject.NoteRecord('','',data)
    if record: db.put(button, record)

    # Force GET of index page
    return redirect(url_for('index'))


@app.route("/notes/", methods=["GET", "POST"])
def notes():
    if request.method == "GET":
        return get('notes')

    return post()


@app.route("/papers/", methods=["GET", "POST"])
def papers():
    if request.method == "GET":
        return get('papers')

    return post()


@app.route("/bookmarks/", methods=["GET", "POST"])
def bookmarks():
    if request.method == "GET":
        return get('bookmarks')

    return post()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return get('')

    return post()
