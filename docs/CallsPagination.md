# CallsPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CallResponse]**](CallResponse.md) | The list of conversations returned. | 
**index** | **int** | The current index of the page selected. | 
**has_next** | **bool** | The total number of conversations. | 

## Example

```python
from voiceos.models.calls_pagination import CallsPagination

# TODO update the JSON string below
json = "{}"
# create an instance of CallsPagination from a JSON string
calls_pagination_instance = CallsPagination.from_json(json)
# print the JSON string representation of the object
print(CallsPagination.to_json())

# convert the object into a dict
calls_pagination_dict = calls_pagination_instance.to_dict()
# create an instance of CallsPagination from a dict
calls_pagination_form_dict = calls_pagination.from_dict(calls_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


