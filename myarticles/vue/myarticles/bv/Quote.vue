<template>
<div style="margin: 5px">
    <b-row>
      <b-col cols="12">
        <b-card>

          <p class="card-text">
            <blockquote>
            <mymedia-text :value="value.texts" :multiline="true"
              @input="v => {value.texts=v; update();}"> </mymedia-text>
            </blockquote>
          </p>

          <p slot='footer'>
            <em slot="footer">引用元:
              <mymedia-text :value="value.source"
                @input="v => {value.source=v; update();}"> </mymedia-text>
            </em>
            <em slot="footer">
              <a :href="value.url">URL</a>:
              <mymedia-text :value="value.url"
                @input="v => {value.url=v; update();}"> </mymedia-text>
            </em>
          </p>
        </b-card>
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
        return {url: 'New URL', texts:'New Quote', source:'New Source', content_type: 'myarticles_quote'};
    },
    update(){
      this.$root.send('element-list', this.value).then((res)=>{
          this.$emit('input', this.value);
      });
    },
  }
}
</script>
