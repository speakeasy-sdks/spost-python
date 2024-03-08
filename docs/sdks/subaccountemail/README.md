# SubaccountEmail
(*subaccount_email*)

### Available Operations

* [email_router_send_email](#email_router_send_email) - Send Email To Contacts
* [email_router_send_email_with_template](#email_router_send_email_with_template) - Send Email To Contacts With Template

## email_router_send_email

Send Email To Contacts

### Example Usage

```python
import sendpost
from sendpost.models import operations

s = sendpost.Sendpost()

req = operations.EmailRouterSendEmailRequest(
    request_body='0x6B34FffDd5'.encode(),
    x_sub_account_api_key='<value>',
)

res = s.subaccount_email.email_router_send_email(req)

if res.body is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.EmailRouterSendEmailRequest](../../models/operations/emailroutersendemailrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.EmailRouterSendEmailResponse](../../models/operations/emailroutersendemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## email_router_send_email_with_template

Send Email To Contacts With Template

### Example Usage

```python
import sendpost
from sendpost.models import operations

s = sendpost.Sendpost()

req = operations.EmailRouterSendEmailWithTemplateRequest(
    request_body='0x5Ade99aeea'.encode(),
    x_sub_account_api_key='<value>',
)

res = s.subaccount_email.email_router_send_email_with_template(req)

if res.body is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.EmailRouterSendEmailWithTemplateRequest](../../models/operations/emailroutersendemailwithtemplaterequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.EmailRouterSendEmailWithTemplateResponse](../../models/operations/emailroutersendemailwithtemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
