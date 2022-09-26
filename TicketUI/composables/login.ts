export const Ultra_login = async (username :any, password :any) => {
    const response = await $fetch('http://127.0.0.1:8000/api/api-token/', { method: 'POST', body: { 'username':username, 'password':password } })
    // console.log(Object.values(response))
    
return Object.values(response)
  }