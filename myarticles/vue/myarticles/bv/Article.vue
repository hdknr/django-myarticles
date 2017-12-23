<template>
<b-row v-if="value" no-gutters="true">

<b-col cols="12" style="min-height:120px">
  <b-row >
    <b-col cols="10">
      <h2 class="fluid">
         <mymedia-text :value="value.title" @input="v => {value.title = v; update();}"> </mymedia-text>
      </h2>


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
      :src="value.catch.data" v-if="value.catch">
    </b-img>
    <b-btn @click="$refs.gallery.$refs.dialog.show()" v-else>Click to select MediaFile</b-btn>

    <mymedia-gallery ref="gallery" @on-select="onImageSelected"></mymedia-gallery>
    </div>
  </b-col>

  <b-col :cols="meta_cols" v-if="show_meta" style="transition: .4s; " >
    <b-card no-body class="mx-1">
      <b-tabs card>

        <b-tab title="Description">
         <mymedia-text
            :value="value.description" :multiline="true"
            @input="v => {value.description = v; update();}">
          </mymedia-text>
        </b-tab>

        <b-tab title="Keywords">
         <mymedia-text
            :value="value.keywords" :multiline="true"
            @input="v => {value.keywords = v; update();}">
          </mymedia-text>
        </b-tab>

        <b-tab no-body title="Catch Picture" active v-if="value.catch">
          <mymedia-mediafile v-model="value.catch"></mymedia-mediafile>
        </b-tab>

      </b-tabs>
    </b-card>
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
    return {
      show_meta: false,
    };
  },
  created(){
    console.log("article.....", this.value);
  },
  computed:{
    endpoint(){
        return this.$root.env.endpoint['article-list'];
    },
    main_cols(){ return this.show_meta ?  8: 12; },
    meta_cols(){ return this.show_meta ?  4: 0; },
  },
  methods: {
    update(){
      this.$root.send('article-list', this.value).then((res)=>{
          this.$emit('input', this.value);
      });
    },
    onImageSelected(image, selected){
      if(selected == true){
        this.value.catch = image;
        this.$refs.gallery.$refs.dialog.hide();
        this.update();
      }
    }
  }
}
</script>
