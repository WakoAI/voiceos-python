# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from voiceos.models.language_model_cost import LanguageModelCost

class TestLanguageModelCost(unittest.TestCase):
    """LanguageModelCost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LanguageModelCost:
        """Test LanguageModelCost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LanguageModelCost`
        """
        model = LanguageModelCost()
        if include_optional:
            return LanguageModelCost(
                provider = 'openai',
                cost = 1.337,
                input_tokens = 56,
                output_tokens = 56,
                external = True
            )
        else:
            return LanguageModelCost(
                provider = 'openai',
                cost = 1.337,
                input_tokens = 56,
                output_tokens = 56,
                external = True,
        )
        """

    def testLanguageModelCost(self):
        """Test LanguageModelCost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
