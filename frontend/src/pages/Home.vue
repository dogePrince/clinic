<template>
  <div class="col-12">
    <div class="row justify-content-center">
      <div class="col-7">
        <div class="row justify-content-center">
          <br/>
          <b-row align-v="center">
            <img src="../image/brand.svg" width="90" height="60" alt="dp">
            <span class="font-h1">诊所系统</span>
          </b-row>
        </div>
        <br/><br/>
      </div>

      <div class="col-7">
        <div class="row justify-content-center">
          <div class="col-4 text-center">
            <b-button :to="{name: 'search', params: {type: 'patient'}}" variant="outline-secondary">
              <div class="text-center">
                <img src="../image/search.svg" width="160" height="160" alt="病例搜索">
              </div>
              <div class="font-h3 text-center">病例搜索</div>
            </b-button>
          </div>

          <div class="col-4 text-center">
            <b-button :to="{name: 'patient', params: {id: 'new'}}" variant="outline-secondary">
              <div class="text-center">
                <img src="../image/add_patient.svg" width="160" height="160" alt="新建访客">
              </div>
              <div class="font-h3 text-center">新建访客</div>
            </b-button>
          </div>

          <div class="col-4 text-center">
            <b-button :to="{name: 'statistic'}" variant="outline-secondary">
              <div class="text-center">
                <img src="../image/statistic.svg" width="160" height="160" alt="数据统计">
              </div>
              <div class="font-h3 text-center">数据统计</div>
            </b-button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.font-h1 {
  font-size: 50px
}
.font-h3 {
  font-size: 30px
}
</style>
