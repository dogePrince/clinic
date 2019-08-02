Vue.component('modal-template', {
  delimiters: ['[%', '%]'],
  props: ["info", "confirm"],
  template: `
  <div class="modal fade" :id="info.id" tabindex="-1" role="dialog" :aria-labelledby="info.id+'Label'" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" :class="[size[info.size]]" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" :id="info.id+'Label'">[% info.title %]</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <slot></slot>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">关闭</button>
          <button type="button" class="btn btn-primary" v-on:click="confirm">保存更改</button>
        </div>
      </div>
    </div>
  </div>
  `,
  data: function() {
    return {
      size: {
        "xl": "modal-xl",
        "lg": "modal-lg"
      }
    };
  }
});
