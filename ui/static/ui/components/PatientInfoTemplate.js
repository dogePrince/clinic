Vue.component('patient-info-template', {
  delimiters: ['[%', '%]'],
  props: ['patient_info'],
  template: `
    <ul>
      <li>姓名: [% patient_info.name %]</li>
      <li>年龄: [% patient_info.age %]</li>
      <li>性别: [% sexes[patient_info.sex] %]</li>
      <li>电话: [% patient_info.phone_number %]</li>
    </ul>
  `,
  data: function() {
    return {
      status_dict: {
        "success": 'alert-success',
        "failed": 'alert-danger'
      }
    };
  }
});
