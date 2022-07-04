<template>
  <div>
    <table v-if="info.length == 1" class="td-padding-table">
      <tr>
        <td>姓名:</td>
        <td>{{ info[0].name }}</td>
      </tr>
      <tr>
        <td>性别:</td>
        <td>{{ sexes[info[0].sex] }}</td>
      </tr>
      <tr>
        <td>年龄:</td>
        <td>{{ info[0].age }}</td>
      </tr>
      <tr>
        <td>电话:</td>
        <td>{{ info[0].phone_number }}</td>
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
        <td>{{ info[0].name }}</td>
        <td>{{ info[1].name }}</td>
      </tr>
      <tr>
        <th scope="row">性别:</th>
        <td>{{ sexes[info[0].sex] }}</td>
        <td>{{ sexes[info[1].sex] }}</td>
      </tr>
      <tr>
        <th scope="row">年龄:</th>
        <td>{{ info[0].age }}</td>
        <td>{{ info[1].age }}</td>
      </tr>
      <tr>
        <th scope="row">电话:</th>
        <td>{{ info[0].phone_number }}</td>
        <td>{{ info[1].phone_number }}</td>
      </tr>
      <tr>
        <th scope="row">注册时间:</th>
        <td>{{ info[0].register_date | date_to_string }}</td>
        <td>{{ info[1].register_date | date_to_string }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import moment from 'moment-timezone'

export default {
  props: ['info'],
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
