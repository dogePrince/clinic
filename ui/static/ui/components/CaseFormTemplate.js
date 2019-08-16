Vue.component('case-form-template', {
  delimiters: ['[%', '%]'],
  props: ['case_obj', 'patient_option', 'template_option'],
  template: `
    <form>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label>姓名</label>
          <select id="patient_select" class="select form-control" type="text" v-model="case_obj.patient" @change="load_patient">
            <option v-for="(option, key) in patient_option" :value="option.id">[%option.name%]</option>
          </select>
        </div>
        <div class="form-group col-md-3">
          <label>年龄</label>
          <input class="form-control" type="number" v-model="patient_obj.age" disabled>
        </div>
        <div class="form-group col-md-3">
          <label>性别</label>
          <select class="select form-control" type="text" v-model="patient_obj.sex" disabled>
            <option v-for="(sex_value, key) in sexes" :value="key">[%sex_value%]</option>
          </select>
        </div>
        <div class="form-group col-md-6">
          <label>注册时间</label>
          <input class="form-control" type="text" v-model="patient_obj.register_date" disabled>
        </div>
        <div class="form-group col-md-6">
          <label>最近来访</label>
          <input v-if="patient_obj.recent" class="form-control" type="text" v-model="patient_obj.recent.pub_date" disabled>
          <input v-else class="form-control" type="text" disabled>
        </div>
        <div v-if="case_obj.id" class="form-group col-md-6">
          <label>此次来访</label>
          <input class="form-control" type="text" v-model="case_obj.pub_date" disabled>
        </div>
        <div class="form-group col-md-12">
          <label>症状</label>
          <auto-text-template v-model="case_obj.symptom"></auto-text-template>
        </div>
        <div class="form-group col-md-6">
          <label>方剂</label>
          <select id="template_select" class="select form-control" type="text" v-model="case_obj.template" @change="load_template">
            <option v-for="(option, key) in template_option" :value="option.id">[%option.name%]</option>
          </select>
        </div>
        <div class="form-group col-md-6">
          <label>份数</label>
          <input class="form-control" type="number" v-model="case_obj.dose_num">
        </div>
        <div class="form-group col-md-12">
          <label>处方</label>
          <auto-text-template v-model="case_obj.prescription"></auto-text-template>
        </div>
      </div>
    </form>
  `,
  computed: {
    template_value: function() {
      return this.case_obj.template;
    }
  },
  methods: {
    load_patient: function() {
      var this_vm = this;
      return this.get_patient_by_id(this.case_obj.patient, {recent_field: true})
        .then(function (response) {
          this_vm.patient_obj = response.data;
        });
    },
    load_template: function() {
      var this_vm = this;
      if (this.case_obj.template == ''){
        this.case_obj.prescription = '';
        return
      }
      this.get_template_by_id(this.case_obj.template)
        .then(function ({data}) {
          this_vm.case_obj.prescription = data.prescription;
        });
    }
  },
  watch: {
    case_obj: function(newVal, oldVal) {
      if (this.case_obj.patient) {
        this.load_patient();
      }
    }
  },
  data: function() {
    return {
      patient_obj: []
    };
  }
});
