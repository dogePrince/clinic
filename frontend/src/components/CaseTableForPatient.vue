<template>
  <table class="table table-hover">
    <slot></slot>
    <thead>
      <tr>
        <th class="text-center">来访日期</th>
        <th class="text-center">症状</th>
        <th class="text-center">方剂</th>
        <th class="text-center">处方</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="_case in cases">
        <td class="text-center"><router-link :to="{name: 'case', params: {id: _case.id}}">{{_case.pub_date | date_to_string}}</router-link></td>
        <td class="text-center">{{_case.symptom}}</td>
        <td class="text-center">{{template_dict[_case.template]}}</td>
        <td class="text-center">{{_case.prescription}}</a></td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import moment from 'moment-timezone'

export default {
  props: ['cases'],
  data: function() {
    return {
      template_dict: {}
    };
  },
  created: function() {
    this.load_template_dict()
  },
  filters: {
    date_to_string: function(date) {
      return moment(date).tz('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss');
    }
  },
  methods: {
    load_template_dict: function() {
      var this_vm = this;
      this.get_template_option()
      .then(function({data}) {
        var dict = {null: "无"};
        for (let item of data.list) {
          dict[item.id] = item.name;
        }
        this_vm.template_dict = dict;
      });
    }
  }
}
</script>

<style scoped>
td {
  padding: 10px;
}
</style>
