<template>
  <div>
    <div class="flex flex-col place-content-center items-center w-full">
      <h1 class="m-4 text-3xl">
        EUCP WP2 - Atlas of constrained climate projections
      </h1>
    </div>
    <div class="flex flex-row-reverse place-content-center items-center space-x-3">
      <button
        v-if="items > 1"
        id="button_minus"
        class="m-2 h-10 px-5 text-black transition-colors duration-150 border border-black rounded-lg focus:shadow-outline hover:bg-gray-800 hover:text-indigo-100"
        @click="items--"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-4 w-4 fill-current"
          viewBox="0 0 20 20"
        >
          <path
            fill-rule="evenodd"
            d="M3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
            clip-rule="evenodd"
          />
        </svg>
      </button>
      <button
        class="h-10 px-5 text-black transition-colors duration-150 border border-black rounded-lg focus:shadow-outline hover:bg-gray-800 hover:text-indigo-100"
        @click="items++"
      >
        <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20">
          <path
            d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z"
            clip-rule="evenodd"
            fill-rule="evenodd"
          />
        </svg>
      </button>
    </div>
    <div
      v-for="(item, i) in items"
      :key="i"
      class=""
    >
      <Atlas class="flex flex-col place-content-center" />
    </div>
    <div class="flex place-content-center space-x-3">
      <Button :text="`More info`" :target="`/about`" />
      <Button :text="`Download data`" />
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      items: 1
    }
  }
}
</script>
