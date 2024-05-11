# VoiceCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**WakoApiModelsSynthesizerProvider**](WakoApiModelsSynthesizerProvider.md) | The provider of the synthetizer. | 
**cost** | **float** | The cost for the voice usage (USD). | 
**characters** | **int** | The number of characters used for the voice. | 

## Example

```python
from voiceos.models.voice_cost import VoiceCost

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceCost from a JSON string
voice_cost_instance = VoiceCost.from_json(json)
# print the JSON string representation of the object
print(VoiceCost.to_json())

# convert the object into a dict
voice_cost_dict = voice_cost_instance.to_dict()
# create an instance of VoiceCost from a dict
voice_cost_form_dict = voice_cost.from_dict(voice_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


