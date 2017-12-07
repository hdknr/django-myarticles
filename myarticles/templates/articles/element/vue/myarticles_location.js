var myArticlesLocation = Vue.extend({
  props: ['value', ],
  template: '#myarticles_location_template',
  mixins: [myArticleElement],
  components:{ 'mymedia-text': TextComponent, },
  computed:{
      location_url(){
          res = "//maps.google.co.jp/maps?q=" + encodeURI(this.value.address) + "&output=embed&t=m&z=16&iwloc=";
          console.log("location....", res);
          return res;
      }
  },
  methods: {
    update(){
        this.send(this.value).then((res) =>{
            this.$forceUpdate();
            this.$emit('input', this.value);
        });
    }
  }
});
