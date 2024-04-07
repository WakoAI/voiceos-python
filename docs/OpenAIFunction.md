# OpenAIFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the name of the function to be called. Must be less than 64 characters (a-z, A-Z, 0-9, including underscores). | 
**wait** | **bool** | If true, the agent will wait for the function to return before continuing. | [optional] [default to False]
**description** | **str** | The description of the OpenAI function call. | 
**parameters** | [**OpenAIFunctionParameter**](OpenAIFunctionParameter.md) | The parameters of the OpenAI function call. | 

## Example

```python
from voiceos.models.open_ai_function import OpenAIFunction

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAIFunction from a JSON string
open_ai_function_instance = OpenAIFunction.from_json(json)
# print the JSON string representation of the object
print(OpenAIFunction.to_json())

# convert the object into a dict
open_ai_function_dict = open_ai_function_instance.to_dict()
# create an instance of OpenAIFunction from a dict
open_ai_function_form_dict = open_ai_function.from_dict(open_ai_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


