<template>
  <table class="table table-hover">
    <slot></slot>
    <thead>
      <tr>
        <th class="text-center">名称</th>
        <th class="text-center">配方</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="template in template_list">
        <td class="text-center">
          <router-link :to="{name: 'template', params: {id: template.id}}">{{template.name}}</router-link>
        </td>
        <td class="text-center">{{template.prescription | hide_part}}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: ['template_list'],
  filters: {
    hide_part: function(string) {
      return string.length > 30 ? string.slice(0, 30) + '...' : string;
    }
  }
}
</script>

<style scoped>
td {
  padding: 10px;
}
</style>
