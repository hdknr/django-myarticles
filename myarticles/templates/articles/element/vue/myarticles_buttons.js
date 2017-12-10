var myArticlesButtons = Vue.extend({
  template: '#myarticles_buttons_template',
  props: ['position', 'showDelete'],
  data: function(){
    return {
        visible: false
    };
  },
  computed:{
  },
  methods: {
  }
});
