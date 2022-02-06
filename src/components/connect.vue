<template>
  <v-dialog width="250" v-model="$store.getters.connect" persistent>
    <v-card width="250">
      <v-card-title class="mb-4">
        <v-row justify="center">
        Connexion
        </v-row>
      </v-card-title>
      <v-card-text>
        <v-form ref="connect" v-model="valid" lazy-validation>
          <v-row justify="center">
            <v-col class="pb-0" cols="10"><v-text-field v-model="emailInput" required label="Email"></v-text-field></v-col>
            <v-col cols="10"><v-text-field @click:append="show = !show" :type="show ? 'text' : 'password'" :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'" v-model="passwordInput" required label="Password"></v-text-field></v-col>
          </v-row>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn outlined class="font-weight-bold" color="red lighten-2" v-on:click="cancel">Cancel</v-btn>
        <v-btn outlined class="font-weight-bold" v-on:click="validate(emailInput, passwordInput)">Connect</v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "connect",
  data() {
    return {
      valid: true,
      show: false,
      emailInput: "",
      passwordInput: ""
    }
  },
  methods: {
    validate(email, mdp) {
      if (this.$refs.connect.validate()) {
        this.$store.dispatch('getUsers')
        setTimeout(() => {
          console.log(this.$store.getters.users)
          this.$store.getters.users.find(v => v.email === email && v.mot_de_passe === mdp)
        }, 2000)
      }
    },
    cancel() {
      this.$store.dispatch('connect', false)
    }
  }
}
</script>

<style scoped>

</style>