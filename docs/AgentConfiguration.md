# AgentConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the agent | 
**initial_message** | **str** | The initial message of the agent | 
**prompt** | **str** | The prompt of the agent | 
**language** | [**AgentLanguage**](AgentLanguage.md) | DO NOT USE! Deprecated! | [optional] 
**language_model** | [**OpenAI**](OpenAI.md) |  | [optional] 
**voice** | [**Voice**](Voice.md) |  | [optional] 
**transcriber** | [**Transcriber**](Transcriber.md) |  | [optional] 
**max_call_duration** | **int** | The maximum call duration in seconds. If null, the call can be of any duration. The default value is 10 min. | [optional] [default to 600]

## Example

```python
from voiceos.models.agent_configuration import AgentConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AgentConfiguration from a JSON string
agent_configuration_instance = AgentConfiguration.from_json(json)
# print the JSON string representation of the object
print(AgentConfiguration.to_json())

# convert the object into a dict
agent_configuration_dict = agent_configuration_instance.to_dict()
# create an instance of AgentConfiguration from a dict
agent_configuration_form_dict = agent_configuration.from_dict(agent_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


