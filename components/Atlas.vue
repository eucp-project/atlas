<template>
  <div class="container">
    <div>
      <div class="relative inline-flex">
        <svg
          class="w-2 h-2 absolute top-0 right-0 m-4 pointer-events-none"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 412 232"
        >
          <path
            d="M206 171.144L42.678 7.822c-9.763-9.763-25.592-9.763-35.355 0-9.763 9.764-9.763 25.592 0 35.355l181 181c4.88 4.882 11.279 7.323 17.677 7.323s12.796-2.441 17.678-7.322l181-181c9.763-9.764 9.763-25.592 0-35.355-9.763-9.763-25.592-9.763-35.355 0L206 171.144z"
            fill="#648299"
            fill-rule="nonzero"
          />
        </svg>
        <select
          v-model="selected"
          class="border border-gray-300 rounded-full text-gray-600 h-10 pl-5 pr-10 bg-white hover:border-gray-400 focus:outline-none appearance-none"
        >
          <option>Choose a color</option>
          <option v-for="item in items" :key="item">
            {{ item }}
          </option>
        </select>
      </div>

      <div>
        <button class="bg-green-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" @click="test">
          Button
        </button>
      </div>

      <img
        :src="require(`~/assets/sample_figures/eur_${selected}_41-60_djf_cmip6_10perc.png`)"
        alt=""
      >
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      image: 'eur_tas_41-60_djf_cmip6_10perc.png',
      items: ['tas', 'pr'],
      selected: 'tas'
    }
  },
  methods: {
    test () {
      this.image = 'eur_tas_41-60_djf_cmip6_10perc.png'
    }
  }
}
</script>
