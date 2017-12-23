<template>
<div style="margin: 5px">
  <b-row>
    <b-col cols="12">
      <mymedia-text :value="value.address"
        @input="v => {value.address=v; update();}"> </mymedia-text>
      <p></p>
      <iframe class="gmap" width="100%" height="450" frameborder="0" style="border:0" allowfullscreen
        :src="location_url">
      </iframe>
    </b-col>
  </b-row>
</div>
</template>

<script>
import Text from 'mymedia/bv/Text.vue'

export default {
  props: ['value', ],
  components:{ 'mymedia-text': Text, },
  computed:{
      location_url(){
          res = "//maps.google.co.jp/maps?q=" + encodeURI(this.value.address) + "&output=embed&t=m&z=16&iwloc=";
          return res;
      }
  },
  methods: {
    newInstance(){
        return {address: 'New Address', content_type: 'myarticles_location'};
    },
    update(){
      this.$root.send('element-list', this.value).then((res)=>{
          this.$emit('input', this.value);
      });
    },
  }
}

</script>
