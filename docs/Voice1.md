# Voice1

The synthesizer of the agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **object** | The voice provider. | [optional] 
**model** | [**Model2**](Model2.md) |  | [optional] 
**speed** | **object** | Control how fast the generated audio should be. A number greater than 0 and less than or equal to 5.0 | [optional] 
**temperature** | **object** | A floating point number between 0, inclusive, and 2, inclusive. If equal to null or not provided, the model&#39;s default temperature will be used. | [optional] 
**text_guidance** | **object** | A number between 1 and 2. This number influences how closely the generated speech adheres to the input text. | [optional] 
**style_guidance** | **object** | A number between 1 and 30. Use lower numbers to to reduce how strong your chosen emotion will be. Higher numbers will create a very emotional performance. | [optional] 
**voice_id** | [**VoiceId**](VoiceId.md) |  | [optional] 
**model_id** | [**ElevenLabsModel**](ElevenLabsModel.md) | The model to use. Defaults to eleven_turbo_v2. | [optional] 
**optimize_latency** | **object** | Optimize for latency. | [optional] 
**use_speaker_boost** | **object** | Use speaker boost. | [optional] 
**similarity_boost** | **object** | Boost the similarity of the generated audio to the input text. | [optional] 
**stability** | **object** | Control the stability of the generated audio. | [optional] 
**pitch** | **object** | The pitch of the voice. | [optional] 
**rate** | **object** | The rate of the voice. | [optional] 
**speaker** | [**Speaker**](Speaker.md) |  | [optional] 
**speed_alpha** | **object** | Adjusts the speed of speech. Lower than 1.0 is faster than default. Higher than 1.0 is slower than default. | [optional] 
**reduce_latency** | **object** | Reduces the latency of response, at the cost of some possible mispronunciation of digits and abbreviations. | [optional] 

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


