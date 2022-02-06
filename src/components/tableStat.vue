<template>
  <v-data-table
      :headers="headers"
      :items="this.$store.getters.stats.map(v => ({date: `${ new Date(v.date).toLocaleDateString()}`, hour: `${new Date(v.date).getHours()}:00`, data: `${v[this.$store.getters.selectedStat]}${this.$store.getters.selectedStat === 'temperature' ? '°C' : '%'}`}))"
      :sort-by="['Value']"
      items-per-page="5"
      class="elevation-1"
  ></v-data-table>
</template>

<script>
export default {
  name: "table",
  methods: {

  },
  data() {
    return {
      Date: Date,
      headers: [
        {
          text: 'Date',
          align: 'start',
          sortable: false,
          value: 'date',
        },
        {text: 'Hour', sortable:false, value: 'hour'},
        {text: 'Value', value: 'data'},
      ]
    }
  },
  mounted() {

  }
}
</script>

<style scoped>

</style>