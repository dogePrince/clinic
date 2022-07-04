<template>
  <div class="col-12">
    <h2>搜索</h2>

    <b-nav tabs align="left">
      <b-nav-item @click="set_type('patient')" :active="query_type=='patient'">搜访客</b-nav-item>
      <b-nav-item @click="set_type('case')" :active="query_type=='case'">搜病例</b-nav-item>
    </b-nav>

    <div class="margin-100"></div>
    <div class="row justify-content-center my-3">
        <b-input v-model="query_string" class="col-5" autofocus></b-input>
        <b-button :to="search_to" squared variant="outline-success"><span class="oi oi-magnifying-glass"/></b-button>
    </div>
    <div v-if="query_type=='case'" class="row justify-content-center my-3">
      <span>时间范围：</span>
      <date-picker v-model="time_range[0]" type="datetime" format="YYYY-MM-DD HH:mm:ss" class="mr-3"></date-picker>
      <date-picker v-model="time_range[1]" type="datetime" format="YYYY-MM-DD HH:mm:ss"></date-picker>
    </div>

    <div v-if="query_type=='patient'" class="row justify-content-center my-3">
      <patient-table :patient_list="patient_list">
        <caption class="caption-top">
          <span class="ml-5">访客列表</span>
          <b-button :to="{name: 'patient', params: {id: 'new'}}" class="float-right mr-5" variant="outline-primary" size="sm">
            新建访客
          </b-button>
        </caption>
      </patient-table>
      <b-pagination-nav v-model="patient_page.page" :link-gen="patient_link_gen" :number-of-pages="patient_page.total_page" use-router></b-pagination-nav>
    </div>

    <div v-if="query_type=='case'" class="row justify-content-center my-3">
      <case-table :case_list="case_list">
        <caption class="caption-top">
          <span class="ml-5">病例列表</span>
          <b-button :to="{name: 'case', params: {id: 'new'}}" class="float-right mr-5" variant="outline-primary" size="sm">
            新建病例
          </b-button>
        </caption>
      </case-table>
      <b-pagination-nav v-model="case_page.page" :link-gen="case_link_gen" :number-of-pages="case_page.total_page" use-router></b-pagination-nav>
    </div>
  </div>
</template>

<script>
import DatePicker from 'vue2-datepicker'
import PatientTable from "../components/PatientTable.vue";
import CaseTable from "../components/CaseTable.vue";

export default {
  props: ['type'],
  components: {DatePicker, PatientTable, CaseTable},
  data: function() {
    return {
      query_string: '',
      query_type: 'patient',
      time_range: [null, null],

      patient_list: [],
      patient_page: {
        page: 1,
        total_page: 1
      },
      patient_query: '',

      case_list: [],
      case_page: {
        page: 1,
        total_page: 1
      },
      case_query: '',
      case_earliest: '',
      case_latest: ''
    };
  },
  created: function() {
    this.query_type = this.$route.params.type;
    if (this.$route.query.query !== undefined) {
      this.query_string = this.$route.query.query;
      if (this.$route.query.earliest) {
        this.time_range[0] = new Date(this.$route.query.earliest);
      }
      if (this.$route.query.latest) {
        this.time_range[1] = new Date(this.$route.query.latest);
      }
      this.do_search();
    }
  },
  watch: {
    $route: function() {
      this.query_type = this.$route.params.type;
      if (this.$route.query.query !== undefined) {
        this.query_string = this.$route.query.query;
        this.do_search();
      }
    }
  },
  computed: {
    earliest: function() {
      return this.time_range[0] instanceof Date ? this.time_range[0].toJSON() : '';
    },
    latest: function() {
      return this.time_range[1] instanceof Date ? this.time_range[1].toJSON() : '';
    },
    search_to: function() {
      var query = {query: this.query_string, page: 1};
      if (this.query_type == 'case') {
        query.earliest = this.earliest;
        query.latest = this.latest;
      }
      return {name: 'search', params: {type: this.query_type}, query: query};
    }
  },
  methods: {
    set_type: function(type) {
      this.query_type = type;
    },
    do_search: function() {
      var this_vm = this;
      var page = parseInt(this.$route.query.page, 10);
      if (this.$route.query.query !== undefined) {
        this.get_search(this.$route.fullPath)
        .then(function({data}) {
          this_vm.$route.params.type == 'patient' && this_vm.set_patient_data(data, this_vm.$route.query.query);
          this_vm.$route.params.type == 'case' && this_vm.set_case_data(data, this_vm.$route.query.query);
        });
      }
    },
    set_patient_data: function(data, query_string) {
      this.patient_list = data.list;
      this.patient_page.page = data.page_num;
      this.patient_page.total_page = data.total_page;
      this.patient_query = query_string;
    },
    set_case_data: function(data, query_string) {
      this.case_list = data.list;
      this.case_page.page = data.page_num;
      this.case_page.total_page = data.total_page;
      this.case_query = query_string;
      this.case_earliest = this.earliest;
      this.case_latest = this.latest;
    },
    patient_link_gen: function(pageNum) {
      return {
        name: 'search',
        params: { type: 'patient' },
        query: { page: pageNum, query: this.patient_query }
      };
    },
    case_link_gen: function(pageNum) {
      return {
        name: 'search',
        params: { type: 'case' },
        query: { page: pageNum, query: this.case_query, earliest: this.case_earliest, latest: this.case_latest }
      };
    },
  }

}
</script>

<style scoped>
.caption-top {
  caption-side: top;
}
.margin-100 {
  margin: 50px
}
.hide-part {
  width: 500px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis
}
</style>
