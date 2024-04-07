# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from voiceos.models.calls_pagination import CallsPagination

class TestCallsPagination(unittest.TestCase):
    """CallsPagination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CallsPagination:
        """Test CallsPagination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CallsPagination`
        """
        model = CallsPagination()
        if include_optional:
            return CallsPagination(
                items = [
                    voiceos.models.call_response.CallResponse(
                        uri = '', 
                        type = null, 
                        status = null, 
                        to_number = '', 
                        from_number = '', 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        agent = null, 
                        agent_id = '', 
                        messages = [
                            voiceos.models.message.Message(
                                role = null, 
                                content = '', )
                            ], 
                        account_id = '', 
                        ended_reason = null, 
                        cost = null, 
                        id = '', )
                    ],
                index = 56,
                has_next = True
            )
        else:
            return CallsPagination(
                items = [
                    voiceos.models.call_response.CallResponse(
                        uri = '', 
                        type = null, 
                        status = null, 
                        to_number = '', 
                        from_number = '', 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        agent = null, 
                        agent_id = '', 
                        messages = [
                            voiceos.models.message.Message(
                                role = null, 
                                content = '', )
                            ], 
                        account_id = '', 
                        ended_reason = null, 
                        cost = null, 
                        id = '', )
                    ],
                index = 56,
                has_next = True,
        )
        """

    def testCallsPagination(self):
        """Test CallsPagination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
