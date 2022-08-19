<template>
    <transition name="fade" mode="out-in">
<div >
<div id="banner" class="container">
      <img src="../assets/images/logo.png" class="brand-logo" />
    </div>
    <h1 class="brand-name">Ultra Servers</h1>
    <h5 class="brand-name-tag">Premium Gaming Servers</h5>
  </div>
  </transition>

</template>

<script setup>
definePageMeta({
  layout: false,
});

const router = useRouter();

async function redirect_home(){
  if (process.client === true ){
     setTimeout(() => router.push({ path: "/auth" }), 10000);
  }
}

redirect_home()
</script>