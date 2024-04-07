# CreateCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_number** | **str** |  | 
**from_number** | **str** |  | 
**agent** | [**Agent**](Agent.md) |  | 

## Example

```python
from voiceos.models.create_call import CreateCall

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCall from a JSON string
create_call_instance = CreateCall.from_json(json)
# print the JSON string representation of the object
print(CreateCall.to_json())

# convert the object into a dict
create_call_dict = create_call_instance.to_dict()
# create an instance of CreateCall from a dict
create_call_form_dict = create_call.from_dict(create_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


