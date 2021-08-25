<template>
  <div class="flex flex-col place-content-center items-center h-full">
    <h1 class="m-4 text-3xl">
      EUCP WP2 - Atlas of constrained climate projections
    </h1>
    <div class="space-x-1">
      <Dropdown v-model="selectedVariable" :options="variables" alttext="Select a variable" />
      <Dropdown v-model="selectedSeason" :options="seasons" alttext="Select a season" />
      <Dropdown v-model="selectedPercentile" :options="percentiles" alttext="Select a percentiles" />
      <Dropdown v-model="selectedDataset" :options="datasets" alttext="Select a dataset" />
      <Dropdown v-model="selectedMethod" :options="methods" alttext="Select a method" />
      <Dropdown v-model="selectedConstrained" :options="constrainedOptions" alttext="Select a constrained" />
    </div>
    <div
      class="bg-center bg-no-repeat bg-contain flex-grow w-full"
      :style="{ backgroundImage: `url(${require('~/assets/processed_figures/eur_' + selectedMethod + '_' + selectedVariable + '_41-60_' + selectedSeason + '_' + selectedDataset + '_' + selectedPercentile + 'perc_' + selectedConstrained + '.png')})` }"
    />
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
