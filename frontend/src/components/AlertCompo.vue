<template>
  <div>
    <div class="alert-container">
      <transition-group name="list" tag="div">
        <b-alert v-for="item in alerts" :key="item.key" :variant="item.variant" fade show>
          {{ item.content }}
        </b-alert>
      </transition-group>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['alerts']
  }
</script>

<style scoped>
.alert-container {
  position:absolute;
  width: 100%;
  z-index: 9999;
}
.list-enter-active {
  transition: all .3s ease;
}
.list-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.list-enter, .list-leave-to {
  transform: translateX(10px);
  opacity: 0;
}
</style>
