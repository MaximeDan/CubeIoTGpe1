<template>
  <v-dialog width="500" v-model="$store.getters.update" persistent>
    <v-card width="500">
      <v-card-title>
        <v-spacer></v-spacer>
        <v-avatar :color="user.color" size="50">
          <span class="text-h5 pa-0 ma-0 text-capitalize" style="color: white" v-if="user.prenom.length >= 1">{{ user.prenom[0] }}</span>
          <span class="text-h5 pa-0 ma-0 text-capitalize" style="color: white" v-if="user.nom.length >= 1"> {{ user.nom[0] }}</span>
        </v-avatar>
        <v-spacer></v-spacer>
      </v-card-title>
      <v-card-text class="pb-0">
        <v-row class="mt-3">
          <v-spacer></v-spacer>
          <v-col cols="6">
            <v-row>
              <v-col v-for="(color, index) in colors" :key="index">
                <v-row justify="center">
                  <v-card v-on:click="user.color = color" height="25" width="25" :color="color"></v-card>
                </v-row>
              </v-col>
            </v-row>
          </v-col>
          <v-spacer></v-spacer>
        </v-row>
        <v-form ref="create" v-model="valid" lazy-validation>
          <v-row>
            <v-col cols="6"><v-text-field v-model="user.prenom" :rules="[v => !!v || 'Firstname is required',v => (v && v.length <= 25 && v.length >= 2) || 'Firstname must be valid']" required label="Firstname"></v-text-field></v-col>
            <v-col cols="6"><v-text-field v-model="user.nom" :rules="[v => !!v || 'Lastname is required',v => (v && v.length <= 25 && v.length >= 2) || 'Lastname must be valid']" required label="Lastname"></v-text-field></v-col>
            <v-col cols="6"><v-text-field @click:append="show = !show" :type="show ? 'text' : 'password'" :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'" v-model="user.mot_de_passe" required :rules="[v => !!v || 'Password is required',v => (v && v.length >= 8) || 'Password must be valid']" label="Password"></v-text-field></v-col>
            <v-col cols="6"><v-text-field @click:append="show1 = !show1" :type="show1 ? 'text' : 'password'" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" required :rules="[v => !!v || 'Verification is required', v => v === user.mot_de_passe]" label="Password verify"></v-text-field></v-col>
            <v-col cols="12"><v-text-field v-model="user.email" required :rules="rulesEmail" outlined label="Email"></v-text-field></v-col>
          </v-row>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn v-on:click="cancel">Cancel</v-btn>
        <v-spacer></v-spacer>
        <v-btn v-on:click="validate">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "update",
  data() {
    return {
      user: JSON.parse(JSON.stringify(this.$store.getters.currentUser)),
      colors: ['purple', 'red', 'blue', 'green', 'black'],
      valid: false,
      show: false,
      show1: false,
      rulesEmail: [
        value => !!value || 'E-mail requis.',
        value => (value || '').length <= 30 || 'Max 30 characters',
        value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || 'E-mail invalide.'
        },
      ]
    }
  },
  methods: {
    validate() {
      if (this.$refs.create.validate()) {
        this.$store.dispatch('udUser', this.user)
        this.$store.dispatch('update', false)
      }
    },
    cancel() {
      this.user = JSON.parse(JSON.stringify(this.$store.getters.currentUser))
      this.$store.dispatch('update', false)
    }
  }
}
</script>

<style scoped>

</style>