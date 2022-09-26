export const ultra_username = async () => {
    if(process.client){
      return await localStorage.getItem("username")
  }
}