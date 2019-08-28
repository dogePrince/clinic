<template>
  <div>
    <b-form>
      <div class="row">
        <div class="col-6">
          <b-form-group id="patient-group" label="访客" label-for="case_patient">
            <b-form-select v-model="data.patient" @change="update_patient" :state="patient_valid" id="case_patient">
              <option v-for="option in patient_options" :value="option.id">{{option.text}}</option>
            </b-form-select>
          </b-form-group>
        </div>

        <div class="col-6">
          <b-form-group id="patient-register-group" label="注册时间" label-for="patient_register_date">
            <date-picker v-model="register_date" type="datetime" format="YYYY-MM-DD HH:mm:ss" id="patient_register_date" disabled></date-picker>
          </b-form-group>
        </div>
        <div class="col-6">
          <b-form-group id="patient-recent-group" label="最近来访" label-for="patient_recent_date">
            <date-picker v-model="recent_date" type="datetime" format="YYYY-MM-DD HH:mm:ss" id="patient_recent_date" disabled></date-picker>
          </b-form-group>
        </div>

        <div class="col-6">
          <b-form-group id="case-pub-date-group" label="此次来访" label-for="case_pub_date">
            <date-picker v-model="data.pub_date" type="datetime" format="YYYY-MM-DD HH:mm:ss" id="case_pub_date"></date-picker>
          </b-form-group>
        </div>
      </div>

      <div class="row">
        <div class="col-12">
          <b-form-group id="case-symptom-group" label="症状" label-for="case_symptom">
            <b-form-textarea v-model="data.symptom" :state="symptom_valid" id="case_symptom" rows="5" max-rows="20"></b-form-textarea>
          </b-form-group>
        </div>

        <div class="col-6">
          <b-form-group id="case-template-group" label="方剂" label-for="case_template">
            <b-form-select v-model="data.template" @change="update_template" :state="template_valid" id="case_template">
              <option v-for="option in template_options" :value="option.id">{{option.text}}</option>
            </b-form-select>
          </b-form-group>
        </div>

        <div class="col-6">
          <b-form-group id="dose_num-group" label="份数" label-for="case_dose_num">
            <b-form-input v-model="data.dose_num" :state="dose_num_valid" id="case_dose_num" type="number"></b-form-input>
          </b-form-group>
        </div>

        <div class="col-12">
          <b-form-group id="prescription-group" label="处方" label-for="case_prescription">
            <b-form-textarea v-model="data.prescription" :state="prescription_valid" id="case_prescription" rows="5" max-rows="20"></b-form-textarea>
          </b-form-group>
        </div>
      </div>
    </b-form>
  </div>
</template>

<script>
import DatePicker from 'vue2-datepicker'

export default {
  props: ['data', 'patient_list', 'template_list'],
  components: { DatePicker },
  data: function() {
    return {
      register_date: '',
      recent_date: ''
    };
  },
  created: function() {
    this.update_patient();
  },
  watch: {
    data: function() {
      this.update_patient();
    },
    patient_list: function() {
      this.update_patient();
    }
  },
  computed: {
    patient_options: function() {
      var options = [];
      for (var patient of this.patient_list) {
        var text = [patient.name, this.sexes[patient.sex], patient.age + "岁"].join('，');
        options.push({id: patient.id, text: text});
      }
      return options;
    },
    patient_dict: function() {
      var dict = {};
      for (var patient of this.patient_list) {
        dict[patient.id] = patient;
      }
      return dict;
    },
    template_options: function() {
      var options = [{id: null, text: '无'}];
      for (var template of this.template_list) {
        options.push({id: template.id, text: template.name});
      }
      return options;
    },
    template_dict: function() {
      var dict = {};
      for (var template of this.template_list) {
        dict[template.id] = template;
      }
      return dict;
    },
    patient_valid: function() {
      return Number.isInteger(this.data.patient);
    },
    symptom_valid: function() {
      return this.data.symptom ? true : false && this.data.symptom.length > 0;
    },
    template_valid: function() {
      return this.data.template === null || Number.isInteger(this.data.template);
    },
    dose_num_valid: function() {
      return Number.isInteger(parseInt(this.data.dose_num));
    },
    prescription_valid: function() {
      return this.data.prescription ? true : false && this.data.prescription.length > 0;
    }
  },
  methods: {
    update_patient: function(){
      var patient = this.patient_dict[this.data.patient];
      if (patient) {
        this.register_date = new Date(patient.register_date);
        this.recent_date = new Date(patient.recent.pub_date);
      }
      else {
        this.register_date = '';
        this.recent_date = '';
      }
    },
    update_template: function(){
      var template = this.template_dict[this.data.template];
      if (template) {
        this.data.prescription = template.prescription;
      }
      else if (this.data.template === null) {
        this.data.prescription = '';
      }
    }
  }
}
</script>

<style scoped>
.mx-datepicker {
  width: 100%;
}
</style>
