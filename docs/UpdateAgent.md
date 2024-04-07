# UpdateAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the agent | [optional] 
**initial_message** | **str** | The initial message of the agent | [optional] 
**prompt** | **str** | The prompt preamble of the agent | [optional] 
**language** | [**AgentLanguage**](AgentLanguage.md) | The language of the agent | [optional] 
**language_model** | [**OpenAI**](OpenAI.md) | The language model of the agent. | [optional] 
**voice** | [**Voice1**](Voice1.md) |  | [optional] 
**transcriber** | [**Transcriber1**](Transcriber1.md) |  | [optional] 
**max_duration_time** | **int** | The maximum call duration in seconds. If null, the call can be of any duration. The default value is 10 min. | [optional] [default to 600]

## Example

```python
from voiceos.models.update_agent import UpdateAgent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgent from a JSON string
update_agent_instance = UpdateAgent.from_json(json)
# print the JSON string representation of the object
print(UpdateAgent.to_json())

# convert the object into a dict
update_agent_dict = update_agent_instance.to_dict()
# create an instance of UpdateAgent from a dict
update_agent_form_dict = update_agent.from_dict(update_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


