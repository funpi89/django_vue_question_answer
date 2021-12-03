<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <NavebarComponent />
    <router-view />
  </div>
</template>

<script>
import { apiService } from '@/common/api.service.js'
import NavebarComponent from './components/Navbar.vue'
export default {
  name: "App",
  components: {
    NavebarComponent
  },
  methods: {
    async setUserInfo(){
      const data = await apiService("/api/user/");
      const requestUser = data['username'];
      window.localStorage.setItem('username', requestUser);
      // console.log(data);
      // console.log(requestUser);

    }
  },
  created(){
    this.setUserInfo();
  }
}
</script>


<style>
html, body {
  height: 100%;
  font-family: "Playfair Display", serif;
}

.btn:focus{
  box-shadow: none !important;
}
</style>
