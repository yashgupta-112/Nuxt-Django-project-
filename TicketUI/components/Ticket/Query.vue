<template>
<div class="container">
    <h1 class="heading">My Support Tickets</h1>
    <table class="table table-dark table-borderless mt-4">
 <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Department</th>
      <th scope="col">Priority</th>
      <th scope="col">Subject</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="data in tickdata" :key="data.id">
      <th scope="row">{{data.id}}</th>
      <td>{{data.department}}</td>
      <td>{{data.priority}}</td>
      <td>{{data.subject}}</td>
    </tr>

  </tbody>
</table>
</div>
</template>


<style scoped>
@import url("../../assets/css/query.css");
</style>


<script setup>
import { onMounted } from 'vue';
const tickdata = ref("");
const username = ref("");

if (process.client) {
  username.value = localStorage.getItem("username");
}

async function Get_function(user){
  const response = await $fetch(`http://127.0.0.1:8000/fetch-ticket/${user}/`)
 const data = response
 tickdata.value = data
  //  console.log(response)
}

onMounted(()=>{
  Get_function(username.value)
  console.log(tickdata.value)
})

</script>