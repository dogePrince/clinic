<template>
  <div class="col-12">
    <div class="row justify-content-center">
      <div class="col-8">
        <h2 v-if="for_new">新建访客</h2>
        <h2 v-else>访客详情</h2>
        <patient-form :data="data"></patient-form>

        <div class="row">
          <div v-if="for_new" class="col-12">
            <b-button variant="primary" @click="save_patient">新建访客</b-button>
          </div>
          <div v-else class="col-12">
            <b-button variant="primary" @click="save_patient" class="mr-2">更改访客</b-button>
            <b-button variant="danger" @click="delete_patient">删除访客</b-button>
          </div>
        </div>
      </div>
    </div>

    <div class="margin-100"></div>
    <div v-if="!for_new" class="row justify-content-center">
      <case-table-for-patient :cases="case_list">
        <caption class="caption-top">
          病例列表
          <b-button :to="{name: 'case', params: {id: 'new'}, query: {patient: this.id}}" class="float-right" variant="outline-primary" size="sm">
            新建病例
          </b-button>
        </caption>
      </case-table-for-patient>
      <div class="my-2"></div>
      <b-pagination-nav v-model="page" :link-gen="linkGen" :number-of-pages="total_page" use-router></b-pagination-nav>
    </div>
    <div class="my-5"></div>

    <modal-compo :id="modal_id" :info="modal_info">
      <patient-info :info="modal_content"></patient-info>
    </modal-compo>
  </div>
</template>

<script>
import PatientForm from "../components/PatientForm.vue"
import ModalCompo from "../components/ModalCompo.vue";
import PatientInfo from "../components/PatientInfo.vue";
import CaseTableForPatient from "../components/CaseTableForPatient.vue"
import Alerts from "../mixins/Alerts.js"

export default {
  props: ['id'],
  components: {PatientForm, ModalCompo, PatientInfo, CaseTableForPatient},
  data: function() {
    return {
      page: null,
      total_page: null,
      data: {},
      old_data: {},
      modal_id: 'modal_id',
      modal_info: {},
      modal_content: [{}],
      new_modal_info: {
        title: '确认新建吗？',
        btn: {
          text: '新建访客',
          variant: 'primary',
          onClick: this.confirm_save
        }
      },
      update_modal_info: {
        title: '确认更改吗？',
        btn: {
          text: '更改访客',
          variant: 'primary',
          onClick: this.confirm_save
        }
      },
      delete_modal_info: {
        title: '确认删除吗？',
        btn: {
          text: '删除访客',
          variant: 'danger',
          onClick: this.confirm_delete
        }
      },
      case_list: [],
      template_dict: {}
    };
  },
  created: function() {
    this.page = this.$route.query.page;
    this.init_page();
  },
  watch: {
    id: function() {
      this.init_page();
      if (!this.for_new) {
        this.load_case_page();
      }
    },
    page: function() {
      if (!this.for_new) {
        this.load_case_page();
      }
    }
  },
  computed: {
    for_new: function() {
      return this.id == 'new';
    }
  },
  methods: {
    init_page: function() {
      var this_vm = this;
      if (this.for_new) {
        this.data = {register_date: new Date()};
        this.data.name = this.$route.query.name;
        this.data.sex = "F";
      }
      else {
        this.get_patient_by_id(this.id, {recent_field: true})
        .then(function ({data}) {
          data.register_date = new Date(data.register_date);
          if (data.recent.pub_date) {
            data.recent.pub_date = new Date(data.recent.pub_date);
          }
          this_vm.data = data;
          this_vm.old_data = _.clone(data);
        }).catch(function () {
          Alerts.push('该页面不存在!', 'danger');
          this_vm.$router.back();
        });
      }
    },
    load_case_page: function() {
      var this_vm = this;
      this.get_case({page: this.page ? this.page : 1, patient_field: true, patient_id: this.id})
        .then(function ({data}) {
          this_vm.case_list = data.list;
          this_vm.page = data.page_num;
          this_vm.total_page = data.total_page;
        });
    },
    save_patient: function() {
      if (this.for_new) {
        Object.assign(this.modal_info, this.new_modal_info);
        this.modal_content = [this.data];
      }
      else {
        Object.assign(this.modal_info, this.update_modal_info);
        this.modal_content = [this.old_data, this.data];
      }
      this.$bvModal.show(this.modal_id);
    },
    delete_patient: function() {
      Object.assign(this.modal_info, this.delete_modal_info);
      this.modal_content = [this.old_data];
      this.$bvModal.show(this.modal_id);
    },
    confirm_save: function() {
      var this_vm = this;
      this.post_patient(this.data)
      .then(function({data}) {
        if (data.success) {
          if (this_vm.for_new) {
            this_vm.$bvModal.hide(this_vm.modal_id);
            Alerts.push('新建成功!', 'success');
            this_vm.$router.push({name: 'patient', params: {id: data.data.id}});
          }
          else {
            this_vm.$bvModal.hide(this_vm.modal_id);
            Alerts.push('修改成功!', 'success');
          }
        }
      });
    },
    confirm_delete: function() {
      var this_vm = this;
      this.delete_patient_by_id(this.data.id)
      .then(function({data}) {
        if (data.success) {
          this_vm.$bvModal.hide(this_vm.modal_id);
          Alerts.push('删除成功!', 'success');
          this_vm.$router.back();
        }
      });
    },
    linkGen: function(pageNum) {
      return {
        name: 'patient',
        params: { id: this.id },
        query: { page: pageNum }
      };
    }
  }
}
</script>

<style scoped>
.caption-top {
  caption-side: top;
}
.margin-100 {
  margin: 100px
}
</style>
