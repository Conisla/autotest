<template>
    <div>
        <p>TABLEVIEW</p>
        <button type="button" @click="fetchData">GET ALL GAMES</button>
        <button type="button" @click="getGameData(id)">GET ALL GAMES</button>
        <button type="button" @click="createGameData()">GET ALL GAMES</button>
        <button type="button" @click="upGameData()">GET ALL GAMES</button>
        <button type="button" @click="delGameData()">GET ALL GAMES</button>

    </div>
</template>

<script>
import GameService from '@/services/api.js'

export default {
    name:'TableView',
    methods: {
        async fetchData() {
            try {
                // console.log(GameService)
                const response = await GameService.getGames()
                // console.log(response) // Afficher les données de réponse dans la console
            } catch (error) {
                console.error(error) // Gérer les erreurs de requête ici
            }
        },

        async getGameData(id) {
            try {
                const response = await GameService.getGame(id)
                console.log(response) // Afficher les données de réponse dans la console
            } catch (error) {
                console.error(error) // Gérer les erreurs de requête ici
            }
        },
        async createGameData(id) {
            try {
                const response = await GameService.createGame(id)
                console.log(response) // Afficher les données de réponse dans la console
            } catch (error) {
                console.error(error) // Gérer les erreurs de requête ici
            }
        },

        async upGameData(id) {
            try {
                const response = await GameService.updateGame(id)
                console.log(response) // Afficher les données de réponse dans la console
            } catch (error) {
                console.error(error) // Gérer les erreurs de requête ici
            }
        },

        async delGameData(id) {
            try {
                const response = await GameService.deleteGame(id)
                console.log(response) // Afficher les données de réponse dans la console
            } catch (error) {
                console.error(error) // Gérer les erreurs de requête ici
            }
        }


    },
    async mounted(){
        this.fetchData()
    }
    
}
</script>