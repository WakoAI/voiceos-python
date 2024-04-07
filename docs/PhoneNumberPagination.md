# PhoneNumberPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PhoneNumberResponse]**](PhoneNumberResponse.md) | The list of phone numbers returned. | 
**index** | **int** | The current index of the page. | 
**has_next** | **bool** | Whether there is a next page. | 

## Example

```python
from voiceos.models.phone_number_pagination import PhoneNumberPagination

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumberPagination from a JSON string
phone_number_pagination_instance = PhoneNumberPagination.from_json(json)
# print the JSON string representation of the object
print(PhoneNumberPagination.to_json())

# convert the object into a dict
phone_number_pagination_dict = phone_number_pagination_instance.to_dict()
# create an instance of PhoneNumberPagination from a dict
phone_number_pagination_form_dict = phone_number_pagination.from_dict(phone_number_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


