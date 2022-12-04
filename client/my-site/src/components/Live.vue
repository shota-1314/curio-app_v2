<!-- ライブ情報 -->
<template>
  <v-container>
    <v-row class="text-center ma-3">
      <v-col cols="12">
        <span class="text-h5">LIVE</span>
      </v-col>
    </v-row>
    <div v-if="!topPage">
      <v-row class="paddingLiveList">
        <v-col
          :id="data.id"
          v-for="(data, index) in livelists"
          :key="data.id"
          cols="12"
          class="text-center"
          sm="4"
        >
          <v-card
            color="transparent"
            elevation="0"
            tile
            class="mx-2"
            @click="showMoreInformation(index)"
          >
            <v-img :src="data.image" height="200px"></v-img>

            <v-card-title v-text="data.title"></v-card-title>

            <v-card-subtitle>{{
              convertDate(data.live_date) + "@" + data.live_house_name
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
            v-for="(data, index) in livelists"
            :key="index"
          >
            <v-card
              color="transparent"
              elevation="0"
              tile
              class="mx-2"
              :width="cardWidth"
              :id="index"
              @click="showMoreInformation(index)"
            >
              <v-img :src="data.image" height="200px"></v-img>

              <v-card-title v-text="data.title"></v-card-title>

              <v-card-subtitle>{{
                convertDate(data.live_date) + "@" + data.live_house_name
              }}</v-card-subtitle>
            </v-card>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </div>
    <v-row v-if="topPage" class="text-center ma-3">
      <v-col cols="12">
        <v-btn to="/live" elevation="0" color="info">すべて表示</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Live",
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
    livelists: function () {
      if (this.topPage) {
        return this.$store.state.liveLists.slice(0, 3);
      } else {
        return this.$store.state.liveLists;
      }
    },
  },
  created: function () {
    console.log(process.env.VUE_APP_API_URL);
    if (this.livelists.length == 0) {
      this.getLiveList();
    }
  },
  methods: {
    getLiveList() {
      this.axios
        .get(process.env.VUE_APP_API_URL + "live/")
        .then((response) => {
          this.$store.dispatch("setLiveList", { liveLists: response.data });
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
      let dateDay = dateObj.getDay();
      let newDate =
        dateYear +
        "年" +
        dateMonth +
        "月" +
        dateDate +
        "日(" +
        this.dayList[dateDay] +
        ")";
      return newDate;
    },
    showMoreInformation(id) {
      this.$router.push({
        name: "liveDetail",
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
