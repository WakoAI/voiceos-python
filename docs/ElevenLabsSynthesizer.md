# ElevenLabsSynthesizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The synthesizer provider. | [optional] [default to 'elevenlabs']
**model** | [**ElevenLabsModel**](ElevenLabsModel.md) | The elevenlabs model to use | [optional] 
**optimize_latency** | **int** | Optimize for latency | [optional] [default to 0]

## Example

```python
from voiceos.models.eleven_labs_synthesizer import ElevenLabsSynthesizer

# TODO update the JSON string below
json = "{}"
# create an instance of ElevenLabsSynthesizer from a JSON string
eleven_labs_synthesizer_instance = ElevenLabsSynthesizer.from_json(json)
# print the JSON string representation of the object
print(ElevenLabsSynthesizer.to_json())

# convert the object into a dict
eleven_labs_synthesizer_dict = eleven_labs_synthesizer_instance.to_dict()
# create an instance of ElevenLabsSynthesizer from a dict
eleven_labs_synthesizer_form_dict = eleven_labs_synthesizer.from_dict(eleven_labs_synthesizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


