import streamlit as st
import functions as f

todos = f.get_todos()
selected_todos = []


def add_todo():
    new_todo = st.session_state["new_todo"].strip()
    if new_todo == "":
        pass
    else:
        new_todo = new_todo.title() + "\n"
        todos.append(new_todo)
        f.write_todos(todos)
        st.session_state["new_todo"] = ""


def complete_todo():
    if selected_todos:
        new_todos = [to_do for nt, to_do in enumerate(todos) if nt not in selected_todos]
        f.write_todos(new_todos)

    else:
        pass


def edit_todo():
    pass


st.title("My Todo app.")
st.subheader("This is my todo app")
st.write("This app is for increasing productivity.")

for i, todo in enumerate(todos):
    s = st.checkbox(todo)
    if s:
        selected_todos.append(i)

st.text("")
st.text("")
st.text("")
st.text("To mark as complete select one or more todo and click 'Complete todo (s)' button.")
st.button(label="Complete todo (s)", on_click=complete_todo)

st.text("")
st.text("")
st.text("")
st.text("To add a todo, enter the todo below and press enter.")
st.text_input(label="Enter new todo :",
              placeholder="Add new todo...",
              label_visibility="hidden",
              on_change=add_todo,
              key="new_todo")



