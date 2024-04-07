# OpenAIFunctionParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**OpenAIFunctionType**](OpenAIFunctionType.md) | This must be set to &#39;object&#39;. It instructs the model to return a JSON object containing the function call properties. | [optional] 
**properties** | **object** | This provides a description of the properties required by the function. | 
**required** | **List[str]** | This specifies the properties that are required by the function. | [optional] [default to []]

## Example

```python
from voiceos.models.open_ai_function_parameter import OpenAIFunctionParameter

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAIFunctionParameter from a JSON string
open_ai_function_parameter_instance = OpenAIFunctionParameter.from_json(json)
# print the JSON string representation of the object
print(OpenAIFunctionParameter.to_json())

# convert the object into a dict
open_ai_function_parameter_dict = open_ai_function_parameter_instance.to_dict()
# create an instance of OpenAIFunctionParameter from a dict
open_ai_function_parameter_form_dict = open_ai_function_parameter.from_dict(open_ai_function_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


