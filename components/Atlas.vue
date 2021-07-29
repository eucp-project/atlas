<template>
  <div class="flex flex-col mx-auto m-0 p-2 w-screen h-screen max-w-4xl self-center">
    <div class="flex place-content-center m-4">
      <img src="~/static/eucp_logo.png" alt="EUCP Logo">
      <h1 class="text-2xl">
        EUCP WP2 - Atlas of constrained climate projections</h2>
      </h1>
    </div>
    <div class="place-content-center space-x-1 space-y-3">
      <Dropdown v-model="selectedVariable" :options="variables" />
      <Dropdown v-model="selectedSeason" :options="seasons" />
      <Dropdown v-model="selectedPercentile" :options="percentiles" />
      <Dropdown v-model="selectedDataset" :options="datasets" />
      <Dropdown v-model="selectedMethod" :options="methods" />
      <Dropdown v-model="selectedConstrained" :options="constrainedOptions" />
    </div>
    <div class="flex overflow-auto place-content-center">
      <img
        class="object-contain h-96 w-auto max-w-full max-h-full"
        :src="require(`~/assets/sample_figures/eur_${selectedVariable}_41-60_${selectedSeason}_${selectedDataset}_${selectedPercentile}perc.png`)"
        alt="Map of climate projections for Europe"
      >
    </div>
    <div class="flex place-content-end space-x-3">
      <Button :text="`More info`" :target="`/about`" />
      <Button :text="`Download data`" />
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
      selectedConstrained: 'diff',
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
      },
      constrainedOptions: {
        constrained: 'Constrained',
        unconstrained: 'Unconstrained',
        diff: 'Difference'
      }
    }
  }
}
</script>

<style>

</style>
