daum = 89000
naver = 751000

def total_price(daum_vol, naver_vol):
    return daum*daum_vol + naver*naver_vol

prev_total = total_price(100, 20)
print('prev total :', prev_total)

daum *= 0.95
naver *= 0.90

cur_total = total_price(100, 20)
print('cur_total :', int(cur_total))

print('손실액 :', int(prev_total - cur_total))