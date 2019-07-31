Vue.component('breadcrumb-template', {
  delimiters: ['[%', '%]'],
  props: ['nav_items'],
  template: `
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
          <li class="breadcrumb-item" v-for="(item, index) in items" v-if="index !== items.length-1">
            <a :href="item.url">[% item.friendly_name %]</a>
          </li>
          <li class="breadcrumb-item active" aria-current="page">[% items[items.length-1].friendly_name %]</li>
      </ol>
    </nav>
  `,
  computed: {
    items: function () {
      var result = [];
      for (var item of this.nav_items) {
        var route_obj = this.route_obj_by_alias(item[0], item[1])
        result.push({url: route_obj.url, friendly_name: route_obj.friendly_name});
      }
      return result;
    }
  }
});
