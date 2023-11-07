<template>
    <button @click="btn">click me</button>
    Hello {{ useRequestEvent.n }}
</template>

<script setup lang="ts">
    import { authorizedFetch } from '~/utils/api';
    
    const btn = async ()=>{
        const respone = await authorizedFetch("http://localhost:8000/api/auth/me")
        console.log(respone.data)
    }
</script>