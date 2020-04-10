# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2020-04-09


def price_order_source(product, quantity, shipping_method):
    base_price = product['base_price'] * quantity
    discount = max(quantity - product['discount_threshold'], 0) * \
               product['base_price'] * product['discount_threshold']
    shipping_per_case = shipping_method['discounted_fee'] if base_price > shipping_method[
        'discount_threshold'] else shipping_method['fee_per_case']
    shipping_cost = quantity * shipping_per_case
    price = base_price - discount + shipping_cost
    return price


def price_order(product, quantity, shipping_method):
    price_date = calculate_pricing_data(product, quantity)
    return apply_shipping(price_date, shipping_method)


def calculate_pricing_data(product, quantity):
    base_price = product['base_price'] * quantity
    discount = max(quantity - product['discount_threshold'], 0) * \
               product['base_price'] * product['discount_threshold']
    return {
        'base_price': base_price,
        'quantity': quantity,
        'discount': discount
    }


def apply_shipping(price_date, shipping_method):
    shipping_per_case = shipping_method['discounted_fee'] if price_date['base_price'] > shipping_method[
        'discount_threshold'] else shipping_method['fee_per_case']
    shipping_cost = price_date['quantity'] * shipping_per_case
    return price_date['base_price'] - price_date['discount'] + shipping_cost
