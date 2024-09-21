import os
import random
import string


class App_Data:
    auth_url = 'https://teststoreforsouthafri.nextbasket.shop/'


    Value = {
        'Homepage-heading': "//h2[contains(text(), 'New')]",
        'accept_cookies': "//button[contains(text(), 'Accept All')]",
        'select_product': "//*[@id='root']/div[2]/main/div/div/div/div[1]/div[1]/div[1]/div/p[contains(text(), 'NEW')]",
        'click_product': "//*[@id='root']/div[2]/main/div/div/div/div[1]/div[1]/a",
        'add_cart': "//button[contains(text(), 'Add to basket')]",
        'pop_up': "//*[@id='__next']/div[1]/div/div/div/div/button",
        'basket': "//button[contains(@class, '_2FTCz zlyBa nExvj ll85s R9U-8')]",
        'check_out': "//button[contains(text(), 'Proceed to Checkout')]",
        'off_label': "//*[@id='root']/div/main/div/div/div/div[3]/div[1]/div[1]/div[2]"

    }