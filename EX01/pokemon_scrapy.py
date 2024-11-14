# https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/
# https://www.digitalocean.com/community/tutorials/como-fazer-crawling-em-uma-pagina-web-com-scrapy-e-python-3-pt
# http://pythonclub.com.br/material-do-tutorial-web-scraping-na-nuvem.html

import scrapy

class PokemonScrapper(scrapy.Spider):
    name = 'pokemon_scrapper'
    domain = "https://pokemondb.net/"
    start_urls = ["https://pokemondb.net/pokedex/all"]

    def parse(self, response):
        pokemons = response.css('#pokedex > tbody > tr')
        for pokemon in pokemons:
            link = pokemon.css("td.cell-name > a::attr(href)").extract_first()
            yield response.follow(self.domain + link, self.parse_pokemon)

    def parse_pokemon(self, response):
        yield {
            'pokemon_id': response.css('.vitals-table > tbody > tr:nth-child(1) > td > strong::text').get(),
            'pokemon_name': response.css('#main > h1::text').get(),
            'weight': response.css('table.vitals-table tr:contains("Weight") td::text').get(),
            'height': response.css('table.vitals-table tr:contains("Height") td::text').get(),
            'types': response.css('table.vitals-table tr:contains("Type") td a::text').getall()
        }

