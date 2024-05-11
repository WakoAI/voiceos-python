# voiceos.ConversationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_phone_call**](ConversationsApi.md#create_phone_call) | **POST** /conversations/create_phone_call | Create Phone Call
[**get_audio_recording**](ConversationsApi.md#get_audio_recording) | **GET** /conversations/{id}/recording | Get Conversation Recording
[**get_conversation**](ConversationsApi.md#get_conversation) | **GET** /conversations/{id} | Get Conversation
[**list_conversations**](ConversationsApi.md#list_conversations) | **GET** /conversations | List Conversations


# **create_phone_call**
> ConversationResponse create_phone_call(create_call)

Create Phone Call

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.conversation_response import ConversationResponse
from voiceos.models.create_call import CreateCall
from voiceos.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = voiceos.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = voiceos.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with voiceos.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voiceos.ConversationsApi(api_client)
    create_call = voiceos.CreateCall() # CreateCall | 

    try:
        # Create Phone Call
        api_response = api_instance.create_phone_call(create_call)
        print("The response of ConversationsApi->create_phone_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->create_phone_call: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_call** | [**CreateCall**](CreateCall.md)|  | 

### Return type

[**ConversationResponse**](ConversationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_recording**
> ConversationRecording get_audio_recording(id)

Get Conversation Recording

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.conversation_recording import ConversationRecording
from voiceos.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = voiceos.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = voiceos.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with voiceos.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voiceos.ConversationsApi(api_client)
    id = 'id_example' # str | The id of the conversation

    try:
        # Get Conversation Recording
        api_response = api_instance.get_audio_recording(id)
        print("The response of ConversationsApi->get_audio_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->get_audio_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the conversation | 

### Return type

[**ConversationRecording**](ConversationRecording.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation**
> ConversationResponse get_conversation(id)

Get Conversation

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.conversation_response import ConversationResponse
from voiceos.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = voiceos.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = voiceos.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with voiceos.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voiceos.ConversationsApi(api_client)
    id = 'id_example' # str | The id of the conversation.

    try:
        # Get Conversation
        api_response = api_instance.get_conversation(id)
        print("The response of ConversationsApi->get_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->get_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the conversation. | 

### Return type

[**ConversationResponse**](ConversationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conversations**
> ConversationsPagination list_conversations(status=status, created_before=created_before, created_after=created_after, index=index, limit=limit)

List Conversations

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.conversations_pagination import ConversationsPagination
from voiceos.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = voiceos.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = voiceos.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with voiceos.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voiceos.ConversationsApi(api_client)
    status = voiceos.ConversationStatus() # ConversationStatus | The status of the conversations. (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime | The date before which the conversations were created. (optional)
    created_after = '2013-10-20T19:20:30+01:00' # datetime | The date after which the conversations were created. (optional)
    index = 1 # int | The index of the page to return. (optional) (default to 1)
    limit = 100 # int | The limit of items to return in the page. (optional) (default to 100)

    try:
        # List Conversations
        api_response = api_instance.list_conversations(status=status, created_before=created_before, created_after=created_after, index=index, limit=limit)
        print("The response of ConversationsApi->list_conversations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->list_conversations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**ConversationStatus**](.md)| The status of the conversations. | [optional] 
 **created_before** | **datetime**| The date before which the conversations were created. | [optional] 
 **created_after** | **datetime**| The date after which the conversations were created. | [optional] 
 **index** | **int**| The index of the page to return. | [optional] [default to 1]
 **limit** | **int**| The limit of items to return in the page. | [optional] [default to 100]

### Return type

[**ConversationsPagination**](ConversationsPagination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

