# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from voiceos.models.transcriber import Transcriber

class TestTranscriber(unittest.TestCase):
    """Transcriber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Transcriber:
        """Test Transcriber
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Transcriber`
        """
        model = Transcriber()
        if include_optional:
            return Transcriber(
                provider = azure,
                model = 'nova-2',
                language = 'en',
                keywords = None,
                languages = None
            )
        else:
            return Transcriber(
        )
        """

    def testTranscriber(self):
        """Test Transcriber"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
