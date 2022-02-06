<template>
  <div>
    <v-container>
      <v-card>
        <v-card-title class="text-capitalize">
          {{ this.$store.getters.selectedStat.replace('_stat', '')}}
          <v-spacer></v-spacer>
          <v-btn outlined>
            Share
            <v-icon>{{icon.share}}</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text>
          <table-stat :item="item"></table-stat>
        </v-card-text>
      </v-card>
    </v-container>
    <v-container>
      <v-card>
        <v-card-title class="text-capitalize">
          {{ this.$store.getters.selectedStat.replace('_stat', '')}}s Chart
          <v-spacer></v-spacer>
          <v-btn outlined>
            Share
            <v-icon>{{icon.share}}</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text>
          <table-chart :item="this.$store.getters.stats.map(v => this.$store.getters.selectedStat === 'temperature' ? v.temperature : v.humidite)" :label="this.$store.getters.stats.map(v => new Date(v.date).toLocaleDateString())" :name="$store.getters.selectedStat.replace('_stat', '')"></table-chart>
        </v-card-text>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import {mdiShare} from "@mdi/js";
import tableStat from "@/components/tableStat";
import tableChart from "@/components/tableChart";

export default {
  name: "Tables",
  props: ['item'],
  components: {
    tableStat,
    tableChart
  },
  data() {
    return {
      Date: Date,
      icon: {
        share:mdiShare
      }
    }
  }
}
</script>

<style scoped>

</style>