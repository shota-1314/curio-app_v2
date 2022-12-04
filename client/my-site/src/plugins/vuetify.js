import Vue from "vue";
import Vuetify from "vuetify/lib/framework";
import "@fortawesome/fontawesome-free/css/all.css";
Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        background: "#F5F5F5",
      },
    },
  },
  icons: {
    iconfont: "fa", // default - only for display purposes
  },
});
