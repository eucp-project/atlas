// https://www.designhammer.com/blog/reusable-vuejs-components-part-2-basic-drop-down-and-v-model
// https://tailwindcomponents.com/component/dropdown-1

<template>
  <div class="relative inline-flex">
    <svg
      class="w-2 h-2 absolute top-0 right-0 m-4 pointer-events-none"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 412 232"
    >
      <path
        d="M206 171.144L42.678 7.822c-9.763-9.763-25.592-9.763-35.355
      0-9.763 9.764-9.763 25.592 0 35.355l181 181c4.88 4.882 11.279 7.323 17.677
      7.323s12.796-2.441 17.678-7.322l181-181c9.763-9.764 9.763-25.592
      0-35.355-9.763-9.763-25.592-9.763-35.355 0L206 171.144z"
        fill="#648299"
        fill-rule="nonzero"
      />
    </svg>
    <div>
      <span
        v-if="hover"
        id="popup"
        class="absolute flex justify-center items-center bg-white bottom-14 right-0
      border border-gray-100 rounded shadow-lg h-20 w-40"
      >
        <div
          class="absolute custom-top bg-white transform rotate-45 z-0
        border-b-3 border-t-0 border-r-3 border-l-0 border-gray-100 p-2"
        />
        <p class="text-gray-600 w-30 text-sm text-center m-1 p-1 z-10">
          {{ alttext }}
        </p>
      </span>
      <select
        v-model="selectedOption"
        class="border border-gray-300 rounded-full cursor-pointer
      text-gray-600 h-10 pl-5 pr-10 bg-white hover:border-gray-400
      focus:outline-none appearance-none"
        @mouseover="hover = true"
        @mouseleave="hover = false"
        @input="event => { $emit('input',
                                 event.target.value) }"
      >
        <option v-for="(option, name) in options" :key="name" :value="name">
          {{ option }}
        </option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    value: null,
    options: {
      type: Object,
      required: true
    },
    alttext: null
  },
  data () {
    return {
      hover: false,
      selectedOption: null
    }
  },
  watch: {
    value (newValue) {
      this.selectedOption = newValue
    }
  },
  mounted () {
    this.selectedOption = this.value
  }
}
</script>

<style>
  .custom-top {
    top: 4.3rem;
  }
</style>
