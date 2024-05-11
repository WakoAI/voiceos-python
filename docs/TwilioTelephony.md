# TwilioTelephony


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**WakoApiModelsPhoneNumberProvider**](WakoApiModelsPhoneNumberProvider.md) | The telephony provider. | 
**phone_number_sid** | **str** | The twilio phone number SID. | 
**account_sid** | **str** | The account sid of the telephony provider (i.e Twilio Account SID). Returns null if the phone number was purchased with VoiceOS. | [optional] 
**auth_token** | **str** | The auth token of the telephony provider (i.e Twilio Auth Token). Returns null if the phone number was purchased with VoiceOS. | [optional] 

## Example

```python
from voiceos.models.twilio_telephony import TwilioTelephony

# TODO update the JSON string below
json = "{}"
# create an instance of TwilioTelephony from a JSON string
twilio_telephony_instance = TwilioTelephony.from_json(json)
# print the JSON string representation of the object
print(TwilioTelephony.to_json())

# convert the object into a dict
twilio_telephony_dict = twilio_telephony_instance.to_dict()
# create an instance of TwilioTelephony from a dict
twilio_telephony_form_dict = twilio_telephony.from_dict(twilio_telephony_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


