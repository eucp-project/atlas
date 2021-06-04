<template>
  <div>
    <div>
      <Dropdown v-model="selectedVariable" :options="variables" />
      <Dropdown v-model="selectedSeason" :options="seasons" />
      <Dropdown v-model="selectedPercentile" :options="percentiles" />
      <Dropdown v-model="selectedDataset" :options="datasets" />
      <div id="main-content">
        <img
          :src="require(`~/assets/sample_figures/eur_${selectedVariable}_41-60_${selectedSeason}_${selectedDataset}_${selectedPercentile}perc.png`)"
          alt="Map of climate projections for Europe"
        >
      </div>
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
      }
    }
  }
}
</script>
