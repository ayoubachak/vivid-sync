export const google_login = async () =>{
    console.log("Google Login")
    window.location.href = "/api/auth/google-oauth2/login/redirect/"

}
export const facebook_login = async () =>{
    console.log("Facebook Login")
    window.location.href = "/accounts/login/google-oauth2/login/redirect/"
}
