<template>
    <div class="relative rounded-xl overflow-hidden ">
        <img :src="image" class="object-cover w-full h-full -z-10" alt="">
        <div class="absolute top-0 h-full w-full bg-gradient-to-t from-black/50 p-3 flex flex-col justify-between">
            
                <a href="#" class="p-2.5 bg-gray-800/80 rounded-lg text-white self-end hover:bg-red-600/80">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
                    </svg>
                </a>
            
            <div class="self-center flex flex-col items-center space-y-2">
                <span class="capitalize text-white font-medium drop-shadow-md"><slot /></span>
                <span class="text-gray-300 text-xs">+{{ movies }} Movies</span>

            </div>
        </div>
    </div>  

    
</template>

<script setup lang="ts">
    const props = defineProps({
        image: {
            type: String,
            required: true,
        },
        movies:{
            type: Number,
            required: true,
        }
    });

    const { image, movies } = props;
</script>
