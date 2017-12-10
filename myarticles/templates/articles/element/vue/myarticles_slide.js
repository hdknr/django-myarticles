var myArticlesSlide = Vue.extend({
  template: '#myarticles_slide_template',
  props: ['value', ],
  mixins: [myArticleElement],
  components: {
    'mymedia-album': AlbumComponent
  },
  data: function(){
    return {
    };
  },
  methods: {
    newInstance(){
        return {album: {title:'New Album', mediafiles:[]}, content_type: 'myarticles_slide'};
    },
    update(){
        this.send(this.value).then((res) =>{
            this.$emit('input', res.data);
        });
    }
  }
});
