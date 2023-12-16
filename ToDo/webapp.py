# import sys
# sys.path.append("..")

import streamlit as st
import functions


def to_do_add():
    todo_ = st.session_state["new_todo"]
    print(todo)


todos = functions.get_todos()

st.title("MY Todo App")
st.subheader("")

for todo in todos:
    st.checkbox(todo, key='hel')

st.text_input(label="Enter a todo:", placeholder="Add new todo...", on_change=to_do_add, key='new_todo')




