# SynthesizerCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**WakoApiModelsSynthesizerProvider**](WakoApiModelsSynthesizerProvider.md) | The provider of the synthetizer. | 
**cost** | **float** | The cost for the synthetizer usage. Returns zero, if the provider account you provided was used. | 
**characters** | **int** | The number of characters used for the synthetizer. | 
**external** | **bool** | Whether the provider account you provided was used. If true, the cost will be zero. | 

## Example

```python
from voiceos.models.synthesizer_cost import SynthesizerCost

# TODO update the JSON string below
json = "{}"
# create an instance of SynthesizerCost from a JSON string
synthesizer_cost_instance = SynthesizerCost.from_json(json)
# print the JSON string representation of the object
print(SynthesizerCost.to_json())

# convert the object into a dict
synthesizer_cost_dict = synthesizer_cost_instance.to_dict()
# create an instance of SynthesizerCost from a dict
synthesizer_cost_form_dict = synthesizer_cost.from_dict(synthesizer_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


