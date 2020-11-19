from selenium import webdriver
import chromedriver_binary  # パスを通す

import module

reservation = []
print('予約したい月、日、パーク(tdlまたはtds)を1つずつスペースを挟み、入力してください。正しい入力が与えられると予約の空きがあるかチェックします。')
for i in range(3):
    reservation.append(input())

module.access_page(int(reservation[0]), int(reservation[1]), reservation[2])
