from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from notebook import Notebook

app = FastAPI()
notebook = Notebook("notes.json")

class Note(BaseModel):
    name: str
    content: str

@app.get("/")
def root():
    return """Welcome! There are four ways to interact with the API. 1 - domain/list will show a list of 
    the names of all notes. 2- domain/find?keyword=<keyword> shows all notes with that keyword. 
    3 - domain/note/<note-name> returns the content of the note with the name <note-name>. 4 - domain/add 
    allows notes to be added with a POST request, with name and content described in a dictionary or json
    format."""

@app.get("/list")
def list():
    return notebook.list_notes()

@app.get("/find")
def find(keyword: str):
    matches = notebook.find(keyword)
    if not matches:
        raise HTTPException(status_code=404, detail=f"Could not find any notes with the term {keyword}")
    return {"keyword": keyword, "matching note": matches}

@app.get("/note/{name}")
def note(name: str):
    if not name in notebook.notes:
        raise HTTPException(status_code=404, detail=f"There is no noted named {name} in the notebook.")
    return notebook.content(name)

@app.post("/add", status_code=201)
def add(note: Note):
    note_dict = note.model_dump()
    if note_dict["name"] in notebook.notes:
        raise HTTPException(status_code=400, detail=f"A note named {note_dict['name']} already exists.")
    notebook.add_note(note_dict["name"], note_dict["content"])
    notebook.write_to_dir()
    return {"detail": f"The note {note_dict['name']} was successfully added."}
