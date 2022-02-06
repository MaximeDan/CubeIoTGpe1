<template>
  <div>
    <canvas id="chart2"></canvas>
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
              label: "Température",
              data: this.$store.getters.stats.slice(this.$store.getters.stats.length - 6, this.$store.getters.stats.length).map(v => v.temperature),
              backgroundColor: "rgba(54,73,93,0)",
              borderColor: "#36495d",
              borderWidth: 3
            },
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
                  labelString: '°C'
                },
                ticks: {
                  beginAtZero: true,
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

    const ctx = document.getElementById('chart2');
    new Chart(ctx, this.planetChartData);
  }
}
</script>