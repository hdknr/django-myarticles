var myArticleElement = {
  data: function(){
    return {
      url: "{% url 'element-list' %}"
    };
  },
  methods: {
    get_endpoint(instance){
        base_url =  this.url;
        return (instance.id) ? base_url+ instance.id + '/' : base_url;
    },
    send(instance){
        var url = this.get_endpoint(instance);
        var config = {};
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        var method = instance.id ? 'patch': 'post';
        return axios[method](url, instance, config);
    }
  } {# methods #}
}   {# myArticleElement #}
