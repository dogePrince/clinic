<template>
  <div>
    <table v-if="info.length == 1" class="td-padding-table">
      <tr>
        <td>名称:</td>
        <td>{{ info[0].name }}</td>
      </tr>
    </table>
    <table v-else class="table table-bordered">
      <tr>
        <th scope="col"></th>
        <th scope="col">修改前：</th>
        <th scope="col">修改后：</th>
      </tr>
      <tr>
        <th scope="row">名称:</th>
        <td>{{ info[0].name }}</td>
        <td>{{ info[1].name }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  props: ['info']
}
</script>

<style scoped>
td {
  padding: 10px;
}
</style>
