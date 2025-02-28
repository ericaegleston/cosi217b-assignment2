import streamlit as st
import pandas as pd
from notebook import Notebook

st.set_page_config(layout="wide")

@st.cache_data()
def load_data():
    return Notebook("notes.json")

if "notebook" not in st.session_state:
    st.session_state.notebook = load_data()

if "notes_list" not in st.session_state:
    st.session_state.notes_list = st.session_state.notebook.list_notes()

st.title('My notebook')
selection_col, view_col = st.columns([0.4, 0.6], gap="medium")

def find_notes():
    matches = st.session_state.notebook.find_notes(st.session_state.keyword)
    if matches:
        st.session_state.notes_list = matches
    else:
        st.session_state.notes_list = st.session_state.notebook.list_notes()
        st.info(f'There are no notes including the keyword "{st.session_state.keyword}"')

with selection_col:
    with st.form("find_notes"):
        st.text_input(label='**Find notes about:**', key="keyword")
        st.form_submit_button(label='Submit', on_click=find_notes())

    with st.container():
        df = pd.DataFrame({'Name': st.session_state.notes_list})
        notes = st.dataframe(df, width=1000, hide_index=True, on_select="rerun", selection_mode='single-row')
        if len(notes.selection.rows):
            selected_row = notes.selection.rows[0]
            name = df.iloc[selected_row]["Name"]
            content = st.session_state.notebook.content(name)
            st.session_state.note_display = f"## {name} \n {content} \n "
        else:
            st.session_state.note_display = "Select a note to the left to see it's contents!"

with view_col:
    note_box = st.empty()

    with note_box.container(border=True):
        st.markdown(st.session_state.note_display)

st.page_link("pages/stream_add.py", label="Add a note!", icon=":material/add:")