<template>
  <div class="col-12">
    <div class="row justify-content-center">
      <div class="col-8">
        <h2>处方管理</h2>

        <div class="row">
          <div class="col-4">
            <b-input v-model="data.name" id="template-name" placeholder="输入处方名" ref="inputVal" @keyup.enter.native="save_template" autofocus></b-input>
          </div>
          <div class="col-6">
            <b-button variant="primary" @click="save_template">添加</b-button>
          </div>
        </div>
      </div>

      <div class="col-8">
        <div class="row">
          <div class="col-12">
            <b-button variant="primary-outline" class="float-right">
              <img src="../image/setting2.svg" @click="show_delete" width="30" height="30" alt="管理">
            </b-button>
          </div>
        </div>
        <div class="row">
          <div class="text-center col-3 border" v-for="(template,index) in template_list" :key="template.id">
            <div class="row justify-content-center">
              <div class="col-8 text-center">
                {{template.name}}
              </div>
              <div class="col-4 text-right" v-if="delete_visible">
                <b-link @click="delte_template(index)">删除</b-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <modal-compo :id="modal_id" :info="delete_modal_info">
      删除“{{template_info}}”
    </modal-compo>
  </div>
</template>

<script>
import ModalCompo from "../components/ModalCompo.vue";
import Alerts from "../mixins/Alerts.js"

export default {
  components: {ModalCompo},
  data: function() {
    return {
      template_list: [],
      data: {},
      modal_id: 'modal_id',
      delete_visible: false,
      delete_modal_info: {
        title: '确认删除吗？',
        btn: {
          text: '删除处方',
          variant: 'danger',
          onClick: this.confirm_delete
        }
      },
      delete_target: -1,
      template_info: ''
    };
  },
  created: function() {
    this.load_template_list();
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
    show_delete: function() {
      this.delete_visible = !this.delete_visible;
    },
    load_template_list: function() {
      var this_vm = this;
      this.get_template()
      .then(function({data}) {
        this_vm.template_list = data.list.sort(this_vm.chinese_compare);
      });
    },
    save_template: function() {
      var this_vm = this;
      this.post_template(this_vm.data)
      .then(function({data}) {
        if (data.success) {
          Alerts.push('新建成功!', 'success');
          this_vm.load_template_list();
        }
      });
      this.data.name = "";
      this.$refs.inputVal.focus();
    },
    delte_template(index) {
      this.delete_target = this.template_list[index].id;
      this.template_info = this.template_list[index].name;
      this.$bvModal.show(this.modal_id);
    },
    confirm_delete: function() {
      var this_vm = this;
      this.delete_template_by_id(this.delete_target)
      .then(function({data}) {
        if (data.success) {
          this_vm.$bvModal.hide(this_vm.modal_id);
          Alerts.push('删除成功!', 'success');
          this_vm.load_template_list();
        }
      });
    },
    chinese_compare: function(var1, var2) {
      return var1.name.localeCompare(var2.name, "zh-CN");
    },
  }
}
</script>
