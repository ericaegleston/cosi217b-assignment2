import os 
from flask import Flask, request, render_template, url_for, flash
from notebook import Notebook

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e14612db01f0a5eb01849080ed9096f4a9a23f53da43ac1ccb9d90c058f9b7f4'
notebook = Notebook("notes.json")

@app.route('/', methods=["GET", "POST"])
def home():
    keyword = request.form.get("keyword", type=str)
    return render_template("home.html", notes=notebook, keyword=keyword, add_url=url_for('add_note'))

@app.route('/note')
def get_note():
    name = request.args.get("name", type=str)
    return render_template("note.html", name=name, notes=notebook, home_url=url_for('home'))

@app.route('/add', methods=["GET", "POST"]) 
def add_note():
    name = request.form.get("name", type=str)
    content = request.form.get("content", type=str)
    if request.method == "POST":
        if not name or not content:
            flash("Please add both content and a name to your note.", "error")
        elif name in notebook.notes:
            flash(f"A note named {name} already exists.", "error")
        else:
            flash(f"The note {name} was successfully added.", "success")
            notebook.add_note(name, content)
            notebook.write_to_dir()
    return render_template("add.html", home_url=url_for('home'))

if __name__ == '__main__':
    app.run(port=8000, debug=True)