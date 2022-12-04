<template>
  <v-app :style="{ background: $vuetify.theme.themes.light.background }">
    <v-app-bar
      v-if="$vuetify.breakpoint.xs"
      clipped-left
      app
      extended
      color="grey lighten-4"
      class="mx-0 px-0 pt-5"
      elevation="0"
    >
      <!-- スマホ画面 -->
      <v-col cols="4" class="mx-0 px-0">
        <v-app-bar-nav-icon
          class="ml-0 pl-0"
          @click.stop="drawer = !drawer"
        ></v-app-bar-nav-icon>
        <v-navigation-drawer
          v-model="drawer"
          app
          disable-route-watcher
          disable-resize-watcher
          clipped
          hide-overlay
          elevation="0"
        >
          <v-list class="mt-15" shaped>
            <v-list-item-group
              color="primary"
              v-for="(item, index) in pageList"
              :key="index"
            >
              <v-list-item
                v-show="item.show"
                @click.stop="drawer = !drawer"
                :to="item.path"
              >
                <v-list-item-title>{{ item.name }}</v-list-item-title>
              </v-list-item>
            </v-list-item-group>
          </v-list>
          <template v-slot:append>
            <v-card flat tile width="100%">
              <v-card-text>
                <v-btn
                  v-for="item in icons"
                  :key="item.icon"
                  :href="item.url"
                  icon
                >
                  <v-icon size="20px"> fa-brands fa-{{ item.icon }} </v-icon>
                </v-btn>
              </v-card-text>

              <v-divider></v-divider>

              <v-card-text class="ml-3">
                © {{ new Date().getFullYear() }} Curiosity.
              </v-card-text>
            </v-card>
          </template>
        </v-navigation-drawer>
      </v-col>
      <v-col class="">
        <router-link to="/">
          <v-img
            alt="Logo"
            class="shrink"
            contain
            src="@/assets/images/logo_mark.svg"
            width="90"
          />
        </router-link>
      </v-col>
    </v-app-bar>
    <!-- デスクトップ画面 -->
    <v-app-bar
      v-else
      app
      color="grey lighten-4 pt-5"
      class="padding"
      extended
      elevation="0"
    >
      <router-link to="/">
        <v-img
          alt="Logo"
          class="shrink"
          contain
          src="@/assets/images/logo_mark.svg"
          width="90"
        />
      </router-link>
      <div v-for="(item, index) in pageList" :key="index">
        <router-link
          color=""
          class="routerlink"
          :to="item.path"
          v-show="item.show"
          ><span class="ml-4 mb-6">{{ item.name }}</span></router-link
        >
      </div>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
    <v-footer>
      <v-card flat tile width="100%" class="grey lighten-4 text-center">
        <v-card-text>
          <v-btn
            v-for="item in icons"
            :key="item.icon"
            :href="item.url"
            class="mx-4"
            icon
          >
            <v-icon size="24px"> fa-brands fa-{{ item.icon }} </v-icon>
          </v-btn>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text> © {{ new Date().getFullYear() }} Curiosity. </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "App",
  computed: {
    margin: function () {
      let val = "mr-2";
      if (this.$vuetify.breakpoint.xs) {
        val = "margin";
      }
      return val;
    },
  },
  data: () => ({
    icons: [
      {
        icon: "youtube",
        url: "https://www.youtube.com/channel/UCKUDk2-9iOtN5LZFVnsAPdA",
      },
      { icon: "twitter", url: "https://twitter.com/curiofficial" },
      {
        icon: "instagram",
        url: "https://www.instagram.com/curiosity._official/?hl=ja",
      },
    ],
    pageList: [],
    drawer: false,
  }),
  created: function () {
    this.pageList = this.$router.options.routes;
  },
  methods: {
    setMeta(route) {
      // タイトルを設定
      if (route.meta.title) {
        let setTitle = route.meta.title;
        document.title = setTitle;
      }
      // ディスクリプションを設定
      if (route.meta.desc) {
        let setDesc = route.meta.desc;
        document
          .querySelector("meta[name='description']")
          .setAttribute("content", setDesc);
      }
    },
  },
  mounted() {
    let route = this.$route;
    this.setMeta(route);
  },
  watch: {
    $route(route) {
      this.setMeta(route);
    },
  },
};
</script>
<style>
.v-application {
  font-family: "Noto Sans JP", sans-serif !important;
}
.routerlink {
  color: #424242 !important;
  text-decoration: none !important;
}
.routerlink :hover {
  text-decoration: underline !important;
}
.z-index {
  z-index: 100 !important;
}
.margin {
  margin-left: 120%;
}
.padding {
  padding: 0 10%;
}
.border {
  border: #424242;
}
</style>
