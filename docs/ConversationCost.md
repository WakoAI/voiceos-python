# ConversationCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | The total cost of the conversation (USD). | 
**voice** | [**VoiceCost**](VoiceCost.md) | The voice cost. | 
**transcriber** | [**TranscriberCost**](TranscriberCost.md) | The transcriber cost. | 
**language_model** | [**LanguageModelCost**](LanguageModelCost.md) | The language model cost. | 
**telephony** | [**TelephonyCost**](TelephonyCost.md) | The telephony cost. Returns null if the conversation was over web. | [optional] 
**agent** | [**AgentCost**](AgentCost.md) | The cost of the agent. | 

## Example

```python
from voiceos.models.conversation_cost import ConversationCost

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationCost from a JSON string
conversation_cost_instance = ConversationCost.from_json(json)
# print the JSON string representation of the object
print(ConversationCost.to_json())

# convert the object into a dict
conversation_cost_dict = conversation_cost_instance.to_dict()
# create an instance of ConversationCost from a dict
conversation_cost_form_dict = conversation_cost.from_dict(conversation_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


