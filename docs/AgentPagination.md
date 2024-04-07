# AgentPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AgentResponse]**](AgentResponse.md) | The list of agents returned. | 
**index** | **int** | The current index of the page selected. | 
**has_next** | **bool** | Whether there is a next page. | 

## Example

```python
from voiceos.models.agent_pagination import AgentPagination

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPagination from a JSON string
agent_pagination_instance = AgentPagination.from_json(json)
# print the JSON string representation of the object
print(AgentPagination.to_json())

# convert the object into a dict
agent_pagination_dict = agent_pagination_instance.to_dict()
# create an instance of AgentPagination from a dict
agent_pagination_form_dict = agent_pagination.from_dict(agent_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


