# Agent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | The name of the agent | 
**initial_message** | **object** | The initial message of the agent | 
**prompt** | **object** | The prompt of the agent | 
**language** | [**AgentLanguage**](AgentLanguage.md) | DO NOT USE! Deprecated! | [optional] 
**language_model** | [**OpenAI**](OpenAI.md) |  | [optional] 
**voice** | [**Voice**](Voice.md) |  | [optional] 
**transcriber** | [**Transcriber**](Transcriber.md) |  | [optional] 
**max_call_duration** | **object** | The maximum call duration in seconds. If null, the call can be of any duration. The default value is 10 min. | [optional] 
**webhooks** | **object** | The webhooks of the agent | [optional] 
**id** | **object** | The id of the agent | 
**uri** | **object** | The uri of the agent | 
**account_id** | **object** | The id of the owner of the agent | 
**created_at** | **object** | The date and time the agent was created | 
**updated_at** | **object** | The date and time the agent was last updated | 

## Example

```python
from voiceos.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print(Agent.to_json())

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_form_dict = agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


