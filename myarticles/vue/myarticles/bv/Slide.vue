<template>
  <div style="margin: 5px">
    <b-row>
      <b-col cols="12">

        <mymedia-album
          :modal-state="true"
          :value="value.album"
          @input="v => {value.album=v; update();}">
        </mymedia-album>

      </b-col>
    </b-row>
  </div>
</template>

<script>
import Album from 'mymedia/bv/Album.vue'

export default {
  props: ['value', ],
  components:{'mymedia-album': Album},
  methods: {
    newInstance(){
      return {album: {title:'New Slide', mediafiles:[]}, content_type: 'myarticles_slide'};
    },
    update(){
      this.$root.send('element-list', this.value).then((res)=>{
          this.$emit('input', this.value);
      });
    },
  }
}

</script>
