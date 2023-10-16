import { defineStore } from 'pinia'

export const useApiResultsStore = defineStore('apiResults', {
  state: () => ({
    results: null as any,
  }),
  actions: {
    setResults(results: any) {
      this.results = results
    },
  },
})
