import scrapy


class TestSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        "https://www.netimoveis.com/imovel/locacao-apartamento-3-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/696424/?tipoUrl=apartamento-3-quartos&bairroUrl=santo-antonio",
        "https://www.netimoveis.com/imovel/locacao-apartamento-2-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/696424/?tipoUrl=apartamento-2-quartos&bairroUrl=santo-antonio",
        "https://www.netimoveis.com/imovel/locacao-apartamento-4-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/61114/",
        "https://www.netimoveis.com/imovel/locacao-apartamento-3-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/798988/",
        "https://www.netimoveis.com/imovel/locacao-apartamento-2-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/807448/",
        "https://www.netimoveis.com/imovel/locacao-apartamento-3-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/749175/",
        "https://www.netimoveis.com/imovel/locacao-apartamento-2-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/50175/",
        "https://www.netimoveis.com/imovel/locacao-apartamento-3-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/798389/",
        "https://www.netimoveis.com/imovel/locacao-apartamento-3-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/822328/?tipoUrl=apartamento-3-quartos&bairroUrl=santo-antonio",
        "https://www.netimoveis.com/imovel/locacao-apartamento-3-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/817313/",
        "https://www.netimoveis.com/imovel/locacao-apartamento-2-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/817313/?tipoUrl=apartamento-2-quartos&bairroUrl=santo-antonio",
        "https://www.netimoveis.com/imovel/locacao-apartamento-5-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/812321/?tipoUrl=apartamento-5-quartos&bairroUrl=santo-antonio",
        "https://www.netimoveis.com/imovel/locacao-apartamento-3-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/802600/",
        "https://www.netimoveis.com/imovel/locacao-apartamento-3-quartos-minas-gerais-belo-horizonte-centro-sul-santo-antonio/586775/",
    ]

    def parse(self, response):
        data = {}
        
        data['location'] = response.css(".text-gray.mb-1 ::text").get().strip()
        data['description'] = response.css(".col.text-justify p ::text").get().strip()
        data['price'] = float(response.css(".detail-value ::text").get().split(',')[0].split('R$ ')[1].replace(".", ""))
        data['picture'] = response.css(".item.image ::attr(src)").get()
        data['area'] = response.css(".detail-value *::text").getall()[4].strip().split('m')[0]

        yield data
        # adjust_data.write_csv(data)
