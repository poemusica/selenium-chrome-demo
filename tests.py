import os
import unittest  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")   

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), 
                                        options=chrome_options)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:5000/')
        self.assertEqual(self.browser.title, 'UberCalc')

    def test_math(self):
        self.browser.get('http://localhost:5000/')

        x = self.browser.find_element_by_id('x-field')
        x.send_keys("3")
        y = self.browser.find_element_by_id('y-field')
        y.send_keys("4")

        btn = self.browser.find_element_by_id('calc-button')
        btn.click()

        result = self.browser.find_element_by_id('result')
        self.assertEqual(result.text, "7")

if __name__ == "__main__":
    unittest.main()