<template>
  <div class="about">
    <div v-if="todo">
      <h3 style="text-decoration: underline" class="mb-2">{{ todo.title }}</h3>
      <div class="text-muted mb-1" style="font-size: 0.9rem">
        Created at {{ new Date(todo.add_time).toString() }}
      </div>
      <div>Notes:- {{ todo.notes }}</div>
    </div>
  </div>
</template>

<script>
import { fetchTodo } from "@/services/todo.js";

export default {
  data() {
    return {
      todo: null,
    };
  },
  created() {
    fetchTodo(this.$route.params.id).then((data) => (this.todo = data));
  },
};
</script>