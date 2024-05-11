# BuyPhoneNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**WakoApiModelsPhoneNumberProvider**](WakoApiModelsPhoneNumberProvider.md) | The telephony provider. | [optional] 
**phone_number** | **str** | The phone number to buy. If null, a random phone number will be purchased. | [optional] 

## Example

```python
from voiceos.models.buy_phone_number import BuyPhoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of BuyPhoneNumber from a JSON string
buy_phone_number_instance = BuyPhoneNumber.from_json(json)
# print the JSON string representation of the object
print(BuyPhoneNumber.to_json())

# convert the object into a dict
buy_phone_number_dict = buy_phone_number_instance.to_dict()
# create an instance of BuyPhoneNumber from a dict
buy_phone_number_form_dict = buy_phone_number.from_dict(buy_phone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


