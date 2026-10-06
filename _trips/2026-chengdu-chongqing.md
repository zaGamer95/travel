---
title: Chengdu → Chongqing, 9 days
date: 2026-12-25
end_date: 2027-01-02
countries: [china]
planned: true             # After the trip, delete this line and add a cover, photos and the write-up.
summary: The Kaan Family's year-end Sichuan trip. Pandas and the Leshan Giant Buddha in Chengdu, Chongqing's night views and hotpot, and New Year's Eve.

# Flights: rendered as cards by {% include flights.html %}
flights:
  - who: Kaan Family (6)
    airline: Singapore Airlines
    flight: SQ846
    from: { code: SIN, city: Singapore, date: Fri 12/25, time: "02:10" }
    to:   { code: TFU, city: Chengdu Tianfu, date: Fri 12/25, time: "06:55" }
  - who: Wonbo
    airline: Air China
    flight: CA404
    from: { code: SIN, city: Singapore T1, date: Fri 12/25, time: "16:00" }
    to:   { code: TFU, city: Chengdu Tianfu T1, date: Fri 12/25, time: "21:05" }
  - who: Kaan Family (all 7)
    airline: Singapore Airlines
    flight: SQ819
    from: { code: CKG, city: Chongqing Jiangbei T3, date: Sat 1/2, time: "02:35" }
    to:   { code: SIN, city: Singapore, date: Sat 1/2, time: "07:50" }
    note: This leaves in the early hours after New Year's Day. Head to the airport around 22:30 on 1/1.

# Day by day: rendered by {% include itinerary.html %}
# status: confirmed or draft. items: [{ t: time, what: plan }]. note and tag are optional.
days:
  - date: Fri 12/25
    city: Chengdu
    status: confirmed
    items:
      - { t: "06:55", what: "Kaan Family lands at Tianfu Airport (about 1.5 hours to town)" }
      - { t: "10:00", what: "Hotel, drop off luggage" }
      - { t: "11:00", what: "Chunxi Road, Taikoo Li and IFS" }
      - { t: "15:00", what: "Hotel check-in and rest" }
      - { t: "18:00", what: "Kuanzhai Alley and dinner" }
      - { t: "21:05", what: "Wonbo lands at Tianfu and heads to the hotel" }
  - date: Sat 12/26
    city: Chengdu
    status: confirmed
    tag: "Day trip"
    note: "Klook small-group tour, about $65 per person, Chinese-speaking guide"
    items:
      - { t: "08:30", what: "Pickup at the hotel" }
      - { t: "10:30", what: "Dujiangyan Panda Base" }
      - { t: "13:00", what: "Lunch (own expense)" }
      - { t: "14:00", what: "Zhongshuge Bookstore" }
      - { t: "14:30", what: "Dujiangyan Scenic Area (the ancient irrigation system)" }
      - { t: "17:00", what: "Yangtianwo Plaza" }
      - { t: "17:30", what: "South Bridge: Nanqiao \"blue tears\" lights, Guankou Ancient Town, Xijie Alley" }
      - { t: "20:30", what: "Return to Chengdu" }
      - { t: "22:00", what: "Back at the hotel" }
  - date: Sun 12/27
    city: Chengdu
    status: confirmed
    tag: "Day trip"
    note: "Klook tour, about $99 per person with lunch and snacks, Chinese-speaking guide, coach"
    items:
      - { t: "06:00", what: "Hotel pickup" }
      - { t: "", what: "Leshan Giant Buddha and Mount Emei" }
      - { t: "19:00", what: "Back at the hotel" }
  - date: Mon 12/28
    city: Chengdu
    status: confirmed
    tag: "Dinner show"
    items:
      - { t: "09:00", what: "People's Park" }
      - { t: "10:30", what: "Wuhou Shrine, dedicated to Zhuge Liang" }
      - { t: "12:00", what: "Lunch and Jinli Ancient Street" }
      - { t: "15:00", what: "Dongjiao Memory: old factory buildings turned into shops, cafes and live music venues" }
      - { t: "17:00", what: "Hong Ding Yan hot pot dinner show (arrive early for hair and makeup)" }
  - date: Tue 12/29
    city: Chengdu → Chongqing
    status: confirmed
    tag: "Travel"
    items:
      - { t: "12:00", what: "Transfer to Chengdu East station" }
      - { t: "13:32", what: "Train G8621 to Chongqing, first class" }
      - { t: "15:13", what: "Arrive Chongqing North station" }
      - { t: "16:00", what: "Transfer to the hotel" }
      - { t: "17:00", what: "Jiefangbei and Hongya Cave" }
      - { t: "19:00", what: "Suggested: dinner near Jiefangbei, then Hongya Cave lit up, best seen from Qiansimen Bridge" }
  - date: Wed 12/30
    city: Chongqing
    status: draft
    note: "From Mum's outline: Liziba, Ciqikou and a river cruise"
    items:
      - { t: "09:30", what: "Liziba station: watch the monorail run through the building from the viewing platform" }
      - { t: "11:00", what: "Metro to Ciqikou Ancient Town, lunch and snacks (Chen Mahua twists)" }
      - { t: "14:30", what: "Back to the hotel to rest" }
      - { t: "16:30", what: "Yangtze River Cableway across the river" }
      - { t: "17:30", what: "Raffles City Exploration Deck at Chaotianmen for sunset" }
      - { t: "18:30", what: "Dinner near Chaotianmen" }
      - { t: "19:30", what: "Two Rivers night cruise from Chaotianmen (about 1 hour)" }
  - date: Thu 12/31
    city: Chongqing
    status: draft
    tag: "New Year's Eve"
    note: "From Mum's outline: Gong Yan palace banquet and New Year's Eve"
    items:
      - { t: "10:00", what: "Three Gorges Museum, with the People's Great Hall across the square (indoors, flat and warm)" }
      - { t: "12:30", what: "Lunch: Chongqing noodles" }
      - { t: "14:00", what: "Rest at the hotel before the late night" }
      - { t: "17:00", what: "Gong Yan (Li Yan Ba Guo) palace banquet: dinner and a dance show, costumes optional. Check the session time when booking" }
      - { t: "21:30", what: "Walk to Jiefangbei for the countdown" }
  - date: Fri 1/1
    city: Chongqing
    status: draft
    note: "From Mum's outline: relaxed day and farewell dinner"
    items:
      - { t: "10:00", what: "Sleep in, check out and leave bags at the hotel" }
      - { t: "11:00", what: "Brunch: Chongqing noodles" }
      - { t: "12:30", what: "Shancheng Alley: old hillside lanes with river views, at an easy pace" }
      - { t: "15:00", what: "Cafe, shopping or rest around Jiefangbei" }
      - { t: "16:30", what: "Nanshan Yikeshu viewpoint at sunset as the city lights up (by car)" }
      - { t: "19:00", what: "Farewell dinner" }
      - { t: "22:30", what: "Collect bags, leave for Jiangbei Airport T3" }
  - date: Sat 1/2
    city: Chongqing → Singapore
    status: confirmed
    tag: "Home"
    items:
      - { t: "02:35", what: "SQ819 departs" }
      - { t: "07:50", what: "Land in Singapore" }

# Restaurant cards: {% include restaurants.html city="chengdu" %}
# warn values: tallow (beef-tallow broth) beef cheese shellfish ok (nothing to avoid)
restaurants:
  chengdu:
    - name: Da Long Yi (大龙燚)
      kind: Hotpot
      why: One of Chengdu's best-known hotpot spots, famous for a very spicy broth.
      warn: [tallow]
      tip: The tallow broth is the whole point here. Order a split pot (鸳鸯锅), a normal menu item, and Wyn's mum eats from the mushroom or tomato side.
      maps: 大龙燚火锅 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Restaurant_Review-g297463-d10586519-Reviews-DaLong_Yi_Hotpot_YuLin-Chengdu_Sichuan.html" }
        - { label: Trip.com, url: "https://us.trip.com/restaurant/china/chengdu/detail/dalong-yi-hotpot-11397473/" }
    - name: Shu Daxia (蜀大侠)
      kind: Hotpot
      why: A big chain, so a table for seven is easy to get.
      warn: [tallow]
      tip: Check the menu for a split pot or a non-tallow broth they already serve; don't ask them to change their red broth.
      maps: 蜀大侠火锅 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com.my/Restaurant_Review-g297463-d10772740-Reviews-Shu_DaXia_Hotpot_Xi_YuLong-Chengdu_Sichuan.html" }
        - { label: Trip.com, url: "https://www.trip.com/restaurant/china/chengdu/detail/shu-daxia-hotpot-26746641/" }
    - name: Yulin Chuanchuan (玉林串串香)
      kind: Chuanchuan skewers
      why: Chengdu-style skewers you pick yourself and cook in the broth.
      warn: [tallow]
      tip: You choose every skewer, so skipping beef is easy. The broth is still tallow and there's usually no split option, so Wyn's mum may want to sit this one out.
      maps: 玉林串串香 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Restaurant_Review-g297463-d4704824-Reviews-YuLin_ChuanChuan_Xiang_YuLin-Chengdu_Sichuan.html" }
        - { label: Food guide, url: "https://quietroutes.com/travel-guide/yulin-neighborhood-food-guide/" }
    - name: Ma Wangzi (马旺子)
      kind: Sichuan dishes
      why: A polished Sichuan restaurant with private rooms, good with parents.
      warn: [beef]
      tip: Skip the beef dishes and order chicken, pork and tofu.
      maps: 马旺子 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Restaurant_Review-g297463-d11715905-Reviews-Ma_Wang_Zi-Chengdu_Sichuan.html" }
        - { label: 240 Hours in China, url: "https://www.240hoursinchina.com/en-us/chengdu/restaurants/ma-wang-zi-sichuan-bistro" }
    - name: Chen Mapo Tofu (陈麻婆豆腐)
      kind: Sichuan dishes
      why: Where mapo tofu was invented.
      warn: [beef]
      tip: Mapo tofu is made with minced beef, so Wyn's mum orders other dishes here.
      maps: 陈麻婆豆腐 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Restaurant_Review-g297463-d1419255-Reviews-Chen_Mapo_tofu_Luomashi-Chengdu_Sichuan.html" }
        - { label: Trip.com, url: "https://us.trip.com/restaurant/china/chengdu/detail/chen-mapo-tofu-luomashi-11383200/" }
    - name: Long Chaoshou (龙抄手)
      kind: Snacks
      why: A long-running wonton shop on Chunxi Road. Good for trying many small snacks.
      warn: [ok]
      maps: 龙抄手 春熙路 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Restaurant_Review-g297463-d1217812-Reviews-Longchaoshou-Chengdu_Sichuan.html" }
        - { label: Trip.com, url: "https://us.trip.com/restaurant/china/chengdu/detail/longchaoshou-10560653/" }
    - name: Zhong Dumplings (钟水饺)
      kind: Snacks
      why: Pork dumplings in a sweet and spicy sauce.
      warn: [ok]
      maps: 钟水饺 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Restaurant_Review-g297463-d3409310-Reviews-ZhongShuiJiao_WuHou-Chengdu_Sichuan.html" }
        - { label: The Mala Market, url: "https://blog.themalamarket.com/chengdu-challenge-15-dumplings-red-oil-zhong-shui-jiao/" }
    - name: Shuangliu Laoma Rabbit Heads (双流老妈兔头)
      kind: Adventurous
      why: Spicy rabbit heads that locals have with beer. Worth trying once.
      warn: [ok]
      maps: 双流老妈兔头 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Restaurant_Review-g297463-d3409037-Reviews-ShuangLiu_LaoMa_TuTou-Chengdu_Sichuan.html" }
        - { label: The World of Chinese, url: "https://www.theworldofchinese.com/2023/01/journey-down-the-rabbit-hole-of-chengdus-favorite-street-snack/" }
  chongqing:
    - name: Peijie Hotpot (佩姐老火锅)
      kind: Hotpot
      why: One of Chongqing's most famous hotpot restaurants. Expect a long queue.
      warn: [tallow, beef]
      tip: Classic Chongqing beef-tallow hotpot with beef tripe (毛肚) as the signature. Go only if they do a split pot; otherwise it's a night out without Wyn's mum.
      maps: 佩姐老火锅 重庆
      links:
        - { label: Trip.com, url: "https://www.trip.com/restaurant/china/chongqing/detail/peijie-hotpot-15318356/" }
        - { label: Hotpot guide, url: "https://chinaexplorertour.com/2025/blog/best-chongqing-hotpot-for-tourists-food-guide/" }
    - name: Dongting air-raid shelter hotpot (洞亭火锅)
      kind: Hotpot
      why: Hotpot inside old air-raid shelter caves, a uniquely Chongqing atmosphere.
      warn: [tallow]
      tip: Mostly tallow broth too. Check that they have a split pot before going.
      maps: 洞亭火锅 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Restaurant_Review-g294213-d3409500-Reviews-Dong_Ting_Xian_Hotpot-Chongqing.html" }
        - { label: Trip.com, url: "https://www.trip.com/restaurant/china/chongqing/detail/dongting-hot-pot-17007883/" }
    - name: Taoranju (陶然居)
      kind: Jianghu home-style dishes
      why: Chongqing home cooking such as laziji (辣子鸡, chili-fried chicken). Has large round tables.
      warn: [ok]
      tip: Just skip the beef dishes when ordering.
      maps: 陶然居 解放碑 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Restaurant_Review-g294213-d3409753-Reviews-TaoRanJu_JieFang_Bei-Chongqing.html" }
        - { label: Trip.com, url: "https://www.trip.com/restaurant/china/chongqing/detail/taoranju-361221/" }
    - name: Huashi Wanza Noodles (花市豌杂面)
      kind: Noodles
      why: Chongqing noodles topped with peas and minced pork. A good breakfast.
      warn: [ok]
      maps: 花市豌杂面 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Restaurant_Review-g294213-d15410877-Reviews-Huashi_Noodle-Chongqing.html" }
        - { label: Trip.com, url: "https://us.trip.com/restaurant/china/chongqing/detail/hua-shi-wan-za-mian-379002/" }
    - name: Haoyoulai Suanlafen (好又来酸辣粉)
      kind: Noodles
      why: Sour and spicy sweet-potato noodles near Jiefangbei.
      warn: [ok]
      maps: 好又来酸辣粉 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Restaurant_Review-g294213-d3409545-Reviews-Hao_YouLai_SuanLa_Fen_JieFang_Bei-Chongqing.html" }
    - name: Bayi Food Street (八一好吃街)
      kind: Street food
      why: A food alley next to Jiefangbei for grazing on a bit of everything.
      warn: [shellfish, cheese]
      tip: Spicy stir-fried clams (花甲) are everywhere (Wonbo skips them), and cheese-topped snacks too (Wyn's mum skips those).
      maps: 八一好吃街 重庆
      links:
        - { label: Trip.com, url: "https://sg.trip.com/moments/detail/chongqing-158-139510275/" }
        - { label: Chinatripedia, url: "https://chinatripedia.com/bayi-food-street-chongqing-foodies-haven/" }
    - name: Chen Mahua (陈麻花)
      kind: Snacks
      why: Ciqikou's famous fried dough twists. Good as gifts too.
      warn: [ok]
      maps: 陈建平老街陈麻花 磁器口 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Restaurant_Review-g294213-d3409457-Reviews-ChenJianPing_LaoJie_Chen_MaHua-Chongqing.html" }
        - { label: Trip.com, url: "https://www.trip.com/restaurant/china/chongqing/detail/chen-jian-ping-378998/" }
# Sight cards: {% include places.html city="chengdu" %}
places:
  chengdu:
    - name: "Chunxi Road, Taikoo Li and IFS"
      kind: Shopping
      why: "The main shopping streets, with the giant panda climbing the IFS building."
      maps: 春熙路 太古里 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d15671160-Reviews-Taikoo_Li-Chengdu_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Chunxi_Road" }
    - name: "Kuanzhai Alley"
      kind: Old town
      why: "Restored Qing-dynasty lanes with snacks, shops and teahouses."
      maps: 宽窄巷子 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d1832089-Reviews-Kuanzhai_Alley-Chengdu_Sichuan.html" }
    - name: "Dujiangyan Panda Base"
      kind: Pandas
      why: "A quieter panda centre in the hills outside Chengdu, on the 12/26 tour."
      maps: 都江堰熊猫谷 中华大熊猫苑
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g681034-d10161574-Reviews-Dujiangyan_Panda_Base-Dujiangyan_Sichuan.html" }
    - name: "Dujiangyan Irrigation System"
      kind: UNESCO
      why: "A 2,000-year-old irrigation system that still waters the Chengdu plain."
      maps: 都江堰景区
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com.sg/Attraction_Review-g681034-d319640-Reviews-Dujiangyan_Irrigation_System-Dujiangyan_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Dujiangyan" }
    - name: "South Bridge and Guankou Ancient Town"
      kind: Night view
      why: "A covered bridge and old town by the river, lit up at night."
      maps: 都江堰南桥 灌县古城
      links:
        - { label: Trip.com photos, url: "https://www.trip.com/moments/detail/dujiangyan-911-122647835/" }
        - { label: Trip.com guide, url: "https://www.trip.com/moments/poi-ancient-town-of-guan-county-20906582/" }
    - name: "Leshan Giant Buddha"
      kind: UNESCO
      why: "A 71m Buddha carved into a riverside cliff. The river boat is the low-stairs way to see it."
      maps: 乐山大佛
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g303771-d488514-Reviews-Leshan_Giant_Buddha-Leshan_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Leshan_Giant_Buddha" }
    - name: "Mount Emei"
      kind: UNESCO
      why: "One of China's four sacred Buddhist mountains, with temples, forest and monkeys."
      maps: 峨眉山
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.co.uk/Attraction_Review-g679672-d319609-Reviews-Mount_Emei_Emeishan-Emeishan_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Mount_Emei" }
    - name: "People's Park"
      kind: Park
      why: "Sip tea at Heming Teahouse and watch locals dance, sing and play mahjong."
      maps: 人民公园 鹤鸣茶社 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d546614-Reviews-Chengdu_Renmin_Park-Chengdu_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/People's_Park_(Chengdu)" }
    - name: "Wuhou Shrine"
      kind: Temple
      why: "The Three Kingdoms memorial temple to Zhuge Liang, next to Jinli."
      maps: 武侯祠 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d508982-Reviews-Wuhou_Memorial_Temple-Chengdu_Sichuan.html" }
    - name: "Jinli Ancient Street"
      kind: Old town
      why: "Lantern-lit lanes with snacks and souvenir shops."
      maps: 锦里古街 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d1832090-Reviews-Jinli_Pedestrian_Street-Chengdu_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Jinli" }
    - name: "Dongjiao Memory"
      kind: Creative park
      why: "An old factory district turned into shops, cafes and live music venues."
      maps: 东郊记忆 成都
      links:
        - { label: Trip.com photos, url: "https://www.trip.com/moments/detail/chengdu-104-130808463/" }
    - name: "Hong Ding Yan"
      kind: Dinner show
      why: "Hot pot dinner with a 100-minute show (face-changing, dances, live guzheng). Hanfu, hair and makeup are optional extras. Around ¥500 per person; book ahead."
      maps: 红鼎宴 成都
      links:
        - { label: Trip.com reviews, url: "https://us.trip.com/restaurant/china/chengdu/detail/hong-ding-yan-151900752/" }
        - { label: Trip.com booking, url: "https://sg.trip.com/things-to-do/detail/95654753/" }
        - { label: Dinner show guide, url: "https://pandastroll.com/best-dinner-shows-in-chengdu/" }
  chongqing:
    - name: "Jiefangbei"
      kind: Landmark
      why: "The city-centre monument and pedestrian area, and the New Year countdown spot."
      maps: 解放碑 重庆
      links:
        - { label: TripAdvisor, url: "https://en.tripadvisor.com.hk/Attraction_Review-g294213-d2003325-Reviews-Jiefang_Monument-Chongqing.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Liberation_Monument_in_Chongqing" }
    - name: "Hongya Cave"
      kind: Night view
      why: "Stilted buildings stacked up the cliff, lit gold at night."
      maps: 洪崖洞 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g294213-d1814790-Reviews-Hongya_Cave-Chongqing.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Hongya_Cave" }
    - name: "Liziba Station"
      kind: Only in Chongqing
      why: "The monorail that runs straight through a residential building."
      maps: 李子坝 轻轨穿楼 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g294213-d15758086-Reviews-Liziba_Station-Chongqing.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Liziba_station" }
    - name: "Ciqikou Ancient Town"
      kind: Old town
      why: "An old river port with snack streets and Chen Mahua shops."
      maps: 磁器口古镇 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g294213-d502852-Reviews-Ciqikou_Porcelain_Port-Chongqing.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Ciqikou,_Chongqing" }
    - name: "Yangtze River Cableway"
      kind: Ride
      why: "A cable car straight across the Yangtze with skyline views."
      maps: 长江索道 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g294213-d6207908-Reviews-Yangtze_River_Cableway-Chongqing.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Yangtze_River_Cableway" }
    - name: "Raffles City Exploration Deck"
      kind: View
      why: "The glass skybridge on top of Raffles City at Chaotianmen, over the meeting of the two rivers."
      maps: 来福士 探索舱 重庆
      links:
        - { label: GetYourGuide, url: "https://www.getyourguide.com/chongqing-l959/chongqing-exploration-skywalk-ticket-at-raffles-city-t1177971/" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Raffles_City_Chongqing" }
    - name: "Two Rivers night cruise"
      kind: Night cruise
      why: "An hour on the river past the lit-up skyline, leaving from Chaotianmen."
      maps: 朝天门 两江游 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g294213-d1814721-Reviews-Chongqing_Chaotianmen-Chongqing.html" }
        - { label: Trip.com tickets, url: "https://us.trip.com/travel-guide/attraction/chongqing/chaotianmen-two-rivers-night-cruise-69571118/" }
    - name: "Three Gorges Museum"
      kind: Museum
      why: "History of Chongqing and the Three Gorges, opposite the People's Great Hall."
      maps: 三峡博物馆 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g294213-d2068774-Reviews-Three_Gorges_Museum-Chongqing.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Three_Gorges_Museum" }
    - name: "Gong Yan (Li Yan Ba Guo)"
      kind: Dinner show
      why: "Palace-style set dinner (about 90 minutes) with dance and music on a stage around the tables. Costumes, makeup and hair are optional extras."
      maps: 礼宴巴国 宫宴 重庆
      links:
        - { label: Official site, url: "https://gongyanshow.com/en/" }
        - { label: Klook, url: "https://www.klook.com/en-US/activity/176894-immersive-experience-of-the-palace-banquet-thousands-of-years-ago/" }
        - { label: Trip.com review, url: "https://sg.trip.com/moments/detail/chongqing-158-143018423/" }
    - name: "Shancheng Alley"
      kind: Old lanes
      why: "Restored hillside lanes with cafes and river views. An easy walk."
      maps: 山城巷 重庆
      links:
        - { label: Trip.com guide, url: "https://www.trip.com/moments/poi-mountain-city-alley-65963918/" }
    - name: "Nanshan Yikeshu viewpoint"
      kind: Night view
      why: "The classic lookout over the whole Chongqing skyline at night."
      maps: 南山一棵树观景台 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g294213-d1814684-Reviews-Chongqing_South_Mountain-Chongqing.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Single_Tree_Vista" }
---

## At a glance

- **Dates**: Fri 2026.12.25 – Sat 2027.01.02
- **Group**: the Kaan Family, 7 people. Wyn, Wyn's parents, Bryon, Meredith, Kj and Wonbo
- **Route**: Singapore → Chengdu (4 nights) → high-speed train → Chongqing (3 nights plus the last day) → Singapore

## Flights (booked)

{% include flights.html %}

- Wyn, her parents, Bryon, Meredith and Kj arrive in the morning, and Wonbo joins that night.
- Wonbo's ticket (CA404) includes one 23kg checked bag.

## Itinerary

{% include itinerary.html %}

- **Chengdu (12/25–12/29) is Mum's plan and confirmed.** The Chongqing days follow Mum's outline, with times and stops filled in as a draft to discuss.
- **12/26 → 12/27**: the Dujiangyan tour gets back around 22:00 and the Leshan pickup is at 06:00, so it's an early night.
- **12/27**: the Leshan cliff stairs are steep with long queues; the river boat view is easier for anyone who'd rather not climb.
- **12/28 Hong Ding Yan**: it's hot pot, so when booking ask for a non-tallow pot or dishes without beef for Wyn's mum.
- **12/31**: the countdown at Jiefangbei is extremely crowded and the streets around it close to traffic. Pick a meeting point in case the group gets separated.
- **12/28 and 12/31 are both dinner shows**: you eat while actors perform. At both, costumes, hair and makeup are an optional extra on top of the dinner, so the family could dress up at one and just watch at the other.

## Sights

Each card links to reviews and photos on TripAdvisor, background on Wikipedia, and a Google Maps search with more reviews and photos.

### Chengdu

{% include places.html city="chengdu" %}

### Chongqing

{% include places.html city="chongqing" %}

## Where to eat

**Wyn's mum can't eat beef or cheese**, and **Wonbo can't eat shellfish**. Famous places are still on the list, with what to watch out for; whoever can't eat a dish just orders something separate. Seven people need a big table, so book popular places ahead or arrive at opening time. Each card links to reviews and photos; for chains the link is one branch, so pick the most convenient one. Check opening hours and locations again before the trip.

### What to watch out for in Sichuan food

- **Hotpot and chuanchuan broth**: red Chongqing-style broth is made with **beef tallow (牛油)**, and at the famous places that broth *is* the dish. As Wyn put it, asking them to swap it is like ordering bak kut teh with hot water instead of the soup and fish instead of pork. So don't ask for a different broth. Pick places that offer a **split pot (鸳鸯锅)** as a normal menu item, and Wyn's mum eats from the mushroom or tomato side. In Chengdu, some places also serve a red broth made with rapeseed oil (菜籽油) as their own recipe; that one is fine.
- **Mapo tofu**: the original recipe uses **minced beef**. Ask for pork, or pick another dish.
- **Beef dishes**: maodu (毛肚, beef tripe), maoxuewang (毛血旺) and fuqi feipian (夫妻肺片) all contain beef or offal.
- **Shellfish**: avoid huajia (花甲, spicy stir-fried clams, common at night markets), clams (蛤蜊), scallops (扇贝) and oysters (生蚝).
- **Cheese**: rare in Sichuan cooking, but cheese foam (芝士) is common on desserts and milk tea these days.

### Chengdu

{% include restaurants.html city="chengdu" %}

### Chongqing

{% include restaurants.html city="chongqing" %}

### Show this when ordering

<div class="phrase-card">
<p class="zh">我们有人不吃牛肉、奶酪和贝类（蛤蜊、花甲、扇贝）。<br>请问哪些菜没有这些？火锅要鸳鸯锅。</p>
<p class="tr">Some of us can't eat beef, cheese or shellfish (clams, scallops). Which dishes don't have these? For hotpot, a split pot please.</p>
</div>

## Where to stay

- **Chengdu (12/25–12/28, 4 nights)**: around Chunxi Road and Taikoo Li, on metro lines 2 and 3.
- The Kaan Family drop off luggage at 10:00 and check in at 15:00, so ask the hotel to hold bags that morning.
- **Chongqing (12/29–12/31, 3 nights)**: around Jiefangbei and Hongyadong, within walking distance after the countdown.
- **1/1**: check out, leave the bags at the hotel, and head to the airport at night. To shower and rest before the red-eye, consider **booking the night of 1/1 too**.
- For seven, book 3–4 rooms or a serviced apartment. In China only places **registered to host foreign guests** can take foreigners, so confirm that before booking.

## Getting around

- **Tianfu Airport → central Chengdu**: about 1.5 hours. The Kaan Family will have a lot of luggage, so a pre-booked van pickup is easiest. Wonbo takes a taxi or Didi at night.
- **Chengdu → Chongqing high-speed train**: G8621, 13:32 Chengdu East → 15:13 Chongqing North, first class. Book with passports on the 12306 app or Trip.com, and buy all seven tickets in one order to sit together.
- **Downtown Chongqing → Jiangbei Airport T3**: about 40 minutes by taxi or Didi. The metro stops before midnight, so go by car at night.
- **In the cities**: the metro is easiest. A taxi or Didi takes four, so split into two cars or call a 6–7 seater.

## To do

- Flights: Wonbo's CA404 out and SQ819 back are booked
- Kaan Family (6) on SQ846 out; confirm all seven are on SQ819 back
- Entry rules: check the current visa-free entry policy (dates and eligible passports) before departure
- Book hotels (foreign guests accepted; extra night on 1/1?)
- Airport van pickup for the Kaan Family on the morning of 12/25
- Klook tours: Dujiangyan (12/26) and Leshan + Mount Emei (12/27)
- Hong Ding Yan dinner show for 12/28 (book ahead)
- Train G8621 Chengdu East → Chongqing North, first class, 12/29
- Gong Yan banquet for 12/31, and the night cruise for 12/30
- Link a foreign card to Alipay and WeChat Pay
- Data: roaming or a travel eSIM (KakaoTalk, WhatsApp and Google keep working)
- Winter clothes: 5–10°C during the day, damp, and indoor heating is weak
- Spice level: ask for "weila (微辣, mildly spicy)" when ordering

## Still to decide

- Chongqing days (12/30–1/1): go through the draft with the family
- Two dinner shows (Hong Ding Yan 12/28, Gong Yan 12/31): keep both, and which one to dress up for
- Whether to keep a hotel room on 1/1 to rest before the red-eye
