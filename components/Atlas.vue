<template>
  <div class="container mx-auto m-0 p-2 h-screen max-w-4xl self-center">
    <div class="flex place-content-center m-4">
      <img src="~/static/eucp_logo.png" alt="EUCP Logo">
      <h1 class="text-2xl">
        EUCP WP2 - Atlas of constrained climate projections</h2>
      </h1>
    </div>
    <div class="flex place-content-center space-x-3">
      <Dropdown v-model="selectedVariable" :options="variables" />
      <Dropdown v-model="selectedSeason" :options="seasons" />
      <Dropdown v-model="selectedPercentile" :options="percentiles" />
      <Dropdown v-model="selectedDataset" :options="datasets" />
      <Dropdown v-model="selectedMethod" :options="methods" />
    </div>
    <div class="flex place-content-center">
      <img
        class="h-96"
        :src="require(`~/assets/sample_figures/eur_${selectedVariable}_41-60_${selectedSeason}_${selectedDataset}_${selectedPercentile}perc.png`)"
        alt="Map of climate projections for Europe"
      >
    </div>
    <div class="flex place-content-end space-x-3">
      <nuxt-link to="/about">
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          More info
        </button>
      </nuxt-link>
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Download data
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      selectedDataset: 'cmip6',
      selectedPercentile: '10',
      selectedSeason: 'djf',
      selectedVariable: 'tas',
      selectedMethod: 'climwip',
      datasets: {
        cmip6: 'CMIP6'
      },
      percentiles: {
        10: '10-percentile',
        25: '25-percentile',
        50: '50-percentile',
        75: '75-percentile',
        90: '90-percentile'
      },
      seasons: {
        djf: 'Winter',
        jja: 'Summer'
      },
      variables: {
        tas: 'Temperature',
        pr: 'Precipitation'
      },
      methods: {
        climwip: 'ClimWIP'
      }
    }
  }
}
</script>
