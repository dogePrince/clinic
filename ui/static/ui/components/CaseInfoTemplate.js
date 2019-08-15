Vue.component('case-info-template', {
  delimiters: ['[%', '%]'],
  props: ['case_info', 'patient_option', 'template_option'],
  template: `
    <div>
      <table v-if="case_info.length == 1" class="td-padding-table">
        <tr>
          <td>姓名:</td>
          <td>[% patient_dict[case_info[0].patient] %]</td>
        </tr>
        <tr>
          <td>症状:</td>
          <td>[% case_info[0].symptom %]</td>
        </tr>
        <tr>
          <td>方剂:</td>
          <td>[% template_dict[case_info[0].template] %]</td>
        </tr>
        <tr>
          <td>份数:</td>
          <td>[% case_info[0].dose_num %]</td>
        </tr>
        <tr>
          <td>处方:</td>
          <td>[% case_info[0].prescription %]</td>
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
          <td>[% patient_dict[case_info[0].patient] %]</td>
          <td>[% patient_dict[case_info[1].patient] %]</td>
        </tr>
        <tr>
          <th scope="row">症状:</th>
          <td>[% case_info[0].symptom %]</td>
          <td>[% case_info[1].symptom %]</td>
        </tr>
        <tr>
          <th scope="row">方剂:</th>
          <td>[% template_dict[case_info[0].template] %]</td>
          <td>[% template_dict[case_info[1].template] %]</td>
        </tr>
        <tr>
          <th scope="row">份数:</th>
          <td>[% case_info[0].dose_num %]</td>
          <td>[% case_info[1].dose_num %]</td>
        </tr>
        <tr>
          <th scope="row">处方:</th>
          <td>[% case_info[0].prescription %]</td>
          <td>[% case_info[1].prescription %]</td>
        </tr>
      </table>
    </div>
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
