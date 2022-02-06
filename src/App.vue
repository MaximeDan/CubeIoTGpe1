<template>
  <v-app>
    <Navbar></Navbar>
    <router-view></router-view>
    <footerP></footerP>
  </v-app>
</template>

<script>
import footerP from "@/components/footer";
import Navbar from "@/components/Navbar";
export default {
  name: 'App',
  components: {
    Navbar,
    footerP
  },
  data: () => ({
    //
  }),
  mounted() {
    this.$store.dispatch('getStats')
    setInterval(() => {
      this.$store.dispatch('getStats')
    }, 6000)
  }
};
</script>

<style>
@font-face {
    font-family: 'comfortaa';
    src: url("../src/assets/font/Comfortaa-VariableFont_wght.ttf");
}
* {
  font-family: 'comfortaa';
}
a
{
  text-decoration: none !important;
}
</style>
