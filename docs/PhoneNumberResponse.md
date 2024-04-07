# PhoneNumberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The uri of the phone number. | 
**inbound_agent_uri** | **str** | The agent uri that will be used for inbound calls. If null, the phone number is will not receive any calls. | [optional] 
**phone_number** | **str** | The phone number. | 
**account_id** | **str** | The account id associated with the phone number. | 
**created_at** | **datetime** | The date the phone number was created. | 
**updated_at** | **datetime** | The date the phone number was last updated. | 
**telephony** | [**TwilioTelephony**](TwilioTelephony.md) | The telephony of the phone number. | 
**stripe_subscription_id** | **str** | The stripe subscription id of the phone number. Returns null if the phone number was imported. | [optional] 
**id** | **str** | The id of the phone number. | 

## Example

```python
from voiceos.models.phone_number_response import PhoneNumberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumberResponse from a JSON string
phone_number_response_instance = PhoneNumberResponse.from_json(json)
# print the JSON string representation of the object
print(PhoneNumberResponse.to_json())

# convert the object into a dict
phone_number_response_dict = phone_number_response_instance.to_dict()
# create an instance of PhoneNumberResponse from a dict
phone_number_response_form_dict = phone_number_response.from_dict(phone_number_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


