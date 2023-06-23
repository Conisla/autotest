import axios from 'axios'

const baseURL = 'http://localhost:8000/api';


const GameService = {
  // Méthode pour récupérer tous les jeux
  getGames() {
    try {
        return axios.get(baseURL + '/jeu')
    } catch (error) {
        console.log(error);
    }
  },

  // Méthode pour récupérer un jeu spécifique par son ID
  getGame(id) {
    return apiClient.get('/jeu/' + id)
  },

  // Méthode pour créer un nouveau jeu
  createGame(game) {
    return apiClient.post('/games', game)
  },

  // Méthode pour mettre à jour un jeu spécifique par son ID
  updateGame(id, game) {
    return apiClient.put('/jeu/' + id, game)
  },

  // Méthode pour supprimer un jeu spécifique par son ID
  deleteGame(id) {
    return apiClient.delete('/jeu/' + id)
  }
}

export default GameService;