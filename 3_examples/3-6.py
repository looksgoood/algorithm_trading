naver_end_price = [474500, 461500, 501000, 500500, 488500]
day_str = '09/%02d'

naver_end_price2 = {}
day = 7
for price in naver_end_price:
    naver_end_price2[day_str % day] = price
    day += 1

print(naver_end_price2)