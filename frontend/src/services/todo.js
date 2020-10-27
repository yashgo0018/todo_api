const ENDPOINT = "http://localhost:8000";

export async function fetchTodos() {
  return (await fetch(`${ENDPOINT}/todos/`)).json();
}

export async function fetchTodo(id) {
  return (await fetch(`${ENDPOINT}/todos/${id}/`)).json();
}

export async function createTodo(title, notes) {
  return (await fetch(`${ENDPOINT}/todos/`, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ title, notes })
  })).json();
}