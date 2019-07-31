Vue.component('template-table-template', {
  delimiters: ['[%', '%]'],
  props: ['template_list'],
  template: `
    <table class="table table-hover">
      <table-caption-template :info="caption_info"></table-caption-template>
      <thead>
        <tr>
          <th class="text-center">名称</th>
          <th class="text-center">配方</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="template in template_list">
          <td class="text-center"><a :href="route_obj_by_alias('template_detail', {id: template.id}).url">[%template.name%]</a></td>
          <td class="text-center">[% template.prescription %]</td>
        </tr>
      </tbody>
    </table>
  `,
  data: function() {
    return {
      caption_info: {
        table_name: "模板列表",
        btn_new: {
          alias: 'template_new',
          param: {}
        }
      }
    }
  }
});
