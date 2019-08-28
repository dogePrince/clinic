import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueRouter from 'vue-router'
import routerConfig from './router.config.js'
import VueLodash from 'vue-lodash'
import axios from 'axios'
import VueAxios from 'vue-axios'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import ApiMixin from "./mixins/ApiMixin.js"

Vue.config.productionTip = false;

const options = { name: 'lodash' };
Vue.use(VueLodash, options);
Vue.use(VueAxios, axios)
Vue.use(BootstrapVue);
Vue.use(VueRouter);

Vue.mixin(ApiMixin);
Vue.mixin({
  beforeCreate: function() {
    this.sexes = {"F": "女", "M": "男", "O": "其他"};
  }
});

const router = new VueRouter(routerConfig);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
