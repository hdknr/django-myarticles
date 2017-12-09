var myArticlesLink = Vue.extend({
  props: ['value', ],
  template: '#myarticles_link_template',
  mixins: [myArticleElement],
  components:{ 'mymedia-text': TextComponent, },
  methods: {
    newInstance(){
        return {
            page_data:{url: ''}, content_type: 'myarticles_link'};
    },
    update(){
        this.send(this.value).then((res) =>{
            Vue.set(this, 'value', res.data);
            this.$emit('input', this.value);
        });
    }
  }
});
