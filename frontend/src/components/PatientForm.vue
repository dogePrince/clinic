<template>
  <div>
    <b-form>
      <div class="row">
        <div class="col-6">
          <b-form-group id="name-group" label="姓名" label-for="patient-name">
            <b-input v-model="data.name" :state="name_valid" id="patient-name"></b-input>
          </b-form-group>
        </div>

        <div class="col-6">
          <b-form-group id="sex-group" label="性别" label-for="patient-sex">
            <b-form-select v-model="data.sex" :state="sex_valid" id="patient-sex">
              <option v-for="(v, k) in sexes" :value="k">{{v}}</option>
            </b-form-select>
          </b-form-group>
        </div>

        <div class="col-6">
          <b-form-group id="age-group" label="年龄" label-for="patient-age">
            <b-form-input v-model="data.age" :state="age_valid" id="patient-age" type="number"></b-form-input>
          </b-form-group>
        </div>

        <div class="col-6">
          <b-form-group id="phone-num-group" label="电话" label-for="patient-phone-num">
            <b-input v-model="data.phone_number" :state="phone_num_valid" id="patient-phone-num"></b-input>
          </b-form-group>
        </div>

        <div class="col-6">
          <b-form-group id="patient-register-date-group" label="注册时间" label-for="patient_register_date">
            <date-picker v-model="data.register_date" type="datetime" format="YYYY-MM-DD HH:mm:ss" id="patient_register_date"></date-picker>
          </b-form-group>
        </div>

        <div v-if="data.recent" class="col-6">
          <b-form-group id="recent-date-group" label="最近来访" label-for="patient_recent_date">
            <date-picker v-model="data.recent.pub_date" type="datetime" format="YYYY-MM-DD HH:mm:ss" id="patient_register_date" disabled></date-picker>
          </b-form-group>
        </div>
      </div>
    </b-form>
  </div>
</template>

<script>
import DatePicker from 'vue2-datepicker'

export default {
  props: ['data'],
  components: {DatePicker},
  computed: {
    name_valid: function() {
      return this.data.name ? true : false && this.data.name.length > 0;
    },
    sex_valid: function() {
      return this.sexes[this.data.sex] ? true : false;
    },
    age_valid: function() {
      return Number.isInteger(parseInt(this.data.age));
    },
    phone_num_valid: function() {
      return this.data.phone_number ? true : false && this.data.phone_number.length > 0;
    }
  }
}
</script>

<style scoped>
.mx-datepicker {
  width: 100%;
}
</style>
