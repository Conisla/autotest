


import { describe, beforeEach, it, expect, vi, test} from 'vitest'

import { mount } from '@vue/test-utils'

import TableView from './TableView.vue'

import axios from 'axios'

// Création du mock pour axios

// Utilisation du mock dans vitest
vi.mock('axios')

describe('GameService', () => {
  it('getGames', async () => {

    // Montage du composant
    const wrapper = mount(TableView)
    const wrapdata = await wrapper.vm.fetchData()
    const gameMock = [ { id_jeu: '2', name: 'Jeu 2' }, { id_jeu: '3', name: 'Jeu 3' } ] 
    console.warn(axios)

    // Attendre que les promesses se résolvent et que Vue ait terminé sa mise à jour
    await wrapper.vm.$nextTick()

    // Vérification que axios.get a bien été appelé
    // expect(mockAxios.get).toHaveBeenCalledTimes(1)

    expect(wrapdata).toStrictEqual(gameMock)
  })
})

// describe('GameService', () => {
//     let gameMock ;
//     test('makes a GET request to fetch GAMES', async () => {
//         gameMock = [ { id_jeu: '2', name: 'Jeu 2' }, { id_jeu: '3', name: 'Jeu 3' } ]
//         axios.get.mockResolvedValue({
//             data: gameMock,
//         })
//       })

//     it('getGames', async () => {
//       const wrapper = mount(TableView)
//       const wrapdata = await wrapper.vm.fetchData()
//       console.warn(wrapdata)

//     //   expect(axios.get).toHaveBeenCalledWith('http://localhost:8000/api/jeu')
//       expect(wrapdata).toStrictEqual(gameMock)
//     })


//   })

  
  
