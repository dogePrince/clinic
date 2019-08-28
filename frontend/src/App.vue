<template>
  <div id="app">
    <navbar-compo></navbar-compo>
    <div class="body-div">
      <breadcrumb-compo></breadcrumb-compo>
      <div class="container">
        <alert-compo :alerts="alerts_list"></alert-compo>
        <div class="row justify-content-center">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavbarCompo from "./components/NavbarCompo.vue";
import BreadcrumbCompo from "./components/BreadcrumbCompo.vue";
import AlertCompo from "./components/AlertCompo.vue";
import Alerts from "./mixins/Alerts.js"

export default {
  name: 'app',
  components: {NavbarCompo, BreadcrumbCompo, AlertCompo},
  data: function() {
    return {
      alerts_list: Alerts.alerts_list
    };
  }
}
</script>

<style scoped>
.body-div {
  padding-top: 72px;
}
.container {
  position: relative;
}
</style>
