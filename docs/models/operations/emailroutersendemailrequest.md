# EmailRouterSendEmailRequest


## Fields

| Field                         | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `request_body`                | *bytes*                       | :heavy_check_mark:            | The Email Message             |
| `x_send_post_mock_email`      | *Optional[bool]*              | :heavy_minus_sign:            | Mock email header             |
| `x_send_post_mock_time_shift` | *Optional[str]*               | :heavy_minus_sign:            | Mock email time shift         |
| `x_sub_account_api_key`       | *str*                         | :heavy_check_mark:            | Sub-Account API Key           |