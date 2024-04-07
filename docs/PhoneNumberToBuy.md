# PhoneNumberToBuy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The telephony provider. | [optional] [default to 'twilio']
**phone_number** | **str** | The phone number. | 
**postal_code** | **str** | The postal code of the phone number. | [optional] 
**iso_country** | **str** | The iso country code of the phone number. | [optional] 

## Example

```python
from voiceos.models.phone_number_to_buy import PhoneNumberToBuy

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumberToBuy from a JSON string
phone_number_to_buy_instance = PhoneNumberToBuy.from_json(json)
# print the JSON string representation of the object
print(PhoneNumberToBuy.to_json())

# convert the object into a dict
phone_number_to_buy_dict = phone_number_to_buy_instance.to_dict()
# create an instance of PhoneNumberToBuy from a dict
phone_number_to_buy_form_dict = phone_number_to_buy.from_dict(phone_number_to_buy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


