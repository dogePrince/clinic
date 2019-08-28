<template>
  <table class="table table-hover">
    <slot></slot>
    <thead>
      <tr>
        <th class="text-center">姓名</th>
        <th class="text-center">性别</th>
        <th class="text-center">年龄</th>
        <th class="text-center">电话</th>
        <th class="text-center">最近来访时间</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="patient in patient_list">
        <td class="text-center">
          <router-link :to="{name: 'patient', params: {id: patient.id}}">{{patient.name}}</router-link>
        </td>
        <td class="text-center">{{sexes[patient.sex]}}</td>
        <td class="text-center">{{patient.age}}</td>
        <td class="text-center">{{patient.phone_number}}</td>
        <td class="text-center">
          <router-link v-if="patient.recent.pub_date" :to="{name: 'case', params: {id: patient.recent.id}}">
            {{patient.recent.pub_date | date_to_string}}
          </router-link>
          <div v-else>-</div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import moment from 'moment-timezone'

export default {
  props: ['patient_list'],
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
