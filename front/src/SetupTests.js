import { afterAll, afterEach, beforeAll } from 'vitest'
import { setupServer } from 'msw/node'
import { rest } from 'msw'
import "whatwg-fetch"

const mockLists = {
    data:[ 
        { id_jeu: '1', name: 'Jeu 1' },
        { id_jeu: '2', name: 'Jeu 2' } 
        ]
    }

export const restHandlers = [
  rest.get('http://127.0.0.1:8000/api', (req, res, ctx) => {
    return res(ctx.status(200), ctx.json(mockLists))
  }),
]

const server = setupServer(...restHandlers)

// Start server before all tests
beforeAll(() => server.listen({ onUnhandledRequest: 'error' }))

//  Close server after all tests
afterAll(() => server.close())

// Reset handlers after each test `important for test isolation`
afterEach(() => server.resetHandlers())