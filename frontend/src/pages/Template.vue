<template>
  <div class="col-8">
    <h2 v-if="for_new">新建模板</h2>
    <h2 v-else>模板详情</h2>
    <template-form :data="data"></template-form>

    <div class="row">
      <div v-if="for_new" class="col-12">
        <b-button variant="primary" @click="save_template">新建模板</b-button>
      </div>
      <div v-else class="col-12">
        <b-button variant="primary" @click="save_template" class="mr-2">更改模板</b-button>
        <b-button variant="danger" @click="delete_template">删除模板</b-button>
      </div>
    </div>

    <modal-compo :id="modal_id" :info="modal_info">
      <template-info :info="modal_content"></template-info>
    </modal-compo>
  </div>
</template>

<script>
import TemplateForm from "../components/TemplateForm.vue";
import ModalCompo from "../components/ModalCompo.vue";
import TemplateInfo from "../components/TemplateInfo.vue";
import Alerts from "../mixins/Alerts.js"

export default {
  props: ['id'],
  components: {TemplateForm, ModalCompo, TemplateInfo},
  data: function() {
    return {
      modal_id: 'modal_id',
      data: {},
      old_data: {},
      modal_info: {},
      modal_content: [{}],
      new_modal_info: {
        title: '确认新建吗？',
        btn: {
          text: '新建模板',
          variant: 'primary',
          onClick: this.confirm_save
        }
      },
      update_modal_info: {
        title: '确认更改吗？',
        btn: {
          text: '更改模板',
          variant: 'primary',
          onClick: this.confirm_save
        }
      },
      delete_modal_info: {
        title: '确认删除吗？',
        btn: {
          text: '删除模板',
          variant: 'danger',
          onClick: this.confirm_delete
        }
      }
    };
  },
  created: function() {
    this.init_page();
  },
  computed: {
    for_new: function() {
      return this.id == 'new';
    }
  },
  watch: {
    id: function() {
      this.init_page();
    }
  },
  methods: {
    init_page: function() {
      var this_vm = this;
      if(this.for_new) {
        this_vm.data = {};
      }
      else {
        this.get_template_by_id(parseInt(this.id, 10))
        .then(function ({data}) {
          this_vm.data = data;
          this_vm.old_data = _.clone(data);
        }).catch(function (error) {
          Alerts.push('该页面不存在!', 'danger');
          this_vm.$router.back();
        });
      }
    },
    save_template: function() {
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
    delete_template: function() {
      Object.assign(this.modal_info, this.delete_modal_info);
      this.modal_content = [this.old_data];
      this.$bvModal.show(this.modal_id);
    },
    confirm_save: function() {
      var this_vm = this;
      this.post_template(this.data)
      .then(function({data}) {
        if (data.success) {
          if (this_vm.for_new) {
            this_vm.$bvModal.hide(this_vm.modal_id);
            Alerts.push('新建成功!', 'success');
            this_vm.$router.push({name: 'template', params: {id: data.data.id}});
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
      this.delete_template_by_id(this.data.id)
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
