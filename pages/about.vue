<template>
  <div>
    <div class="flex place-content-center bg-gray-100 m-3">
      <h1 class="text-xl p-3 align-middle">
        FAQ
      </h1>
    </div>
    <div class="flex flex-col items-center">
      <div v-for="(item, index) in items" :key="index" class="p-2 w-1/2 m-2">
        <span>
          <h1 class="m-2 text-xl" @click="toggle(item)">
            {{ item.question }}
            <font-awesome-icon v-if="item.isActive" :icon="['fas', 'angle-up']" />
            <font-awesome-icon v-else :icon="['fas', 'angle-down']" />
          </h1>
        </span>
        <p v-show="item.isActive" class="m-2">
          {{ item.answer }}
        </p>
        <img
          v-show="item.isActive"
          v-if="!!item.figure"
          :src="item.figure"
          alt=""
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      items: [
        {
          question: 'What do these maps show?',
          answer:
            'This atlas shows several different model projections of the European climate in 2050, illustrating the effect of constraining the projections. Not all climate simulations are equally likely, however this is not routinely addressed in current climate projections. Methods of isolating the more likely projections include comparing a simulation of the past to observed climate data recorded at the time. This can suggest how well the simulation may project the future. This process is known as ‘constraint’ and can affect the results given by an ensemble of climate simulations by ruling out the poorer simulations.',
          isActive: false
        },
        {
          question: 'What are the differences between the methods?',
          answer:
            'There are several differences between the constraint methods used in this analysis, including the kind of observational data they use and how the results are handled statistically. For instance, the UKCP and ClimWIP methods both use multiple observed variables (eg. temperature, precipitation) to constrain their projections, rather than just using the target variable being reported. Some methods constrain their variables at different spatial scales, from global to local, before deriving constrained local projections. Different methods also handle uncertainty in the projections differently. The following table includes the key characteristics of the different methods and is reprinted from Brunner et al. (2020), which contains more information on the differences between these methods.',
          isActive: false,
          figure: 'methods.png'
        },
        {
          question: 'What do the percentiles mean?',
          answer:
            'A percentile is the level below which a given percentage of simulations fall when they are put in order according to a variable such as temperature. For instance, the 50th percentile in the atlas includes the lower 50% of the climate projections. The 10th percentile of precipitation projections may show significant drying, while the 90th percentile might show much wetter conditions.',
          isActive: false
        },
        {
          question: 'Which method is best?',
          answer:
            'The question of which constraint method is best depends on what the projection is being used for. Some methods have particular strengths over others.  For example, some methods provide relative weights of available simulations that could be used to select models to drive downstream climate impact analysis, and some methods can provide physically consistent projections for a number of variables. Method performance can be different in different areas or with different variables. One method, for instance, could bring significant improvements over unconstrained projections in northern Europe but not in the Mediterranean region.   It should be noted, however, that all the constraint methods used in the Atlas confer some improvement over unconstrained projections for summer temperature, and strongly related variables, and most provide improvements for all regions.',
          isActive: false
        },
        {
          question: 'Where can I find more information?',
          answer:
            'Please view the references section below for more on the background research behind this Atlas. For more on the EUCP project, please head to our website. This Atlas has been produced by Work Package 2 of EUCP, which is described in more detail here.',
          isActive: false
        }
      ]
    }
  },
  // async mounted () {
  //   const items = await this.$content('items').fetch()
  //   console.log(items)
  //   // this.index = index
  // },
  methods: {
    toggle (item) {
      item.isActive = !item.isActive
    }
  }
}
</script>
