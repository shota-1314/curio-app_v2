import Vue from "vue";
import VueRouter from "vue-router";

//各Viewファイル
import HomeView from "../views/HomeView.vue";
import NewsView from "../views/NewsView.vue";
import LiveView from "../views/LiveView.vue";
import MusicView from "../views/MusicView.vue";
import MovieView from "../views/MovieView.vue";
import LiveDetail from "../components/LiveDetail.vue";
import MusicDetail from "../components/MusicDetail.vue";
import NewsDetail from "../components/NewsDetail.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "HOME",
    show: false,
    meta: { title: "Curiosity.", desc: "Curiosity. official website" },
    component: HomeView,
  },
  {
    path: "/news",
    name: "NEWS",
    show: true,
    meta: { title: "NEWS | Curiosity.", desc: "Curiosity. official website" },
    component: NewsView,
  },
  {
    path: "/news/:id",
    name: "newsDetail",
    show: false,
    meta: { title: "NEWS | Curiosity.", desc: "Curiosity. official website" },
    component: NewsDetail,
  },
  {
    path: "/live",
    name: "LIVE",
    show: true,
    meta: { title: "LIVE | Curiosity.", desc: "Curiosity. official website" },
    component: LiveView,
  },
  {
    path: "/discography",
    name: "DISCOGRAPHY",
    show: true,
    meta: {
      title: "DISCOGRAPHY | Curiosity.",
      desc: "Curiosity. official website",
    },
    component: MusicView,
  },
  {
    path: "/movie",
    name: "MOVIE",
    show: true,
    meta: {
      title: "MOVIE | Curiosity.",
      desc: "Curiosity. official website",
    },
    component: MovieView,
  },
  {
    path: "/profile",
    name: "PROFILE",
    show: true,
  },
  {
    path: "/photos",
    name: "PHOTOS",
    show: false,
  },
  {
    path: "/live/:id",
    name: "liveDetail",
    show: false,
    meta: { title: "LIVE | Curiosity.", desc: "Curiosity. official website" },
    component: LiveDetail,
  },
  {
    path: "/discography/:id",
    name: "musicDetail",
    show: false,
    meta: { title: "MUSIC | Curiosity.", desc: "Curiosity. official website" },
    component: MusicDetail,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
