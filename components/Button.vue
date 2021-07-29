<template>
  <div>
    <NuxtLink :to="target">
      <button
        class="bg-transparent hover:bg-gray-500 active:bg-gray-700
        text-gray-700 font-semibold hover:text-white py-2 px-4 border
        border-gray-500 hover:border-transparent rounded-full
        focus:outline-none"
      >
        {{ text }}
      </button>
    </NuxtLink>
  </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true
    },
    target: {
      type: String,
      required: false,
      default: ''
    }
  }
}
</script>
