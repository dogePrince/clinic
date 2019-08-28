<template>
  <b-breadcrumb :items="route_list"></b-breadcrumb>
</template>

<script>
export default {
  data: function() {
    return {
      route_list: [
        { text: '主页', to: {name: 'home'} }
      ],
      url_enhance: {
        'home': {name: '主页', weight: 1},
        'search': {name: '搜索', weight: 2},
        'statistic': {name: '统计', weight: 2},
        'patient': {name: '访客', weight: 3},
        'case': {name: '病例', weight: 4},
        'template': {name: '模板', weight: 5}
      }
    };
  },
  watch: {
    $route: function(new_route) {
      this.push_url(new_route);
    }
  },
  created: function() {
    this.push_url(this.$route)
  },
  methods: {
    push_url: function(route) {
      const extra_enhance_url = ['patient', 'case', 'template'];

      while (this.should_pop(route)) {
        this.route_list.pop();
      }

      var url_name = this.url_enhance[route.name].name;
      if (extra_enhance_url.includes(route.name)) {
        if (route.params.id == 'new') {
          url_name = '新建' + url_name;
        }
        else {
          url_name = url_name + '详情';
        }
      }
      this.route_list.push({
        to: route,
        text: url_name
      });
    },
    should_pop: function(route) {
      return this.route_list.length > 0 && this.url_enhance[this.route_list[this.route_list.length - 1].to.name].weight >= this.url_enhance[route.name].weight;
    }
  }
}
</script>
