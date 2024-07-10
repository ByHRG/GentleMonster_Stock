import requests
import json


class GENTLE:
    def __init__(self):
        self.url = "https://www.gentlemonster.com/kr/inhouse/order/api/get_pickup_store"

    def url_setting(self, url):
        return url.split("?")[0].split("/")[-1]

    def run(self, product_code):
        if "gentlemonster" in product_code:
            product_code = self.url_setting(product_code)
        payload = json.dumps({
          "sku": product_code,
          "store_city": None
        })
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Length': '40',
            'Content-Type': 'application/json',
            'Origin': 'https://www.gentlemonster.com',
            'Priority': 'u=1, i',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }
        req = requests.post(self.url, headers=headers, data=payload)
        output = {
            "Stock": {},
        }
        for i in req.json()["전국"]:
            data = {
                i["STORE_NAME"]: i["QTY"]
            }
            output["Stock"].update(data)
        if output["Stock"] == {}:
            output["Msg"] = "재고없음"
        return output


url = "https://www.gentlemonster.com/kr/shop/item/ron01/QUQPPBO74NXK"

print(GENTLE().run(url))

