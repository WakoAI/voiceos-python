# UpdatePhoneNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound_agent_id** | **str** | The agent id that will be used for inbound calls. If null, the phone number is will not receive any calls. | [optional] 
**webhooks** | [**List[PhoneNumberWebhook]**](PhoneNumberWebhook.md) | The webhooks of the phone number. This is used to fetch the agent at the start of the conversation. | [optional] 

## Example

```python
from voiceos.models.update_phone_number import UpdatePhoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePhoneNumber from a JSON string
update_phone_number_instance = UpdatePhoneNumber.from_json(json)
# print the JSON string representation of the object
print(UpdatePhoneNumber.to_json())

# convert the object into a dict
update_phone_number_dict = update_phone_number_instance.to_dict()
# create an instance of UpdatePhoneNumber from a dict
update_phone_number_form_dict = update_phone_number.from_dict(update_phone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


