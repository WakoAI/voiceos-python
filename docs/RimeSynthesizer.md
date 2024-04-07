# RimeSynthesizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The synthesizer provider. | [optional] [default to 'rime']
**speaker** | **str** | The speaker of the voice. | [optional] [default to 'abbie']
**reduce_lantency** | **bool** | Reduces the latency of response, at the cost of some possible mispronunciation of digits and abbreviations. | [optional] [default to False]
**speed_alpha** | **float** | Adjusts the speed of speech. Lower is faster. Higher is slower. | [optional] [default to 1]

## Example

```python
from voiceos.models.rime_synthesizer import RimeSynthesizer

# TODO update the JSON string below
json = "{}"
# create an instance of RimeSynthesizer from a JSON string
rime_synthesizer_instance = RimeSynthesizer.from_json(json)
# print the JSON string representation of the object
print(RimeSynthesizer.to_json())

# convert the object into a dict
rime_synthesizer_dict = rime_synthesizer_instance.to_dict()
# create an instance of RimeSynthesizer from a dict
rime_synthesizer_form_dict = rime_synthesizer.from_dict(rime_synthesizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


