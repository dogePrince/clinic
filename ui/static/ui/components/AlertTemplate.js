Vue.component('alert-template', {
  delimiters: ['[%', '%]'],
  props: ['status'],
  template: `
  <div class="alert" :class="status_dict[status]" role="alert">
    <slot></slot>
  </div>
  `,
  data: function() {
    return {
      status_dict: {
        "success": 'alert-success',
        "failed": 'alert-danger'
      }
    };
  }
});
