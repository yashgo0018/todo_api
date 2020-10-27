<template>
  <div class="list-group">
    <a
      v-for="todo in todos"
      :key="todo.id"
      :href="`/todos/${todo.id}`"
      class="list-group-item list-group-item-action"
      >{{ todo.title }}</a
    >
  </div>
</template>

<script>
export default {
  name: "TodoList",
  props: ["todos"],
};
</script>