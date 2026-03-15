from parsel import Selector
import httpx

response = httpx.get("http://www.ipeadata.gov.br/ExibeSerie.aspx?serid=38590&module=M")
selector = Selector(response.text)

dollar = []
for data in selector.css("tr.dxgvDataRow"):
#    day_1 = data.css("td.dxgv::text").get()
    day_1 = data.css("td.dxgv::text").getall()[1]
    dollar.append(day_1)
#    print(dollar)
    for currency in dollar:
        print(currency, "\n")
