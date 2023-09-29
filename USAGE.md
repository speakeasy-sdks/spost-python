<!-- Start SDK Example Usage -->


```python
import sendpost
from sendpost.models import operations, shared

s = sendpost.Sendpost()

req = operations.EmailRouterSendEmailRequest(
    request_body=':k13|`asY9'.encode(),
    x_send_post_mock_email=False,
    x_send_post_mock_time_shift='Recycled',
    x_sub_account_api_key='Supervisor',
)

res = s.subaccount_email.email_router_send_email(req)

if res.body is not None:
    # handle response
```
<!-- End SDK Example Usage -->