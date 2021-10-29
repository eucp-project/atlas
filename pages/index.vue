<template>
  <div class="flex flex-col items-center h-full">
    <div class="flex flex-col justify-start gap-1">
      <div v-for="(map, i) in maps" :key="i">
        <MapSelector v-model="map.path" />
        <button v-if="maps.length!=1" @click="maps.splice(i, 1)">
          Remove
        </button>
        <button v-if="i===maps.length-1" @click="maps.push(clone(map))">
          Add
        </button>
      </div>
    </div>
    <div class="flex flex-grow w-full">
      <span
        v-for="(map, id) in maps"
        :key="id"
        class="bg-center bg-no-repeat bg-contain flex-grow"
        :style="{backgroundImage: `url(${map.path})`}"
      />
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
  },
  methods: {
    clone (item) {
      return JSON.parse(JSON.stringify(item))
    }
  }
}
</script>
