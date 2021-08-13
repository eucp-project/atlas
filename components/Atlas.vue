<template>
  <div class="container mx-auto m-0 p-2 h-screen max-w-4xl self-center">
    <div class="flex place-content-center m-4">
      <img src="~/static/eucp_logo.png" alt="EUCP Logo">
      <h1 class="text-2xl">
        EUCP WP2 - Atlas of constrained climate projections
      </h1>
    </div>
    <div class="flex place-content-center space-x-3">
      <Dropdown v-model="selectedVariable" :options="variables" />
      <Dropdown v-model="selectedSeason" :options="seasons" />
      <Dropdown v-model="selectedPercentile" :options="percentiles" />
      <Dropdown v-model="selectedDataset" :options="datasets" />
      <Dropdown v-model="selectedMethod" :options="methods" />
      <Dropdown v-model="selectedConstrained" :options="constrainedOptions" />
    </div>
    <div class="flex place-content-center">
      <img
        class="h-96"
        :src="require(`~/assets/processed_figures/eur_${selectedMethod}_${selectedVariable}_41-60_${selectedSeason}_${selectedDataset}_${selectedPercentile}perc_${selectedConstrained}.png`)"
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
      selectedMethod: 'ETHZ_ClimWIP',
      selectedConstrained: 'cons',
      datasets: {
        cmip6: 'CMIP6'
        // cmip5: 'CMIP5'
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
        ETHZ_ClimWIP: 'ClimWIP',
        IPSL_REA: 'REA'
      },
      constrainedOptions: {
        cons: 'Constrained',
        uncons: 'Unconstrained'
      }
    }
  }
}
</script>
