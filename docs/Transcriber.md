# Transcriber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **object** | The transcriber provider. | [optional] 
**model** | [**Model1**](Model1.md) |  | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**keywords** | **object** | Specific keywords you want to detect in the transcription. This is useful to correctly understand product or company names. | [optional] 
**languages** | **object** | The selected languages for the transcription. | [optional] 

## Example

```python
from voiceos.models.transcriber import Transcriber

# TODO update the JSON string below
json = "{}"
# create an instance of Transcriber from a JSON string
transcriber_instance = Transcriber.from_json(json)
# print the JSON string representation of the object
print(Transcriber.to_json())

# convert the object into a dict
transcriber_dict = transcriber_instance.to_dict()
# create an instance of Transcriber from a dict
transcriber_form_dict = transcriber.from_dict(transcriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


