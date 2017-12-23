<template>
  <div style="margin: 5px">
    <b-row>
      <b-col cols="12">
      <h2>
        <mymedia-text
          :value="value.title"
          @input="v => {value.title=v; update();}">
        </mymedia-text>
      </h2>
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
        return {title: 'New Section', content_type: 'myarticles_section'};
    },
    update(){
      this.$root.send('element-list', this.value).then((res)=>{
          this.$emit('input', this.value);
      });
    },
  }
}

</script>
