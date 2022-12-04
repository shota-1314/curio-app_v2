import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  //メンバ変数
  state: {
    // ライブリスト
    liveLists: [],
    // ライブリスト
    albumLists: [],
    // ニュースリスト
    newsLists: [],
    // 動画リスト
    movieLists: [],
  },
  mutations: {
    _setLiveList: (state, payload) => {
      state.liveLists = payload;
    },
    _setAlbumList: (state, payload) => {
      state.albumLists = payload;
    },
    _setNewsList: (state, payload) => {
      state.newsLists = payload;
    },
    _setMovieList: (state, payload) => {
      state.movieLists = payload;
    },
    _reset: (state) => {
      state.liveLists = [];
      state.albumLists = [];
      state.newsLists = [];
      state.movieLists = [];
    },
  },
  actions: {
    setLiveList: ({ commit }, liveLists) => {
      commit("_setLiveList", liveLists.liveLists);
    },
    setAlbumList: ({ commit }, albumLists) => {
      commit("_setAlbumList", albumLists.albumLists);
    },
    setNewsList: ({ commit }, newsLists) => {
      commit("_setNewsList", newsLists.newsLists);
    },
    setMovieList: ({ commit }, movieLists) => {
      commit("_setMovieList", movieLists.movieLists);
    },
    reset: ({ commit }) => {
      commit("_reset");
    },
  },
  modules: {},
});
