Vue.component('navbar-template', {
  delimiters: ['[%', '%]'],
  template: `
    <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">
      <a :href="route_obj_by_alias('home').url" class="navbar-brand">
        <table>
          <tbody>
            <tr>
              <td class="align-middle">
                <img src="/static/ui/icons/brand.svg" width="40" height="40" alt="dp">
              </td>
              <td class="align-middle">
                <span class="navbar-text">诊所系统</span>
              </td>
            </tr>
          </tbody>
        </table>
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggler" aria-controls="navbarToggler" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarToggler">
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li v-for="item in items" class="nav-item active">
            <a class="nav-link" :href="item.url">[% item.friendly_name %]</a>
          </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <select class="custom-select mr-sm-2" id="inlineFormCustomSelect">
            <option value="by_patient" selected>按名字</option>
            <option value="by_case">按症状</option>
          </select>
          <input class="form-control mr-sm-2" type="search" placeholder="搜索" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">搜索</button>
        </form>
      </div>
    </nav>
  `,
  data: function () {
    return {
      nav_items: [['home'], ['search'], ['queue'], ['statistics']]
    }
  },
  computed: {
    items: function () {
      var result = [];
      for (var item of this.nav_items) {
        var route_obj = this.route_obj_by_alias(item[0], item[1])
        result.push({url: route_obj.url, friendly_name: route_obj.friendly_name});
      }
      return result;
    },

  }
});
