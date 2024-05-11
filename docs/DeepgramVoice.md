# DeepgramVoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The synthesizer provider. | [optional] [default to 'deepgram']
**model** | [**Model2**](Model2.md) |  | [optional] 

## Example

```python
from voiceos.models.deepgram_voice import DeepgramVoice

# TODO update the JSON string below
json = "{}"
# create an instance of DeepgramVoice from a JSON string
deepgram_voice_instance = DeepgramVoice.from_json(json)
# print the JSON string representation of the object
print(DeepgramVoice.to_json())

# convert the object into a dict
deepgram_voice_dict = deepgram_voice_instance.to_dict()
# create an instance of DeepgramVoice from a dict
deepgram_voice_form_dict = deepgram_voice.from_dict(deepgram_voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


