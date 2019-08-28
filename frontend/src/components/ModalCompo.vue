<template>
  <div>
    <b-modal :id="id" v-model="show" :title="info.title" centered>
      <slot></slot>

      <template slot="modal-footer">
        <b-button size="sm" variant="secondary" @click="show = !show">
          关闭
        </b-button>
        <b-button v-if="info.btn" size="sm" :variant="info.btn.variant" @click="info.btn.onClick">
          {{info.btn.text}}
        </b-button>
      </template>
    </b-modal>
  </div>
</template>

<script>
  export default {
    props: ['id', 'info'],
    data() {
      return {
        show: false
      }
    }
  }
</script>
