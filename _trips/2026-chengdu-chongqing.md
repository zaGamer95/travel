---
title: Chengdu → Chongqing, 9 days
date: 2026-12-25
end_date: 2027-01-02
countries: [china]
planned: true             # After the trip, delete this line and add a cover, photos and the write-up.
summary: A year-end Sichuan trip for seven. Pandas and the Leshan Giant Buddha in Chengdu, Chongqing's night views and hotpot, and New Year's Eve.

# Flights: rendered as cards by {% include flights.html %}
flights:
  - who: Group of 6
    airline: Singapore Airlines
    flight: SQ846
    from: { code: SIN, city: Singapore, date: Fri 12/25, time: "02:10" }
    to:   { code: TFU, city: Chengdu Tianfu, date: Fri 12/25, time: "06:55" }
  - who: Wonbo
    airline: Air China
    flight: CA404
    from: { code: SIN, city: Singapore T1, date: Fri 12/25, time: "16:00" }
    to:   { code: TFU, city: Chengdu Tianfu T1, date: Fri 12/25, time: "21:05" }
  - who: All 7
    airline: Singapore Airlines
    flight: SQ819
    from: { code: CKG, city: Chongqing Jiangbei T3, date: Sat 1/2, time: "02:35" }
    to:   { code: SIN, city: Singapore, date: Sat 1/2, time: "07:50" }
    note: This leaves in the early hours after New Year's Day. Head to the airport around 22:30 on 1/1.

# Day by day: rendered by {% include itinerary.html %}
days:
  - date: Fri 12/25
    city: Chengdu
    day: "Group of 6: land 06:55, drop bags at the hotel and rest. Afternoon tea in People's Park, stroll Kuanzhai Alley"
    night: "Group of 6: dinner near the hotel. Wonbo: lands 21:05, to the hotel (about 1 hour)"
  - date: Sat 12/26
    city: Chengdu
    day: Panda Base (pandas are most active in the morning; use the electric carts inside), Wenshu Monastery
    night: Sichuan opera face-changing show, hotpot
  - date: Sun 12/27
    city: Chengdu
    tag: Day trip
    day: Leshan Giant Buddha (about 1 hour by high-speed train). The cliff stairs are steep with long queues, so the parents can see it from the river cruise instead
    night: Back to Chengdu, chuanchuan skewers
  - date: Mon 12/28
    city: Chengdu
    day: Wuhou Shrine and Jinli Old Street, Du Fu Thatched Cottage
    night: Chunxi Road and Taikoo Li, Anshun Bridge and Jiuyan Bridge at night
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
      tip: Order the split pot (鸳鸯锅) with a mushroom or tomato broth on one side for anyone avoiding beef.
    - name: Shu Daxia (蜀大侠)
      kind: Hotpot
      why: A big chain, so a table for seven is easy to get.
      warn: [tallow]
      tip: They offer a vegetable-oil broth (清油锅底).
    - name: Yulin Chuanchuan (玉林串串香)
      kind: Chuanchuan skewers
      why: Chengdu-style skewers you pick yourself and cook in the broth.
      warn: [tallow]
      tip: You choose every skewer, so skipping beef is easy. Ask for the 清油 broth.
    - name: Ma Wangzi (马旺子)
      kind: Sichuan dishes
      why: A polished Sichuan restaurant with private rooms, good with parents.
      warn: [beef]
      tip: Skip the beef dishes and order chicken, pork and tofu.
    - name: Chen Mapo Tofu (陈麻婆豆腐)
      kind: Sichuan dishes
      why: Where mapo tofu was invented.
      warn: [beef]
      tip: Mapo tofu is made with minced beef. Ask for a separate pork version.
    - name: Long Chaoshou (龙抄手)
      kind: Snacks
      why: A long-running wonton shop on Chunxi Road. Good for trying many small snacks.
      warn: [ok]
    - name: Zhong Dumplings (钟水饺)
      kind: Snacks
      why: Pork dumplings in a sweet and spicy sauce.
      warn: [ok]
    - name: Shuangliu Laoma Rabbit Heads (双流老妈兔头)
      kind: Adventurous
      why: Spicy rabbit heads that locals have with beer. Worth trying once.
      warn: [ok]
  chongqing:
    - name: Peijie Hotpot (佩姐老火锅)
      kind: Hotpot
      why: One of Chongqing's most famous hotpot restaurants. Expect a long queue.
      warn: [tallow, beef]
      tip: The default broth is beef tallow and the signature dish is beef tripe (毛肚). Get a split pot with one side 清油.
    - name: Air-raid shelter hotpot (防空洞火锅)
      kind: Hotpot
      why: Hotpot inside old air-raid shelter caves, a uniquely Chongqing atmosphere.
      warn: [tallow]
      tip: Every place is different, so ask first whether they have a 清油 broth.
    - name: Taoranju (陶然居)
      kind: Jianghu home-style dishes
      why: Chongqing home cooking such as laziji (辣子鸡, chili-fried chicken). Has large round tables.
      warn: [ok]
      tip: Just skip the beef dishes when ordering.
    - name: Huashi Wanza Noodles (花市豌杂面)
      kind: Noodles
      why: Chongqing noodles topped with peas and minced pork. A good breakfast.
      warn: [ok]
    - name: Haoyoulai Suanlafen (好又来酸辣粉)
      kind: Noodles
      why: Sour and spicy sweet-potato noodles near Jiefangbei.
      warn: [ok]
    - name: Bayi Food Street (八一好吃街)
      kind: Street food
      why: A food alley next to Jiefangbei for grazing on a bit of everything.
      warn: [shellfish, cheese]
      tip: Spicy stir-fried clams (花甲) and cheese-topped snacks are common here. Pick around them.
    - name: Chen Mahua (陈麻花)
      kind: Snacks
      why: Ciqikou's famous fried dough twists. Good as gifts too.
      warn: [ok]
---

## At a glance

- **Dates**: Fri 2026.12.25 – Sat 2027.01.02
- **Group**: 7 people. My girlfriend, her parents, her younger brother, her younger sister, her sister's boyfriend, and me (Wonbo)
- **Route**: Singapore → Chengdu (4 nights) → high-speed train → Chongqing (3 nights plus the last day) → Singapore

## Flights (booked)

{% include flights.html %}

- My girlfriend's family of 6 arrives in the morning and I join them that night.
- My ticket (CA404) includes one 23kg checked bag.

## Itinerary

{% include itinerary.html %}

- The group of 6 arrives after an overnight flight, so day 1 stays light and close to the hotel. Places we all want to see together, like the Panda Base, start the next day once I've joined.
- With parents in the group, places with lots of stairs also list a way to do less walking.
- The New Year countdown at Jiefangbei is extremely crowded and the streets around it are closed to traffic. Pick a meeting point in case the group gets separated.
- The 12/30 day trip is optional. For seven people, hiring a van with a driver for the day is easier than splitting up across trains and taxis.

## Where to eat

Someone in the group **can't eat beef or cheese**, and someone **can't eat shellfish**. Famous places are still on the list, with what to watch out for; whoever can't eat a dish just orders something separate. Seven people need a big table, so book popular places ahead or arrive at opening time. Check opening hours and locations again before the trip.

### What to watch out for in Sichuan food

- **Hotpot and chuanchuan broth**: red Chongqing-style broth is made with **beef tallow (牛油)** by default. Ask for **qingyou (清油, vegetable-oil) broth**, or get a split pot (鸳鸯锅) with a mushroom or tomato side.
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
<p class="zh">我们有人不吃牛肉、奶酪和贝类（蛤蜊、花甲、扇贝）。<br>请用清油锅底，不要牛油。</p>
<p class="tr">Some of us can't eat beef, cheese or shellfish. Please use vegetable-oil broth, not beef tallow.</p>
</div>

## Where to stay

- **Chengdu (12/25–12/28, 4 nights)**: around Chunxi Road and Taikoo Li, on metro lines 2 and 3.
- The group of 6 arrives at 7am, long before the usual 2pm check-in. To rest right away, **book from the night of 12/24** or request early check-in ahead of time.
- **Chongqing (12/29–12/31, 3 nights)**: around Jiefangbei and Hongyadong, within walking distance after the countdown.
- **1/1**: check out, leave the bags at the hotel, and head to the airport at night. To shower and rest before the red-eye, consider **booking the night of 1/1 too**.
- For seven, book 3–4 rooms or a serviced apartment. In China only places **registered to host foreign guests** can take foreigners, so confirm that before booking.

## Getting around

- **Tianfu Airport → central Chengdu**: about 1 hour by metro line 18 or taxi. The group of 6 has a lot of luggage, so a pre-booked van pickup is easiest. I'll take a taxi or Didi at night.
- **Chengdu → Chongqing high-speed train**: Chengdu East → Chongqing West or Chongqing North, about 1h10m–1h40m. Book with passports on the 12306 app or Trip.com, and buy all seven tickets in one order to sit together.
- **Downtown Chongqing → Jiangbei Airport T3**: about 40 minutes by taxi or Didi. The metro stops before midnight, so go by car at night.
- **In the cities**: the metro is easiest. A taxi or Didi takes four, so split into two cars or call a 6–7 seater.

## To do

- Flights: Wonbo's CA404 out and SQ819 back are booked
- Group of 6 on SQ846 out; confirm all seven are on SQ819 back
- Entry rules: check the current visa-free entry policy (dates and eligible passports) before departure
- Book hotels (foreign guests accepted; extra nights on 12/24 and 1/1?)
- Airport van pickup for the group of 6 on the morning of 12/25
- High-speed train Chengdu → Chongqing and train to Leshan (book early over the holidays)
- Panda Base tickets (booked under real names)
- Link a foreign card to Alipay and WeChat Pay
- Data: roaming or a travel eSIM (KakaoTalk, WhatsApp and Google keep working)
- Winter clothes: 5–10°C during the day, damp, and indoor heating is weak
- Spice level: ask for "weila (微辣, mildly spicy)" when ordering

## Still to decide

- Compare with my girlfriend's sister's plan and merge the two
- One day trip or both
- Whether to book Chengdu from the night of 12/24, and an extra night in Chongqing on 1/1
