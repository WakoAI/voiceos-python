# OpenAI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The language model provider. | [optional] [default to 'openai']
**model** | [**Model3**](Model3.md) |  | [optional] 

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


