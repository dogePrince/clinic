Vue.component('template-info-template', {
  delimiters: ['[%', '%]'],
  props: ['template_info'],
  template: `
    <table>
      <tr><td style="width: 60px;" class="align-top">名称:</td><td>[% template_info.name %]</td></tr>
      <tr><td class="align-top">配方:</td><td>[% template_info.prescription %]</td></tr>
    </table>
  `
});
