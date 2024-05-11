# AzureTranscriber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The transcriber provider. | [optional] [default to 'azure']
**languages** | [**List[AzureTranscriberLanguagesInner]**](AzureTranscriberLanguagesInner.md) | The selected languages for the transcription. | [optional] [default to [en-US]]

## Example

```python
from voiceos.models.azure_transcriber import AzureTranscriber

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTranscriber from a JSON string
azure_transcriber_instance = AzureTranscriber.from_json(json)
# print the JSON string representation of the object
print(AzureTranscriber.to_json())

# convert the object into a dict
azure_transcriber_dict = azure_transcriber_instance.to_dict()
# create an instance of AzureTranscriber from a dict
azure_transcriber_form_dict = azure_transcriber.from_dict(azure_transcriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


