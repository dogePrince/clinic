Vue.component('template-info-template', {
  delimiters: ['[%', '%]'],
  props: ['template_info'],
  template: `
    <div>
      <table v-if="template_info.length == 1" class="td-padding-table">
        <tr>
          <td>名称:</td>
          <td>[% template_info[0].name %]</td>
        </tr>
        <tr>
          <td>配方:</td>
          <td>[% template_info[0].prescription %]</td>
        </tr>
      </table>
      <table v-else class="table table-bordered">
        <tr>
          <td></td>
          <td>修改前：</td>
          <td>修改前：</td>
        </tr>
        <tr>
          <td>名称:</td>
          <td>[% template_info[0].name %]</td>
          <td>[% template_info[1].name %]</td>
        </tr>
        <tr>
          <td>配方:</td>
          <td>[% template_info[0].prescription %]</td>
          <td>[% template_info[1].prescription %]</td>
        </tr>
      </table>
    </div>
  `
});
