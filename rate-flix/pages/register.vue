
<template>
    <div class="bg-gradient-to-tr from-indigo-400 to-rose-800 h-screen w-full flex justify-center items-center">
        <div class="w-full bg-cyan-800 sm:w-1/2 md:w-9/12 lg:w-1/2 shadow-md flex flex-col md:flex-row items-center mx-5 sm:m-0 rounded">
          <div class="w-full md:w-1/2 hidden md:flex flex-col justify-center items-center text-white">
            <h1 class="text-3xl">Welcome to</h1>
            <p class="text-5xl font-extrabold">RateFlix <i>!</i></p>
          </div>
          <div class="bg-white w-full md:w-1/2 flex flex-col items-center py-32 px-8">
            <h3 class="text-3xl font-bold text-blue-700 mb-4">
              REGISTER
            </h3>
            <form action="#" class="w-full flex flex-col justify-center">
              <div class="mb-4">
                <input type="email" placeholder="Email" v-model="user.email" class="w-full p-3 rounded border placeholder-gray-400 focus:outline-none focus:border-blue-700" />
              </div>
              <div class="mb-4">
                <input type="text" placeholder="Name" v-model="user.name" class="w-full p-3 rounded border placeholder-gray-400 focus:outline-none focus:border-blue-700" />
              </div>
              <div class="mb-4 flex">
                <input type="password" placeholder="Password" v-model="user.password" class="w-full p-3 rounded border placeholder-gray-400 focus:outline-none focus:border-blue-700" />
                <input type="password" v-model="password2" placeholder="Repeat" class="w-full p-3 ml-3 rounded border placeholder-gray-400 focus:outline-none focus:border-blue-700" />
              </div>



              <button @click.prevent="register" class="bg-blue-700 font-bold text-white focus:outline-none rounded p-3">
                Submit
              </button>
            </form>
            <div class="mt-4 flex items-center w-full justify-between">
                    <span class="border-b w-1/5 md:w-1/4"></span>
                    <NuxtLink to="/login" class="text-xs text-gray-500 uppercase">or login</NuxtLink>
                    <span class="border-b w-1/5 md:w-1/4"></span>
            </div>
          </div>
        </div>
      </div>
</template>
    
    
<script lang="ts" setup>
    import { ref } from 'vue';
    import { useRouter } from 'vue-router';
    import { useAuthStore } from '~/store/auth';

    const { registerUser, authenticateUser } = useAuthStore();
    const { authenticated } = storeToRefs(useAuthStore());

    const user = ref({
        email: '',
        password: '',
        name: '',
    });

    const password2 = ref('');
    const router = useRouter();

    const register = async () => {
    if (password2.value === user.value.password) {
        const IsRegistered = await registerUser(user.value);
      
        if (IsRegistered){
            const LoginUser = ref({
                email:user.value.email,
                password:user.value.password
            });

            await authenticateUser(LoginUser.value);

        } else {
            alert("Please Try Again.");
        }
        
       if(authenticated){
            router.push('/');
       }


    } else {
        alert("Password and its repeat do not match");
    }
    };
</script>