<template>
  <div>
    <canvas id="chart"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";

export default {
  name: "charts",
  data() {
    return {
      planetChartData: {
        type: "line",
        data: {
          labels: this.$store.getters.stats.slice(this.$store.getters.stats.length - 6, this.$store.getters.stats.length).map(v => `${new Date(v.date).getHours()}:${new Date(v.date).getMinutes()}`),
          datasets: [
            {
              label: "Humidité",
              data:this.$store.getters.stats.slice(this.$store.getters.stats.length - 6, this.$store.getters.stats.length).map(v => v.humidite),
              backgroundColor: "rgba(71, 183,132,0)",
              borderColor: "#47b784",
              borderWidth: 3
            }
          ]
        },
        options: {
          responsive: true,
          lineTension: 1,
          scales: {
            yAxes: [
              {
                scaleLabel: {
                  display: true,
                  labelString: '%'
                },
                ticks: {
                  beginAtZero: false,
                  padding: 25
                }
              }
            ]
          }
        }
      }
    }
  },
  mounted() {
    const ctx = document.getElementById('chart');
    new Chart(ctx, this.planetChartData)

    // setInterval(() => {
    //   this.planetChartData.data.labels = this.$store.getters.stats.slice(this.$store.getters.stats.length - 6, this.$store.getters.stats.length).map(v => `${new Date(v.date).getHours()}:00`)
    //   this.planetChartData.data.datasets.data = this.$store.getters.stats.slice(this.$store.getters.stats.length - 6, this.$store.getters.stats.length).map(v => v.humidite)
    //   console.log(this.planetChartData.data.datasets.data)
    // }, 1000)
  }
}
</script>