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
        
    @property
    def tracking_number(self):
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, arg):
        self._tracking_number = arg

    @property
    def display(self):
        return f'{self.shipping_company, self.tracking_number}'


class Shipment:
    def __init__(self, shipping_company, tracking_number):
        # self._tracking_information = tracking_info
        self._shipping_company = shipping_company
        self._tracking_number = tracking_number

    @property
    def tracking_info(self):
        # return self._tracking_information.display
        return self.display

    # @property
    # def tracking_information(self):
    #     return self._tracking_information

    # @tracking_information.setter
    # def tracking_information(self, a_tracking_information):
    #     self._tracking_information = a_tracking_information

    @property
    def shipping_company(self):
        return self.shipping_company

    @shipping_company.setter
    def shipping_company(self, arg):
        self.shipping_company = arg

    @property
    def display(self):
        return f'{self.shipping_company, self.tracking_number}'

    @property
    def tracking_number(self):
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, arg):
        self._tracking_number = arg