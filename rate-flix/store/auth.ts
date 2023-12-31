// store/auth.ts

import { defineStore } from 'pinia';

interface UserLoginPayloadInterface {
  email: string;
  password: string;
}

interface UserRegisterPayloadInterface {
  email: string;
  password: string;
  name: string;
}

const BaseURL = "http://localhost:8000/api/auth/"

export const useAuthStore = defineStore('auth', {
  state: () => ({
    authenticated: false,
    loading: false,
  }),
  actions: {
    async authenticateUser({ email, password }: UserLoginPayloadInterface) {
      // useFetch from nuxt 3
      const { data, pending }: any = await useFetch(BaseURL + 'login/', {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: {
          email,
          password,
        },
      });
      this.loading = pending;

      if (data.value) {
        // Set the token expiration time
        const accessExpire = new Date().getTime() + 15 * 60 * 1000 // 15 min
        const token = useCookie('token', { expires: new Date(accessExpire) });

        const refreshTokenExpire = new Date().getTime() + 3 * 3600 * 1000 // 3 hours;
        const refreshToken = useCookie('refreshToken', { expires: new Date(refreshTokenExpire) });

        const user = useCookie('user');

        user.value = data?.value?.user;
        token.value = data?.value?.access;
        refreshToken.value = data?.value?.refresh;

        this.authenticated = true;
      }
    },

    async registerUser({email, password, name}: UserRegisterPayloadInterface) {
        // useFetch from nuxt 3
        const { data, pending }: any = await useFetch(BaseURL + 'register/', {
          method: 'post',
          headers: { 'Content-Type': 'application/json' },
          body: {
            email,
            password,
            name
          },
        });
        this.loading = pending;
  
        if (data.value) {
          return data.value
        }
    },

    logUserOut() {
      const token = useCookie('token'); // useCookie new hook in nuxt 3
      const user = useCookie('user');
      const refreshToken = useCookie('refreshToken');
      this.authenticated = false; // set authenticated  state value to false
      token.value = null; // clear the token cookie
      user.value = null
      refreshToken.value = null;
    },
  },
});