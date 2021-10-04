<template>
  <div class="flex flex-col place-content-center items-center h-full">
    <h1 class="m-4 text-3xl">
      EUCP WP2 - Atlas of constrained climate projections
    </h1>
    <div class="space-x-1">
      <Dropdown v-model="selectedVariable" :options="variables" alttext="Choose a variable." />
      <Dropdown v-model="selectedSeason" :options="seasons" alttext="Select a season. Winter is DJF and summer is JJA." />
      <Dropdown v-model="selectedPercentile" :options="percentiles" alttext="Percentiles indicate how likely these changes are." />
      <Dropdown v-model="selectedDataset" :options="datasets" alttext="Select a dataset. Currently only CMIP6 is included." />
      <Dropdown v-model="selectedMethod" :options="methods" alttext="Select a method. See More info for explanations of the methods." />
      <Dropdown v-model="selectedConstrained" :options="constrainedOptions" alttext="Whether to display constrained or unconstrained projections." />
    </div>
    <div
      class="bg-center bg-no-repeat bg-contain flex-grow w-full"
      :style="{backgroundImage: `url(${bgImage})`}"
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
      selectedMethod: 'ClimWIP',
      selectedConstrained: 'cons',
      datasets: {
        cmip6: 'CMIP6',
        cmip5: 'CMIP5'
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
        ASK: 'ASK',
        ClimWIP: 'ClimWIP',
        HistC: 'HistC',
        REA: 'REA',
        UKCP: 'UKCP'
      },
      constrainedOptions: {
        cons: 'Constrained',
        uncons: 'Unconstrained'
      }
    }
  },
  computed: {
    bgImage () {
      const fallback = 'placeholder.png'
      try {
        return require('~/assets/processed_figures/eur_' + this.selectedMethod + '_' + this.selectedVariable + '_41-60_' + this.selectedSeason + '_' + this.selectedDataset + '_' + this.selectedPercentile + 'perc_' + this.selectedConstrained + '.png')
      } catch (err) {
        return fallback
      }
    }
  }
}
</script>
