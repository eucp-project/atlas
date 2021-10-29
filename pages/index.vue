<template>
  <div>
    <div v-for="(map, i) in maps" :key="i">
      <MapSelector v-model="map.path" />
      <button v-if="maps.length!=1" @click="maps.splice(i, 1)">Remove</button>
      <button v-if="i===maps.length-1" @click="maps.push(map)">Add</button>
    </div>
    <div class="flex">
      <img v-for="(map, id) in maps" :key="id" :src="map.path" :alt="id" class="h-96">
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      maps: [
        { path: require('~/assets/processed_figures/eur_ASK_tas_41-60_djf_cmip6_10perc_cons.png') },
        { path: require('~/assets/processed_figures/eur_ASK_tas_41-60_djf_cmip6_50perc_cons.png') },
        { path: require('~/assets/processed_figures/eur_ASK_tas_41-60_djf_cmip6_90perc_cons.png') }
      ]
    }
  }
}
</script>
