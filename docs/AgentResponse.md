# AgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_message** | **str** | The initial message that the agent will say. If null, the agent will wait for the user to speak first. | [optional] 
**prompt** | **str** | The prompt of the agent. | [optional] 
**voice** | [**Voice**](Voice.md) |  | [optional] 
**language_model** | [**OpenAI**](OpenAI.md) |  | [optional] 
**transcriber** | [**Transcriber**](Transcriber.md) |  | [optional] 
**max_duration_seconds** | **int** | The maximum conversation duration in seconds. If null, the conversation can be of any duration. The default value is 10 min. | [optional] [default to 600]
**webhooks** | [**List[Webhook]**](Webhook.md) | The webhooks of the agent. These are used for real-time conversation events such as function_calls, messages and much more. | [optional] 
**metadata** | **Dict[str, str]** | The metadata of the agent. This is used to store additional information about the agent. | [optional] 
**uri** | **str** | The uri of the agent. | 
**account_id** | **str** | The id of the owner of the agent. | 
**created_at** | **datetime** | The date and time the agent was created. | 
**updated_at** | **datetime** | The date and time the agent was last updated. | 
**id** | **str** | The id of the agent. | 

## Example

```python
from voiceos.models.agent_response import AgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentResponse from a JSON string
agent_response_instance = AgentResponse.from_json(json)
# print the JSON string representation of the object
print(AgentResponse.to_json())

# convert the object into a dict
agent_response_dict = agent_response_instance.to_dict()
# create an instance of AgentResponse from a dict
agent_response_form_dict = agent_response.from_dict(agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


