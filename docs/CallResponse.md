# CallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The uri of the conversation. | 
**type** | [**CallType**](CallType.md) | The type of the call. | 
**status** | [**CallStatus**](CallStatus.md) | The status of the conversation (live or ended). | 
**to_number** | **str** | The phone number that the call is going to. | [optional] 
**from_number** | **str** | The phone number that call is coming from. | [optional] 
**start_time** | **datetime** | The start time of the conversation. | 
**end_time** | **datetime** | The end time of the conversation. | [optional] 
**agent** | [**AgentResponse**](AgentResponse.md) | The agent used for the call. | 
**agent_id** | **str** | The id of the agent used in the call. Returns null if the call did not use an existing agent. | [optional] 
**messages** | [**List[Message]**](Message.md) | The messages of the conversation. | [optional] [default to []]
**account_id** | **str** | The account id associated with of the conversation. | 
**ended_reason** | [**EndedReasons**](EndedReasons.md) | The reasons the conversation ended. | [optional] 
**cost** | [**CallCost**](CallCost.md) | The cost of the conversation. | [optional] 
**id** | **str** | The id of the conversation. | 

## Example

```python
from voiceos.models.call_response import CallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CallResponse from a JSON string
call_response_instance = CallResponse.from_json(json)
# print the JSON string representation of the object
print(CallResponse.to_json())

# convert the object into a dict
call_response_dict = call_response_instance.to_dict()
# create an instance of CallResponse from a dict
call_response_form_dict = call_response.from_dict(call_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


