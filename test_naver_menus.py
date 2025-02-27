import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Chrome WebDriver 설정
@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.maximize_window()
    yield driver
    driver.quit()

# Naver 홈페이지가 정상적으로 로딩되는지 확인
def test_naver_homepage(driver):
    driver.get('https://www.naver.com')
    assert 'NAVER' in driver.title  # 페이지 타이틀에 'NAVER'가 포함되어 있는지 확인

# 검색창이 있는지 확인
def test_search_bar_exists(driver):
    driver.get('https://www.naver.com')
    search_box = driver.find_element(By.ID, 'query')  # 검색창의 ID는 'query'
    assert search_box.is_displayed()  # 검색창이 화면에 표시되는지 확인

# 로그인 버튼이 화면에 표시되는지 확인
def test_login_button_exists(driver):
    driver.get('https://www.naver.com')
    login_button = driver.find_element(By.CLASS_NAME, 'link_login')  # 로그인 버튼 클래스명
    assert login_button.is_displayed()  # 로그인 버튼이 화면에 표시되는지 확인

# 간단한 검색 테스트
def test_search_function(driver):
    driver.get('https://www.naver.com')
    search_box = driver.find_element(By.ID, 'query')
    search_box.send_keys('Python')  # 'Python'을 검색창에 입력
    search_box.submit()  # 검색 실행
    assert 'Python' in driver.title  # 검색 후 페이지 타이틀에 'Python'이 포함되어 있는지 확인

# 메일 메뉴 클릭 후 페이지 이동 확인
def test_mail_menu(driver):
    driver.get('https://www.naver.com')
    mail_menu = driver.find_element(By.LINK_TEXT, '메일')  # '메일' 메뉴 텍스트로 찾기
    mail_menu.click()
    time.sleep(2)  # 페이지 로딩 시간 기다리기
    assert '네이버 메일' in driver.title  # 메일 페이지로 이동했는지 확인

# 카페 메뉴 클릭 후 페이지 이동 확인
def test_cafe_menu(driver):
    driver.get('https://www.naver.com')
    cafe_menu = driver.find_element(By.LINK_TEXT, '카페')  # '카페' 메뉴 텍스트로 찾기
    cafe_menu.click()
    time.sleep(2)
    assert '네이버 카페' in driver.title  # 카페 페이지로 이동했는지 확인

# 블로그 메뉴 클릭 후 페이지 이동 확인
def test_blog_menu(driver):
    driver.get('https://www.naver.com')
    blog_menu = driver.find_element(By.LINK_TEXT, '블로그')  # '블로그' 메뉴 텍스트로 찾기
    blog_menu.click()
    time.sleep(2)
    assert '네이버 블로그' in driver.title  # 블로그 페이지로 이동했는지 확인

# 스토어 메뉴 클릭 후 페이지 이동 확인
def test_store_menu(driver):
    driver.get('https://www.naver.com')
    store_menu = driver.find_element(By.LINK_TEXT, '스토어')  # '스토어' 메뉴 텍스트로 찾기
    store_menu.click()
    time.sleep(2)
    assert '네이버 스토어' in driver.title  # 스토어 페이지로 이동했는지 확인

# 뉴스 메뉴 클릭 후 페이지 이동 확인
def test_news_menu(driver):
    driver.get('https://www.naver.com')
    news_menu = driver.find_element(By.LINK_TEXT, '뉴스')  # '뉴스' 메뉴 텍스트로 찾기
    news_menu.click()
    time.sleep(2)
    assert '네이버 뉴스' in driver.title  # 뉴스 페이지로 이동했는지 확인

# 증권 메뉴 클릭 후 페이지 이동 확인
def test_stock_menu(driver):
    driver.get('https://www.naver.com')
    stock_menu = driver.find_element(By.LINK_TEXT, '증권')  # '증권' 메뉴 텍스트로 찾기
    stock_menu.click()
    time.sleep(2)
    assert '네이버 증권' in driver.title  # 증권 페이지로 이동했는지 확인

# 부동산 메뉴 클릭 후 페이지 이동 확인
def test_real_estate_menu(driver):
    driver.get('https://www.naver.com')
    real_estate_menu = driver.find_element(By.LINK_TEXT, '부동산')  # '부동산' 메뉴 텍스트로 찾기
    real_estate_menu.click()
    time.sleep(2)
    assert '네이버 부동산' in driver.title  # 부동산 페이지로 이동했는지 확인

# 지도 메뉴 클릭 후 페이지 이동 확인
def test_map_menu(driver):
    driver.get('https://www.naver.com')
    map_menu = driver.find_element(By.LINK_TEXT, '지도')  # '지도' 메뉴 텍스트로 찾기
    map_menu.click()
    time.sleep(2)
    assert '네이버 지도' in driver.title  # 지도 페이지로 이동했는지 확인

# 웹툰 메뉴 클릭 후 페이지 이동 확인
def test_webtoon_menu(driver):
    driver.get('https://www.naver.com')
    webtoon_menu = driver.find_element(By.LINK_TEXT, '웹툰')  # '웹툰' 메뉴 텍스트로 찾기
    webtoon_menu.click()
    time.sleep(2)
    assert '네이버 웹툰' in driver.title  # 웹툰 페이지로 이동했는지 확인

if __name__ == '__main__':
    pytest.main()
