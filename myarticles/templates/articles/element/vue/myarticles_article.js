var myArticlesArticle = Vue.extend({
  template: '#myarticles_article_template',
  props: ['value', ],
  components:{
    'mymedia-text': TextComponent,
    'mymedia-gallery': Gallery,
    'mymedia-mediafile': MediaFileComponent,
    'mymedia-toggle': ToggleComponent,
  },
  data: function(){
    return {
      show_meta: false,
      endpoint: "{% url 'article-list' %}",
    };
  },
  computed:{
      main_cols(){ return this.show_meta ?  8: 12; },
      meta_cols(){ return this.show_meta ?  4: 0; },
  },
  methods: {
    get_endpoint(instance){
          if(instance.id){
              return this.endpoint  + instance.id + '/';
          }
          return this.endpoint;
    },
    update(){
      console.log("uploading....")
      var url = this.get_endpoint(this.value);
      var vm = this;
      var config = {};
      axios.defaults.xsrfCookieName = 'csrftoken';
      axios.defaults.xsrfHeaderName = 'X-CSRFToken';
      var method = vm.value.id ? 'patch': 'post';
      return axios[method](url, vm.value, config).then((res) =>{
          console.log("updated...", res);
          vm.$emit('input', vm.value);
      });
    },
    onImageSelected(image, selected){
      if(selected == true){
          this.value.catch = image;
          this.$refs.gallery.$refs.dialog.hide();
          this.update();
      }
    }
  }
});
