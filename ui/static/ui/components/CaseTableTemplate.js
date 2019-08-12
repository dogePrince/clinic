Vue.component('case-table-template', {
  delimiters: ['[%', '%]'],
  props: ['case_list', 'btn_param'],
  template: `
    <table class="table table-hover">
      <table-caption-template :info="caption_info"></table-caption-template>
      <thead>
        <tr>
          <th class="text-center">姓名</th>
          <th class="text-center">性别</th>
          <th class="text-center">年龄</th>
          <th class="text-center">来访日期</th>
          <th class="text-center">症状</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="case_obj in case_list">
          <td class="text-center"><a :href="route_obj_by_alias('patient_detail', {id: case_obj.patient.id}).url">[%case_obj.patient.name%]</a></td>
          <td class="text-center">[%sexes[case_obj.patient.sex]%]</td>
          <td class="text-center">[%case_obj.patient.age%]</td>
          <td class="text-center">[%case_obj.pub_date%]</td>
          <td class="text-center"><a :href="route_obj_by_alias('case_detail', {id: case_obj.id}).url">[%case_obj.symptom%]</a></td>
        </tr>
      </tbody>
    </table>
  `,
  data: function() {
    return {
      caption_info: {
        table_name: "病例列表",
        btn_new: {
          alias: 'case_new',
          param: this.btn_param
        }
      }
    }
  }
});
