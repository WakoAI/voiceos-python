# LanguageModelCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**WakoApiModelsLanguageModelProvider**](WakoApiModelsLanguageModelProvider.md) | The provider of the language model. | 
**cost** | **float** | The cost for the language model usage (USD). | 
**input_tokens** | **int** | The number of input tokens used for the language model. | 
**output_tokens** | **int** | The number of output tokens used for the language model. | 

## Example

```python
from voiceos.models.language_model_cost import LanguageModelCost

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageModelCost from a JSON string
language_model_cost_instance = LanguageModelCost.from_json(json)
# print the JSON string representation of the object
print(LanguageModelCost.to_json())

# convert the object into a dict
language_model_cost_dict = language_model_cost_instance.to_dict()
# create an instance of LanguageModelCost from a dict
language_model_cost_form_dict = language_model_cost.from_dict(language_model_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


