<template>
  <div class="flex flex-col items-center h-full max-h-full">
    <!-- Adding the selectors -->
    <div class="flex flex-col justify-start gap-1">
      <div v-for="(map, i) in maps" :key="i">
        <!-- <span v-if="maps.length>1" class="text-xl"> {{ getLetter(i) }} </span> -->
        <MapSelector v-model="map.path" />
        <button v-if="maps.length!=1" class="mx-4" @click="maps.splice(i, 1)">
          <font-awesome-icon :icon="['fas', 'trash']" />
        </button>
        <button v-if="i===maps.length-1" class="mx-4" @click="maps.push(clone(map))">
          <font-awesome-icon :icon="['fas', 'plus']" />
        </button>
      </div>
    </div>
    <!-- Adding the maps -->
    <div class="flex flex-grow w-full">
      <span
        v-for="(map, id) in maps"
        :key="id"
        class="bg-center bg-no-repeat bg-contain flex-grow"
        :style="{backgroundImage: `url(${map.path})`}"
      >
        <p class="absolute bottom-8 left-1/4 text-center text-sm">
          Figures can be used under a
          <a href="https://creativecommons.org/licenses/by/4.0/"> CC-BY 4.0 licence.
          </a>
          see <NuxtLink :to="`/about`" class="hover:text-blue-400 underline">ABOUT</NuxtLink> page on how to cite the Atlas.
        </p>
        <a href="https://creativecommons.org/licenses/by/4.0/">
          <img class="absolute bottom-8 right-1/3" src="~/static/ccby_logo.png" alt="CC BY Logo">
        </a>
        <!-- <p v-if="maps.length>1" class="text-xl m-24"> {{ getLetter(id) }} </p> -->
      </span>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      maps: [
        { path: require('~/assets/processed_figures/eur_ClimWIP_tas_41-60_djf_cmip6_10perc_cons.png') }
      ]
    }
  },
  methods: {
    clone (item) {
      return JSON.parse(JSON.stringify(item))
    },
    getLetter (n) {
      return String.fromCharCode(65 + n)
    }
  }
}
</script>
