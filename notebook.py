import json
import os

class Notebook:
    def __init__(self, notes_directory=None):
        self.notes: dict[str: str] = {}
        self.notes_directory: str = "notes.json"
        self.username: str = None
        if os.path.exists(notes_directory):
            with open(notes_directory, "r") as file:
                content = json.load(file)
                if "username" in content:
                    self.username = content["username"]
                self.notes = content['notes']
            self.notes_directory = notes_directory
            file.close()

    def add_note(self, name: str, content: str):
        self.notes[name] = content

    def add_username(self, username: str):
        self.username = username

    def list_notes(self):
        return list(self.notes)

    def find_notes(self, keyword: str):
        return list(filter(lambda name: self.notes[name].lower().find(keyword.lower()) != -1, list(self.notes)))


    def content(self, name: str):
        return self.notes[name]
    
    def write_to_dir(self):
        notes_dict = {"username": self.username, "notes": self.notes}
        with open(self.notes_directory, "w") as outfile:
            outfile.write(json.dumps(notes_dict, ensure_ascii=False, indent=4))
        outfile.close()

            