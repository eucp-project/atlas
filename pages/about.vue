<template>
  <div>
    <div class="flex place-content-center bg-gray-100 m-3">
      <h1 class="text-xl m-3 align-middle">
        About: frequently asked questions
      </h1>
    </div>
    <div class="flex flex-col items-center">
      <div v-for="(item, index) in questions" :key="index" class="w-1/2">
        <span>
          <h1 class="m-2 text-xl" role="button" @click="toggle(item)">
            {{ item.question }}
            <font-awesome-icon v-if="item.isActive" :icon="['fas', 'angle-up']" />
            <font-awesome-icon v-else :icon="['fas', 'angle-down']" />
          </h1>
        </span>
        <nuxt-content v-show="item.isActive" :document="item" class="m-2" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      questions: []
    }
  },
  async mounted () {
    const questions = await this.$content('questions').sortBy('sort').fetch()
    this.questions = questions.map(obj => ({ ...obj, isActive: false }))
  },
  methods: {
    toggle (item) {
      item.isActive = !item.isActive
    }
  }
}
</script>
