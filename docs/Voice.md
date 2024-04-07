# Voice


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
from voiceos.models.voice import Voice

# TODO update the JSON string below
json = "{}"
# create an instance of Voice from a JSON string
voice_instance = Voice.from_json(json)
# print the JSON string representation of the object
print(Voice.to_json())

# convert the object into a dict
voice_dict = voice_instance.to_dict()
# create an instance of Voice from a dict
voice_form_dict = voice.from_dict(voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


