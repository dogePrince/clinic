Vue.component('template-form-template', {
  delimiters: ['[%', '%]'],
  props: ['template_obj'],
  template: `
    <form>
      <input type="hidden" name="id" id="id_id" v-if="template_obj.id" v-model="template_obj.id" >
      <div class="form-row">
        <div class="form-group">
          <label>名称</label>
          <input class="form-control" type="text" v-model="template_obj.name" placeholder="输入名称">
        </div>
      </div>
      <div class="form-row">
        <div class="form-group col-md-12">
          <label>配方</label>
          <textarea class="textarea form-control" v-model="template_obj.prescription"></textarea>
        </div>
      </div>
    </form>
  `
});
