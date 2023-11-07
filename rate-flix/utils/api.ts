export async function authorizedFetch(url: string, options: any = {}) {
  const token = useCookie('token')

  if (token.value) {
    options.headers = {
      ...options.headers,
      Authorization: `Bearer ${token.value}`,
    };
    
  }
  return useFetch(url, options);
}
