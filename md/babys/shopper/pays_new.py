# pip install pycrypto
# pip install alipay-sdk-python
# 买家账号：ltyavg2644@sandbox.com
# 登录和支付密码：111111


import logging
from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a', )
logger = logging.getLogger('')

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAizM2r9tsEowVmi5P5RIniEBEKvd1byAvA3p1w37oEOV8e5pEmZb51Uh3wXQgExOPXUTM5vUm35CCxfNJ8aixZ7EH54ZyufL0AqwfSgwhQ0xASEK6lBxtwVJGr4H/wfKJh1TGRbxunV/tcPdKgIuRBdc55NZgWWc1Ran0zWb3moZ6e7Nc/8E2BsKaAdjCV8QfKtQDc0vSiqhqMwQe0SZA4CUPE8hSPVLo+jucR3Yjb8HyNXFCxz+TerHknIwaOoiN/hWx8GeL1XjEcpbHBLStXUD1V5fk2wJRwMRU1v0DjfujmjYQAPsRZrnSXttePL6pRvE6dsMUHDomVRgCLXBWlQIDAQAB
-----END PUBLIC KEY-----"""
app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAo5Uz9RJ0YT45zuxx6H3cNkjwnJR6leI0LcvAeXy696WgLiymU1m9b4gXJu9bsjRe0IeeNvlv6qjFpV6lKBygojSpsUxw+MYP8GTal/8im3L6jbgeiN7Eazl3TicJMvv2yUOZWvWfWOPWnxaf7pNQFN1JBBtyxYiqbntrfy4Q6RN+WNNjl+CvWoStHanrSGDv3ydsiPgsgNS0GSlCK3jtoxwQj5gawRdh23xQarwr4vuxhyywOtYDFrQbjmya7ij7Rev/Ke0AMlbqJeyczhYl6pPyk49ktae6WSOGr6mW7tDMOnsKIS30VsMQCpylKB3yMmL+44RuR3xBa6/SJGXKMwIDAQABAoIBAHP2onWaVoxVK2/oKDvzdTe6b2/gxiIY0HqilVjKNlS2wh3ZozM1S9iT9i2wwyVKgOh9K4i3PUJx0GMR/Cy6VpmGkcFRekixR71YEapswKDIWpw6qNLIcR++BjiN7bSJ8AHvfPiBZSwDoDL5O/lJzxxrXoad2rfz0TYvIh5vjqda8/v1f/XVVneBvt5C8vP5UP4O1bUSVHydCiVwXqoLBgBWEskAZ7pFZC0v/VpmOjJyifZIxoSiWPbAB492lu/LpRNhnavuipWA2fe2mjf9X/nTHZKgNhozrWEVEbGOYn28kP+Ac7CdIH1sGaKUd+TjSE2ANkYSFibPCGN56dWKj2ECgYEA/6fn3fJHQlbIo/6eY6gSDLHvmTBbqli8VrZsM98y/cy/1Br6ws6MUmjblJR+HOow0pLDT6b9Drzm16eKJ0bS0G0xIUKv6xwthwTfX4zCWDGg3IW/MCxYrdFx6o+JgVx25hhwLzj803BfeILp8VizK+zo4Sp32Sb7NkSSqwbLABECgYEAo82SEFfZJ9LMBM0b3c/tFiCxutN73604NEmomIUYsSxH7iYvuArN2lp8kpXKoHXarXI9QgVhj5niyViWYuOv3oNfYrakhe4wInlzA4ExdslQf7x2HUfotaxtlOz5L+//ToCAeyTupwhXAC6lhllMeQCoJ8WfHAYK/FamJYPiKgMCgYAES4DUtLZHwgd64dMtX2x2NCMPUsWndfgsCMKGmJBVvTPXz2A5F5k55TMTKu93cuPBFeAcHXUQ41GJe/IRONpf0AXMRj+IVp/ZLdbG1ymIq8TFD6YnnAcdXHBqfWDVAIWq1exEjtOIhdHEx4ZAnLnd2gwLhFghGMuNnNdN8j5E0QKBgBLwHHgJQBELnQzdDeC6PmX1h7ba5pJ4u2vILFbd5Hnvba2J+rBjh2M8XPSxnsiod4zgDVcJujrZBtBSjqiGPHoUZD3Mcf8OB8Ckm/iGwkpCgi0Sg/Fks/H1KoIyV6kELVdNIg2auoDTRQO/YOHEh0PiII7gmUGrLS/5cKIbulUzAoGACqUhHYzewnqcJOz2CV21ozCFqNCqJ3kfgvwiTrFsIF6V6MzGg38wZ+xquBv1gIyV+lJbjI559jjTmjBbiI1Z3UZpVIQI100q6hHXhKYNrvteWZ4hYLiy0n5GUS8nrz/Mn7hv7Rj5i06TefE/aHrzrgglfg4raLft2bKB86UTe4Q=
-----END RSA PRIVATE KEY-----"""
alipay_client_config = AlipayClientConfig()
alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
alipay_client_config.app_id = '2016102000726748'
alipay_client_config.app_private_key = app_private_key_string
alipay_client_config.alipay_public_key = alipay_public_key_string
client = DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)


def get_pay(out_trade_no, total_amount, return_url):
    model = AlipayTradePagePayModel()
    model.out_trade_no = out_trade_no
    model.total_amount = str(total_amount)
    model.subject = "测试"
    model.body = "支付宝测试"
    model.product_code = "FAST_INSTANT_TRADE_PAY"

    request = AlipayTradePagePayRequest(biz_model=model)

    request.notify_url = return_url + '?t=' + out_trade_no
    request.return_url = return_url + '?t=' + out_trade_no
    response = client.page_execute(request, http_method="GET")
    return response
