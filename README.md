## A simple notekingtaking app

### About
Welcome to My Notebook! This is a simple way to make and store notes in a single place. There are three primary ways that you can interact with My Notebook:
- Viewing a list of all notes in the notebook
- Searching for notes that contain some term in their content
- Adding a note to the notebook

### Getting started
To activate My Notebook, first clone this repository and install the requirements found in requirements.txt. Once installed, it should be easy to boot up the application with:
```
python app.py
```
or, you can use an alterative layout by running: 
```
streamlit run stream.py
```
Notes created by My Notebook are stored in a .json file, making it possible to upload your own notes for My Notebook to use, without having to input they individually. If you'd like to provide a list of notes that will appear in My Notebook at start-up, add a file named **notes.json** to this repository, with the following schema:
```
{
    "username": "<your-name>",
    "notes": {
        "<note-name>": "<note-content>"
    }
}
```
As you can see, this setup doesn't allow two notes to share a name. If you attempt to create a note with same name as an existing note, the original note should remain persistent — you are not allowed to add that new note to My Notebook. 

### API Interaction
Using the interface of My Notebook isn't the only way to interact with the application! There are four ways to interact with the API. 1. domain/list will show a list of the names of all notes. 
2. domain/find?keyword=<keyword> shows all notes with that keyword. 
3. domain/note/<note-name> returns the content of the note with the name <note-name>.  
4. domain/add allows notes to be added with a POST request, with name and content described in a dictionary or json format.

The schema for notes added with the POST method is as follows:
```
{
    "name": "<name>",
    "content: "<content>:
}
```
The following API call is suggested for adding a note:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d
```
If using a json to add the note, please provide a .json file with only a single json object, formatted exactly as above. If using a dictionary, then provide a dictionary with only the keys "name" and "content"
- You can indicate a dictionary submission with the flag -d
- You can indicate a json submission with the flag -d @<json-file>