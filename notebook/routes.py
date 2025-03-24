from notebook import app
from notebook import notes
from flask import render_template, request, flash, redirect, url_for


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", type=str)
        content = request.form.get("content", type=str)
        success = notes.add_note(name, content)
        flash(notes.feedback(
            success, "Your note has been successfully added."))

    keyword = request.args.get("keyword", type=str)
    names = notes.list_notes()

    if request.method == "GET":
        if "keyword" in request.args:
            names = notes.find_notes(keyword).all()
    if not names and keyword:
        names = notes.list_notes()
        flash(f"There are no notes that contain the keyword {keyword}.")
        keyword = None
    return render_template("home.html", names=names, keyword=keyword)


@app.route('/note/<name>', methods=["GET", "POST"])
def get_note(name):
    if request.method == "POST":
        note = notes.retrieve_note(name)
        comment = request.form.get("comment", type=str)
        success = notes.add_comment(comment, note)
        flash(notes.feedback(success, "Your comment was successfully added!"))

    note = notes.retrieve_note(name)

    if request.method == "GET":
        if "delete" in request.args:
            success = notes.delete_note(note)
            flash(notes.feedback(
                success,
                f"The note \"{note.name}\" has been successfully deleted."))
            return redirect(url_for("home"))
    return render_template("note.html", note=note)
