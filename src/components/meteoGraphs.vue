<template>
  <div id="meteoGraphs">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-card outlined>
            <v-card-title>
              Chart
              <v-spacer></v-spacer>
              <v-btn outlined>
                Share
                <v-icon>{{icon.share}}</v-icon>
              </v-btn>
            </v-card-title>
            <v-card-text>
              <v-row>
                <v-col cols="12" md="6">
                  <chart-temp-rature/>
                </v-col>
                <v-col cols="12" md="6">
                  <chartHumidite></chartHumidite>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import {mdiShare} from "@mdi/js";
import chartTempRature from "@/components/chartTempérature";
import chartHumidite from "@/components/chartHumidite";

export default {
  name: "meteoGraphs",
  components: {
    chartTempRature,
    chartHumidite
  },
  data() {
    return {
      icon: {
        share: mdiShare,
      }
    }
  }
}
</script>

<style scoped>

</style>