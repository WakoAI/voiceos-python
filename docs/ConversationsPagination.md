# ConversationsPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ConversationResponse]**](ConversationResponse.md) | The list of conversations returned. | 
**index** | **int** | The current index of the page selected. | 
**has_more** | **bool** | The total number of conversations. | 

## Example

```python
from voiceos.models.conversations_pagination import ConversationsPagination

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationsPagination from a JSON string
conversations_pagination_instance = ConversationsPagination.from_json(json)
# print the JSON string representation of the object
print(ConversationsPagination.to_json())

# convert the object into a dict
conversations_pagination_dict = conversations_pagination_instance.to_dict()
# create an instance of ConversationsPagination from a dict
conversations_pagination_form_dict = conversations_pagination.from_dict(conversations_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


