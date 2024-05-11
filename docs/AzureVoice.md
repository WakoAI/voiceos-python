# AzureVoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The voice provider. | [optional] [default to 'azure']
**model** | [**Model**](Model.md) |  | [optional] 
**pitch** | **int** | The pitch of the voice. | [optional] [default to 0]
**rate** | **int** | The rate of the voice. | [optional] [default to 0]

## Example

```python
from voiceos.models.azure_voice import AzureVoice

# TODO update the JSON string below
json = "{}"
# create an instance of AzureVoice from a JSON string
azure_voice_instance = AzureVoice.from_json(json)
# print the JSON string representation of the object
print(AzureVoice.to_json())

# convert the object into a dict
azure_voice_dict = azure_voice_instance.to_dict()
# create an instance of AzureVoice from a dict
azure_voice_form_dict = azure_voice.from_dict(azure_voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


