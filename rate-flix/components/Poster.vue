

<template>
    <div class="flex flex-col justify-between mt-4 bg-black/10 bg-blend-multiply rounded-3xl h-80 overflow-hidden bg-cover bg-center px-7 pt-4 pb-6 text-white"
        style="background-image: url('https://mazyar1128.github.io/tailwindcss-movie-dashboard/images/inception.jpg');" >

        <div class="bg-gradient-to-r from-black/30 to-transparent -mx-7 -mb-6 px-7 pb-6 pt-2 mt-auto">
            <span class="uppercase text-3xl font-semibold drop-shadow-lg "><slot /></span>
            <div class="mt-2">
                <a href="#" v-for="(genre, index) in genres" :key="index" class="text-gray-200 text-xs">{{genre}}, </a>
                
            </div>
            <div class="mt-4 flex space-x-3 items-center">
                <a href="#" class="px-5 py-2.5 bg-red-600 hover:bg-red-700 text-white rounded-lg text-xs inline-block">Watch</a>
                <a href="#" class="p-2.5 bg-gray-800/80 rounded-lg hover:bg-red-600">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
                    </svg>
                </a>
            </div>
        </div>
    </div>

</template>

<script setup lang="ts">
    const props = defineProps({
        genres: {
            type: Array as PropType<string[]>,
            required: true,

        },
    });
</script>
