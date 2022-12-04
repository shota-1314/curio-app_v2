<!-- アルバム詳細情報 -->
<template>
  <v-container>
    <v-row class="text-center ma-3">
      <v-col cols="12">
        <span class="text-h5">NEWS</span>
      </v-col>
    </v-row>
    <v-row :class="paddingNewsDetailList">
      <v-col cols="12" class="">
        <div>
          <v-card-subtitle class="text-left">{{
            convertDate(newsLists[this.$route.params.id]["news_date"])
          }}</v-card-subtitle>
          <v-card-title
            v-text="newsLists[this.$route.params.id]['title']"
          ></v-card-title>
          <v-card-text
            class="text-left overflow"
            v-text="newsLists[this.$route.params.id]['detail']"
          ></v-card-text>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "NewsDetail",
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
    newsLists: function () {
      return this.$store.state.newsLists;
    },
    paddingNewsDetailList: function () {
      let val = "paddingNewsDetailList";
      if (this.$vuetify.breakpoint.xs) {
        val = " ";
      }
      return val;
    },
  },
  created: function () {
    if (this.newsLists.length == 0) {
      this.getLiveList();
    }
  },
  methods: {
    getLiveList() {
      this.axios
        .get(process.env.VUE_APP_API_URL + "news/")
        .then((response) => {
          this.$store.dispatch("setNewsList", { newsLists: response.data });
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
.paddingNewsDetailList {
  padding: 0 20%;
}
.color {
  color: white;
}
.overflow {
  display: inline-block;
  overflow-wrap: break-word;
  width: 100%; /* 追加 */
  max-width: 100%;
}
</style>
