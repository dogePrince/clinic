Vue.component('patient-form-template', {
  delimiters: ['[%', '%]'],
  props: ['patient_obj'],
  template: `
    <form>
      <input type="hidden" name="id" id="id_id" v-if="patient_obj.id" v-model="patient_obj.id" >
      <div class="form-row">
        <div class="form-group col-md-6">
          <label>姓名</label>
          <input class="form-control" type="text" v-model="patient_obj.name" placeholder="输入姓名">
        </div>
        <div class="form-group col-md-6">
          <label>年龄</label>
          <input class="form-control" type="number" v-model="patient_obj.age" placeholder="输入年龄">
        </div>
        <div class="form-group col-md-6">
          <label>性别</label>
          <select class="select form-control" type="text" v-model="patient_obj.sex">
            <option v-for="(sex_value, key) in sexes" :value="key">[%sex_value%]</option>
          </select>
        </div>
        <div class="form-group col-md-6">
          <label>电话</label>
          <input class="form-control" type="text" v-model="patient_obj.phone_number" placeholder="输入电话">
        </div>
        <div v-if="patient_obj.register_date" class="form-group col-md-6">
          <label>注册时间</label>
          <input class="form-control" type="text" v-model="patient_obj.register_date">
        </div>
        <div v-if="patient_obj.recent" class="form-group col-md-6">
          <label>最近来访</label>
          <input class="form-control" type="text" v-model="patient_obj.recent.pub_date" disabled>
        </div>
      </div>
    </form>
  `
});



  // .then(function (response) {
  //   console.log(response)
  // }).catch(function (error) {
  //   console.log(error)
  // });
