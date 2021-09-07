#!python3
# -*- coding: utf-8 -*-
# automation_olx/
# salim suprayogi
# 07 september 2021
# Program Automation OLX
"""
Goal Automation:
1. Login akun OLX
2. Input lokasi
3. Pilih kategori Properti
4. Mengambil data nama pengiklan dan nomor telepon jika ada, jika tidak ada datanya lanjut ke produk selanjutnya

Requirement:
1. Install selenium webdriver
2. install python
3. chromedriver.exe
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

#   url | olx
url = "https://www.olx.co.id/"

driver = webdriver.Chrome(executable_path=r"/chromedriver.exe")
driver.implicitly_wait(10)
driver.get(url)
title_page = "{}".format(driver.title)
print(title_page)
name_browser = "Open Browser Chrome"
print(name_browser)
print("*"*50)

wait = WebDriverWait(driver, 10)

#   login
#   <button type="button" data-aut-id="btnLogin" class="rui-3sH3b rui-17DJY rui-1zK8h RgSo4 _1oFFI"><span>Login/Daftar</span></button>
elem_login = "//button[@data-aut-id=\"btnLogin\"]"
wait_login = wait.until(
    EC.presence_of_element_located((By.XPATH, elem_login)))
wait_login.click()

# Input Email
#   <button type="button" data-aut-id="emailLogin" class="rui-3sH3b rui-3K5JC rui-1zK8h _2_t7- rui-3uQ0M"><span>Login/Daftar dengan Email</span></button>
elem_email = "//button[@data-aut-id=\"emailLogin\"]"
wait_email = wait.until(
    EC.presence_of_element_located((By.XPATH, elem_email)))
wait_email.click()

#   <input id="email_input_field" name="email" type="text" autocomplete="username" placeholder="Email" class="rui-1ekfu rui-3oSYn" value="">
elem_email_field = "email_input_field"
wait_email_field = wait.until(
    EC.presence_of_element_located((By.ID, elem_email_field)))
wait_email_field.send_keys("namaemail@gmail.com") #masukan email disini

#   <button type="submit" data-aut-id="" class="rui-3sH3b rui-2yJ_A rui-1zK8h _2_t7-"><span>Lanjut</span></button>
# elem_lanjut = "Lanjut"
# class="BEs0P"
form_lanjut = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "BEs0P")))

wait_form_lanjut = form_lanjut.find_element_by_tag_name("button")
wait_form_lanjut.click()

# Input password
#   <input id="password" name="password" type="password" autocomplete="current-password" placeholder="kata sandi" class="rui-1ekfu rui-3oSYn" value="">
elem_pass_field = "password"
wait_pass_field = wait.until(
    EC.presence_of_element_located((By.ID, elem_pass_field)))
wait_pass_field.send_keys("input pasword") # masukan password disini

form_login = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "BEs0P")))

wait_form_login = form_login.find_element_by_tag_name("button")
wait_form_login.click()


time.sleep(30)
# Jika muncul pop up sementara masih manual close pop up allow nya


# pilih kota
#   <input class="_2xvhw" placeholder="Cari kota, area, atau lokalitas" value="Indonesia">
# cari_kota = driver.find_element_by_class_name("_2xvhw")
cari_kota = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "_2xvhw")))
cari_kota.click()
cari_kota.clear()
time.sleep(3)
cari_kota.send_keys("Jawa Barat")
time.sleep(5)

#   class="_2HzJo"
# lokasi_item = driver.find_element_by_class_name("_2HzJo")
lokasi_item = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "_2HzJo")))
#   class="_1jtbH"
items = lokasi_item.find_elements_by_class_name("_1jtbH")[0]
items.click()

# #   wait load elemen all kategori
# wait.until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME, "_2xg5B"))):
while True:
    try:
        wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "_3OKe_")))
        break
    except:
        print("waiting element")
        time.sleep(3)

# mencari header kategori
all_category = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "_2xg5B")))
if all_category:
    #   sub elemen all category
    #   class="_3AGJR _18NX_"
    sub_category = all_category.find_elements_by_class_name("_18NX_")[2]
    if sub_category:
        #   len(sub_category)) = 6 [ 0-5 ] // cari indek ke 2 [ properti ]
        klik = sub_category.find_element_by_class_name("_2fitb")
        if klik:
            klik.click()

# menunggu kategori properti muncul
while True:
    try:
        wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "_3etsg")))
        break
    except:
        print("waiting element")
        time.sleep(3)

# Cek total list yang ada di dalam kategory properti
#   list item box property
#   <ul class="rl3f9 _3mXOU" data-aut-id="itemsList"><li data-aut-id="itemBox"
# data-aut-id="itemsList"
temp = []
items_list = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "_3mXOU")))
#   <li data-aut-id="itemBox" class="EIR5N">
item_box = items_list.find_elements_by_class_name("EIR5N")
len1 = len(item_box)
temp.append(len1)
leng = len1
print("temp : ", temp)
#   print(len(item_box)) // list item pertama = 20 list
#   testing ambil element

i = 0
while i < temp[-1]:
    # for i in range(temp[-1]):
    no_list = i+1
    print("Data No :", no_list)
    items_list_back = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "_3mXOU")))
    item_box_back = items_list_back.find_elements_by_class_name("EIR5N")
    items = item_box_back[i]
    # print(item.text)
    items.click()
    try:
        nama_penjuals = driver.find_element_by_class_name("_3oOe9")
        nama_penjual = nama_penjuals.text
        try:
            # tampilkan_no = driver.find_element_by_class_name("_2b6xv")
            tampilkan_no = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "_2b6xv")))
            tampilkan_no.click()
            # get_phone = driver.find_element_by_class_name("_1uXYV")
            get_phone = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "_1uXYV")))
            time.sleep(1)
            print(nama_penjual)
            phone_penjual = get_phone.text
            print("tampilkan no telepon : ", phone_penjual)
        except:
            print(nama_penjual)
            print("tidak ada data no telepon")
    except:
        print("data tidak ditemukan")

    driver.back()
    i += 1

    if no_list == temp[-1]:
        muat_lain = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "JbJAl")))
        klik_lain = muat_lain.find_element_by_xpath(
            '//button[@data-aut-id="btnLoadMore"]')
        klik_lain.click()
        print("klik")
        time.sleep(10)
        items_list2 = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "_3mXOU")))
        item_box2 = items_list2.find_elements_by_class_name("EIR5N")
        len2 = len(item_box2)
        leng += len2
        temp.append(len2)
        print("len2 : ", len2)
    time.sleep(1)

print(temp)
print("END")
print("*"*50)
# Program akan berhenti kalau daftar iklan properti sudah habis
