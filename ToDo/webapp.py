import streamlit as st
import functions

todos = functions.get_todos()


def todo_to_added():
    new_todo = st.session_state['new'] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("TODo App")

st.subheader("TO Improve your Productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ", placeholder="Enter todo...", on_change=todo_to_added, key='new')

print("Hello")

st.session_state