Vue.component('table-caption-template', {
  delimiters: ['[%', '%]'],
  props: ['info'],
  template: `
    <caption class="caption-top">
      [% info.table_name %]
      <a v-if="info.btn_new"
         class="btn btn-outline-primary div-short float-right"
         :href="route_obj.url">
        [% route_obj.friendly_name %]
      </a>
    </caption>
  `,
  computed: {
    route_obj: function() {
      return this.route_obj_by_alias(this.info.btn_new.alias, this.info.btn_new.param);
    }
  }
});
