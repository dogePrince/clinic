Vue.component('patient-info-template', {
  delimiters: ['[%', '%]'],
  props: ['patient_info'],
  template: `
    <div>
      <table v-if="patient_info.length == 1" class="td-padding-table">
        <tr>
          <td>姓名:</td>
          <td>[% patient_info[0].name %]</td>
        </tr>
        <tr>
          <td>年龄:</td>
          <td>[% patient_info[0].age %]</td>
        </tr>
        <tr>
          <td>性别:</td>
          <td>[% sexes[patient_info[0].sex] %]</td>
        </tr>
        <tr>
          <td>电话:</td>
          <td>[% patient_info[0].phone_number %]</td>
        </tr>
      </table>
      <table v-else class="table table-bordered">
        <tr>
          <th scope="col"></th>
          <th scope="col">修改前：</th>
          <th scope="col">修改后：</th>
        </tr>
        <tr>
          <th scope="row">姓名:</th>
          <td>[% patient_info[0].name %]</td>
          <td>[% patient_info[1].name %]</td>
        </tr>
        <tr>
          <th scope="row">年龄:</th>
          <td>[% patient_info[0].age %]</td>
          <td>[% patient_info[1].age %]</td>
        </tr>
        <tr>
          <th scope="row">性别:</th>
          <td>[% sexes[patient_info[0].sex] %]</td>
          <td>[% sexes[patient_info[1].sex] %]</td>
        </tr>
        <tr>
          <th scope="row">电话:</th>
          <td>[% patient_info[0].phone_number %]</td>
          <td>[% patient_info[1].phone_number %]</td>
        </tr>
      </table>
    </div>
  `
});
