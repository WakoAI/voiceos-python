# RimeVoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The voice provider. | [optional] [default to 'rime']
**speaker** | [**Speaker**](Speaker.md) |  | [optional] 
**speed_alpha** | **float** | Adjusts the speed of speech. Lower than 1.0 is faster than default. Higher than 1.0 is slower than default. | [optional] [default to 1.0]
**reduce_latency** | **bool** | Reduces the latency of response, at the cost of some possible mispronunciation of digits and abbreviations. | [optional] [default to False]

## Example

```python
from voiceos.models.rime_voice import RimeVoice

# TODO update the JSON string below
json = "{}"
# create an instance of RimeVoice from a JSON string
rime_voice_instance = RimeVoice.from_json(json)
# print the JSON string representation of the object
print(RimeVoice.to_json())

# convert the object into a dict
rime_voice_dict = rime_voice_instance.to_dict()
# create an instance of RimeVoice from a dict
rime_voice_form_dict = rime_voice.from_dict(rime_voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


