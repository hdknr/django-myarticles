<template>
  <div style="margin: 5px">
    <b-row>
      <b-col cols="12">
        <mymedia-text :value="value.page_data.url"
          @input="v => {value.page_data.url=v; update();}"> </mymedia-text>
        <p>
        <div v-if="value.page_data.embed" v-html="value.page_data.embed">
        </div>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import Text from 'mymedia/bv/Text.vue'

export default {
  props: ['value', ],
  components:{ 'mymedia-text': Text, },
  methods: {
    newInstance(){
        return {
            page_data:{url: ''}, content_type: 'myarticles_link'};
    },
    update(){
      this.$root.send('element-list', this.value).then((res)=>{
          vm.$emit('input', this.value);
      });
    },
  }
}
</script>
