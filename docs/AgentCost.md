# AgentCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**AgentProvider**](AgentProvider.md) | The provider of the agent (i.e VoiceOS). | 
**cost** | **float** | The cost for the agent usage (USD). | 
**seconds** | **float** | The number of seconds used for the agent orchestration. | 

## Example

```python
from voiceos.models.agent_cost import AgentCost

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCost from a JSON string
agent_cost_instance = AgentCost.from_json(json)
# print the JSON string representation of the object
print(AgentCost.to_json())

# convert the object into a dict
agent_cost_dict = agent_cost_instance.to_dict()
# create an instance of AgentCost from a dict
agent_cost_form_dict = agent_cost.from_dict(agent_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


