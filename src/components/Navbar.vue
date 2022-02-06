<template>
  <v-toolbar color="black" max-height="55">
    <v-toolbar-title>
      <v-col>
        <v-row v-on:click="home" class="pointing" style="color: white; font-weight: lighter">
          <v-img class="mr-2" max-height="35" max-width="35" src="images/meteoLogo.png"></v-img>
          Meteous v1.1
        </v-row>
      </v-col>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
<!--      <p class="pt-5 mr-3" style="color: white"><v-icon class="pb-1" :color="$store.getters.espConnected ? 'green' : 'red'">{{icon.circle}}</v-icon> ESP</p>-->
      <v-menu class="mx-1" bottom min-width="200px" rounded offset-y>
        <template v-slot:activator="{ on }">
          <v-btn class="pt-3" small icon v-on="on" style="height: 52px !important; ">
            <v-avatar v-if="$store.getters.currentUser !== undefined" :color="$store.getters.currentUser.color" size="30">
              <span class="white--text text-caption text-capitalize">{{ $store.getters.currentUser.prenom[0] }} {{ $store.getters.currentUser.nom[0] }}</span>
            </v-avatar>
            <v-icon color="white" v-else>
              {{ icon.account }}
            </v-icon>
          </v-btn>
        </template>
        <v-card>
          <v-list-item-content class="justify-center">
            <div class="mx-auto text-center" v-if="$store.getters.currentUser !== undefined">
              <v-avatar :color="$store.getters.currentUser.color">
                      <span class="white--text text-h5">
                        {{ $store.getters.currentUser.prenom[0] }} {{ $store.getters.currentUser.nom[0] }}
                      </span>
              </v-avatar>
              <h3>{{ $store.getters.currentUser.prenom }} {{$store.getters.currentUser.nom}}</h3>
              <p class="text-caption mt-1">
                {{ $store.getters.currentUser.email }}
              </p>
              <v-divider class="my-3"></v-divider>
              <v-btn v-on:click="updateIt" depressed rounded text>
                Edit Account
              </v-btn>
              <v-divider class="my-3"></v-divider>
              <v-btn depressed rounded text v-on:click="disconnectUser">
                Disconnect
              </v-btn>
            </div>
            <div class="mx-auto text-center" v-else>
              <v-btn depressed rounded text v-on:click="connect">
                Connect
              </v-btn>
              <v-divider class="my-3"></v-divider>
              <v-btn depressed rounded text v-on:click="create">
                Create Account
              </v-btn>
            </div>
          </v-list-item-content>
        </v-card>
      </v-menu>
      <v-btn small icon class="mx-1">
        <v-icon color="white">{{ icon.vertical }}</v-icon>
      </v-btn>
    </v-toolbar-items>
    <v-menu v-if="!$vuetify.breakpoint.mdAndUp">
      <template v-slot:activator="{ on }">
        <v-btn icon small v-on="on">
          <v-app-bar-nav-icon style="color: white"></v-app-bar-nav-icon>
        </v-btn>
      </template>
      <v-icon slot="activator"></v-icon>
      <v-list>
        <v-list-item class="pa-0 ma-0 ml-8">
          <v-menu bottom min-width="200px" rounded offset-y>
            <template v-slot:activator="{ on }">
              <v-btn small icon v-on="on">
                <v-avatar v-if="$store.getters.currentUser !== undefined" :color="$store.getters.currentUser.color">
                  <span class="white--text text-caption text-capitalize">{{ $store.getters.currentUser.prenom[0] }} {{ $store.getters.currentUser.nom[0] }}</span>
                </v-avatar>
                <v-icon color="black" v-else>
                  {{ icon.account }}
                </v-icon>
              </v-btn>
            </template>
            <v-card>
              <v-list-item-content class="justify-center">
                <div class="mx-auto text-center" v-if="$store.getters.currentUser !== undefined">
                  <v-avatar :color="$store.getters.currentUser.color">
                      <span class="white--text text-h5">
                        {{ $store.getters.currentUser.prenom[0] }} {{ $store.getters.currentUser.nom[0] }}
                      </span>
                  </v-avatar>
                  <h3>{{ $store.getters.currentUser.prenom }} {{$store.getters.currentUser.nom}}</h3>
                  <p class="text-caption mt-1">
                    {{ $store.getters.currentUser.email }}
                  </p>
                  <v-divider class="my-3"></v-divider>
                  <v-btn v-on:click="updateIt" depressed rounded text>
                    Edit Account
                  </v-btn>
                  <v-divider class="my-3"></v-divider>
                  <v-btn depressed rounded text v-on:click="disconnectUser">
                    Disconnect
                  </v-btn>
                </div>
                <div class="mx-auto text-center" v-else>
                  <v-btn depressed rounded text v-on:click="connect">
                    Connect
                  </v-btn>
                  <v-divider class="my-3"></v-divider>
                  <v-btn depressed rounded text v-on:click="create">
                    Create Account
                  </v-btn>
                </div>
              </v-list-item-content>
            </v-card>
          </v-menu>
        </v-list-item>
<!--        <v-list-item>-->
<!--          <p class="pt-5" style="color: black"><v-icon class="pb-1" :color="$store.getters.espConnected ? 'green' : 'red'">{{icon.circle}}</v-icon> ESP</p>-->
<!--        </v-list-item>-->
      </v-list>
    </v-menu>
    <connect></connect>
    <create></create>
    <update></update>
  </v-toolbar>
</template>

<script>
import { mdiHeart, mdiMagnify, mdiDotsVertical, mdiAccount, mdiFlare } from '@mdi/js'
import update from "@/components/update";
import Connect from "@/components/connect";
import Create from "@/components/create";

export default {
  name: "Navbar",
  components: {Create, Connect, update},
  data() {
    return {
      icon: {
        heart: mdiHeart,
        magnify: mdiMagnify,
        vertical: mdiDotsVertical,
        account: mdiAccount,
        circle: mdiFlare
      }
    }
  },
  methods: {
    disconnectUser() {
      this.$store.dispatch("disconnect")
      console.log(this.$store.getters.currentUser)
    },
    create() {
      this.$store.dispatch('create', true)
    },
    home() {
      this.$router.push('/')
    },
    connect() {
      this.$store.dispatch('connect', true)
    },
    updateIt() {
      this.$store.dispatch('update', true)
    }
  },
}
</script>

<style scoped>

</style>