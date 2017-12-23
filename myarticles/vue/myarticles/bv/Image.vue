<template>
<b-row v-if="value" no-gutters="true">

<b-col cols="12">
  <b-row >
    <b-col cols="10">
    </b-col>
    <b-col cols="2" class="text-right">
      <mymedia-toggle v-model="show_meta"> </mymedia-toggle>
    </b-col>
  </b-row>

  <b-row>
  <b-col :cols="main_cols" style="transition: .4s;">
    <div class="mx-1">

    <b-img fluid class="rounded" style="padding-top: 5px"
      @click="$refs.gallery.$refs.dialog.show()"
      :src="value.mediafile.data" v-if="value.mediafile.data">
    </b-img>
    <b-button v-else @click="$refs.gallery.$refs.dialog.show()">Select Image</b-button>

    <mymedia-gallery ref="gallery" @on-select="onImageSelected"></mymedia-gallery>
    </div>
  </b-col>

  <b-col :cols="meta_cols" v-if="show_meta" style="transition: .4s; " >
    <mymedia-mediafile v-model="value.mediafile"></mymedia-mediafile>
  </b-col>
</b-row>

</b-col>
</b-row>
</template>

<script>
import Text from 'mymedia/bv/Text.vue'
import Gallery from 'mymedia/bv/Gallery.vue'
import MediaFileEditor from 'mymedia/bv/MediaFileEditor.vue'
import Toggle from 'mymedia/bv/Toggle.vue'


export default {
  props: ['value', ],
  components:{
    'mymedia-text': Text,
    'mymedia-gallery': Gallery,
    'mymedia-mediafile': MediaFileEditor,
    'mymedia-toggle': Toggle,
  },
  data: function(){
    return {show_meta: false};
  },
  computed:{
      main_cols(){ return this.show_meta ?  8: 12; },
      meta_cols(){ return this.show_meta ?  4: 0; },
  },
  methods: {
    newInstance(){
        return {content_type: 'myarticles_image', mediafile: {data: null}};
    },
    update(){
      this.$root.send('element-list', this.value).then((res)=>{
          vm.$emit('input', this.value);
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
}

</script>
