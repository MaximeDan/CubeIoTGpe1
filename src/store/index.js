import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        users:[],
        stats:[{date: new Date(2022, 2,3,2),humidite: 6,temperature: 1}, {date: new Date(2022, 2,3,3),humidite: 7,temperature: 2}, {date: new Date(2022, 2,3,4),humidite: 8,temperature: 3}, {date: new Date(2022, 2,3,5),humidite: 9,temperature: 4}, {date: new Date(2022, 2,3,6),humidite: 10,temperature: 5}, {date: new Date(2022, 2,3,7),humidite: 11,temperature: 6}, {date: new Date(2022, 2,3,8),humidite: 12,temperature: 7}, {date: new Date(2022, 2,3,9),humidite: 13,temperature: 8}, {date: new Date(2022, 2,3,10),humidite: 21, farenheit: 20 , temperature: 9}],
        currentUser: { nom: "Morisseau", prenom: "Ugo", email: 'ugo.morisseau@gmail.com', color: 'red', mot_de_passe:'123', type:"utilisateur" },
        connect: false,
        create: false,
        espConnected: false,
        selectedStat: "temperature",
        update: false,
    },
    getters: {
        users: state => state.users,
        stats: state => state.stats,
        currentUser: state => state.currentUser,
        connect: state => state.connect,
        create: state => state.create,
        espConnected: state => state.espConnected,
        selectedStat: state => state.selectedStat,
        update: state => state.update
    },
    mutations: {
        setUsers(state, users){
            state.users = users
        },
        setStats(state, stats){
            state.stats = stats
        },
        setCurrentUser(state, currentUser){
            state.currentUser = currentUser
        },
        setConnect(state, connect){
            state.connect = connect
        },
        setCreate(state, create) {
            state.create = create
        },
        setUpdate(state, update) {
            state.update = update
        },
        isConnected(state, espConnected) {
            state.espConnected = espConnected
        },
        setSelected(state, select) {
            state.selectedStat = select
        }
    },
    actions: {
        async getUsers(state) {
            const users = await axios.get('http://192.168.43.60:5000/api/v1/utilisateurs/')
            state.commit("setUsers", users.data)
        },
        async addUser(state, user) {
            await axios.post('http://192.168.43.60:5000/api/v1/user/ajouter/', user)
        },
        async udUser(state, editedItem) {
            await axios.put('http://192.168.43.60:5000/api/v1/user/modifier/', editedItem)
        },
        async rmUser(state, id) {
            await axios.delete('http://192.168.43.60:5000/api/v1/user/supprimer/', id)
        },

        async getStats(state) {
            const stats = await axios.get('http://192.168.43.60:5000/api/v1/donnees/')
            state.commit("setStats", stats.data)
        },
        async addStat(state, stat) {
            await axios.post(`http://192.168.43.60:5000/api/v1/donnee/ajouter/`, stat)
        },
        async udStat(state, editedItem) {
            await axios.put('http://192.168.43.60:5000/api/v1/donnee/modifier/', editedItem)
        },
        async rmStat(state, id) {
            await axios.delete('http://192.168.43.60:5000/api/v1/donnee/supprimer/', id)
        },

        async getCapteurs(state) {
            const stats = await axios.get('http://192.168.43.60:5000/api/v1/capteurs/')
            state.commit("setStats", stats.data)
        },
        async addCapteur(state, stat) {
            await axios.post(`http://192.168.43.60:5000/api/v1/capteur/ajouter/`, stat)
        },
        async udCapteur(state, editedItem) {
            await axios.put('http://192.168.43.60:5000/api/v1/capteur/modifier/', editedItem)
        },
        async rmCapteur(state, id) {
            await axios.delete('http://192.168.43.60:5000/api/v1/capteur/supprimer/', id)
        },
        
        async getCurrentUser(state, user) {
          const currentUser = await axios.get('http://192.168.43.60:5000/user/get-currentUser/', user)
          state.commit("setCurrentUser", currentUser.data)
        },
        async isEspConnected(state) {
            const isConnected = await axios.get('http://192.168.43.60:5000/esp/connected')
            state.commit("isConnected", isConnected)
        },
        
        async setSelectedStat(state, select) {
            state.commit("setSelected", select)
        },
        async update(state, bool) {
            console.log('im here')
            state.commit("setUpdate", bool)
        },
        async disconnect(state) {
            state.commit("setCurrentUser", undefined)
        },
        async create(state, bool) {
            state.commit("setCreate", bool)
        },
        async connect(state, bool) {
            state.commit("setConnect", bool)
        },
    },
    modules: {
    }
})
