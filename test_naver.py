import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# 테스트를 위한 fixture
@pytest.fixture(scope="module")
def driver():
    # ChromeDriver 자동 설치 및 실행
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()  # 브라우저 최대화
    yield driver
    driver.quit()  # 테스트 후 종료

# 네이버 홈페이지가 제대로 로딩되는지 확인하는 테스트
def test_naver_homepage_title(driver):
    driver.get("https://www.naver.com")
    assert "NAVER" in driver.title  # 페이지 제목에 'NAVER'가 포함되어 있는지 확인

# 네이버 검색창이 로딩되는지 확인
def test_naver_searchbox(driver):
    driver.get("https://www.naver.com")
    search_box = driver.find_element(By.ID, "query")  # 검색창 요소 찾기
    assert search_box.is_displayed()  # 검색창이 페이지에 표시되는지 확인

# 네이버 로그인 버튼이 제대로 작동하는지 확인
def test_naver_login_button(driver):
    driver.get("https://www.naver.com")
    login_button = driver.find_element(By.CSS_SELECTOR, "a.link_login")
    login_button.click()  # 로그인 버튼 클릭
    time.sleep(2)  # 로그인 페이지가 로딩될 시간을 잠깐 대기
    assert "로그인" in driver.title  # 로그인 페이지로 이동했는지 확인

# 검색 기능이 제대로 동작하는지 확인
def test_naver_search_function(driver):
    driver.get("https://www.naver.com")
    search_box = driver.find_element(By.ID, "query")
    search_box.send_keys("Python")  # 검색창에 'Python' 입력
    search_box.send_keys(Keys.RETURN)  # Enter 키를 눌러 검색 실행
    time.sleep(2)  # 검색 결과가 로딩될 시간을 잠깐 대기
    assert "Python" in driver.title  # 제목에 'Python'이 포함되어 있는지 확인
    assert "결과" in driver.page_source  # 페이지 소스에 '결과'라는 단어가 포함되어 있는지 확인

