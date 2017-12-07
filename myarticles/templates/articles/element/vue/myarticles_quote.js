var myArticlesQuote = Vue.extend({
  props: ['value', ],
  template: '#myarticles_quote_template',
  mixins: [myArticleElement],
  components:{ 'mymedia-text': TextComponent, },
  methods: {
    update(){
        this.send(this.value).then((res) =>{
            this.$emit('input', this.value);
        });
    }
  }
});
