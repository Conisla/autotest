export const get = vi.fn(
    () => new Promise.resolve({
        data: [ { id_jeu: '2', name: 'Jeu 2' }, { id_jeu: '3', name: 'Jeu 3' } ] 
    }))
  

  