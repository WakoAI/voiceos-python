# AzureSynthesizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The synthesizer provider. | [optional] [default to 'azure']
**model** | [**AzureModel**](AzureModel.md) | The azure model to use | [optional] 
**pitch** | **int** | The pitch of the voice | [optional] [default to 0]
**rate** | **int** | The rate of the voice | [optional] [default to 0]

## Example

```python
from voiceos.models.azure_synthesizer import AzureSynthesizer

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSynthesizer from a JSON string
azure_synthesizer_instance = AzureSynthesizer.from_json(json)
# print the JSON string representation of the object
print(AzureSynthesizer.to_json())

# convert the object into a dict
azure_synthesizer_dict = azure_synthesizer_instance.to_dict()
# create an instance of AzureSynthesizer from a dict
azure_synthesizer_form_dict = azure_synthesizer.from_dict(azure_synthesizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


