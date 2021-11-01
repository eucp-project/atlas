<template>
  <div>
    <div class="flex place-content-center bg-gray-100 m-3">
      <h1 class="text-xl p-3 align-middle">
        FAQ
      </h1>
    </div>
    <div class="flex flex-col items-center">
      <div v-for="(item, index) in questions.items" :key="index" class="p-2 w-1/2 m-2">
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
      questions: {}
    }
  },
  async mounted () {
    const questions = await this.$content('items').fetch()
    console.log(questions)
    this.questions = questions
  },
  methods: {
    toggle (item) {
      item.isActive = !item.isActive
    }
  }
}
</script>
