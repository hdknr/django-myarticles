<template>
<div style="min-height: 10px;"
  @mouseenter="visible=true"
  @mouseleave="visible=false" class="my-1 py-2 border border-success rounded">

  <b-row v-if="!visible">
    <b-col cols="12" class="text-center bg-success text-white" >
      Add Element ....
    </b-col>
  </b-row>

  <b-row  v-else>
    <b-col cols="10">
    <b-nav>
        <b-nav-item @click="$emit('on-new','myarticles_section')">Section</b-nav-item>
        <b-nav-item @click="$emit('on-new','myarticles_subsection')">Subsecton</b-nav-item>
        <b-nav-item @click="$emit('on-new','myarticles_text')">Text</b-nav-item>
        <b-nav-item @click="$emit('on-new','myarticles_link')">Link</b-nav-item>
        <b-nav-item @click="$emit('on-new','myarticles_image')">Image</b-nav-item>
        <b-nav-item @click="$emit('on-new','myarticles_slide')">Slide</b-nav-item>
        <b-nav-item @click="$emit('on-new','myarticles_quote')">Quote</b-nav-item>
        <b-nav-item @click="$emit('on-new','myarticles_location')">Location</b-nav-item>
    </b-nav>
    </b-col>
    <b-col cols="2" v-if="showDelete">
        <b-button variant="danger" class="far fa-trash-alt" @click="$emit('on-delete')">
            Delete
        </b-button>
    </b-col>
  </b-row>
</div>
</template>

<script>
export default {
  props: ['position', 'showDelete'],
  data: function(){
    return { visible: false };
  }
}
</script>
