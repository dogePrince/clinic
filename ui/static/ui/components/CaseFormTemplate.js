Vue.component('case-form-template', {
  delimiters: ['[%', '%]'],
  props: ['case_obj'],
  template: `
    <form>
      <input type="hidden" name="id" id="id_id" v-if="case_obj.id" v-model="case_obj.id" >
      <div class="form-row">
        <div class="form-group col-md-6">
          <label>姓名</label>
          <input class="form-control" type="text" v-model="case_obj.patient.id">
        </div>
        <div class="form-group col-md-3">
          <label>年龄</label>
          <input class="form-control" type="number" v-model="case_obj.patient.age" disabled>
        </div>
        <div class="form-group col-md-3">
          <label>性别</label>
          <select class="select form-control" type="text" v-model="case_obj.patient.sex" disabled>
            <option v-for="(sex_value, key) in sexes" :value="key">[%sex_value%]</option>
          </select>
        </div>
        <div class="form-group col-md-6">
          <label>注册时间</label>
          <input class="form-control" type="text" v-model="case_obj.patient.register_date" disabled>
        </div>
        <div class="form-group col-md-6">
          <label>最近来访</label>
          <input class="form-control" type="text" v-model="case_obj.patient.recent.pub_date" disabled>
        </div>
        <div class="form-group col-md-12">
          <label>症状</label>
          <textarea class="textarea form-control" v-model="case_obj.symptom"></textarea>
        </div>
        <div class="form-group col-md-6">
          <label>方剂</label>
          <select class="select form-control" type="text" v-model="case_obj.template" >
            <option value="">无</option>
            <option v-for="(option, key) in template_option" :value="option.id">[%option.name%]</option>
          </select>
        </div>
        <div class="form-group col-md-6">
          <label>份数</label>
          <input class="form-control" type="number" v-model="case_obj.dose_num">
        </div>
        <div class="form-group col-md-12">
          <label>处方</label>
          <textarea class="textarea form-control" v-model="case_obj.prescription"></textarea>
        </div>
      </div>
    </form>
  `,
  created: function() {
    this_vm = this;
    this.get_template_option().then(function (response) {
      this_vm.template_option = response.data.list;
    }).catch(function (error) {
      console.log(error)
    });
  },
  computed: {
    template_value: function() {
      return this.case_obj.template;
    }
  },
  watch: {
    template_value: function(newTemp, oldTemp) {
      if (newTemp) {
        console.log(typeof newTemp);
      }
    }
  },
  data: function() {
    return {
      template_option: [],
      sexes: {"F": "女", "M": "男", "O": "其他"}
    }
  }
});
