<template>
  <img alt="RMVAI Logo" src="./assets/CVtD.gif">
  <h1>Sasha, le bot qui a réponse à tout !</h1>
  <InputComponent :backend_url="backend_url" style="margin-top: 100px;" />
</template>

<script>
import InputComponent from './components/InputComponent.vue'

export default {
  name: 'App',
  components: {
    InputComponent
  },
  data: () => {
    return {
      backend_url: 'http://' + window.location.hostname + ':5667'
    }
  }
}
</script>

<style>
h1 {
  color: white;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
body {
  background-color: #222222;
}
</style>
