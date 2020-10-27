<template>
  <div>
    <div v-if="todos.length != 0">
      <h2 class="mb-3">Recent Todos</h2>
      <TodoList :todos="todos" />
    </div>
    <div v-else class="text-center">No Todo created yet!!!</div>
  </div>
</template>

<script>
// @ is an alias to /src
import TodoList from "@/components/TodoList.vue";
import { fetchTodos } from "@/services/todo.js";

export default {
  name: "Home",
  components: {
    TodoList,
  },
  data: () => ({
    todos: [],
  }),
  created() {
    fetchTodos().then((data) => (this.todos = data));
  },
};
</script>
