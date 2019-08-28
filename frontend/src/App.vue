<template>
  <div id="app">
    <div class="headers">
      <li v-for="item in navlist" :key="item.id">
        <router-link :to="{name:item.name}">{{ item.title }}</router-link>
      </li>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  height: 100%;
}
</style>
