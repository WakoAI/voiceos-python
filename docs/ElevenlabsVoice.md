# ElevenlabsVoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The voice provider. | [optional] [default to 'elevenlabs']
**voice_id** | [**VoiceId**](VoiceId.md) |  | [optional] 
**model_id** | [**ElevenLabsModel**](ElevenLabsModel.md) | The model to use. Defaults to eleven_turbo_v2. | [optional] 
**optimize_latency** | **int** | Optimize for latency. | [optional] [default to 3]
**use_speaker_boost** | **bool** | Use speaker boost. | [optional] [default to False]
**similarity_boost** | **int** | Boost the similarity of the generated audio to the input text. | [optional] [default to 0.5]
**stability** | **int** | Control the stability of the generated audio. | [optional] [default to 0.5]

## Example

```python
from voiceos.models.elevenlabs_voice import ElevenlabsVoice

# TODO update the JSON string below
json = "{}"
# create an instance of ElevenlabsVoice from a JSON string
elevenlabs_voice_instance = ElevenlabsVoice.from_json(json)
# print the JSON string representation of the object
print(ElevenlabsVoice.to_json())

# convert the object into a dict
elevenlabs_voice_dict = elevenlabs_voice_instance.to_dict()
# create an instance of ElevenlabsVoice from a dict
elevenlabs_voice_form_dict = elevenlabs_voice.from_dict(elevenlabs_voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


