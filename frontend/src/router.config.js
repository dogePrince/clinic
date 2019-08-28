import Home from './pages/Home.vue'
import Search from './pages/Search.vue'
import Statistic from './pages/Statistic.vue'
import Patient from './pages/Patient.vue'
import Case from './pages/Case.vue'
import Template from './pages/Template.vue'

export default{
  routes: [
    {path: '/', name:'home', component: Home},
    {path: '/search/:type', name:'search', component: Search},
    {path: '/statistic', name:'statistic', component: Statistic},
    {path: '/patient/:id', name:'patient', component: Patient, props: true},
    {path: '/case/:id', name:'case', component: Case, props: true},
    {path: '/template/:id', name:'template', component: Template, props: true},
    {path: '*', redirect: '/'},
  ]
}
