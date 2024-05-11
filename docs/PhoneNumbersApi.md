# voiceos.PhoneNumbersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**available_numbers_to_buy**](PhoneNumbersApi.md#available_numbers_to_buy) | **GET** /phone_numbers/buy | Available Phone Numbers To Buy
[**buy_phone_number**](PhoneNumbersApi.md#buy_phone_number) | **POST** /phone_numbers/buy | Buy Phone Number
[**delete_phone_number**](PhoneNumbersApi.md#delete_phone_number) | **DELETE** /phone_numbers/{phone_number} | Delete Phone Number
[**get_phone_number**](PhoneNumbersApi.md#get_phone_number) | **GET** /phone_numbers/{phone_number} | Get Phone Number
[**list_phone_numbers**](PhoneNumbersApi.md#list_phone_numbers) | **GET** /phone_numbers | List Phone Numbers
[**update_phone_number**](PhoneNumbersApi.md#update_phone_number) | **PATCH** /phone_numbers/{phone_number} | Update Phone Number


# **available_numbers_to_buy**
> List[PhoneNumberToBuy] available_numbers_to_buy(contains=contains, limit=limit)

Available Phone Numbers To Buy

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.phone_number_to_buy import PhoneNumberToBuy
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
    api_instance = voiceos.PhoneNumbersApi(api_client)
    contains = 'contains_example' # str | The digits that the phone number contains. (optional)
    limit = 10 # int | The number of available phone numbers to return. (optional) (default to 10)

    try:
        # Available Phone Numbers To Buy
        api_response = api_instance.available_numbers_to_buy(contains=contains, limit=limit)
        print("The response of PhoneNumbersApi->available_numbers_to_buy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->available_numbers_to_buy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contains** | **str**| The digits that the phone number contains. | [optional] 
 **limit** | **int**| The number of available phone numbers to return. | [optional] [default to 10]

### Return type

[**List[PhoneNumberToBuy]**](PhoneNumberToBuy.md)

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

# **buy_phone_number**
> PhoneNumberResponse buy_phone_number(buy_phone_number)

Buy Phone Number

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.buy_phone_number import BuyPhoneNumber
from voiceos.models.phone_number_response import PhoneNumberResponse
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
    api_instance = voiceos.PhoneNumbersApi(api_client)
    buy_phone_number = voiceos.BuyPhoneNumber() # BuyPhoneNumber | 

    try:
        # Buy Phone Number
        api_response = api_instance.buy_phone_number(buy_phone_number)
        print("The response of PhoneNumbersApi->buy_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->buy_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buy_phone_number** | [**BuyPhoneNumber**](BuyPhoneNumber.md)|  | 

### Return type

[**PhoneNumberResponse**](PhoneNumberResponse.md)

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

# **delete_phone_number**
> PhoneNumber delete_phone_number(phone_number, release_phone_number=release_phone_number)

Delete Phone Number

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.phone_number import PhoneNumber
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
    api_instance = voiceos.PhoneNumbersApi(api_client)
    phone_number = 'phone_number_example' # str | The phone number including the country code.
    release_phone_number = False # bool |  (optional) (default to False)

    try:
        # Delete Phone Number
        api_response = api_instance.delete_phone_number(phone_number, release_phone_number=release_phone_number)
        print("The response of PhoneNumbersApi->delete_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->delete_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**| The phone number including the country code. | 
 **release_phone_number** | **bool**|  | [optional] [default to False]

### Return type

[**PhoneNumber**](PhoneNumber.md)

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

# **get_phone_number**
> PhoneNumberResponse get_phone_number(phone_number)

Get Phone Number

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.phone_number_response import PhoneNumberResponse
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
    api_instance = voiceos.PhoneNumbersApi(api_client)
    phone_number = 'phone_number_example' # str | The phone number including the country code.

    try:
        # Get Phone Number
        api_response = api_instance.get_phone_number(phone_number)
        print("The response of PhoneNumbersApi->get_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->get_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**| The phone number including the country code. | 

### Return type

[**PhoneNumberResponse**](PhoneNumberResponse.md)

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

# **list_phone_numbers**
> PhoneNumberPagination list_phone_numbers(created_after=created_after, created_before=created_before, index=index, limit=limit)

List Phone Numbers

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.phone_number_pagination import PhoneNumberPagination
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
    api_instance = voiceos.PhoneNumbersApi(api_client)
    created_after = '2013-10-20T19:20:30+01:00' # datetime | The date the phone number was created after. (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime | The date the phone number was created before. (optional)
    index = 1 # int | The index of the page to return. (optional) (default to 1)
    limit = 100 # int | The number of phone numbers to return in the page. (optional) (default to 100)

    try:
        # List Phone Numbers
        api_response = api_instance.list_phone_numbers(created_after=created_after, created_before=created_before, index=index, limit=limit)
        print("The response of PhoneNumbersApi->list_phone_numbers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->list_phone_numbers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**| The date the phone number was created after. | [optional] 
 **created_before** | **datetime**| The date the phone number was created before. | [optional] 
 **index** | **int**| The index of the page to return. | [optional] [default to 1]
 **limit** | **int**| The number of phone numbers to return in the page. | [optional] [default to 100]

### Return type

[**PhoneNumberPagination**](PhoneNumberPagination.md)

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

# **update_phone_number**
> PhoneNumberResponse update_phone_number(phone_number, update_phone_number)

Update Phone Number

### Example

* Bearer Authentication (Bearer):

```python
import voiceos
from voiceos.models.phone_number_response import PhoneNumberResponse
from voiceos.models.update_phone_number import UpdatePhoneNumber
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
    api_instance = voiceos.PhoneNumbersApi(api_client)
    phone_number = 'phone_number_example' # str | The phone number including the country code.
    update_phone_number = voiceos.UpdatePhoneNumber() # UpdatePhoneNumber | 

    try:
        # Update Phone Number
        api_response = api_instance.update_phone_number(phone_number, update_phone_number)
        print("The response of PhoneNumbersApi->update_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->update_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**| The phone number including the country code. | 
 **update_phone_number** | [**UpdatePhoneNumber**](UpdatePhoneNumber.md)|  | 

### Return type

[**PhoneNumberResponse**](PhoneNumberResponse.md)

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

