<template>
  <div>
    <b-form>
      <div class="row">
        <div class="col-6">
          <b-form-group id="name-group" label="名称" label-for="template-name">
            <b-input v-model="data.name" :state="name_valid" id="template-name"></b-input>
          </b-form-group>
        </div>

        <div class="col-12">
          <b-form-group id="prescription-group" label="内容" label-for="template-prescription">
            <b-form-textarea
              v-model="data.prescription"
              :state="prescription_valid"
              id="template-prescription"
              rows="5"
              max-rows="20"
            ></b-form-textarea>
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
    },
    prescription_valid: function() {
      return this.data.prescription ? true : false && this.data.prescription.length > 0;
    }
  }
}
</script>
