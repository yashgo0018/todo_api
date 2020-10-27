<template>
  <div>
    <h3>Create Todo</h3>
    <form class="mt-3 col-md-7 col-lg-5" @submit="checkForm">
      <div class="form-group">
        <label for="title">Title</label>
        <input
          type="title"
          class="form-control"
          id="title"
          v-model="title"
          aria-describedby="titleHelp"
        />
        <small
          v-if="errors.title != ''"
          id="titleHelp"
          class="form-text text-muted"
          >{{ errors.title }}</small
        >
      </div>
      <div class="form-group">
        <label for="notes">Notes</label>
        <textarea
          class="form-control"
          id="notes"
          rows="3"
          v-model="notes"
          aria-describedby="notesHelp"
        ></textarea>
        <small
          v-if="errors.notes != ''"
          id="notesHelp"
          class="form-text text-muted"
          >{{ errors.notes }}</small
        >
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import { createTodo } from "@/services/todo.js";

export default {
  data: () => ({
    title: "s",
    notes: "",
    errors: {
      title: "",
      notes: "",
    },
  }),
  methods: {
    checkForm(e) {
      let valid = true;
      if (this.title.length <= 50) {
        this.errors.title = "";
      } else {
        this.errors.title = "Title cannot be longer than 50 characters";
        valid = false;
      }
      if (this.notes.length <= 500) {
        this.errors.notes = "";
      } else {
        this.errors.notes = "Notes cannot be longer than 500 characters";
        valid = false;
      }
      if (valid) {
        createTodo(this.title, this.notes).then((data) => {
          console.log(data);
          this.$router.push("/");
        });
      }
      e.preventDefault();
    },
  },
};
</script>