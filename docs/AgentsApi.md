# voiceos.AgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent**](AgentsApi.md#create_agent) | **POST** /agents | Create Agent
[**delete_agent**](AgentsApi.md#delete_agent) | **DELETE** /agents/{id} | Delete Agent
[**get_agent**](AgentsApi.md#get_agent) | **GET** /agents/{id} | Get Agent
[**list_agents**](AgentsApi.md#list_agents) | **GET** /agents | List Agents
[**update_agent**](AgentsApi.md#update_agent) | **PATCH** /agents/{id} | Update Agent


# **create_agent**
> AgentResponse create_agent(agent_configuration)

Create Agent

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.agent_configuration import AgentConfiguration
from voiceos.models.agent_response import AgentResponse
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
    api_instance = voiceos.AgentsApi(api_client)
    agent_configuration = voiceos.AgentConfiguration() # AgentConfiguration | 

    try:
        # Create Agent
        api_response = api_instance.create_agent(agent_configuration)
        print("The response of AgentsApi->create_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->create_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_configuration** | [**AgentConfiguration**](AgentConfiguration.md)|  | 

### Return type

[**AgentResponse**](AgentResponse.md)

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

# **delete_agent**
> AgentResponse delete_agent(id)

Delete Agent

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.agent_response import AgentResponse
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
    api_instance = voiceos.AgentsApi(api_client)
    id = 'id_example' # str | The id of the agent.

    try:
        # Delete Agent
        api_response = api_instance.delete_agent(id)
        print("The response of AgentsApi->delete_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->delete_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the agent. | 

### Return type

[**AgentResponse**](AgentResponse.md)

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

# **get_agent**
> AgentResponse get_agent(id)

Get Agent

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.agent_response import AgentResponse
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
    api_instance = voiceos.AgentsApi(api_client)
    id = 'id_example' # str | The id of the agent.

    try:
        # Get Agent
        api_response = api_instance.get_agent(id)
        print("The response of AgentsApi->get_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the agent. | 

### Return type

[**AgentResponse**](AgentResponse.md)

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

# **list_agents**
> AgentPagination list_agents(created_after=created_after, created_before=created_before, index=index, limit=limit)

List Agents

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.agent_pagination import AgentPagination
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
    api_instance = voiceos.AgentsApi(api_client)
    created_after = '2013-10-20T19:20:30+01:00' # datetime | The date after which the agent was created. (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime | The date before which the agent was created. (optional)
    index = 1 # int | The index of the page to return. (optional) (default to 1)
    limit = 100 # int | The limit of items to return in the page. (optional) (default to 100)

    try:
        # List Agents
        api_response = api_instance.list_agents(created_after=created_after, created_before=created_before, index=index, limit=limit)
        print("The response of AgentsApi->list_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**| The date after which the agent was created. | [optional] 
 **created_before** | **datetime**| The date before which the agent was created. | [optional] 
 **index** | **int**| The index of the page to return. | [optional] [default to 1]
 **limit** | **int**| The limit of items to return in the page. | [optional] [default to 100]

### Return type

[**AgentPagination**](AgentPagination.md)

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

# **update_agent**
> AgentResponse update_agent(id, update_agent)

Update Agent

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.agent_response import AgentResponse
from voiceos.models.update_agent import UpdateAgent
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
    api_instance = voiceos.AgentsApi(api_client)
    id = 'id_example' # str | The id of the agent.
    update_agent = voiceos.UpdateAgent() # UpdateAgent | 

    try:
        # Update Agent
        api_response = api_instance.update_agent(id, update_agent)
        print("The response of AgentsApi->update_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->update_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the agent. | 
 **update_agent** | [**UpdateAgent**](UpdateAgent.md)|  | 

### Return type

[**AgentResponse**](AgentResponse.md)

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

