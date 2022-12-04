const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: ["vuetify"],
  configureWebpack: {
    watch: true,
  },
  devServer: {
    client: {
      webSocketURL: "ws://0.0.0.0:8080/ws",
    },
  },
  pages: {
    index: {
      entry: "src/main.js",
      title: "Curiosity.",
    },
  },
});
