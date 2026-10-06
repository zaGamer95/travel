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
days:
  - date: Fri 12/25
    city: Chengdu
    day: "Kaan Family: land 06:55, drop bags at the hotel and rest. Afternoon tea in People's Park, stroll Kuanzhai Alley"
    night: "Kaan Family: dinner near the hotel. Wonbo: lands 21:05, to the hotel (about 1 hour)"
  - date: Sat 12/26
    city: Chengdu
    day: Panda Base (pandas are most active in the morning; use the electric carts inside), Wenshu Monastery
    night: Hotpot
  - date: Sun 12/27
    city: Chengdu
    tag: Day trip
    day: Leshan Giant Buddha (about 1 hour by high-speed train). The cliff stairs are steep with long queues, so the parents can see it from the river cruise instead
    night: Back to Chengdu, chuanchuan skewers
  - date: Mon 12/28
    city: Chengdu
    tag: Dress-up day (TBC)
    day: Wuhou Shrine, then traditional costume rental with hair and makeup at Jinli Old Street and photos around the old lanes
    night: Traditional banquet dinner with a live show (Sichuan opera, face-changing) in front of the table, then Anshun Bridge at night
  - date: Tue 12/29
    city: Chengdu → Chongqing
    tag: Travel
    day: Morning high-speed train (about 1.5 hours), check in
    night: Walk around Jiefangbei, Hongyadong lit up at night, first Chongqing hotpot
  - date: Wed 12/30
    city: Chongqing
    tag: Day trip
    day: Dazu Rock Carvings (mostly flat) or Wulong Karst (lots of gorge stairs)
    night: Something easy near the hotel
  - date: Thu 12/31
    city: Chongqing
    day: Liziba station (the monorail that runs through a building), Ciqikou Ancient Town
    night: Yangtze River Cable Car, New Year countdown at Jiefangbei
  - date: Fri 1/1
    city: Chongqing
    day: Sleep in, Nanshan Yikeshu viewpoint, shopping
    night: Last hotpot, leave for the airport around 22:30 (about 40 minutes from downtown)
  - date: Sat 1/2
    city: Chongqing → Singapore
    tag: Home
    day: Depart 02:35, land in Singapore 07:50

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
    - name: "Giant Panda Base"
      kind: Sight
      why: "The breeding research base where you see pandas, cubs and red pandas up close."
      maps: 成都大熊猫繁育研究基地
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d457089-Reviews-Chengdu_Research_Base_of_Giant_Panda_Breeding-Chengdu_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Chengdu_Research_Base_of_Giant_Panda_Breeding" }
    - name: "Wenshu Monastery"
      kind: Temple
      why: "A working Buddhist monastery with gardens and a vegetarian restaurant."
      maps: 文殊院 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d457103-Reviews-Wenshu_Yuan_Monastery-Chengdu_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Wenshu_Temple_(Chengdu)" }
    - name: "People's Park and Heming Teahouse"
      kind: Park
      why: "Sip tea under the trees and watch locals dance, sing and play mahjong."
      maps: 人民公园 鹤鸣茶社 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d546614-Reviews-Chengdu_Renmin_Park-Chengdu_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/People's_Park_(Chengdu)" }
    - name: "Kuanzhai Alley"
      kind: Old town
      why: "Restored Qing-dynasty lanes with snacks, shops and teahouses."
      maps: 宽窄巷子 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d1832089-Reviews-Kuanzhai_Alley-Chengdu_Sichuan.html" }
    - name: "Leshan Giant Buddha"
      kind: Day trip
      why: "A 71m Buddha carved into a riverside cliff, UNESCO-listed. The river cruise is the low-stairs way to see it."
      maps: 乐山大佛
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g303771-d488514-Reviews-Leshan_Giant_Buddha-Leshan_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Leshan_Giant_Buddha" }
    - name: "Wuhou Shrine"
      kind: Temple
      why: "A Three Kingdoms-era memorial temple next to Jinli."
      maps: 武侯祠 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d508982-Reviews-Wuhou_Memorial_Temple-Chengdu_Sichuan.html" }
    - name: "Jinli Ancient Street"
      kind: Old town
      why: "Lantern-lit lanes, and the classic place to rent traditional costumes for photos."
      maps: 锦里古街 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d1832090-Reviews-Jinli_Pedestrian_Street-Chengdu_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Jinli" }
    - name: "Du Fu Thatched Cottage"
      kind: Garden
      why: "A quiet garden and museum for the Tang-dynasty poet Du Fu."
      maps: 杜甫草堂 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d488516-Reviews-Du_Fu_Cottage-Chengdu_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Du_Fu_Thatched_Cottage" }
    - name: "Anshun Bridge"
      kind: Night view
      why: "A covered bridge over the Jin River, lit up at night."
      maps: 安顺廊桥 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d9757726-Reviews-Anshun_Bridge_Dongmen_Bridge-Chengdu_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Anshun_Bridge" }
    - name: "Chunxi Road and Taikoo Li"
      kind: Shopping
      why: "The main shopping streets, with the giant panda climbing the IFS building."
      maps: 春熙路 太古里 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d15671160-Reviews-Taikoo_Li-Chengdu_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Chunxi_Road" }
    - name: "Shu Feng Ya Yun (Sichuan opera)"
      kind: Show
      why: "A well-known face-changing and Sichuan opera show, if the banquet show falls through."
      maps: 蜀风雅韵 成都
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g297463-d1759437-Reviews-Shu_Feng_Ya_Yun_Sichuan_Opera-Chengdu_Sichuan.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Bian_lian" }
  chongqing:
    - name: "Jiefangbei"
      kind: Landmark
      why: "The city-centre monument and pedestrian area, and the New Year countdown spot."
      maps: 解放碑 重庆
      links:
        - { label: TripAdvisor, url: "https://en.tripadvisor.com.hk/Attraction_Review-g294213-d2003325-Reviews-Jiefang_Monument-Chongqing.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Liberation_Monument_in_Chongqing" }
    - name: "Hongyadong"
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
    - name: "Nanshan Yikeshu viewpoint"
      kind: Night view
      why: "The classic lookout over the whole Chongqing skyline at night."
      maps: 南山一棵树观景台 重庆
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g294213-d1814684-Reviews-Chongqing_South_Mountain-Chongqing.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Single_Tree_Vista" }
    - name: "Dazu Rock Carvings"
      kind: Day trip
      why: "UNESCO-listed Buddhist cliff carvings, mostly flat paths."
      maps: 大足石刻
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g325577-d319625-Reviews-The_Dazu_Rock_Carvings-Dazu_County.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Dazu_Rock_Carvings" }
    - name: "Wulong Karst"
      kind: Day trip
      why: "Giant natural stone bridges and gorges, with lots of stairs."
      maps: 武隆天生三桥
      links:
        - { label: TripAdvisor, url: "https://www.tripadvisor.com/Attraction_Review-g1372315-d1814702-Reviews-Wulong_Tiankeng_Three_Bridges-Wulong_County.html" }
        - { label: Wikipedia, url: "https://en.wikipedia.org/wiki/Wulong_Karst" }
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

- The Kaan Family arrive after an overnight flight, so day 1 stays light and close to the hotel. Places everyone wants to see together, like the Panda Base, start the next day once Wonbo has joined.
- **Dress-up day (12/28, Wyn is checking)**: a package with costume rental, hair and makeup, then a traditional banquet where everyone sits and watches a show while eating. Jinli Old Street is the classic place for the costumes in Chengdu, so it's paired with Wuhou Shrine next door. The face-changing show moved here from 12/26.
- With parents in the group, places with lots of stairs also list a way to do less walking.
- The New Year countdown at Jiefangbei is extremely crowded and the streets around it are closed to traffic. Pick a meeting point in case the group gets separated.
- The 12/30 day trip is optional. For seven people, hiring a van with a driver for the day is easier than splitting up across trains and taxis.

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
- The Kaan Family arrive at 7am, long before the usual 2pm check-in. To rest right away, **book from the night of 12/24** or request early check-in ahead of time.
- **Chongqing (12/29–12/31, 3 nights)**: around Jiefangbei and Hongyadong, within walking distance after the countdown.
- **1/1**: check out, leave the bags at the hotel, and head to the airport at night. To shower and rest before the red-eye, consider **booking the night of 1/1 too**.
- For seven, book 3–4 rooms or a serviced apartment. In China only places **registered to host foreign guests** can take foreigners, so confirm that before booking.

## Getting around

- **Tianfu Airport → central Chengdu**: about 1 hour by metro line 18 or taxi. The Kaan Family will have a lot of luggage, so a pre-booked van pickup is easiest. Wonbo takes a taxi or Didi at night.
- **Chengdu → Chongqing high-speed train**: Chengdu East → Chongqing West or Chongqing North, about 1h10m–1h40m. Book with passports on the 12306 app or Trip.com, and buy all seven tickets in one order to sit together.
- **Downtown Chongqing → Jiangbei Airport T3**: about 40 minutes by taxi or Didi. The metro stops before midnight, so go by car at night.
- **In the cities**: the metro is easiest. A taxi or Didi takes four, so split into two cars or call a 6–7 seater.

## To do

- Flights: Wonbo's CA404 out and SQ819 back are booked
- Kaan Family (6) on SQ846 out; confirm all seven are on SQ819 back
- Entry rules: check the current visa-free entry policy (dates and eligible passports) before departure
- Book hotels (foreign guests accepted; extra nights on 12/24 and 1/1?)
- Airport van pickup for the Kaan Family on the morning of 12/25
- Dress-up package and banquet dinner show for 12/28 (Wyn is checking)
- High-speed train Chengdu → Chongqing and train to Leshan (book early over the holidays)
- Panda Base tickets (booked under real names)
- Link a foreign card to Alipay and WeChat Pay
- Data: roaming or a travel eSIM (KakaoTalk, WhatsApp and Google keep working)
- Winter clothes: 5–10°C during the day, damp, and indoor heating is weak
- Spice level: ask for "weila (微辣, mildly spicy)" when ordering

## Still to decide

- Compare with Meredith's plan and merge the two
- One day trip or both
- Whether to book Chengdu from the night of 12/24, and an extra night in Chongqing on 1/1
