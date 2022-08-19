<template>
<div>
  <nav class="navbar navbar-expand-lg bg-dark">
  <div class="container-fluid">
    <img src="../../assets/images/ultra.png" height="55" width="230">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mb-1 mb-lg-0">
        <li class="nav-item">
          <NuxtLink  class="nav-heading" to="/query">Query</NuxtLink>
        </li>
        <li class="nav-item">
         <NuxtLink class="nav-heading" to="/sysadmin">Sumbit Ticket</NuxtLink>
        </li>
       
      </ul>
      
    </div>
    <button type="button"  class="btn btn-outline-danger">Logout</button>
  </div>
  
</nav>
</div>
</template>

<style scoped >
@import url(../../assets/css/nav.css);

</style>