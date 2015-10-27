# iamport
결제모듈 연동 서비스 아임포트 I'mport;(http://www.iamport.kr) 의 파이썬 파인딩.

(originally from https://github.com/pythonkr/pyconkr-2015)

## 경고
**WORK IN PROGRESS**

이 라이브러리를 실제 프로덕트에서 사용하지 않기를 권장합니다.

구현과 테스트에 많은 작업이 필요한 상태입니다.

## 사용예

```
access_token = get_access_token(API_KEY, API_SECRET)
iamport = Iamport(access_token)

# 비인증결제 요청
iamport.onetime(
    merchant_uid=merchant_uid,  # 고유 주문번호
    amount=29900,  # 결제금액
    card_number='42xx-0000-0000-0000',  # 신용카드번호
    expiry='2015-10',  # 카드 유효기간(YYYY-MM)
    birth='871231'  # 생년월일6자리
)

# 결제내역 가져오기
iamport.find_by_merchant_uid(merchant_uid)
```
