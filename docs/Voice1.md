# Voice1

The synthesizer of the agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **object** | The synthesizer provider. | [optional] 
**model** | [**AzureModel**](AzureModel.md) | The azure model to use | [optional] 
**optimize_latency** | **object** | Optimize for latency | [optional] 
**pitch** | **object** | The pitch of the voice | [optional] 
**rate** | **object** | The rate of the voice | [optional] 
**speaker** | **object** | The speaker of the voice. | [optional] 
**reduce_lantency** | **object** | Reduces the latency of response, at the cost of some possible mispronunciation of digits and abbreviations. | [optional] 
**speed_alpha** | **object** | Adjusts the speed of speech. Lower is faster. Higher is slower. | [optional] 

## Example

```python
from voiceos.models.voice1 import Voice1

# TODO update the JSON string below
json = "{}"
# create an instance of Voice1 from a JSON string
voice1_instance = Voice1.from_json(json)
# print the JSON string representation of the object
print(Voice1.to_json())

# convert the object into a dict
voice1_dict = voice1_instance.to_dict()
# create an instance of Voice1 from a dict
voice1_form_dict = voice1.from_dict(voice1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


