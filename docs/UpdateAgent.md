# UpdateAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_message** | **str** | The initial message that the agent will say. If null, the agent will wait for the user to speak first. | [optional] 
**prompt** | **str** | The prompt of the agent. | [optional] 
**voice** | [**Voice1**](Voice1.md) |  | [optional] 
**language_model** | [**OpenAI**](OpenAI.md) | The language model of the agent. | [optional] 
**transcriber** | [**Transcriber1**](Transcriber1.md) |  | [optional] 
**max_duration_seconds** | **int** | The maximum conversation duration in seconds. If null, the conversation can be of any duration. The default value is 10 min. | [optional] [default to 600]
**webhooks** | [**List[Webhook]**](Webhook.md) | The webhooks of the agent. These are used for real-time conversation events such as function_calls, messages and much more. | [optional] 
**metadata** | **Dict[str, str]** | The metadata of the agent. This is used to store additional information about the agent. | [optional] 

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


