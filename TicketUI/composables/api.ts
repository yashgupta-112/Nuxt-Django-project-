export const Ultra_request = async (username :any, password :any,email :any) => {
    const response = await $fetch('http://127.0.0.1:8000/signup', { method: 'POST', body: { 'username':username, 'password':password , 'email': email} })
    // console.log(Object.values(response))
    
return Object.values(response)
  }