<template>
  <NewsList />
</template>

<script>
import NewsList from "../components/News";

export default {
  name: "news",

  components: {
    // eslint-disable-next-line vue/no-unused-components
    NewsList,
  },
};
</script>
