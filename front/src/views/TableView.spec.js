import {describe, it, expect, vi} from 'vitest'
import { mount, flushPromises } from '@vue/test-utils'
import TableView from './TableView.vue'
import axios from 'axios'

const mockLists = {
    data:[ 
        { id_jeu: '1', name: 'Jeu 1' },
        { id_jeu: '2', name: 'Jeu 2' } 
        ]
    }

vi.spyOn(axios, 'get').mockResolvedValue(mockLists)

test( 'GameService', async () => {
    const wrapper = mount(TableView);
    await wrapper.get('button').trigger('click')
    console.log(await wrapper.get('button'))
})