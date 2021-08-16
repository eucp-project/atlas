<template>
  <div class="p-4 min-h-screen h-screen max-h-screen flex flex-col">
    <div class="flex flex-row gap-4 justify-around">
      <NuxtLink :to="`/`">
        <img src="~/static/eucp_logo.png" alt="EUCP Logo">
      </NuxtLink>
      <div class="flex items-center">
        <NuxtLink :to="`/`">
          <p class="text-sm text-gray-400">
            Home
          </p>
        </NuxtLink>
        <input class="w-32 h-8 focus:shadow-outline rounded text-sm px-2 pl-4" type="search" placeholder="Search...">
      </div>
    </div>
    <Nuxt class="flex-grow" />
  </div>
</template>
