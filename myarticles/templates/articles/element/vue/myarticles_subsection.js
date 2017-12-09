var myArticlesSubsection= Vue.extend({
  props: ['value', ],
  template: '#myarticles_subsection_template',
  mixins: [myArticleElement],
  components:{ 'mymedia-text': TextComponent, },
  methods: {
    newInstance(){
        return {title: 'New Subsection', content_type: 'myarticles_subsection'};
    },
    update(title){
        this.value.title = title;
        this.send(this.value).then((res) =>{
            this.$emit('input', this.value);
        });
    }
  }
});
