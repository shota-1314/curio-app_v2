<!-- ライブ情報 -->
<template>
  <v-container>
    <v-row class="text-center ma-3">
      <v-col cols="12">
        <span class="text-h5">MOVIE</span>
      </v-col>
    </v-row>
    <div v-if="!topPage">
      <v-row class="paddingLiveList">
        <v-col
          :id="index"
          v-for="(data, index) in movieLists"
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
            @click="showMoreInformation(data.url)"
          >
            <v-img :src="data.thumbnail" height="180px"></v-img>

            <v-card-subtitle v-text="data.title"></v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>
    </div>
    <div v-if="topPage">
      <v-sheet color="transparent" class="mx-auto">
        <v-slide-group multiple show-arrows>
          <v-slide-item
            :id="index"
            v-for="(data, index) in movieLists"
            :key="index"
            v-slot="{ active }"
          >
            <v-card
              color="transparent"
              elevation="0"
              :input-value="active"
              tile
              :id="index"
              class="mx-2"
              :width="cardWidth"
              @click="showMoreInformation(data.url)"
            >
              <v-img :src="data.thumbnail" height="180px"></v-img>

              <v-card-subtitle>{{ data.title }}</v-card-subtitle>
            </v-card>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </div>
    <v-row v-if="topPage" class="text-center ma-3">
      <v-col cols="12">
        <v-btn to="/movie" elevation="0" color="info">すべて表示</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "MOVIE",
  props: {
    topPage: { type: Boolean, default: false },
  },
  data: () => ({}),
  computed: {
    cardWidth: function () {
      let val = 380;
      if (this.$vuetify.breakpoint.xs) {
        val = 220;
      }
      return val;
    },
    movieLists: function () {
      if (this.topPage) {
        return this.$store.state.movieLists.slice(0, 3);
      } else {
        return this.$store.state.movieLists;
      }
    },
  },
  created: function () {
    if (this.movieLists.length == 0) {
      this.getMovieList();
    }
  },
  methods: {
    getMovieList() {
      this.axios
        .get("http://localhost:8000/api/movie/")
        .then((response) => {
          this.$store.dispatch("setMovieList", { movieLists: response.data });
        })
        .catch((e) => {
          alert(e);
        });
    },
    showMoreInformation(url) {
      window.open(url, "_blank");
      return;
    },
  },
};
</script>
<style>
.paddingLiveList {
  padding: 0 1.5%;
}
.show-btns {
  color: rgba(255, 255, 255, 1) !important;
}
.v-card {
  transition: opacity 0.4s ease-in-out;
}

.v-card:not(.on-hover) {
  opacity: 100;
}
</style>
