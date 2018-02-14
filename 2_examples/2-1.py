daum = 89000
naver = 751000

def total_price(daum_vol, naver_vol):
    return daum*daum_vol + naver*naver_vol

print('total :',total_price(100, 20))