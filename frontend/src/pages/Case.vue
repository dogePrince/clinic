<template>
  <div class="col-8">
    <h2 v-if="for_new">新建病例</h2>
    <h2 v-else>
      病例详情
      <span class="font-20"> / <router-link :to="{name: 'patient', params:{id: data.patient}}">回到访客 {{patient_name}}</router-link></span>
    </h2>
    <case-form :data="data" :patient_list="patient_list" :template_list="template_list"></case-form>

    <div class="row">
      <div v-if="for_new" class="col-12">
        <b-button variant="primary" @click="save_case">新建病例</b-button>
      </div>
      <div v-else class="col-12">
        <b-button variant="primary" @click="save_case" class="mr-2">更改病例</b-button>
        <b-button variant="danger" @click="delete_case">删除病例</b-button>
        <b-button :to="{name: 'case', params: {id: 'new'}, query: {case: id}}" class="float-right" variant="primary">复制病例</b-button>
      </div>
    </div>

    <modal-compo :id="modal_id" :info="modal_info">
      <case-info :info="modal_content" :patient_list="patient_list" :template_list="template_list"></case-info>
    </modal-compo>
  </div>
</template>

<script>
import CaseForm from "../components/CaseForm.vue";
import ModalCompo from "../components/ModalCompo.vue";
import CaseInfo from "../components/CaseInfo.vue";
import Alerts from "../mixins/Alerts.js"

export default {
  props: ['id'],
  components: {CaseForm, ModalCompo, CaseInfo},
  data: function() {
    return {
      data: {},
      old_data: {},
      modal_id: 'modal_id',
      modal_info: {},
      modal_content: [{}],
      patient_list: [],
      template_list: [],
      new_modal_info: {
        title: '确认新建吗？',
        btn: {
          text: '新建病例',
          variant: 'primary',
          onClick: this.confirm_save
        }
      },
      update_modal_info: {
        title: '确认更改吗？',
        btn: {
          text: '更改病例',
          variant: 'primary',
          onClick: this.confirm_save
        }
      },
      delete_modal_info: {
        title: '确认删除吗？',
        btn: {
          text: '删除病例',
          variant: 'danger',
          onClick: this.confirm_delete
        }
      }
    };
  },
  created: function() {
    this.init_page();
    this.load_patient_list();
    this.load_template_list();
  },
  watch: {
    id: function() {
      this.init_page();
    }
  },
  computed: {
    for_new: function() {
      return this.id == 'new';
    },
    patient_name: function() {
      for (let item of this.patient_list) {
        if (item.id == this.old_data.patient) {
          return "“" + item.name + "”";
        }
      }
      return ''
    }
  },
  methods: {
    init_page: function() {
      var this_vm = this;
      if (this.for_new) {
        if (this.$route.query.patient) {
          this.data = {patient: parseInt(this.$route.query.patient), template: null, prescription: '', pub_date: new Date()};
        }else if(this.$route.query.case) {
          this.get_case_by_id(parseInt(this.$route.query.case, 10))
          .then(function ({data}) {
            data.pub_date = new Date();
            this_vm.data = data;
            this_vm.data.id = null;
          });
        }
        else {
          this.data = {template: null, prescription: '', pub_date: new Date()};
        }
      }
      else {
        this.get_case_by_id(parseInt(this.id, 10))
        .then(function ({data}) {
          data.pub_date = new Date(data.pub_date);
          this_vm.data = data;
          this_vm.old_data = _.clone(data);
        }).catch(function (error) {
          Alerts.push('该页面不存在!', 'danger');
          this_vm.$router.back();
        });
      }
    },
    chinese_compare: function(var1, var2) {
      return var1.name.localeCompare(var2.name, "zh-CN");
    },
    load_patient_list: function() {
      var this_vm = this;
      this.get_patient({recent_field: true})
      .then(function({data}) {
        this_vm.patient_list = data.list.sort(this_vm.chinese_compare);
      });
    },
    load_template_list: function() {
      var this_vm = this;
      this.get_template()
      .then(function({data}) {
        this_vm.template_list = data.list.sort(this_vm.chinese_compare);
      });
    },
    save_case: function() {
      if (this.for_new) {
        Object.assign(this.modal_info, this.new_modal_info);
        this.modal_content = [this.data];
      }
      else {
        Object.assign(this.modal_info, this.update_modal_info);
        this.modal_content = [this.old_data, this.data];
      }
      this.$bvModal.show(this.modal_id)
    },
    delete_case: function() {
      Object.assign(this.modal_info, this.delete_modal_info);
      this.modal_content = [this.old_data];
      this.$bvModal.show(this.modal_id);
    },
    confirm_save: function() {
      var this_vm = this;
      this.post_case(this.data)
      .then(function({data}) {
        if (data.success) {
          if (this_vm.for_new) {
            this_vm.$bvModal.hide(this_vm.modal_id);
            Alerts.push('新建成功!', 'success');
            this_vm.$router.push({name: 'case', params: {id: data.data.id}});
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
      this.delete_case_by_id(this.data.id)
      .then(function({data}) {
        if (data.success) {
          this_vm.$bvModal.hide(this_vm.modal_id);
          Alerts.push('删除成功!', 'success');
          this_vm.$router.back();
        }
      });
    }
  }
}
</script>

<style scoped>
.font-20 {
  font-size: 20px;
}
</style>
