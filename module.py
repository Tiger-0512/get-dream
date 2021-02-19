from datetime import datetime
from time import sleep
from dateutil.relativedelta import relativedelta
import sys

from selenium import webdriver
import chromedriver_binary  # パスを通す


# 予約の条件を見極め
def prepare(month, day):
    dt_now = datetime.now()
    year = dt_now.year

    # 3ヶ月以内しか調べられないため、それ以外を除外
    one_month_after = (dt_now + relativedelta(months=1)).month
    two_month_after = (dt_now + relativedelta(months=2)).month
    if [dt_now.month, one_month_after, two_month_after].count(month) == 0:
        print('{}月、{}月または{}月について検索してください'.format(dt_now.month, one_month_after, two_month_after))
        sys.exit()

    # 過去の日付を調べることがないようにする
    if month < dt_now.month:
        year += 1

    # 日付の整形
    # 月が一桁の場合
    if len(str(month)) == 1:
        month = '0' + str(month)
    # 日が一桁の場合
    if len(str(day)) == 1:
        day = '0' + str(day)
    ymd = str(year) + str(month) + str(day)

    return ymd


# 予約可能かどうかをチェック
def check_date(ymd, park):
    driver = webdriver.Chrome()
    url = 'https://www.tokyodisneyresort.jp/ticket/sales_status/' + ymd[:6]
    driver.get(url)

    # 予約が埋まっている日付を格納
    calendar = driver.find_elements_by_class_name('is-none')
    print(calendar)

    for i in calendar:
        date = i.find_element_by_class_name('js-modal-open-calendar')
        if ymd == date.get_attribute('data-ymd') and park == date.get_attribute('data-park'):
            print('{}年{}月{}日の{}は予約が埋まっています。'.format(ymd[:4], ymd[4:6], ymd[6:8], date.get_attribute('data-park')))
            return False
    print(ymd)
    print('指定した日付に空きがあります！３秒毎に予約画面へのアクセスを試みます。')
    return True


# ３秒ごとに予約画面へアクセス
def access_page(month, day, park):
    ymd = prepare(month, day)

    if check_date(ymd, park):
        driver = webdriver.Chrome()
        url = 'https://reserve.tokyodisneyresort.jp/ticket/search/?outside=1&route=1&useDays=1&useDateFrom=' + ymd + '&parkTicketSalesForm=1'
        '''
        エラーテスト用URL
        url = 'https://reserve.tokyodisneyresort.jp/fo/ticket/index.html'
        '''
        driver.get(url)

        flag = 0
        while flag == 0:
            try:
                driver.find_element_by_class_name('new-ui-theme')
                flag = 1
            except:
                sleep(3)
                driver.back()
                driver.get(url)

        print('アクセスができたよ！ハハッ！')
        print('終了する際はターミナルでエンターキーを押してください。')
        input()
        print('終了処理が実行されました。ページを閉じます。')
        sys.exit()

    else:
        sys.exit()

