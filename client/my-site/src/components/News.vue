<!-- ライブ情報 -->
<template>
  <v-container>
    <v-row class="text-center ma-3">
      <v-col cols="12">
        <span class="text-h5">NEWS</span>
      </v-col>
    </v-row>
    <div v-if="!topPage" class="py-7">
      <v-row class="paddingNewsList">
        <v-col
          :id="index"
          v-for="(data, index) in newsLists"
          :key="index"
          class="ma-0 pa-0"
          cols="12"
        >
          <v-card
            color="transparent"
            elevation="0"
            tile
            :id="index"
            class="mx-2"
            @click="showMoreInformation(index)"
          >
            <v-divider class=""></v-divider>
            <div class="d-flex px-sm-12 px-sm-12 px-4">
              <v-card-subtitle :class="padding">{{
                convertDate(data.news_date)
              }}</v-card-subtitle>
              <v-card-title
                :class="textSize"
                v-text="data.title"
              ></v-card-title>
              <v-spacer></v-spacer>
              <v-icon>fas fa-chevron-right</v-icon>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </div>
    <div v-if="topPage" class="py-7">
      <v-row class="paddingNewsTopList">
        <v-col
          :id="index"
          v-for="(data, index) in newsLists"
          :key="index"
          class="ma-0 pa-0"
          cols="12"
        >
          <v-card
            color="transparent"
            elevation="0"
            tile
            :id="index"
            class="mx-2"
            v-if="index <= 1"
            @click="showMoreInformation(index)"
          >
            <v-divider class=""></v-divider>
            <div class="d-flex">
              <v-card-subtitle :class="padding">{{
                convertDate(data.news_date)
              }}</v-card-subtitle>
              <v-card-title
                :class="textSize"
                v-text="data.title"
              ></v-card-title>
              <v-spacer></v-spacer>
              <v-icon>fas fa-chevron-right</v-icon>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </div>
    <v-row v-if="topPage" class="text-center ma-3">
      <v-col cols="12">
        <v-btn to="/news" elevation="0" color="info">すべて表示</v-btn>
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
    textSize: function () {
      let val = "text-subtitle-1";
      if (this.$vuetify.breakpoint.xs) {
        val = "text-body-1";
      }
      return val;
    },
    padding: function () {
      let val = "pt-5";
      if (this.$vuetify.breakpoint.xs) {
        val = "pt-4";
      }
      return val;
    },
    paddingList: function () {
      let val = "px-12";
      if (this.$vuetify.breakpoint.xs) {
        val = "blank";
      }
      return val;
    },
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
  },
  created: function () {
    if (this.newsLists.length == 0) {
      this.getNewsList();
    }
  },
  methods: {
    getNewsList() {
      this.axios
        .get("http://localhost:8000/api/news/")
        .then((response) => {
          this.$store.dispatch("setNewsList", { newsLists: response.data });
        })
        .catch((e) => {
          alert(e);
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
    test() {
      return;
    },
    showMoreInformation(id) {
      this.$router.push({
        name: "newsDetail",
        params: { id: id },
      });
    },
  },
};
</script>
<style>
.paddingNewsList {
  padding: 0 11%;
}
.paddingNewsTopList {
  padding: 0 5%;
}
</style>
