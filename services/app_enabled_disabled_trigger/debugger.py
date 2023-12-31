from lambda_function import lambda_handler

payload = {
  "version": "2.0",
  "routeKey": "$default",
  "rawPath": "/path/to/resource",
  "rawQueryString": "",
  "cookies": [
    "cookie1",
    "cookie2"
  ],
  "headers": {

  },
  "queryStringParameters": {

  },
  "requestContext": {
    "accountId": "123456789012",
    "apiId": "api-id",
    "authentication": {
      "clientCert": {
        "clientCertPem": "CERT_CONTENT",
        "subjectDN": "www.example.com",
        "issuerDN": "Example issuer",
        "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
        "validity": {
          "notBefore": "May 28 12:30:02 2019 GMT",
          "notAfter": "Aug  5 09:36:04 2021 GMT"
        }
      }
    },
    "authorizer": {
      "jwt": {
        "claims": {
          "claim1": "value1",
          "claim2": "value2"
        },
        "scopes": [
          "scope1",
          "scope2"
        ]
      }
    },
    "domainName": "id.execute-api.us-east-1.amazonaws.com",
    "domainPrefix": "id",
    "http": {
      "method": "POST",
      "path": "/path/to/resource",
      "protocol": "HTTP/1.1",
      "sourceIp": "192.168.0.1/32",
      "userAgent": "agent"
    },
    "requestId": "id",
    "routeKey": "$default",
    "stage": "$default",
    "time": "12/Mar/2020:19:03:58 +0000",
    "timeEpoch": 1583348638390
  },
  "body": "{\"Services\": [ {\"UUID\": \"27a2cc75-7d63-4235-b45a-be3c9ad9b324\",\"Enabled\": false },{\"UUID\": \"fa18b2f8-d7c9-4db0-8949-b57a67f1d3eb\",\"Enabled\": true}]}",
  "pathParameters": {
  },
  "isBase64Encoded": True,
  "stageVariables": {
    "stageVariable1": "value1",
    "stageVariable2": "value2"
  }
}

response = lambda_handler(payload, None)

print(response)