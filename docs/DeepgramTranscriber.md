# DeepgramTranscriber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The transcriber provider. | [optional] [default to 'deepgram']
**model** | [**Model1**](Model1.md) |  | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**keywords** | **List[str]** | Specific keywords you want to detect in the transcription. This is useful to correctly understand product or company names. | [optional] [default to []]

## Example

```python
from voiceos.models.deepgram_transcriber import DeepgramTranscriber

# TODO update the JSON string below
json = "{}"
# create an instance of DeepgramTranscriber from a JSON string
deepgram_transcriber_instance = DeepgramTranscriber.from_json(json)
# print the JSON string representation of the object
print(DeepgramTranscriber.to_json())

# convert the object into a dict
deepgram_transcriber_dict = deepgram_transcriber_instance.to_dict()
# create an instance of DeepgramTranscriber from a dict
deepgram_transcriber_form_dict = deepgram_transcriber.from_dict(deepgram_transcriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


