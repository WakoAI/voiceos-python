# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from voiceos.models.buy_phone_number import BuyPhoneNumber

class TestBuyPhoneNumber(unittest.TestCase):
    """BuyPhoneNumber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BuyPhoneNumber:
        """Test BuyPhoneNumber
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuyPhoneNumber`
        """
        model = BuyPhoneNumber()
        if include_optional:
            return BuyPhoneNumber(
                provider = 'twilio',
                phone_number = ''
            )
        else:
            return BuyPhoneNumber(
                phone_number = '',
        )
        """

    def testBuyPhoneNumber(self):
        """Test BuyPhoneNumber"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
