Vue.component('auto-text-template', {
  delimiters: ['[%', '%]'],
  props: ['value'],
  template: `
    <textarea class="textarea form-control" ref="textarea" :value="value" @input="$emit('input', $event.target.value)"></textarea>
  `,
  methods: {
    auto_height: function() {
      this.$refs.textarea.style.height = '100px';
      this.$refs.textarea.style.height = this.$refs.textarea.scrollHeight + 'px';
    },
  },
  updated: function() {
    this.auto_height();
  }
});
