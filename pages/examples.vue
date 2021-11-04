<template>
  <div class="h-full">
    <div class="flex bg-gray-100 m-3">
      <button
        v-for="(item, i) in users"
        :key="i"
        class="text-gray-600 py-4 px-6 block hover:text-blue-500 focus:outline-none"
        :class="item.isActive ? 'text-blue-500 border-b-2 font-medium border-blue-500' : ''"
        @click="toggle(i)"
      >
        {{ item.function }}
      </button>
    </div>
    <div class="flex gap-8">
      <div class="flex flex-col gap-4">
        <h1 class="text-xl">Their interest in climate data</h1>
        <p>{{ user.interest }}</p>
        <h1 class="text-xl">Their decision process</h1>
        <p>{{ user.process }}</p>
      </div>
      <div class="bg-blue-100 flex flex-col items-center p-4 min-w-1/4">
        <img :src="user.avatar" alt="profile picture" class="object-contain rounded-full">
        <h1 class="text-xl">{{ user.name }}</h1>
        <h2 class="italic">{{ user.function }}</h2>
        <p class="m-4">{{ user.about }}</p>
        <a href="https://www.vecteezy.com/free-vector/persona-icon" class="self-end text-sm">Persona Icon Vectors by Vecteezy</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      user: {},
      users: []
    }
  },
  async mounted () {
    const users = await this.$content('users').fetch()
    this.users = users.items.map(obj => ({ ...obj, isActive: false }))
    this.toggle(0)
  },
  methods: {
    toggle (i) {
      this.user = this.users[i]
      // eslint-disable-next-line no-return-assign
      this.users.map(obj => obj.isActive = false)
      this.users[i].isActive = true
    }
  }
}
</script>
