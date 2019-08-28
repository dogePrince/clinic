<template>
  <b-navbar toggleable="lg" fixed="top" type="light" variant="light">
    <b-navbar-brand :to="to_home">
      <td class="align-middle">
        <img src="../image/brand.svg" width="40" height="40" alt="dp">
      </td>
      <td class="align-middle">
        <span class="navbar-text">诊所系统</span>
      </td>
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item :to="to_home">主页</b-nav-item>
        <b-nav-item :to="to_search">搜索</b-nav-item>
        <b-nav-item :to="to_statistic">统计</b-nav-item>
        <b-nav-item-dropdown text="新建">
          <b-dropdown-item :to="to_new_patient">新建访客</b-dropdown-item>
          <b-dropdown-item :to="to_new_case">新建病例</b-dropdown-item>
          <b-dropdown-item :to="to_new_template">新建模板</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-select v-model="search_param.type" :options="search_options" size="sm" class="mr-sm-2"></b-form-select>
          <b-form-input v-model="search_param.query" size="sm" class="mr-sm-2" placeholder="输入以搜索..."></b-form-input>
          <b-button @click="search_with_param" :to="search_to" size="sm" class="my-2 my-sm-0" variant="outline-success">
            <span class="oi oi-magnifying-glass"/>
          </b-button>
        </b-nav-form>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  data: function() {
    return {
      to_home: {name: 'home'},
      to_search: {name: 'search', params: {type: 'patient'}},
      to_statistic: {name: 'statistic'},
      to_new_patient: {name: 'patient', params: {id: 'new'}},
      to_new_case: {name: 'case', params: {id: 'new'}},
      to_new_template: {name: 'template', params: {id: 'new'}},

      search_param: {
        type: 'patient',
        query: ''
      },
      search_options: [
        { value: 'patient', text: '搜访客' },
        { value: 'case', text: '搜病例' },
        { value: 'template', text: '搜模板' }
      ]
    };
  },
  computed: {
    search_to: function() {
      var query = {query: this.search_param.query, page: 1};
      if (this.search_param.type == 'case') {
        query.earliest = '';
        query.latest = '';
      }
      return {name: 'search', params: {type: this.search_param.type}, query: query};
    }
  },
  methods: {
    search_with_param: function() {
      this.search_param.query = '';
    }
  }
}
</script>
