<!-- ライブ情報 -->
<template>
  <v-container>
    <v-row class="text-center ma-3">
      <v-col cols="12">
        <span class="text-h5">LIVE</span>
      </v-col>
    </v-row>
    <div>
      <v-row>
        <v-col>
          <div>
            <v-img
              contain
              max-width="500"
              :src="liveLists[this.$route.params.id]['image']"
              class="mx-auto my-5"
            ></v-img>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col :class="padding" class="mx-3">
          <v-card-title
            class="text-center text-sm-h6"
            v-text="liveLists[this.$route.params.id]['title']"
          ></v-card-title>
          <div class="d-flex ma-0 pa-0">
            <v-btn
              icon
              color="blue"
              class="pl-0"
              @click="goGoogleMap(liveLists[this.$route.params.id]['address'])"
            >
              <v-icon>fa-map-location-dot</v-icon>
            </v-btn>
            <v-card-subtitle class="pt-1 pl-0">
              {{ liveLists[this.$route.params.id]["live_house_name"] }}
            </v-card-subtitle>
          </div>
          <v-card-subtitle class="text-left py-0 my-0">{{
            convertDate(liveLists[this.$route.params.id]["live_date"])
          }}</v-card-subtitle>
          <v-card-text
            v-text="liveLists[this.$route.params.id]['detail']"
            style="white-space: pre-line"
            class="py-0 my-3 text-left"
          ></v-card-text>
          <div class="d-flex mt-6">
            <v-icon>fa-clock-time-eight-outline</v-icon>
            <v-card-subtitle class="pl-1 py-0">
              OPEN : {{ liveLists[this.$route.params.id]["open_time"] }} / START
              :
              {{ liveLists[this.$route.params.id]["start_time"] }}
            </v-card-subtitle>
          </div>
          <div class="d-flex">
            <v-icon>fa-ticket-confirmation-outline</v-icon>
            <v-card-subtitle class="pl-1 py-0">
              ADV : ¥{{ liveLists[this.$route.params.id]["adv_price"] }} / DOOR
              : ¥{{ liveLists[this.$route.params.id]["door_price"] }}
            </v-card-subtitle>
          </div>
          <a class="text-left" :href="liveLists[this.$route.params.id]['url']"
            >more info...</a
          >
          <!-- <v-dialog v-model="dialog" persistent max-width="600px">
		<template v-slot:activator="{ on, attrs }">
			<v-btn color="primary" dark v-bind="attrs" v-on="on">
			取り置き
			</v-btn>
		</template>
		<v-card class="pa-3">
			<v-card-title>
			<span class="text-center">取り置き予約フォーム</span>
			</v-card-title>
			<v-card-text>
			<p class="my-0">{{ data.title }}</p>
			<p class="my-0">{{ data.live_house_name }}</p>
			<p class="my-0">{{ convertDate(data.live_date) }}</p>
			<p class="my-0">
				チケット料金 : ¥{{ data.adv_price }} + ドリンク代
			</p>
			<p class="my-0">
				OPEN : {{ data.open_time }} / START : {{ data.start_time }}
			</p>
			</v-card-text>
			<v-card-text>
			<v-container>
				<v-row>
				<v-col cols="12" class="py-0 my-0">
					<v-text-field label="名前" required></v-text-field>
				</v-col>
				<v-col cols="12" class="py-0 my-0">
					<v-text-field
					label="メールアドレス"
					required
					></v-text-field>
				</v-col>
				<v-col cols="12" class="py-0 my-0">
					<v-text-field
					label="チケット枚数"
					value="0"
					suffix="枚"
					></v-text-field>
				</v-col>
				</v-row>
			</v-container>
			</v-card-text>
			<v-card-actions>
			<v-spacer></v-spacer>
			<v-btn color="blue darken-1" text @click="dialog = false">
				閉じる
			</v-btn>
			<v-btn color="blue darken-1" text @click="dialog = false">
				確認
			</v-btn>
			</v-card-actions>
		</v-card>
		</v-dialog> -->
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",
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
    liveLists: function () {
      return this.$store.state.liveLists;
    },
    padding: function () {
      let val = "paddingLive";
      if (this.$vuetify.breakpoint.xs) {
        val = "";
      }
      return val;
    },
  },
  created: function () {
    if (this.liveLists.length == 0) {
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
          console.log(e);
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
.paddingLive {
  padding: 0 20%;
}
</style>
