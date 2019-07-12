var routes_mixin = {
  beforeCreate: function() {
    this.type_to_regex= {
      'number': '\\d',
      'string': '\\w'
    };
    this.param_pattern = /<([a-z]+):([a-z]+)>/;
  },
  data: function () {
    return {
      routes: [
        this.route_object('/ui', 'home', '主页'),

        this.route_object('/ui/search', 'search', '搜索'),
        this.route_object('/ui/queue', 'queue', '病例队列'),
        this.route_object('/ui/statistics', 'statistics', '数据统计'),

        this.route_object('/ui/patient', 'patient', '访客总览'),
        this.route_object('/ui/patient/<number:id>', 'patient_detail', '访客详情'),
        this.route_object('/ui/patient/new', 'patient_new', '新建访客'),

        this.route_object('/ui/case', 'case', '病例总览'),
        this.route_object('/ui/case/<number:id>', 'case_detail', '病例详情'),
        this.route_object('/ui/case/new', 'case_new', '新建病例'),

        this.route_object('/ui/test', 'test', '测试页面')
      ]
    }
  },
  methods: {
    route_object: function(template, alias, friendly_name) {
      return {
        'template': template,
        'alias': alias,
        'friendly_name': friendly_name,
        'regex': this.url_template_to_regex(template)
      };
    },
    route_by_alias: function (alias) {
      for (var route of this.routes) {
        if (alias === route.alias) {
          return route;
        }
      }
      throw `Failed to find route by alias name "${alias}".`;
    },
    route_by_url: function (url) {
      for (var route of this.routes) {
        if (route.regex.exec(url)) {
          return route;
        }
      }
      throw `Failed to find route by url "${url}"`;
    },
    reverse_url: function (route, kwargs) {
      var url = route.template;
      var has_used = {};
      var match = this.get_url_param_match(url);
      var i = 1;
      while (match) {
        var index = match.index;
        var length = match[0].length;
        var type = match[1];
        var name = match[2];
        var arg = kwargs[name];
        if (typeof arg !== type) {
          throw `Invalid type "${typeof arg}" of param ${name}(${type}).`;
        }

        url = url.substring(0, index) + arg + url.substring(index+length);
        match = this.get_url_param_match(url);

        i++;
        has_used[name] = true;
      }

      var params = [];
      for (var key in kwargs) {
        if (!has_used[key]) {
          params.push(`${key}=${kwargs[key]}`);
        }
      }
      if (params.length !== 0) {
        url += '?' + params.join('&')
      }

      return url;
    },
    reverse_url_by_alias: function (alias, kwargs) {
      var route = this.route_by_alias(alias);
      return this.reverse_url(route, kwargs);
    },
    url_template_to_regex: function (url) {
      var regex = url;
      var match = this.get_url_param_match(regex);
      while (match) {
        var index = match.index;
        var length = match[0].length;
        var type = match[1];
        var name = match[2];
        var filler = `(?<${name}>${this.type_to_regex[type]}+)`;

        regex = regex.substring(0, index) + filler + regex.substring(index+length);
        match = this.get_url_param_match(regex);
      }
      return new RegExp('^' + regex + '$');
    },
    get_url_param_match: function (url) {
      return this.param_pattern.exec(url);
    }
  }
}
