<template>
  <div style="margin: 5px">
    <b-row>
      <b-col cols="12">
        <mymedia-text
          :value="value.texts"
          :multiline="true"
          @input="v => {value.texts=v; update();}"> </mymedia-text>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import TextEdit from 'mymedia/bv/Text.vue'

export default {
  props: ['value', ],
  components:{ 'mymedia-text': TextEdit, },
  methods: {
    newInstance(){
      return {texts: 'New Text', content_type: 'myarticles_text'};
    },
    update(){
      this.$root.send('element-list', this.value).then((res)=>{
          this.$emit('input', this.value);
      });
    },
  }
}

</script>
