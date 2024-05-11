# PhoneNumberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The uri of the phone number. | 
**inbound_agent_id** | **str** | The agent id that will be used for inbound calls. If null, the phone number will not receive any calls. | [optional] 
**phone_number** | **str** | The phone number including the country code. | 
**account_id** | **str** | The account id associated with the phone number. | 
**created_at** | **datetime** | The date the phone number was created. | 
**updated_at** | **datetime** | The date the phone number was last updated. | 
**telephony** | [**TwilioTelephony**](TwilioTelephony.md) | The telephony provider for the phone number. | 
**webhooks** | [**List[PhoneNumberWebhook]**](PhoneNumberWebhook.md) | The webhooks of the phone number. This is used to fetch the agent at the start of the conversation. | [optional] 
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


