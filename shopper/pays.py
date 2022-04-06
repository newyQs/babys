# pip install pycryptodome
# pip install python-alipay-sdk
from alipay import AliPay

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAizM2r9tsEowVmi5P5RIniEBEKvd1byAvA3p1w37oEOV8e5pEmZb51Uh3wXQgExOPXUTM5vUm35CCxfNJ8aixZ7EH54ZyufL0AqwfSgwhQ0xASEK6lBxtwVJGr4H/wfKJh1TGRbxunV/tcPdKgIuRBdc55NZgWWc1Ran0zWb3moZ6e7Nc/8E2BsKaAdjCV8QfKtQDc0vSiqhqMwQe0SZA4CUPE8hSPVLo+jucR3Yjb8HyNXFCxz+TerHknIwaOoiN/hWx8GeL1XjEcpbHBLStXUD1V5fk2wJRwMRU1v0DjfujmjYQAPsRZrnSXttePL6pRvE6dsMUHDomVRgCLXBWlQIDAQAB
-----END PUBLIC KEY-----"""
app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAo5Uz9RJ0YT45zuxx6H3cNkjwnJR6leI0LcvAeXy696WgLiymU1m9b4gXJu9bsjRe0IeeNvlv6qjFpV6lKBygojSpsUxw+MYP8GTal/8im3L6jbgeiN7Eazl3TicJMvv2yUOZWvWfWOPWnxaf7pNQFN1JBBtyxYiqbntrfy4Q6RN+WNNjl+CvWoStHanrSGDv3ydsiPgsgNS0GSlCK3jtoxwQj5gawRdh23xQarwr4vuxhyywOtYDFrQbjmya7ij7Rev/Ke0AMlbqJeyczhYl6pPyk49ktae6WSOGr6mW7tDMOnsKIS30VsMQCpylKB3yMmL+44RuR3xBa6/SJGXKMwIDAQABAoIBAHP2onWaVoxVK2/oKDvzdTe6b2/gxiIY0HqilVjKNlS2wh3ZozM1S9iT9i2wwyVKgOh9K4i3PUJx0GMR/Cy6VpmGkcFRekixR71YEapswKDIWpw6qNLIcR++BjiN7bSJ8AHvfPiBZSwDoDL5O/lJzxxrXoad2rfz0TYvIh5vjqda8/v1f/XVVneBvt5C8vP5UP4O1bUSVHydCiVwXqoLBgBWEskAZ7pFZC0v/VpmOjJyifZIxoSiWPbAB492lu/LpRNhnavuipWA2fe2mjf9X/nTHZKgNhozrWEVEbGOYn28kP+Ac7CdIH1sGaKUd+TjSE2ANkYSFibPCGN56dWKj2ECgYEA/6fn3fJHQlbIo/6eY6gSDLHvmTBbqli8VrZsM98y/cy/1Br6ws6MUmjblJR+HOow0pLDT6b9Drzm16eKJ0bS0G0xIUKv6xwthwTfX4zCWDGg3IW/MCxYrdFx6o+JgVx25hhwLzj803BfeILp8VizK+zo4Sp32Sb7NkSSqwbLABECgYEAo82SEFfZJ9LMBM0b3c/tFiCxutN73604NEmomIUYsSxH7iYvuArN2lp8kpXKoHXarXI9QgVhj5niyViWYuOv3oNfYrakhe4wInlzA4ExdslQf7x2HUfotaxtlOz5L+//ToCAeyTupwhXAC6lhllMeQCoJ8WfHAYK/FamJYPiKgMCgYAES4DUtLZHwgd64dMtX2x2NCMPUsWndfgsCMKGmJBVvTPXz2A5F5k55TMTKu93cuPBFeAcHXUQ41GJe/IRONpf0AXMRj+IVp/ZLdbG1ymIq8TFD6YnnAcdXHBqfWDVAIWq1exEjtOIhdHEx4ZAnLnd2gwLhFghGMuNnNdN8j5E0QKBgBLwHHgJQBELnQzdDeC6PmX1h7ba5pJ4u2vILFbd5Hnvba2J+rBjh2M8XPSxnsiod4zgDVcJujrZBtBSjqiGPHoUZD3Mcf8OB8Ckm/iGwkpCgi0Sg/Fks/H1KoIyV6kELVdNIg2auoDTRQO/YOHEh0PiII7gmUGrLS/5cKIbulUzAoGACqUhHYzewnqcJOz2CV21ozCFqNCqJ3kfgvwiTrFsIF6V6MzGg38wZ+xquBv1gIyV+lJbjI559jjTmjBbiI1Z3UZpVIQI100q6hHXhKYNrvteWZ4hYLiy0n5GUS8nrz/Mn7hv7Rj5i06TefE/aHrzrgglfg4raLft2bKB86UTe4Q=
-----END RSA PRIVATE KEY-----"""


def get_pay(out_trade_no, total_amount, return_url):
    # 实例化支付应用
    alipay = AliPay(
        appid="2016102000726748",
        app_notify_url=None,
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2"
    )
    # 发起支付请求
    order_string = alipay.api_alipay_trade_page_pay(
        # 订单号，每次发送请求都不能一样
        out_trade_no=out_trade_no,
        # 支付金额
        total_amount=str(total_amount),
        # 交易信息
        subject="测试",
        return_url=return_url + '?t=' + out_trade_no,
        notify_url=return_url + '?t=' + out_trade_no
    )
    return 'https://openapi.alipaydev.com/gateway.do?' + order_string
