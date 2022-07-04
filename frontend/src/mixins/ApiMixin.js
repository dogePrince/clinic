export default {
  beforeCreate: function() {
    this.axios_instance = this.axios.create({
      baseURL: '/backend',
      timeout: 1000
    });
  },
  methods: {
    get_patient: function({ page=null, recent_field=null } = {}) {
      return this.axios_instance.get('/patient', {
        params: {
          page: page,
          recent_field: recent_field
        }
      });
    },
    get_patient_option: function() {
      return this.axios_instance.get('/patient', {
        params: {
          tiny_field: true
        }
      });
    },
    get_patient_by_id: function(id, { recent_field=null } = {}) {
      return this.axios_instance.get(`/patient/${id}`, {
        params: {
          recent_field: recent_field
        }
      });
    },
    post_patient: function(form) {
      return this.axios_instance.post('/patient/save', {
        id: form.id,
        name: form.name,
        sex: form.sex,
        age: form.age,
        phone_number: form.phone_number,
        register_date: form.register_date.toJSON()
      })
    },
    delete_patient_by_id: function(id) {
      return this.axios_instance.get(`/patient/delete`, {
        params: {
          id: id
        }
      });
    },
    get_case: function({ page=null, patient_field=null, patient_id=null } = {}) {
      return this.axios_instance.get('/case', {
        params: {
          page: page,
          patient_field: patient_field,
          patient_id: patient_id
        }
      });
    },
    get_case_by_id: function(id, { patient_field=null } = {}) {
      return this.axios_instance.get(`/case/${id}`, {
        params: {
          patient_field: patient_field
        }
      });
    },
    post_case: function(form) {
      return this.axios_instance.post('/case/save', {
        id: form.id,
        patient: form.patient,
        pub_date: form.pub_date.toJSON(),
        symptom: form.symptom,
        template: form.template,
        prescription: form.prescription
      })
    },
    delete_case_by_id: function(id) {
      return this.axios_instance.get(`/case/delete`, {
        params: {
          id: id
        }
      });
    },
    get_template: function({ page=null } = {}) {
      return this.axios_instance.get('/template', {
        params: {
          page: page
        }
      });
    },
    get_template_option: function() {
      return this.axios_instance.get('/template', {
        params: {
          tiny_field: true
        }
      });
    },
    get_template_by_id: function(id) {
      return this.axios_instance.get(`/template/${id}`);
    },
    post_template: function(form) {
      return this.axios_instance.post('/template/save', {
        id: form.id,
        name: form.name,
      })
    },
    delete_template_by_id: function(id) {
      return this.axios_instance.get(`/template/delete`, {
        params: {
          id: id
        }
      });
    },
    get_search: function(search_url) {
      return this.axios_instance.get(search_url);
    }
  }
}
