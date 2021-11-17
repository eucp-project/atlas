<template>
  <div class="p-4 min-h-screen h-screen max-h-screen flex flex-col">
    <div class="flex flex-row gap-4 justify-around">
      <NuxtLink :to="`/`">
        <img src="~/static/eucp_logo.png" alt="EUCP Logo">
      </NuxtLink>
      <h1 class="m-2 text-xl">
        EUCP WP2 - Atlas of constrained climate projections
      </h1>
      <div class="flex items-center place-content-center space-x-5 text-sm custom-text-col">
        <NuxtLink :to="`/`" class="hover:text-blue-400">HOME</NuxtLink>
        <NuxtLink :to="`/about`" class="hover:text-blue-400">ABOUT</NuxtLink>
        <NuxtLink :to="`/examples`" class="hover:text-blue-400" >EXAMPLES</NuxtLink>
        <a href="https://doi.org/10.5281/zenodo.5645153" class="hover:text-blue-400" >DOWNLOAD DATA</a>
      </div>
    </div>
    <Nuxt class="m-4 h-full" />
  </div>
</template>

<style>
  .custom-text-col {
    color: #1d477c;
  }

</style>
