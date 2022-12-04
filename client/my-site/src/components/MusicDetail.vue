<!-- アルバム詳細情報 -->
<template>
  <v-container>
    <v-row class="text-center ma-3">
      <v-col cols="12">
        <span class="text-h5">DISCOGRAPHY</span>
      </v-col>
    </v-row>
    <v-row class="text-center ma-3">
      <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
        <div>
          <v-img
            max-width="400"
            max-hight="400"
            :src="albumLists[this.$route.params.id]['image']"
            class="mx-auto my-5"
          ></v-img>
        </div>
      </v-col>
      <v-col
        cols="12"
        xs="12"
        sm="12"
        md="6"
        lg="6"
        xl="6"
        class="d-flex mt-3 flex-no-wrap justify-space-between"
      >
        <div>
          <v-card-title
            class="text-left"
            v-text="albumLists[this.$route.params.id]['title']"
          ></v-card-title>
          <v-card-subtitle class="pb-0 mb-0 text-left">{{
            convertDate(albumLists[this.$route.params.id]["releasedate"])
          }}</v-card-subtitle>
          <v-card-subtitle class="pt-0 mt-0 text-left">{{
            albumLists[this.$route.params.id]["section"]
          }}</v-card-subtitle>
          <v-card-subtitle
            v-for="(data, index) in albumLists[this.$route.params.id]['track']"
            :key="index"
            class="mb-2 pb-0 pt-0 mt-0 text-left"
            ><span v-if="index.includes('track') && data != null">
              {{ concertInt(index) + ".&nbsp;&nbsp;&nbsp;" + data }}
            </span></v-card-subtitle
          >
          <v-card-title>
            <div class="d-flex">
              <v-btn
                class="pl-0 ml-0"
                :href="albumLists[this.$route.params.id]['apple_url']"
                outlined
                small
                fab
              >
                <v-icon>fa-brands fa-apple</v-icon>
              </v-btn>
              <v-btn
                class="ml-5"
                :href="albumLists[this.$route.params.id]['spotify_url']"
                outlined
                small
                fab
              >
                <v-icon>fa-brands fa-spotify</v-icon>
              </v-btn>
              <v-btn
                class="ml-5"
                :href="albumLists[this.$route.params.id]['line_url']"
                outlined
                small
                fab
              >
                <v-icon>fa-brands fa-line</v-icon>
              </v-btn>
            </div>
          </v-card-title>
          <v-card-title>
            <v-btn
              depressed
              color="black text-button"
              :href="albumLists[this.$route.params.id]['url']"
              ><span class="color">配信サイト一覧</span>
            </v-btn>
          </v-card-title>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "MusicDetail",
  data: () => ({
    model: null,
  }),
  computed: {
    cardWidth: function () {
      let val = 380;
      if (this.$vuetify.breakpoint.xs) {
        val = 220;
      }
      return val;
    },
    albumLists: function () {
      return this.$store.state.albumLists;
    },
  },
  created: function () {
    if (this.albumLists.length == 0) {
      this.getLiveList();
    }
  },
  methods: {
    getLiveList() {
      this.axios
        .get(process.env.VUE_APP_API_URL + "album/")
        .then((response) => {
          this.$store.dispatch("setAlbumList", { albumLists: response.data });
        })
        .catch((e) => {
          console.log(e);
        });
    },
    convertDate(date) {
      let dateObj = new Date(date);
      let dateYear = dateObj.getFullYear();
      let dateMonth = dateObj.getMonth() + 1;
      let dateDate = dateObj.getDate();
      let newDate = dateYear + "." + dateMonth + "." + dateDate;
      return newDate;
    },
    concertInt(track) {
      let result = track.substr(6);
      return result;
    },
  },
};
</script>
<style>
.padding {
  padding: 0 10%;
}
.color {
  color: white;
}
</style>
