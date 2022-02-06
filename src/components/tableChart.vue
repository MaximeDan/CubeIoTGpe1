<template>
  <div>
    <canvas id="chart3"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";

export default {
  name: "tableChart",
  props: ['name', 'item', 'label'],
  data() {
    return {
      planetChartData: {
        type: "line",
        data: {
          labels: this.label,
          datasets: [
            {
              label: this.name,
              data: this.item,
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

    const ctx = document.getElementById('chart3');
    new Chart(ctx, this.planetChartData);
  }
}
</script>