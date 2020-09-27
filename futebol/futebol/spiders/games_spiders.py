import scrapy
from Endereco_jogos import convert_json
from utils import adjust_data, options_scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = convert_json.json_importer(options_scrapy.file_to_convert)

    def parse(self, response):
        data = {}

        data["home_team"] = adjust_data.fix_teams_names(
            response.url.split("/")[7]
        )
        data["away_team"] = adjust_data.fix_teams_names(
            response.url.split("/")[8]
        )

        game_headers = response.css("ul > .gamehead a::text").getall()
        data["season_year"] = game_headers[2].strip()
        data["season_round"] = adjust_data.get_season_round(game_headers[3])

        result = response.css(".f-score::text").get()
        data["home_team_goals"] = result.split(" - ")[0]
        data["away_team_goals"] = result.split(" - ")[1]

        
        fields = options_scrapy.statistic_fields

        for field in fields:
            data[f"home_team_{field}"] = response.css(f'.{field} > .stat_value_number_team_A::text').get() or ""
            data[f"away_team_{field}"] = response.css(f'.{field} > .stat_value_number_team_B::text').get() or ""

        adjust_data.write_csv(data)
