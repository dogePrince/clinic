<template>
  <div>
    <table v-if="info.length == 1" class="td-padding-table">
      <tr>
        <td>姓名:</td>
        <td>{{ patient_dict[info[0].patient] | get('name') }}</td>
      </tr>
      <tr>
        <td>来访时间:</td>
        <td>{{ info[0].pub_date | date_to_string }}</td>
      </tr>
      <tr>
        <td>症状:</td>
        <td>{{ info[0].symptom }}</td>
      </tr>
      <tr>
        <td>方剂:</td>
        <td>{{ template_dict[info[0].template] | get('name') }}</td>
      </tr>
      <tr>
        <td>份数:</td>
        <td>{{ info[0].dose_num }}</td>
      </tr>
      <tr>
        <td>处方:</td>
        <td>{{ info[0].prescription }}</td>
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
        <td>{{ patient_dict[info[0].patient] | get('name') }}</td>
        <td>{{ patient_dict[info[1].patient] | get('name') }}</td>
      </tr>
      <tr>
        <th scope="row">来访时间:</th>
        <td>{{ info[0].pub_date | date_to_string }}</td>
        <td>{{ info[1].pub_date | date_to_string }}</td>
      </tr>
      <tr>
        <th scope="row">症状:</th>
        <td>{{ info[0].symptom }}</td>
        <td>{{ info[1].symptom }}</td>
      </tr>
      <tr>
        <th scope="row">方剂:</th>
        <td>{{ template_dict[info[0].template] | get('name') }}</td>
        <td>{{ template_dict[info[1].template] | get('name') }}</td>
      </tr>
      <tr>
        <th scope="row">份数:</th>
        <td>{{ info[0].dose_num }}</td>
        <td>{{ info[1].dose_num }}</td>
      </tr>
      <tr>
        <th scope="row">处方:</th>
        <td>{{ info[0].prescription }}</td>
        <td>{{ info[1].prescription }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import moment from 'moment-timezone'

export default {
  props: ['info', 'patient_list', 'template_list'],
  computed: {
    patient_dict: function() {
      var dict = {};
      for (var patient of this.patient_list) {
        dict[patient.id] = patient;
      }
      return dict;
    },
    template_dict: function() {
      var dict = {};
      dict[null] = {name: '无'};
      for (var template of this.template_list) {
        dict[template.id] = template;
      }
      return dict;
    }
  },
  filters: {
    get: function(obj, key) {
      return (obj ? obj : {})[key];
    },
    date_to_string: function(date) {
      return moment(date).tz('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss');
    }
  }
}
</script>

<style scoped>
td {
  padding: 10px;
}
</style>
