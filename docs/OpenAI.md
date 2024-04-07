# OpenAI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The lnaguage model provider. | [optional] [default to 'openai']
**model** | [**ChatGPT**](ChatGPT.md) | The OpenAI Chat GPT model to use | [optional] 
**functions** | [**List[OpenAIFunction]**](OpenAIFunction.md) | The list of OpenAI function calls. | [optional] 

## Example

```python
from voiceos.models.open_ai import OpenAI

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAI from a JSON string
open_ai_instance = OpenAI.from_json(json)
# print the JSON string representation of the object
print(OpenAI.to_json())

# convert the object into a dict
open_ai_dict = open_ai_instance.to_dict()
# create an instance of OpenAI from a dict
open_ai_form_dict = open_ai.from_dict(open_ai_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


