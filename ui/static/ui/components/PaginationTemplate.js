Vue.component('pagination-template', {
  delimiters: ['[%', '%]'],
  props: ['info', 'jump'],
  template: `
  <div v-if="info.current" class="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
    <div class="btn-group mr-2" role="group" aria-label="First group">
      <button type="button" class="btn" :class="[is_first? 'btn-outline-secondary' : 'btn-outline-primary']" v-on:click="jump(1)" :disabled="is_first">&lt&lt</button>
      <button type="button" class="btn" :class="[is_first? 'btn-outline-secondary' : 'btn-outline-primary']" v-on:click="jump(info.current - 1)" :disabled="is_first">&lt</button>

      <button v-for="index in nums()" :key="index" type="button" class="btn" :class="[is_current(index)? 'btn-outline-secondary' : 'btn-outline-primary']" v-on:click="jump(index)" :disabled="is_current(index)">[%index%]</button>

      <button type="button" class="btn" :class="[is_last? 'btn-outline-secondary' : 'btn-outline-primary']" v-on:click="jump(info.current + 1)" :disabled="is_last">&gt</button>
      <button type="button" class="btn" :class="[is_last? 'btn-outline-secondary' : 'btn-outline-primary']" v-on:click="jump(info.total)" :disabled="is_last">&gt&gt</button>
    </div>
  </div>
  `,
  computed: {
    is_first: function() {
      return this.info.current == 1;
    },

    is_last: function() {
      return this.info.current == this.info.total;
    }
  },
  methods: {
    is_current: function(num) {
      return this.info.current == num;
    },
    nums: function() {
      var first = 1;
      var current = this.info.current;
      var last = this.info.total;

      var left = current - first;
      var right = last - current;
      var distance = last - first;

      if (distance <= 6) {
        var start = first;
        var end = last;
      }
      else {
        if (left < 3) {
          var start = first;
          var end = current - left + 6;
        }
        else if (right < 3) {
          var start = current + right - 6;
          var end = last;
        }
        else {
          var start = current - 3;
          var end = current + 3;
        }
      }
      return _.range(start, end + 1);
    }
  }
});
