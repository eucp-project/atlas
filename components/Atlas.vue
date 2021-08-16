<template>
  <div class="flex flex-col place-content-center items-center min-h-full h-full max-h-full border-4">
    <h1 class="m-4 text-3xl">
      EUCP WP2 - Atlas of constrained climate projections
    </h1>
    <div class="space-x-1">
      <Dropdown v-model="selectedVariable" :options="variables" />
      <Dropdown v-model="selectedSeason" :options="seasons" />
      <Dropdown v-model="selectedPercentile" :options="percentiles" />
      <Dropdown v-model="selectedDataset" :options="datasets" />
      <Dropdown v-model="selectedMethod" :options="methods" />
      <Dropdown v-model="selectedConstrained" :options="constrainedOptions" />
    </div>
    <div class="bg-center bg-no-repeat bg-contain flex-shrink flex-grow w-full border-4"  :style="{ backgroundImage: `url(${require('~/assets/sample_figures/eur_' + selectedVariable + '_41-60_' + selectedSeason + '_' + selectedDataset + '_' + selectedPercentile + 'perc.png')})` }" />
    <!-- <img
      class="object-contain h-full border-4"
      :src="require(`~/assets/sample_figures/eur_${selectedVariable}_41-60_${selectedSeason}_${selectedDataset}_${selectedPercentile}perc.png`)"
      alt="Map of climate projections for Europe"
    > -->
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
