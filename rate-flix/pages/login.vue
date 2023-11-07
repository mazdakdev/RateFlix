
<template>
<div class="bg-gradient-to-tr from-indigo-400 to-rose-800 h-screen w-full flex justify-center items-center">
    <div class="w-full bg-cyan-800 sm:w-1/2 md:w-9/12 lg:w-1/2 shadow-md flex flex-col md:flex-row items-center mx-5 sm:m-0 rounded">
      <div class="w-full md:w-1/2 hidden md:flex flex-col justify-center items-center text-white">
        <h1 class="text-3xl">Welcome to</h1>
        <p class="text-5xl font-extrabold">RateFlix <i>!</i></p>
      </div>
      <div class="bg-white w-full md:w-1/2 flex flex-col items-center py-32 px-8">
        <h3 class="text-3xl font-bold text-blue-700 mb-4">
          LOGIN
        </h3>
        <form action="#" class="w-full flex flex-col justify-center">
          <div class="mb-4">
            <input type="email" v-model="user.email" placeholder="Email" class="w-full p-3 rounded border placeholder-gray-400 focus:outline-none focus:border-blue-700" />
          </div>
          <div class="mb-4">
            <input type="password" v-model="user.password" placeholder="Password" class="w-full p-3 rounded border placeholder-gray-400 focus:outline-none focus:border-blue-700" />
          </div>
          <button @click.prevent="login" class="bg-blue-700 font-bold text-white focus:outline-none rounded p-3">
            Submit
          </button>
        </form>
        <div class="mt-4 flex items-center w-full justify-between">
                <span class="border-b w-1/5 md:w-1/4"></span>
                <NuxtLink to="/register" class="text-xs text-gray-500 uppercase">or sign up</NuxtLink>
                <span class="border-b w-1/5 md:w-1/4"></span>
        </div>
      </div>
    </div>
  </div>
</template>


<script lang="ts" setup>
    import { storeToRefs } from 'pinia'; // import storeToRefs helper hook from pinia
    import { useAuthStore } from '~/store/auth'; // import the auth store we just created

    const { authenticateUser } = useAuthStore(); // use authenticateUser action from  auth store

    const { authenticated } = storeToRefs(useAuthStore()); // make authenticated state reactive with storeToRefs

    const user = ref({
        email: '', 
        password: '',
    });
    const router = useRouter();

    const login = async () => {
        await authenticateUser(user.value); // call authenticateUser and pass the user object
        // redirect to homepage if user is authenticated
        if (authenticated) {
            router.push('/');
        }
    };
</script>
