import streamlit as st

if "_notebook" not in st.session_state:
    st.session_state["_notebook"] = st.session_state.notebook

def evaluate_submission():
    if st.session_state.name=="" or st.session_state.content=="":
        st.error("Please add both content and a name.")
    elif st.session_state.name in st.session_state["_notebook"].notes:
        st.error(f"A note named {st.session_state.name} already exists.")
    else:
        st.success("Your note has been added!")
        st.balloons()
        st.session_state["_notebook"].add_note(st.session_state.name, st.session_state.content)
        st.session_state["_notebook"].write_to_dir()
        st.session_state.notebook = st.session_state["_notebook"]

st.title("My notebook")
with st.container():
    st.subheader("Add a note!")
    with st.form("add_note"):
        st.text_input(label="Name", key="name")
        st.text_area(label="Content", key="content")
        st.form_submit_button(label="Submit", on_click=evaluate_submission())

st.page_link("stream.py", label="Go home", icon=":material/home:")