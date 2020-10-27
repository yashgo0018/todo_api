<template>
  <div id="app">
    <nav class="navbar navbar-dark bg-dark">
      <div class="container">
        <router-link class="navbar-brand" to="/">Todo Manager</router-link>
      </div>
    </nav>
    <div class="container mt-4">
      <router-view />
    </div>
    <router-link
      to="/create"
      class="float"
      data-toggle="tooltip"
      data-placement="left"
      title="Create Todo"
    >
      <i class="fa fa-plus my-float"></i>
    </router-link>
  </div>
</template>

<style scoped>
.float {
  position: fixed;
  width: 60px;
  height: 60px;
  bottom: 40px;
  right: 40px;
  background-color: #2c3e50;
  color: #fff;
  border-radius: 50px;
  text-align: center;
  box-shadow: 2px 2px 3px #999;
}

.my-float {
  margin-top: 22px;
}
</style>
