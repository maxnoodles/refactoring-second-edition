# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2020-04-11


class TrackingInformation:

    def __init__(self, shipping_company, tracking_number):
        self._shipping_company = shipping_company
        self._tracking_number = tracking_number

    @property
    def shipping_company(self):
        return self._shipping_company

    @shipping_company.setter
    def shipping_company(self, arg):
        self._shipping_company = arg