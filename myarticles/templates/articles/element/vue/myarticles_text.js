var myArticlesText = Vue.extend({
  props: ['value', ],
  template: '#myarticles_text_template',
  mixins: [myArticleElement],
  components:{ 'mymedia-text': TextComponent, },
  methods: {
    update(texts){
        this.value.texts = texts;
        this.send(this.value).then((res) =>{
            this.$emit('input', this.value);
        });
    }
  }
});
