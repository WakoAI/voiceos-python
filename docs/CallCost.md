# CallCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | The total cost of the call. | 
**synthesizer** | [**SynthesizerCost**](SynthesizerCost.md) | The synthetizer cost. | 
**transcriber** | [**TranscriberCost**](TranscriberCost.md) | The transcriber cost. | 
**language_model** | [**LanguageModelCost**](LanguageModelCost.md) | The language model cost. | 
**telephony** | [**TelephonyCost**](TelephonyCost.md) | The telephony cost. Returns null if the call was not a phone call. | [optional] 
**agent** | [**AgentCost**](AgentCost.md) | The cost of the agent. | 
**currency** | [**Currency**](Currency.md) | The currency used. As of now, we only offer USD. | [optional] 

## Example

```python
from voiceos.models.call_cost import CallCost

# TODO update the JSON string below
json = "{}"
# create an instance of CallCost from a JSON string
call_cost_instance = CallCost.from_json(json)
# print the JSON string representation of the object
print(CallCost.to_json())

# convert the object into a dict
call_cost_dict = call_cost_instance.to_dict()
# create an instance of CallCost from a dict
call_cost_form_dict = call_cost.from_dict(call_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


