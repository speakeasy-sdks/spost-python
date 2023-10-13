<!-- Start SDK Example Usage -->


```python
import sendpost
from sendpost.models import operations, shared

s = sendpost.Sendpost()

req = operations.EmailRouterSendEmailRequest(
    request_body=':k13|`asY9'.encode(),
    x_sub_account_api_key='Recycled',
)

res = s.subaccount_email.email_router_send_email(req)

if res.body is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->