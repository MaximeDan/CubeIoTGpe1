<template>
  <div id="meteoStats">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-card outlined>
            <v-card-title>
              Last Data
              <v-spacer></v-spacer>
              <v-btn outlined>
                Share
                <v-icon>{{icon.share}}</v-icon>
              </v-btn>
            </v-card-title>
            <v-card-text>
              <v-row justify="center">
                <v-slide-group show-arrows>
                  <v-slide-item class="mx-1 my-2" v-for="(stat, index) in items" :key="index">
                    <v-scale-transition>
                      <v-card v-on:click="showTables(stat.prop)" v-if="showStats" height="90" width="150">
                        <v-card-title>
                          <p class="pa-0 ma-0 text-caption font-weight-light">{{ stat.name }}</p>
                          <v-spacer></v-spacer>
                          <v-btn x-small outlined v-on:click="stat.like = !stat.like">
                            <v-icon :color="stat.like ? 'blue' : 'black'" size="15">{{icon.heart}}</v-icon>
                          </v-btn>
                        </v-card-title>
                        <v-row justify="center">
                          <v-col cols="12">
                            <v-row class="pt-2">
                              <v-col class="pa-0 ml-3" cols="6">
                                <p v-if="stat.data === undefined" class="text-h4 pa-0 ma-0 pl-3" :style="stat.limit[1] !== '-' ? lastStat[stat.prop] >= stat.limit[0] ? 'color: #0095b8' : 'color: #47b784' : lastStat[stat.prop] >= stat.limit[0] ? 'color: green' : 'color: #c1edfe'">{{Math.round(lastStat[stat.prop])}}{{ stat.symbole }}</p>
                                <p v-else class="text-h4 pa-0 ma-0 pl-3" :style="stat.limit[1] !== '-' ? Math.round(getStat(stat.data)) >= stat.limit[0] ? 'color: #0095b8' : 'color: #47b784' : Math.round(getStat(stat.data)) >= stat.limit[0] ?  'color: green' : 'color: #c1edfe'">{{Math.round(getStat(stat.data))}}{{ stat.symbole }}</p>
                              </v-col>
                              <v-spacer></v-spacer>
                              <v-col class="pa-0 mr-5" cols="3">
                                <v-img v-if="stat.data === undefined" class="pb-0 mb-0" height="35" width="35" :src="stat.limit[1] !== '-' ? lastStat[stat.prop] >= stat.limit[0] ? 'images/drop.png' : 'images/thermometer.png' : lastStat[stat.prop] <= stat.limit[0] ? 'images/snowflake.png' : 'images/sun.png'"></v-img>
                                <v-img v-else class="pb-0 mb-0" height="35" width="35" :src="stat.limit[1] !== '-' ? Math.round(getStat(stat.data)) >= stat.limit[0] ? 'images/drop.png' : 'images/thermometer.png' : Math.round(getStat(stat.data)) <= stat.limit[0] ? 'images/snowflake.png' : 'images/sun.png'"></v-img>
                              </v-col>
                            </v-row>
                          </v-col>
                        </v-row>
                      </v-card>
                    </v-scale-transition>
                  </v-slide-item>
                </v-slide-group>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script defer>
import { mdiShare, mdiHeart } from '@mdi/js'

export default {
  name: "meteoStats",
  data() {
    return {
      math: Math,
      icon: {
        share: mdiShare,
        heart: mdiHeart
      },
      lastStat: {},
      items: [
        {name: "Température" , prop: 'temperature', limit: [0, '-'], symbole: '°C', like: false},
        {name: "Humidité", prop:'humidite', limit: [50, '+'], symbole: '%', like:false},
        {name: "T. Fahrenheit", prop:'farenheit', limit: [0, '-'], symbole: '°F', like:false},
        {name: "H. Min", prop:'humidite', limit: [50, '+'], symbole: '%', like:false, data: 'humiMin'},
        {name: "T. Max", prop:'temperature', limit: [0, '-'], symbole: '°C', like:false, data: 'tempMax'},
        {name: "T. Min", prop:'temperature', limit: [0, '-'], symbole: '°C', like:false, data: 'tempMin'},
        {name: "H. Max", prop:'humidite', limit: [50, '+'], symbole: '%', like:false, data: 'humiMax'},
      ],
      stats: [{id: 0, temperature: 0, humidite: 0, date: new Date()}],
      showStats: false,
    }
  },
  methods: {
    setStat() {
      this.stats = this.$store.getters.stats
      this.lastStat = this.stats[this.stats.length - 1]
    },
    getStat(item) {
      switch (item) {
        case 'humiMax':
          return this.humiMax()
        case 'humiMin':
          return this.humiMin()
        case 'tempMax':
          return this.tempMax()
        case 'tempMin':
          return this.tempMin()
      }
    },
    showTables(item) {
      this.$store.dispatch("setSelectedStat", item)
      this.$router.push('/table')
    },
    tempMax() {
      let test = this.$store.getters.stats.map(v => Number(v.temperature))
      return Math.max(...test)
    },
    tempMin() {
      let test = this.$store.getters.stats.map(v => v.temperature)
      return Math.min(...test)
    },

    humiMax() {
      let test = this.$store.getters.stats.map(v => Number(v.humidite))
      return Math.max(...test)
    },
    humiMin() {
      let test = this.$store.getters.stats.map(v => Number(v.humidite))
      return Math.min(...test)
    },
    humiMoy() {
     return 0
    },
  },
  mounted() {
    setInterval(() => {this.setStat()}, 1000)
    setTimeout(() => { this.showStats = true }, 500)
  }
}
</script>

<style scoped>

</style>