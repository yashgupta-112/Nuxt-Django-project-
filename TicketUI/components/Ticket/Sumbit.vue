<template>
  <div class="container">
    <h1 class="heading">Create New Support Request</h1>
    <div class="ticket-box">
      <div v-if="alert_ticket" class="alert alert-success" role="alert">
        Your ticket has been sumbited.
      </div>
      <form>
        <div class="row">
          <div class="col-6">
            <label for="exampleFormControlInput1" class="form-label"
              >Username</label
            >
            <input
              type="text"
              v-model.trim="user"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Username"
            />
          </div>
          <div class="col-6">
            <label for="exampleFormControlInput1" class="form-label"
              >Email address</label
            >
            <input
              type="email"
              v-model.trim="email"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Email"
            />
          </div>
        </div>

        <div class="row mt-2">
          <div class="col">
            <label for="exampleFormControlInput1" class="form-label"
              >Subject</label
            >
            <input
              type="text"
              v-model.trim="subject"
              class="form-control"
              id="exampleFormControlInput1"
            />
          </div>
        </div>

        <div class="row mt-3">
          <div class="col">
            <div class="form-floating">
              <select
                class="form-select"
                v-model.trim="department"
                id="floatingSelectGrid"
              >
                <option selected>Support</option>
                <option value="UCP">UCP</option>
                <option value="Sales">Sales</option>
              </select>
              <label for="floatingSelectGrid">Department</label>
            </div>
          </div>
          <div class="col-6">
            <div class="form-floating">
              <select
                class="form-select"
                v-model.trim="priority"
                id="floatingSelectGrid"
              >
                <option selected>Medium</option>
                <option value="Low">Low</option>
                <option value="High">High</option>
              </select>
              <label for="floatingSelectGrid">Priority</label>
            </div>
          </div>
        </div>

        <div class="row mt-4">
          <div class="form-floating">
            <textarea
              v-model.trim="message"
              class="form-control"
              placeholder="Leave a comment here"
              id="floatingTextarea2"
              style="height: 150px"
            ></textarea>
            <label for="floatingTextarea2">Add your message here...</label>
          </div>
        </div>

        <div class="d-grid gap-2 col-2 mt-4 mx-auto">
          <button @click="sumbit" class="btn btn-primary" type="button">
            Sumbit
          </button>
        </div>
      </form>
    </div>

    <hr>
<ul class="list-group bg-dark" v-for="res in guide" :key="res.title">
  <li class="list-group-item mb-2" v-if="message.match(res.title)"> <a :href=res.url target="_blank">{{res.url}}</a></li>
</ul>
  </div>
  <br>
</template>

<style scoped>
@import url("../../assets/css/sysadmin.css");
</style>

<script setup>
const nuxtApp = useNuxtApp();
const user = ref("");
const email = ref("");
const subject = ref("");
const department = ref("");
const priority = ref("");
const message = ref("");
const guide = ref("");
const search_query = ref("");
const alert_ticket = ref(false);
if (process.client) {
  user.value = localStorage.getItem("username");
}

const { data } = await useAsyncData("count", () =>
  $fetch("http://127.0.0.1:8000/email")
);



async function guides() {

  const response = await $fetch("http://127.0.0.1:8000/guide")
  const data = response
  guide.value =  data
  
   
}



onMounted(() => {
  for (let i = 0; i < data.value.length; i++) {
    if (data.value[i][0] == user.value) {
      email.value = data.value[i][1];
    }
  }
  // function to get closet match depends on user queries
  guides()
});



async function sumbit() {
  if (
    user.value.length >= 4 &&
    email.value.length >= 4 &&
    subject.value.length >= 4 &&
    message.value.length >= 4
  ) {
    const response = await ticketrequest(
      user.value,
      email.value,
      subject.value,
      department.value,
      priority.value,
      message.value
    );
    alert_ticket.value = true;
    setTimeout(() => {
      alert_ticket.value = false;
    }, 3000);

    email.value = "";
    subject.value = "";
    department.value = "";
    priority.value = "";
    message.value = "";
  }
}
</script>
