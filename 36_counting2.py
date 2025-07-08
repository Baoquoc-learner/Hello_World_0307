# Using countinue in a loop

currentNumber = 0
while currentNumber < 10:
    currentNumber += 1
    if currentNumber % 2 == 0:
        # break  # break sẽ kết thúc ngay lập tức
        # continue  # chuyển sang giá trị tiếp theo của vòng lập
        continue
        # print(currentNumber)

    print(currentNumber)
