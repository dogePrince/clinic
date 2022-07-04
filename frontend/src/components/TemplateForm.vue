<template>
  <div>
    <b-form>
      <div class="row">
        <div class="col-6">
          <b-form-group id="name-group" label="名称" label-for="template-name">
            <b-input v-model="data.name" :state="name_valid" id="template-name"></b-input>
          </b-form-group>
        </div>
      </div>
    </b-form>
  </div>
</template>

<script>
export default {
  props: ['data'],
  computed: {
    name_valid: function() {
      return this.data.name ? true : false && this.data.name.length > 0;
    }
  }
}
</script>
