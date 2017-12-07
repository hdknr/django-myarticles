var myArticlesLink = Vue.extend({
  props: ['value', ],
  template: '#myarticles_link_template',
  mixins: [myArticleElement],
  components:{ 'mymedia-text': TextComponent, },
  methods: {
    update(){
        this.send(this.value).then((res) =>{
            Vue.set(this, 'value', res.data);
            this.$emit('input', this.value);
        });
    }
  }
});
