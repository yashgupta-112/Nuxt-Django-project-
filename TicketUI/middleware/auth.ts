const token = await ultra_auth()
export default defineNuxtRouteMiddleware (()=>{
    
    if (token === null) {
        return navigateTo("/auth")
        // return abortNavigation()

      }

})