import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


def get_list_of_references_acmdl(doi):
    driver.get("https://doi.org/" + doi)
    driver.find_element_by_id("tab-1015-btnEl").click()    
    refs_table_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="cf_layoutareareferences"]/div/table/tbody'))).text
    refs_list = refs_table_text.split('\n')[1::2]
    return refs_list


def get_references_pdf(refs_list):
    valid_pdfs_url = []
    counter = 1
    total = len(refs_list)
    for ref in refs_list:
        driver.get("https://scholar.google.com.br/scholar?q="+ref)
        try:
            pdf_url = driver.find_element_by_class_name("gs_ggs").find_element_by_tag_name('a').get_attribute('href')
        except:
            print("{} of {}: Could not find the pdf for: {} \t Skipping...".format(counter, total, ref))
            counter += 1
            continue
        if not pdf_url.endswith("pdf"):
            pdf_url += ".pdf"
        valid_pdfs_url.append(pdf_url)
        print("{} of {}: {}".format(counter, total, pdf_url))
        counter += 1
    return valid_pdfs_url


def download_all_pdfs(pdfs_url):
    counter = 1
    total = len(pdfs_url)
    for url in pdfs_url:
        try:
            urllib.request.urlretrieve(url, url[url.rindex('/')+1:])
            print("{} of {}: Downloading {} ...".format(counter, total, url))
            counter += 1
        except urllib.error.HTTPError:
            print("{} of {}: Could not download {}".format(counter, total, url))
            counter += 1

