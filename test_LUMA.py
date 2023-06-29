import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://magento.softwaretestingboard.com/'

@pytest.mark.usefixtures('setup')
class test_LUMA:

    @allure.feature('Тест LUMA')
    @allure.story('Тест Whats New')
    @allure.description('')
    def test_1(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Whats New'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-3"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Hoodies & Sweatshirts'):
            element = self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div/div/ul[1]/li[1]/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Whats New')
    @allure.description('')
    def test_2(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Whats New'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-3"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Jackets'):
            element = self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div/div/ul[2]/li[2]/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Women')
    @allure.description('')
    def test_3(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Women'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-4"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Tops'):
            element = self.browser.find_element(By.XPATH, '//*[@id="narrow-by-list2"]/dd/ol/li[1]/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Women')
    @allure.description('')
    def test_4(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Women'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-4"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bottoms'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/div[2]/div[1]/div[2]/dl/dd/ol/li[2]/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Men')
    @allure.description('')
    def test_5(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Men'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-5"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Tops'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/div[2]/div[1]/div[2]/dl/dd/ol/li[1]/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Men')
    @allure.description('')
    def test_6(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Men'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-5"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bottoms'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/div[2]/div[1]/div[2]/dl/dd/ol/li[2]/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Gear')
    @allure.description('')
    def test_7(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Gear'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-6"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bags'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/div[2]/div[1]/div[2]/dl/dd/ol/li[1]/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Gear')
    @allure.description('')
    def test_8(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Gear'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-6"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Fitness Equipment'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/div[2]/div[1]/div[2]/dl/dd/ol/li[2]/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Gear')
    @allure.description('')
    def test_9(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Gear'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-6"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Watches'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/div[2]/div[1]/div[2]/dl/dd/ol/li[3]/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Training')
    @allure.description('')
    def test_10(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Training'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-7"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Video Download'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/div[2]/div/div[2]/dl/dd/ol/li/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Sale')
    @allure.description('')
    def test_11(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Sale'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-8"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Fitness Equipment'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/div[2]/div/div/ul[3]/li[2]/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Shop New Yoga')
    @allure.description('')
    def test_12(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Shop New Yoga'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[2]/div[1]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть List'):
            element = self.browser.find_element(By.XPATH, '//*[@id="mode-list"]').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Search Terms')
    @allure.description('')
    def test_13(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Search Terms'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/footer/div/ul/li[1]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Zoltan Gym Tee'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/ul/li[100]/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Privacy and Cookie Policy')
    @allure.description('')
    def test_14(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Privacy and Cookie Policy'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/footer/div/ul/li[2]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Contact Us'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[2]/div[1]/p[33]/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Argus All-Weather Tank')
    @allure.description('')
    def test_15(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Argus All-Weather Tank'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[2]/div[3]/div/div/ol/li[3]/div/div/strong/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Pierce Gym Short'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[5]/div[2]/div/ol/li[2]/div/div/strong/a').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Fusion Backpack')
    @allure.description('')
    def test_16(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Fusion Backpack'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[2]/div[3]/div/div/ol/li[5]/div/div/strong/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть 3 Reviews'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[1]/div[2]/div[2]/a[1]').is_enabled()
            assert element == True

    @allure.feature('Тест LUMA')
    @allure.story('Тест Radiant Tee')
    @allure.description('')
    def test_17(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Radiant Tee'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[2]/div[3]/div/div/ol/li[1]/div/div/strong/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть 3 Reviews'):
            element = self.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[1]/div[2]/div[2]/a[1]').is_enabled()
            assert element == True