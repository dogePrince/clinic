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
          <li v-for="item in reversed_nav_items" class="nav-item active">
            <a class="nav-link" :href="item.url">[% item.friendly_name %]</a>
          </li>
          <li class="nav-item dropdown active">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              新建...
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a v-for="item in reversed_new_items" class="dropdown-item" :href="item.url">[% item.friendly_name %]</a>
            </div>
          </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <select v-model="search_obj.type" class="custom-select mr-sm-2">
            <option v-for="item in search_options" :value="item.value">[% item.option %]</option>
          </select>
          <input v-model="search_obj.string" class="form-control mr-sm-2" type="search" placeholder="输入以搜索..." aria-label="Search">
          <button @click.prevent="search" class="btn btn-outline-success my-2 my-sm-0"><span class="oi oi-magnifying-glass"></button>
        </form>
      </div>
    </nav>
  `,
  data: function () {
    return {
      nav_items: [['home'], ['search'], ['statistics']],
      new_items: [['patient_new'], ['case_new'], ['template_new']],
      search_options: [{option: '搜访客', value:'patient'}, {option: '搜病例', value:'case'}, {option: '搜模板', value:'template'}],
      search_obj: {type: 'patient', string: ''}
    }
  },
  computed: {
    reversed_nav_items: function() {
      var result = [];
      for (var item of this.nav_items) {
        var route_obj = this.route_obj_by_alias(item[0], item[1])
        result.push(route_obj);
      }
      return result;
    },
    reversed_new_items: function() {
      var result = [];
      for (var item of this.new_items) {
        var route_obj = this.route_obj_by_alias(item[0], item[1])
        result.push(route_obj);
      }
      return result;
    },
    search_string: function() {
      return this.search_obj.string.split(/ +/).join('+');
    }
  },
  methods: {
    search: function() {
      console.log(this.search_obj.type + '=' + this.search_string);
    }
  }
});
