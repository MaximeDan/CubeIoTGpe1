<template>
  <v-container>
    <meteo-graphs></meteo-graphs>
    <v-expand-transition>
      <meteo-stats v-if="douille"></meteo-stats>
    </v-expand-transition>
  </v-container>
</template>

<script>
  import MeteoStats from "@/components/meteoGraphs";
  import MeteoGraphs from "@/components/meteoStats";

  export default {
    name: 'Home',
    components: {
      MeteoGraphs,
      MeteoStats
    },
    data() {
      return {
        douille: false
      }
    },
    mounted() {
      setTimeout(() => {this.douille = true}, 1000)
    }
  }
</script>
