import json

# JSON 파일에서 딕셔너리 불러오기
with open("resistor_codes.json", "r") as f:
    codes = json.load(f)

color_code = codes["color_code"]
multiplier_code = codes["multiplier_code"]
tolerance_code = codes["tolerance_code"]

def color_to_resistance():
    while True:
        try:
            bands = input("저항 색 코드를 공백으로 구분하여 입력하세요 (예: yellow violet red gold 또는 brown black black red brown, 종료: exit): ").strip()
            if bands.lower() == "exit":
                print("프로그램을 종료합니다.")
                break

            bands = bands.split()

            if len(bands) == 4:
                value = (color_code[bands[0]] * 10 + color_code[bands[1]]) * multiplier_code[bands[2]]
                tolerance = tolerance_code[bands[3]]
                print(f"저항값: {value}Ω ±{tolerance}%\n")

            elif len(bands) == 5:
                value = (color_code[bands[0]] * 100 + color_code[bands[1]] * 10 + color_code[bands[2]]) * multiplier_code[bands[3]]
                tolerance = tolerance_code[bands[4]]
                print(f"저항값: {value}Ω ±{tolerance}%\n")

            else:
                print("잘못된 입력입니다. 색 코드는 4개 또는 5개여야 합니다.")
                continue

            # Y/N 반복 처리
            while True:
                again = input("한 번 더 계산하시겠습니까? (Y/N): ").strip().lower()
                if again == "y":
                    break
                elif again == "n":
                    print("프로그램을 종료합니다.")
                    return
                else:
                    print("Y 또는 N만 입력해주세요.")

        except KeyError:
            print("잘못된 색 코드가 입력되었습니다. 올바른 색상을 입력해주세요.")
        except Exception as e:
            print("오류 발생:", e)

# 프로그램 실행
color_to_resistance()

