<template>
  <div class="container md:mx-auto m-0 p-2 md:h-screen">
    <div class="flex m-4 justify-around">
      <NuxtLink :to="`/`">
        <img src="~/static/eucp_logo.png" alt="EUCP Logo">
      </NuxtLink>
      <div class="flex m-4 justify-around items-center">
        <NuxtLink :to="`/`">
          <p class="text-sm text-gray-400">
            Home
          </p>
        </NuxtLink>
        <input class="w-32 h-8 focus:shadow-outline rounded text-sm px-2 pl-4" type="search" placeholder="Search...">
      </div>
    </div>
    <Nuxt />
  </div>
</template>
