def outer():
    outer_data = "외부 함수의 데이터"

    def inner():
        nonlocal outer_data
        #함수 내부에 데이터를 생성하지 않고 외부의 데이터를 사용하기 위해서 이름을 다시 등록
        outer_data ="내부에서 -"
        print(outer_data)
    inner()
    print(outer_data)
outer()
