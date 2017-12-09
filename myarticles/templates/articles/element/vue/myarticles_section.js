myArticlesSection = Vue.extend({
  template: '#myarticles_section_template',
  mixins: [myArticleElement],
  props: ['value', ],
  components:{ 'mymedia-text': TextComponent, },
  methods: {
    newInstance(){
        return {title: 'New Section', content_type: 'myarticles_section'};
    },
    update(title){
        this.value.title = title;
        this.send(this.value).then((res) =>{
            this.$emit('input', this.value);
        });
    }
  }
});
