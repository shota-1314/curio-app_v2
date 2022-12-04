<template>
  <div>
    <v-img
      :height="cardHeight"
      class="position-relative"
      gradient="to top right, rgba(0,0,8,0.6629245448179272), rgba(0,0,0,0.10270045518207283)"
      src="@/assets/images/artist.jpeg"
    >
      <v-row justify="center">
        <v-col class="text-center" cols="12">
          <div>
            <v-img
              class="mx-auto position-absolute"
              width="60%"
              contain
              src="@/assets/images/logo_type.svg"
            ></v-img>
          </div>
        </v-col>
      </v-row>
    </v-img>
    <NewsList :topPage="true" />
    <LiveList :topPage="true" />
    <MusicList :topPage="true" />
    <MovieList :topPage="true" />
  </div>
</template>

<script>
import LiveList from "../components/Live";
import MusicList from "../components/Music";
import NewsList from "../components/News";
import MovieList from "../components/Movie";
export default {
  components: {
    // eslint-disable-next-line vue/no-unused-components
    LiveList,
    MusicList,
    NewsList,
    MovieList,
  },
  name: "HelloWorld",

  data: () => ({
    livelists: [],
    model: null,
    dayList: ["日", "月", "火", "水", "木", "金", "土"],
  }),
  created: function () {
    this.getLiveList();
  },
  computed: {
    cardHeight: function () {
      let val = 750;
      if (this.$vuetify.breakpoint.xs) {
        val = 500;
      }
      return val;
    },
  },
  methods: {
    getLiveList() {
      this.axios
        .get("http://localhost:8000/api/live/")
        .then((response) => {
          this.livelists = response.data;
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
  },
};
</script>
<style>
.position-relative {
  position: relative !important;
}
.position-absolute {
  position: absolute !important;
  left: 20%;
  top: 45%;
}
</style>
