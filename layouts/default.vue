<template>
  <div class="p-4 min-h-screen h-screen max-h-screen flex flex-col">
    <div class="flex flex-row gap-4 justify-around">
      <NuxtLink :to="`/`">
        <img src="~/static/eucp_logo.png" alt="EUCP Logo">
      </NuxtLink>
      <div class="flex items-center place-content-center space-x-5 text-sm custom-text-col">
        <NuxtLink :to="`/`" class="hover:text-blue-400">HOME</NuxtLink>
        <NuxtLink :to="`/about`" class="hover:text-blue-400">ABOUT</NuxtLink>
        <NuxtLink :to="`/examples`" class="hover:text-blue-400" >EXAMPLES</NuxtLink>
        <NuxtLink :to="`/references`" class="hover:text-blue-400" >DOWNLOAD DATA</NuxtLink>
        <NuxtLink :to="`/references`" class="hover:text-blue-400">REFERENCES</NuxtLink>
        <NuxtLink :to="`/faq`" class="hover:text-blue-400">FAQ</NuxtLink>
      </div>
    </div>
    <Nuxt class="flex-grow" />
  </div>
</template>

<style>
  .custom-text-col {
    color: #1d477c;
  }

</style>
