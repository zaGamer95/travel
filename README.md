# 여행 기록 (wonbo.site/travel/)

Jekyll로 만든 여행 블로그예요. GitHub Pages 프로젝트 사이트라서 홈페이지(wonbo.site)의 커스텀 도메인을 그대로 따라 `wonbo.site/travel/` 에 올라가요.

## 처음 한 번만 설정

1. 레포 **Settings → Pages → Build and deployment → Source** 를 **GitHub Actions** 로 바꿔 주세요.
   (나라별·연도별 페이지를 자동으로 만드는 플러그인 때문에 기본 빌드 대신 `.github/workflows/pages.yml` 로 빌드해요.)
2. 홈페이지 레포에서 `/travel/` 로 가는 링크를 하나 걸어 주세요.

## 주소 구조

| 주소 | 내용 |
| --- | --- |
| `/travel/` | 전체 여행 목록 (최신순, 한국 · 일본 · 싱가포르 · 그 외 탭) |
| `/travel/2025-tokyo/` | 여행 하나 |
| `/travel/2025-tokyo/day-2/` | 그 여행의 하위 글 (선택) |
| `/travel/country/japan/` | 나라별 모아보기 (자동 생성) |
| `/travel/year/2025/` | 연도별 모아보기 (자동 생성) |

## 새 여행 글 쓰기

1. **사진 줄이기.** 원본을 `raw/2026-osaka/` 에 넣고 실행해요. `raw/` 는 커밋되지 않아요.
   ```sh
   pip install pillow            # 처음 한 번 (아이폰 HEIC는 pillow-heif 도)
   python3 scripts/resize_photos.py raw/2026-osaka 2026-osaka --rename
   ```
   긴 변 1600px WebP로 줄여서 `assets/photos/2026-osaka/01.webp, 02.webp …` 로 저장하고, GPS 같은 위치 정보는 지워요.

2. **글 파일 만들기.** `_trips/2026-osaka.md`
   ```yaml
   ---
   title: 오사카 2박 3일
   date: 2026-05-01          # 출발일. 연도별 페이지와 정렬에 쓰여요.
   end_date: 2026-05-03      # 선택
   countries: [japan]        # 여러 나라면 [japan, korea]
   cover: 01.webp            # 목록에 나오는 대표 사진
   summary: 한 줄 소개
   album_url: https://...    # 선택: 전체 앨범 링크 (Google Photos 등)
   ---
   ```
   본문에서 사진은 이렇게 넣어요.
   ```liquid
   {% include photo.html src="03.webp" caption="도톤보리" %}
   ```

3. **날마다 나눠 쓰고 싶으면** `_trips/2026-osaka/day-2.md` 처럼 같은 이름의 폴더 안에 파일을 만들면 돼요. 여행 본문 아래에 목록으로 자동 연결돼요.

4. **새 나라**는 `_data/countries.yml` 에 `slug: 표시 이름` 한 줄을 추가하세요. 메인 탭에 따로 띄울 나라는 `_config.yml` 의 `featured_countries` 에서 바꿔요.

## 내 컴퓨터에서 미리 보기

```sh
bundle install
bundle exec jekyll serve
# http://localhost:4000/travel/
```

## 용량 관리

본문 사진은 장당 200~400KB 정도라 레포 권장 용량(1GB) 안에서 여행 수십 개는 충분해요. 원본은 커밋하지 말고 앨범 서비스에 올려 `album_url` 로 연결하세요. 나중에 용량이 차면 사진만 외부 저장소(Cloudflare R2 등)로 옮기고 경로를 바꾸면 돼요.
