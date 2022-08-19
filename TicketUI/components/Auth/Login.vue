<template>
  <div class="section">
    <div class="container">
      <div class="row full-height justify-content-center">
        <div class="col-12 text-center align-self-center py-5">
          <div class="section pb-5 pt-5 pt-sm-2 text-center">
            <h6 class="mb-0 pb-3">
              <span id="option-heading">Log In </span
              ><span id="option-heading">Sign Up</span>
            </h6>
            <input
              class="checkbox"
              type="checkbox"
              id="reg-log"
              name="reg-log"
            />

            <label for="reg-log"></label>
            <div class="card-3d-wrap mx-auto">
              <div class="card-3d-wrapper">
                <div class="card-front">
                  <div class="center-wrap">
                    <div class="section text-center">
                      <h4 id="Auth-heading" class="mb-4 pb-3">Log In</h4>
                      <div class="form-group">
                        <input
                          type="email"
                          name="logemails"
                          class="form-style"
                          placeholder="Your Username"
                          id="logemails"
                          autocomplete="off"
                          v-model.trim="login_username"
                        />
                        <i class="input-icon uil uil-at"></i>
                      </div>
                      <div class="form-group mt-2">
                        <input
                          type="password"
                          name="logpass"
                          class="form-style"
                          placeholder="Your Password"
                          id="logpass"
                          autocomplete="off"
                          v-model.trim="login_password"
                        />
                        <i class="input-icon uil uil-lock-alt"></i>
                      </div>
                      <a href="#" @click="login" class="btn mt-4">submit</a>
                    </div>
                  </div>
                </div>
                <div class="card-back">
                  <div class="center-wrap">
                    <div class="section text-center">
                      <h4 id="Auth-heading" class="mb-4 pb-3">Sign Up</h4>
                      <div class="form-group">
                        <input
                          type="text"
                          name="logname"
                          class="form-style"
                          placeholder="Your Username"
                          id="logname1"
                          autocomplete="off"
                          v-model.trim="signup_username"
                        />
                        <i class="input-icon uil uil-user"></i>
                      </div>
                      <div class="form-group mt-2">
                        <input
                          type="email"
                          name="logemail1"
                          class="form-style"
                          placeholder="Your Email"
                          id="logemail"
                          autocomplete="off"
                          v-model.trim="signup_email"
                        />
                        <i class="input-icon uil uil-at"></i>
                      </div>
                      <div class="form-group mt-2">
                        <input
                          type="password"
                          name="logpass1"
                          class="form-style"
                          placeholder="Your Password"
                          id="logpasss"
                          autocomplete="off"
                          v-model.trim="signup_password"
                        />
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

const login_username = ref("");
const login_password = ref("");

const signup_username = ref("");
const signup_password = ref("");
const signup_email = ref("");

function signup(){
  console.log(process.client,process.server)
}


</script>