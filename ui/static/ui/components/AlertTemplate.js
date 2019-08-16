Vue.component('alert-template', {
  delimiters: ['[%', '%]'],
  props: ['status'],
  template: `
  <div class="alert" :class="status_class" role="alert">
    <slot></slot>
  </div>
  `,
  computed: {
    status_class: function() {
      return 'alert-' + this.status;
    }
  }
});
