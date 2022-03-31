
ERROR_LIMIT_USERS = [
        {
            "loc": [
                "body",
                "request_body",
                "users"
            ],
            "msg": "Exceeded the limit of users, the limit is 100",
            "type": "value_error.limit.users"
        }
    ]

ERROR_API_KEY = [
        {
            "loc": [
                "body",
                "request_body",
                "apikey"
            ],
            "msg": "Unauthorized, Invalid ApiKey",
            "type": "value_error.missing"
        }
    ]
