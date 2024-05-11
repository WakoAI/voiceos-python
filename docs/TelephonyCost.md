# TelephonyCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**WakoApiModelsPhoneNumberProvider**](WakoApiModelsPhoneNumberProvider.md) | The provider of the phone number used. | 
**cost** | **float** | The cost for the telephony usage. Returns zero, if the phone number was imported. | 
**seconds** | **float** | The number of seconds used for the telephony. | 

## Example

```python
from voiceos.models.telephony_cost import TelephonyCost

# TODO update the JSON string below
json = "{}"
# create an instance of TelephonyCost from a JSON string
telephony_cost_instance = TelephonyCost.from_json(json)
# print the JSON string representation of the object
print(TelephonyCost.to_json())

# convert the object into a dict
telephony_cost_dict = telephony_cost_instance.to_dict()
# create an instance of TelephonyCost from a dict
telephony_cost_form_dict = telephony_cost.from_dict(telephony_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


