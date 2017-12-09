var myArticlesQuote = Vue.extend({
  props: ['value', ],
  template: '#myarticles_quote_template',
  mixins: [myArticleElement],
  components:{ 'mymedia-text': TextComponent, },
  methods: {
    newInstance(){
        return {url: 'New URL', texts:'New Quote', source:'New Source', content_type: 'myarticles_quote'};
    },
    update(){
        this.send(this.value).then((res) =>{
            this.$emit('input', this.value);
        });
    }
  }
});
