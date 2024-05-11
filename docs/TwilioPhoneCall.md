# TwilioPhoneCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The telephony provider of the phone call. | 
**to_number** | **str** | The phone number called. | 
**from_number** | **str** | The phone number from which the call was made. | 

## Example

```python
from voiceos.models.twilio_phone_call import TwilioPhoneCall

# TODO update the JSON string below
json = "{}"
# create an instance of TwilioPhoneCall from a JSON string
twilio_phone_call_instance = TwilioPhoneCall.from_json(json)
# print the JSON string representation of the object
print(TwilioPhoneCall.to_json())

# convert the object into a dict
twilio_phone_call_dict = twilio_phone_call_instance.to_dict()
# create an instance of TwilioPhoneCall from a dict
twilio_phone_call_form_dict = twilio_phone_call.from_dict(twilio_phone_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


