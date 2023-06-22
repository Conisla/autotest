<template>
    <div>


    </div>
</template>

<script>
import GameService from '@/services/api.js'

export default {
    methods: {
        async fetchData() {
            try {
                return await GameService.getGames()
                .then(response => {return response})
                
            } catch (error) {
                console.error(error);
            }
        },
    }
}
</script>