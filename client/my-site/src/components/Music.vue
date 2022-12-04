<!-- ライブ情報 -->
<template>
  <v-container>
    <v-row class="text-center ma-3">
      <v-col cols="12">
        <span class="text-h5">DISCOGRAPHY</span>
      </v-col>
    </v-row>
    <div v-if="!topPage">
      <v-row class="paddingLiveList">
        <v-col
          :id="index"
          v-for="(data, index) in albumLists"
          :key="index"
          cols="12"
          sm="4"
        >
          <v-card
            color="transparent"
            elevation="0"
            tile
            :id="index"
            class="mx-2"
            @click="showMoreInformation(index)"
          >
            <v-img :src="data.image" height="300px"></v-img>

            <v-card-title v-text="data.title"></v-card-title>

            <v-card-subtitle class="pb-0 mb-0">{{
              convertDate(data.releasedate)
            }}</v-card-subtitle>
            <v-card-subtitle class="pl-4 pt-0 mt-0">{{
              data.section
            }}</v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>
    </div>
    <div v-if="topPage">
      <v-sheet color="transparent" class="mx-auto">
        <v-slide-group multiple show-arrows>
          <v-slide-item
            :id="index"
            v-for="(data, index) in albumLists"
            :key="index"
          >
            <v-card
              color="transparent"
              elevation="0"
              tile
              :id="index"
              class="mx-2"
              :width="cardWidth"
              @click="showMoreInformation(index)"
            >
              <v-img :src="data.image" height="200px"></v-img>

              <v-card-title v-text="data.title"></v-card-title>

              <v-card-subtitle class="pb-0 mb-0">{{
                convertDate(data.releasedate)
              }}</v-card-subtitle>
              <v-card-subtitle class="pl-4 pt-0 mt-0">{{
                data.section
              }}</v-card-subtitle>
            </v-card>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </div>
    <v-row v-if="topPage" class="text-center ma-3">
      <v-col cols="12">
        <v-btn to="/discography" elevation="0" color="info">すべて表示</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "DISCOGRAPHY",
  props: {
    topPage: { type: Boolean, default: false },
  },
  data: () => ({
    model: null,
    dayList: ["日", "月", "火", "水", "木", "金", "土"],
    dialog: false,
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
      if (this.topPage) {
        return this.$store.state.albumLists.slice(0, 3);
      } else {
        return this.$store.state.albumLists;
      }
    },
  },
  created: function () {
    if (this.albumLists.length == 0) {
      this.getAlbumList();
    }
  },
  methods: {
    getAlbumList() {
      this.axios
        .get(process.env.VUE_APP_API_URL + "album/")
        .then((response) => {
          this.$store.dispatch("setAlbumList", { albumLists: response.data });
        })
        .catch((e) => {
          alert(e);
        });
    },
    goGoogleMap(address) {
      let url = "'https://maps.google.co.jp/maps/search/'" + address;
      window.open(url, "_blank");
    },
    convertDate(date) {
      let dateObj = new Date(date);
      let dateYear = dateObj.getFullYear();
      let dateMonth = dateObj.getMonth() + 1;
      let dateDate = dateObj.getDate();
      let newDate = dateYear + "." + dateMonth + "." + dateDate;
      return newDate;
    },
    showMoreInformation(id) {
      this.$router.push({
        name: "musicDetail",
        params: { id: id },
      });
    },
  },
};
</script>
<style>
.paddingLiveList {
  padding: 0 1.5%;
}
</style>
