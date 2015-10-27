# -*- coding: utf-8 -*-
u"""
    결제모듈 연동 서비스 아임포트 I'mport;(http://www.iamport.kr) 의 파이썬 바인딩.
    이 모듈은 https://api.iamport.kr 의 내용을 바탕으로 만들어졌습니다.
"""
import requests


class IamportError(Exception):
    def __init__(self, code=None, message=None):
        self.code = code
        self.message = message


def get_access_token(api_key, api_secret):
    u"""
    API 호출시 필요한 access token 발급
    """
    url = u'https://api.iamport.kr/users/getToken'
    response = requests.post(url, data=dict(
        imp_key=api_key,
        imp_secret=api_secret,
    ))

    if response.status_code != 200:
        raise IOError  # TODO

    result = response.json()

    if result[u'code'] is not 0:
        raise IamportError(result[u'code'], result[u'message'])

    return result[u'response'][u'access_token']


class Iamport(object):
    u"""
    아임포터 결제 모듈
    """
    TOKEN_HEADER = u'X-ImpTokenHeader'

    def __init__(self, access_token):
        self._access_code = access_token

    def _set_default(self, data, headers):
        if not data:
            data = {}

        if not headers:
            headers = {}
        headers[self.TOKEN_HEADER] = self._access_code

        return data, headers

    def _parse_response(self, response):
        if response.status_code != 200 or not response.content:
            raise IOError

        result = response.json()

        if result[u'code'] is not 0:
            raise IamportError(result[u'code'], result[u'message'])

        return result[u'response']

    def _get(self, url, data=None, headers=None):
        data, headers = self._set_default(data, headers)
        response = requests.get(url, headers=headers, params=data)

        return self._parse_response(response)

    def _post(self, url, data=None, headers=None):
        data, headers = self._set_default(data, headers)
        response = requests.post(url, headers=headers, data=data)

        return self._parse_response(response)

    def onetime(self, **params):
        u"""
        비인증 결제 요청

        필수 keyword arguments:
            merchant_uid -- 상점의 고유 주문번호
            amount       -- 결제금액
            card_number  -- 신용카드번호(dddd-dddd-dddd-dddd)
            expiry       -- 카드 유효기간(YYYY-MM)
            birth        -- 생년월일6자리
            pwd_2digit   -- 카드비밀번호 앞 2자리
        추가 keyword arguments:
            vat            -- 결제금액 중 부가세 금액
            customer_uid   -- string 타입의 고객 고유번호
            name           -- 주문명
            buyer_name     -- 주문자명
            buyer_email    -- 주문자 email 주소
            buyer_tel      -- 주문자 전화번호
            buyer_addr     -- 주문자 주소
            buyer_postcode -- 주문자 우편번호

        자세한 설명은 https://api.iamport.kr/#!/subscribe/sbcr_onetime 참고.
       """
        url = u'https://api.iamport.kr/subscribe/payments/onetime/'
        keys = [u'token', u'merchant_uid', u'amount', u'vat', u'card_number', u'expiry', u'birth', u'pwd_2digit',
                u'remember_me', u'customer_uid', u'buyer_name', u'buyer_email', ]
        data = {k: v for k, v in params.items() if k in keys}

        return self._post(url, data)

    def find_by_merchant_uid(self, merchant_uid):
        u"""
        결제 내역 확인
        """
        url = u'https://api.iamport.kr/payments/find/{merchant_uid}'.format(merchant_uid=merchant_uid)

        return self._get(url)

    def cancel(self, merchant_uid):
        u"""
        결제 취소
        """
        raise NotImplemented
