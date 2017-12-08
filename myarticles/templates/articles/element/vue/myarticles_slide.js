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
  created(){
  },
  methods: {
    update(){
        this.send(this.value).then((res) =>{
            Vue.set(this, 'value', res.data);
            this.value.album.current = this.value.album.mediafiles[0];
            this.$emit('input', this.value);
        });
    }
  }
});
