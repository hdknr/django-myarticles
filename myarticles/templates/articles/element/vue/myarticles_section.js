var myArticlesSection = Vue.extend({
  template: '#myarticles_section_template',
  props: ['value', ],
  components:{
    'mymedia-text': TextComponent,
  },
  data: function(){
    return {
    };
  },
  created(){
  },
  methods: {
    get_endpoint(instance){
        url = "{% url 'element-list' %}";
        if(instance.id){
            return url+ instance.id + '/';
        }
        return url;
    },
    send(){
        var url = this.get_endpoint(this.value);
        var vm = this;
        var config = {};
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        var method = vm.value.id ? 'patch': 'post';
        return axios[method](url, vm.value, config).then((res) =>{
            vm.$emit('input', vm.value);
        });
    },
    update(title){
        this.value.title = title;
        this.send();
    }
  }
});
