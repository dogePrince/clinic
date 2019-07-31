Vue.component('patient-table-template', {
  delimiters: ['[%', '%]'],
  props: ['patient_list'],
  template: `
    <table class="table table-hover">
      <table-caption-template :info="caption_info"></table-caption-template>
      <thead>
        <tr>
          <th class="text-center">姓名</th>
          <th class="text-center">性别</th>
          <th class="text-center">年龄</th>
          <th class="text-center">最近来访</th>
          <th class="text-center">症状</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="patient in patient_list">
          <td class="text-center"><a :href="route_obj_by_alias('patient_detail', {id: patient.id}).url">[%patient.name%]</a></td>
          <td class="text-center">[%sexes[patient.sex]%]</td>
          <td class="text-center">[%patient.age%]</td>
          <td class="text-center">[%patient.recent ? patient.recent.pub_date : '-'%]</td>
          <td class="text-center"><a :href="patient.recent ? route_obj_by_alias('case_detail', {id: patient.recent.id}).url : null">[%patient.recent ? patient.recent.symptom : '-'%]</a></td>
        </tr>
      </tbody>
    </table>
  `,
  data: function() {
    return {
      caption_info: {
        table_name: "访客列表",
        btn_new: {
          alias: 'patient_new',
          param: {}
        }
      },
      sexes: {"F": "女", "M": "男", "O": "其他"}
    }
  }
});
