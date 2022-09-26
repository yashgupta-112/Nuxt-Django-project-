<template>
  <div class="section">
    <div class="container">
      <div class="row full-height justify-content-center">
        <div class="col-12 text-center align-self-center py-5">
          <div class="section pb-5 pt-5 pt-sm-2 text-center">
            <h6 class="mb-0 pb-3">
              <span id="option-heading">Log In </span><span id="option-heading">Sign Up</span>
            </h6>
            <input class="checkbox" type="checkbox" id="reg-log" name="reg-log" />

            <label for="reg-log"></label>
            <div class="card-3d-wrap mx-auto">
              <div class="card-3d-wrapper">
                <div class="card-front">
                  <div class="center-wrap">
                    <div class="section text-center">
                      <h4 id="Auth-heading" class="mb-4 pb-3">Log In</h4>
                      <div v-if="login_user" class="alert alert-success" role="alert">
                        <h6>Login successful</h6>
                      </div>
                      <div v-if="invalid_login" class="alert alert-danger" role="alert">
                        <h6>{{ error_message[0] }}</h6>
                      </div>
                      <div class="form-group">
                        <input type="email" name="logemails" class="form-style" placeholder="Your Username"
                          id="logemails" autocomplete="off" v-model.trim="login_username" />
                        <i class="input-icon uil uil-at"></i>
                      </div>
                      <div class="form-group mt-2">
                        <input type="password" name="logpass" class="form-style" placeholder="Your Password"
                          id="logpass" autocomplete="off" v-model.trim="login_password" />
                        <i class="input-icon uil uil-lock-alt"></i>
                      </div>
                      <a href="#" @click="login" class="btn mt-4">Login</a>
                    </div>
                  </div>
                </div>
                <div class="card-back">
                  <div class="center-wrap">
                    <div class="section text-center">
                      <h4 id="Auth-heading" class="mb-4 pb-3">Sign Up</h4>
                      <div v-if="user_created" class="alert alert-success" role="alert">
                        <h6>{{ temp_user[0] }} ,User has been created</h6>
                      </div>
                      <div v-if="invalid_detail" class="alert alert-danger" role="alert">
                        <h6>Password,Username length should be more than 3</h6>
                      </div>

                      <div class="form-group">
                        <input type="text" name="logname" class="form-style" placeholder="Your Username" id="logname1"
                          autocomplete="off" v-model.trim="signup_username" />
                        <i class="input-icon uil uil-user"></i>
                      </div>
                      <div class="form-group mt-2">
                        <input type="email" name="logemail1" class="form-style" placeholder="Your Email" id="logemail"
                          autocomplete="off" v-model.trim="signup_email" />
                        <i class="input-icon uil uil-at"></i>
                      </div>
                      <div class="form-group mt-2">
                        <input type="password" name="logpass1" class="form-style" placeholder="Your Password"
                          id="logpasss" autocomplete="off" v-model.trim="signup_password" />
                        <i class="input-icon uil uil-lock-alt"></i>
                      </div>
                      <a @click="signup" class="btn mt-4">submit</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url("../../assets/css/login.css");
</style>

<script setup>

  
const router = useRouter();
const login_username = ref("");
const login_password = ref("");
const user_created = ref(false);
const temp_user = ref("");
const invalid_detail = ref(false);

const signup_username = ref("");
const signup_password = ref("");
const signup_email = ref("");
const invalid_login = ref(false);
const login_user = ref(false);
const token = ref("");
const error_message = ref("");



async function signup() {
  const username = signup_username.value;
  const password = signup_password.value;
  const email = signup_email.value;
  // const response = await $fetch('http://127.0.0.1:8000/signup', { method: 'POST', body: { 'username':username, 'password':password , 'email': email} })
  if (username.length > 3 && password.length > 3) {
    const response = await Ultra_request(username, password, email);
    signup_username.value = "";
    signup_password.value = "";
    signup_email.value = "";
    temp_user.value = Object.values(response);
    user_created.value = true;
    console.log(Object.values(response), user_created.value);
    setTimeout(() => {
      user_created.value = false; //
    }, 3000);
  } else {
    invalid_detail.value = true;
    signup_username.value = "";
    signup_password.value = "";
    signup_email.value = "";
    setTimeout(() => {
      invalid_detail.value = false; //
    }, 3000);
  }
}

async function login() {
  const username = login_username.value;
  const password = login_password.value;
  
  // const response = await $fetch('http://127.0.0.1:8000/api/api-token/', { method: 'POST', body: { 'username':username, 'password':password } })
  if (username.length > 3 && password.length > 3) {
    const response = await Ultra_login(username, password).catch((error) => {
      invalid_login.value = true;
      setTimeout(() => {
        invalid_login.value = false;
      }, 4000);
      error_message.value = Object.values(error.data);
    });
    token.value = response[1];
    console.log(response)
    localStorage.setItem("authToken", response[1])
    localStorage.setItem("username", login_username.value)
    if (token.value != null) {
      login_user.value = true;
      //  setTimeout(() => {
       router.push({ path: "/sysadmin" })
    // }, 4000);
      
    } else {
      console.log("valid user");
    }
  }


}
</script>
