
def get_bmi_result(weight, height):
    bmi = weight / (height * 0.01)**2

    print('BMI : ', bmi)
    result = ''
    if bmi < 18.5:
        result = '마른 체형'
    elif bmi < 25:
        result = '표준'
    elif bmi <30:
        result = '비만'
    else :
        result = '고도 비만'
    
    return result

if __name__ == '__main__':
    print(get_bmi_result(87, 180))
    print(get_bmi_result(70, 180))
