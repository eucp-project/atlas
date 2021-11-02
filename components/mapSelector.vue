<template>
  <span class="space-x-1">
    <Dropdown v-model="selectedVariable" :options="variables" alttext="Choose a variable." @input="$emit('input', updatedValue)" />
    <Dropdown v-model="selectedSeason" :options="seasons" alttext="Select a season. Winter is DJF and summer is JJA." @input="$emit('input', updatedValue)" />
    <Dropdown v-model="selectedPercentile" :options="percentiles" alttext="Percentiles indicate how likely these changes are." @input="$emit('input', updatedValue)" />
    <Dropdown v-model="selectedDataset" :options="datasets" alttext="Select a dataset. CMIP6, CMIP5 and CORDEX are available." @input="$emit('input', updatedValue)" />
    <Dropdown v-model="selectedMethod" :options="methods" alttext="Select a method. See More info for explanations of the methods." @input="$emit('input', updatedValue)" />
    <Dropdown v-model="selectedConstrained" :options="constrainedOptions" alttext="Whether to display constrained or unconstrained projections." @input="$emit('input', updatedValue)" />
  </span>
</template>

<script>
export default {
  props: ['value'],
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
        cmip5: 'CMIP5',
        cordex: 'CORDEX'
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
        CALL: 'CALL',
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
    updatedValue () {
      try {
        return require('~/assets/processed_figures/eur_' + this.selectedMethod + '_' + this.selectedVariable + '_41-60_' + this.selectedSeason + '_' + this.selectedDataset + '_' + this.selectedPercentile + 'perc_' + this.selectedConstrained + '.png')
      } catch (err) {
        return 'placeholder.png'
      }
    }
  },
  mounted () {
    // Make selections consistent
    const name = this.value.split('/').slice(-1)[0]
    if (name === 'placeholder.png') {
      // Placeholder doesn't carry enough info to reconstruct copied selection
      // Instead, make sure the figure matches the default selection
      this.$emit('input', this.updatedValue)
    }

    const parts = name.split('_')
    // console.log(parts)
    // [ "eur", "ASK", "tas", "41-60", "djf", "cmip6", "10perc", "cons.png" ]

    // Update selected values based on the input path
    this.selectedMethod = parts[1]
    this.selectedVariable = parts[2]
    this.selectedSeason = parts[4]
    this.selectedDataset = parts[5]
    this.selectedPercentile = parseInt(parts[6].slice(0, 2))
    this.selectedConstrained = parts[7].slice(0, parts[7].length - 4)
  }
}
</script>
