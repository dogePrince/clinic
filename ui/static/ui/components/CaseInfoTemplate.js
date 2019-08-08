Vue.component('case-info-template', {
  delimiters: ['[%', '%]'],
  props: ['case_info', 'patient_option', 'template_option'],
  template: `
    <table>
      <tr><td style="width: 60px;" class="align-top">姓名:</td><td>[% patient_dict[case_info.patient] %]</td></tr>
      <tr><td class="align-top">症状:</td><td>[% case_info.symptom %]</td></tr>
      <tr><td class="align-top">方剂:</td><td>[% template_dict[case_info.template] %]</td></tr>
      <tr><td class="align-top">份数:</td><td>[% case_info.dose_num %]</td></tr>
      <tr><td class="align-top">处方:</td><td>[% case_info.prescription %]</td></tr>
    </table>
  `,
  computed: {
    patient_dict: function() {
      var dict = {};
      for (item of this.patient_option) {
        dict[item.id] = item.name;
      }
      return dict;
    },
    template_dict: function() {
      var dict = {};
      for (item of this.template_option) {
        dict[item.id] = item.name;
      }
      return dict;
    }
  }
});
