# Transcriber1

The transcriber of the agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **object** | The transcriber provider. | [optional] 
**model** | [**DeepgramModel**](DeepgramModel.md) | The deepgram model to use. | [optional] 
**language** | [**DeepgramLanguages**](DeepgramLanguages.md) | The selected language for the transcription. | [optional] 
**keywords** | **object** | Specific keywords you want to detect in the transcription. This is usefull to correctly understand product or company names. | [optional] 
**languages** | **object** | The selected languages for the transcription. | [optional] 

## Example

```python
from voiceos.models.transcriber1 import Transcriber1

# TODO update the JSON string below
json = "{}"
# create an instance of Transcriber1 from a JSON string
transcriber1_instance = Transcriber1.from_json(json)
# print the JSON string representation of the object
print(Transcriber1.to_json())

# convert the object into a dict
transcriber1_dict = transcriber1_instance.to_dict()
# create an instance of Transcriber1 from a dict
transcriber1_form_dict = transcriber1.from_dict(transcriber1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


