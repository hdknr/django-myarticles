var myArticlesImage = Vue.extend({
  template: '#myarticles_image_template',
  props: ['value', ],
  mixins: [myArticleElement],
  components:{
    'mymedia-text': TextComponent,
    'mymedia-gallery': Gallery,
    'mymedia-mediafile': MediaFileComponent,
    'mymedia-toggle': ToggleComponent,
  },
  data: function(){
    return {show_meta: false};
  },
  computed:{
      main_cols(){ return this.show_meta ?  8: 12; },
      meta_cols(){ return this.show_meta ?  4: 0; },
  },
  methods: {
    update(){
        this.send(this.value).then((res) =>{
            Vue.set(this, 'value', res.data);
            this.$emit('input', this.value);
        });
    },
    onImageSelected(image, selected){
      if(selected == true){
          Vue.set(this.value, 'mediafile', image);
          this.$emit('input', this.value);
          this.$refs.gallery.$refs.dialog.hide();
          this.update();
      }
    }
  }
});
