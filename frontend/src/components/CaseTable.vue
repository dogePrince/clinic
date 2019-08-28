<template>
  <table class="table table-hover">
    <slot></slot>
    <thead>
      <tr>
        <th class="text-center">姓名</th>
        <th class="text-center">来访日期</th>
        <th class="text-center">症状</th>
        <th class="text-center">方剂</th>
        <th class="text-center">处方</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="_case in case_list">
        <td class="text-center">
          <router-link :to="{name: 'patient', params: {id: _case.patient.id}}">{{_case.patient.name}}</router-link>
        </td>
        <td class="text-center">
          <router-link :to="{name: 'case', params: {id: _case.id}}">
            {{_case.pub_date | date_to_string}}
          </router-link>
        </td>
        <td class="text-center">{{_case.symptom}}</td>
        <td class="text-center">
          <router-link v-if="_case.template.id" :to="{name: 'template', params: {id: _case.template.id}}">
            {{_case.template.name}}
          </router-link>
          <div v-else>无</div>
        </td>
        <td class="text-center">{{_case.prescription}}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import moment from 'moment-timezone'

export default {
  props: ['case_list'],
  filters: {
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
