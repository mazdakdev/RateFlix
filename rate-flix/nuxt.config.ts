// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  modules: ['@nuxtjs/ionic'],
  css: [
    '~/assets/css/ionic.css',
    '~/assets/css/main.css',
  ],
  devtools: { enabled: true },
  ssr: false,
  ionic: {
    integrations: {
      //
    },
    css: {
      //
    },
    config: {
      //
    }
  },

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

})
