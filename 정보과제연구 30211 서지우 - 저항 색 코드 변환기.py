color_code = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9
}

multiplier_code = {
    "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
    "green": 100000, "blue": 1000000, "violet": 10000000, "gray": 100000000, "white": 1000000000,
    "gold": 0.1, "silver": 0.01
}

tolerance_code = {
    "brown": 1, "red": 2, "green": 0.5, "blue": 0.25, "violet": 0.1, "gray": 0.05, "gold": 5, "silver": 10
}

def color_to_resistance():
    while True:
        try:
            bands = input("저항 색 코드를 공백으로 구분하여 입력하세요 (예: yellow violet red gold, 종료: exit): ").strip()
            if bands.lower() == "exit":
                print("프로그램을 종료합니다.")
                break

            bands = bands.split()
            if len(bands) != 4:
                print("잘못된 입력입니다. 네 개의 색 코드를 입력하세요.")
                continue

            value = (color_code[bands[0]] * 10 + color_code[bands[1]]) * multiplier_code[bands[2]]
            tolerance = tolerance_code[bands[3]]

            print(f"저항값: {value}Ω ±{tolerance}%\n")

            again = input("한 번 더 계산하시겠습니까? (Y/N): ").strip().lower()
            if again != "y":
                print("프로그램을 종료합니다.")
                break

        except KeyError:
            print("잘못된 색 코드가 입력되었습니다. 올바른 색상을 입력해주세요.")
        except Exception as e:
            print("오류 발생:", e)

# 프로그램 실행
color_to_resistance()
