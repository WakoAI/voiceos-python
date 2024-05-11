# ConversationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The uri of the conversation. | 
**type** | [**ConversationType**](ConversationType.md) | The type of conversation. | 
**account_id** | **str** | The account id associated with of the conversation. | 
**status** | [**ConversationStatus**](ConversationStatus.md) | The status of the conversation. | 
**started_at** | **datetime** | The start time of the conversation. | [optional] 
**ended_at** | **datetime** | The end time of the conversation. Returns null if the conversation is has not ended. | [optional] 
**agent_config** | [**AgentConfiguration**](AgentConfiguration.md) | The agent configuration used for the conversation. | 
**agent_id** | **str** | The id of the agent used in the conversation. Returns null if the conversation did not use an existing agent. | [optional] 
**messages** | [**List[Message]**](Message.md) | The messages of the conversation. | [optional] [default to []]
**phone_call** | [**TwilioPhoneCall**](TwilioPhoneCall.md) | The phone call details of the conversation. Returns null if the conversation was over web. | [optional] 
**ended_reason** | [**EndedReasons**](EndedReasons.md) | The reasons the conversation ended. | [optional] 
**cost_breakdown** | [**ConversationCost**](ConversationCost.md) | The cost breakdown of the conversation. | [optional] 
**id** | **str** | The id of the conversation. | 

## Example

```python
from voiceos.models.conversation_response import ConversationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationResponse from a JSON string
conversation_response_instance = ConversationResponse.from_json(json)
# print the JSON string representation of the object
print(ConversationResponse.to_json())

# convert the object into a dict
conversation_response_dict = conversation_response_instance.to_dict()
# create an instance of ConversationResponse from a dict
conversation_response_form_dict = conversation_response.from_dict(conversation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


