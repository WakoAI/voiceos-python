# PlayhtVoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The voice provider. | [optional] [default to 'playht']
**model** | [**Model4**](Model4.md) |  | [optional] 
**speed** | **float** | Control how fast the generated audio should be. A number greater than 0 and less than or equal to 5.0 | [optional] [default to 1.0]
**temperature** | **float** | A floating point number between 0, inclusive, and 2, inclusive. If equal to null or not provided, the model&#39;s default temperature will be used. | [optional] 
**text_guidance** | **float** | A number between 1 and 2. This number influences how closely the generated speech adheres to the input text. | [optional] 
**style_guidance** | **float** | A number between 1 and 30. Use lower numbers to to reduce how strong your chosen emotion will be. Higher numbers will create a very emotional performance. | [optional] 

## Example

```python
from voiceos.models.playht_voice import PlayhtVoice

# TODO update the JSON string below
json = "{}"
# create an instance of PlayhtVoice from a JSON string
playht_voice_instance = PlayhtVoice.from_json(json)
# print the JSON string representation of the object
print(PlayhtVoice.to_json())

# convert the object into a dict
playht_voice_dict = playht_voice_instance.to_dict()
# create an instance of PlayhtVoice from a dict
playht_voice_form_dict = playht_voice.from_dict(playht_voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


