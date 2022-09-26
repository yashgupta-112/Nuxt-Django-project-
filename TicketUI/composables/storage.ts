export const ultra_auth = async () => {
    if(process.client){
      return await localStorage.getItem("authToken")
  }
}