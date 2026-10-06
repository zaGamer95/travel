# 여행 글(_trips)의 countries / date 정보로 나라별, 연도별 목록 페이지를 자동 생성합니다.
#   /travel/country/<slug>/
#   /travel/year/<yyyy>/
#
# _trips/2025-tokyo.md          -> 여행 본문 (slug: 2025-tokyo)
# _trips/2025-tokyo/day-2.md    -> 같은 여행의 하위 글 (목록에는 안 나오고 본문에서 링크)
# planned: true                 -> 아직 안 다녀온 여행 계획. 메인 위쪽 "다가오는 여행"에만 나와요.
module Travel
  class ListPage < Jekyll::Page
    def initialize(site, dir, layout, data)
      @site = site
      @base = site.source
      @dir  = dir
      @name = "index.html"
      process(@name)
      @content = ""
      @data = { "layout" => layout }.merge(data)
    end
  end

  class Generator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      trips = site.collections["trips"]&.docs || []
      countries = site.data["countries"] || {}

      trips.each do |doc|
        parts = doc.relative_path.sub(%r{\A_trips/}, "").sub(/\.[^.]+\z/, "").split("/")
        doc.data["trip_slug"] = parts.first
        doc.data["subpage"] = parts.length > 1
        doc.data["year"] = doc.date.year
        doc.data["countries"] = Array(doc.data["countries"])
      end

      # planned: true 인 여행은 "다가오는 여행"으로 따로 모으고, 나라·연도 목록에는 넣지 않아요.
      all_main = trips.reject { |d| d.data["subpage"] }
      planned = all_main.select { |d| d.data["planned"] }.sort_by(&:date)
      main = (all_main - planned).sort_by(&:date).reverse
      all_main.each do |doc|
        doc.data["subpages"] = trips.select { |d| d.data["subpage"] && d.data["trip_slug"] == doc.data["trip_slug"] }
                                    .sort_by { |d| [d.date, d.relative_path] }
      end
      trips.select { |d| d.data["subpage"] }.each do |d|
        d.data["parent_trip"] = all_main.find { |m| m.data["trip_slug"] == d.data["trip_slug"] }
      end

      main.flat_map { |d| d.data["countries"] }.uniq.each do |slug|
        site.pages << ListPage.new(site, "country/#{slug}", "list", {
          "title" => countries.fetch(slug, slug),
          "list_kind" => "country",
          "trips" => main.select { |d| d.data["countries"].include?(slug) },
        })
      end

      main.map { |d| d.data["year"] }.uniq.each do |year|
        site.pages << ListPage.new(site, "year/#{year}", "list", {
          "title" => "#{year}년",
          "list_kind" => "year",
          "trips" => main.select { |d| d.data["year"] == year },
        })
      end

      site.data["main_trips"] = main
      site.data["planned_trips"] = planned
      site.data["trip_years"] = main.map { |d| d.data["year"] }.uniq.sort.reverse
    end
  end
end
