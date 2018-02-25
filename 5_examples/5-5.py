import module5_4 as bmi


while True:
    weight = float(input('몸무게(kg) : '))
    height = float(input('키(cm) : '))

    print('결과 : ', bmi.get_bmi_result(weight, height))