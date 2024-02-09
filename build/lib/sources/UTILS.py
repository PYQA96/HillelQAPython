import string
import random
from  enum import global_enum



CREATED_STATUS_CODE = 201
SUCSESSFUL_STATUS_CODE = 200
ERROR_STATUS_CODE_CREATED = 400
EROR_STATUS_CODE_AUTH= 401
NOT_FOUND_STATUS_CODE = 404
ERROR_MESAGES = 'К сожлению такой пользователь был создан '
SUCSECFULL_MASAGES = 'Запрос прошел '
VALIDATION_SCHEMA_OK = 'validation passed!'
VALIDATION_SCHEMA_FAIL= 'validation failed'
TYPE_TEST_NEGATIVE = "Negative test"
TYPE_TEST_POSITIVE= "Positive test"

random_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
headers_fake = {
            'Cookie': 'sid=s%3AxQldEO2TRBdPrpYwoqcTu12tmS-GLE_o.xdBV9F5MPENwCljNqSlJD2zjZ3PMu8u0bGErRAlGUc012313'
        }

json_schema_users_created_sucsess = {
    "type": "object",
    "properties": {
        "status": {"type": "string","enum": ["ok"]},
        "data": {
            "type": "object",
            "properties": {
                "userId": {"type": "number"},
                "photoFilename": {"type": "string"},
                "distanceUnits": {"type": "string"},
                "currency": {"type": "string"},
            },
            "required": ["userId", "photoFilename" ,'distanceUnits' ]
        }
    },
    "required": ["status", "data"]
}

json_schema_users_fail = {
    "type": "object",
    "properties": {
        "status": {"type": "string","enum": ["error"]},
        "message": {"type": "string"},
    },
    "required": ["status", "message"]
}
#
json_schema_users_created_auth = {
    "type": "object",
    "properties": {
        "status": {"type": "string","enum": ["ok"]},
        "data": {
            "type": "object",
            "properties": {
                "userId": {"type": "number"},
                "photoFilename": {"type": "string"},
                "name": {"type": "string"},
                "lastName": {"type": "string"},
            },
            "required": ["userId", "name" ,"lastName"   ]
        }
    },
    "required": ["status", "data"]
}

json_schema_users_settings = {
    "type": "object",
    "properties": {
        "status": {"type": "string","enum": ["ok"]},
        "data": {
            "type": "object",
            "properties": {
                "currency": {"type": "string"},
                "distanceUnits": {"type": "string"},
            },
            "required": ["currency", "distanceUnits"]
        }
    },
    "required": ["status", "data"]
}

body_to_request_profile_edit= {
            "photo": "Test.jpg",
            "name": "Test",
            "lastName": "Test",
            "dateBirth": "2021-03-17T15:21:05.000Z",
            "country": "Test"
        }
body_to_request_users_settings = {
  "currency": "usd",
  "distanceUnits": "km"
}


json_schema_users_updated = {
    "type": "object",
    "properties": {
        "status": {"type": "string","enum": ["ok"]},
        "data": {
            "type": "object",
            "properties": {
                "userId": {"type": "number"},
                "photoFilename": {"type": "string"},
                "name" : {"type": "string","enum": ["Test"]},
                 "lastName": {"type": "string","enum": ["Test"]},
                "dateBirth":{"type": "string","format": "date-time"},
                "country":{"type": "string","enum": ["Test"]}
            },
            "required": ["userId", "photoFilename"]
        }
    },
    "required": ["status", "data"]
}

json_schema_profile_updated = {
    "type": "object",
    "properties": {
        "status": {"type": "string","enum": ["ok"]},
        "data": {
                "currency": {"type": "number"},
                "distanceUnits": {"type": "string"},
        },

    },
    "required": ["status",]
}
json_schema_email_ok={
    "type": "object",
    "properties": {
        "status": {
            "type": "string",
            "enum": ["ok"]
        },
        "data": {
            "type": "object",
            "properties": {
                "userId": {
                    "type": "number"
                }
            },
            "required": ["userId"]
        }
    },
    "required": ["status", "data"]
}

created_car_sucsessfull = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "enum": ["ok"]},
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "carBrandId": {"type": "integer"},
                "carModelId": {"type": "integer"},
                "initialMileage": {"type": "integer"},
                "updatedMileageAt": {"type": "string", "format": "date-time"},
                "carCreatedAt": {"type": "string", "format": "date-time"},
                "mileage": {"type": "integer"},
                "brand": {"type": "string"},
                "model": {"type": "string"},
                "logo": {"type": "string"}
            },
            "required": ["id", "carBrandId", "carModelId", "initialMileage", "updatedMileageAt", "carCreatedAt",
                         "mileage", "brand", "model", "logo"]
        }
    },
    "required": ["status", "data"]
}

created_car_not_crated = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "enum": ["error"]},
        "message": {"type": "string","enum": ["Not authenticated"]},
    },
    "required": ["status", "message"]
}

sucsessful_masage_expenses_created={
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": ["ok"]
    },
    "data": {
      "type": "object",
      "properties": {
        "carId": {
          "type": "integer"
        },
        "reportedAt": {
          "type": "string",
          "pattern": "^\\d{4}-\\d{1,2}-\\d{1,2}$"
        },
        "liters": {
          "type": "number"
        },
        "id": {
          "type": "integer"
        },
        "mileage": {
          "type": "integer"
        },
        "totalCost": {
          "type": "number"
        }
      },
      "required": ["carId", "reportedAt", "liters", "id", "mileage", "totalCost"]
    }
  },
  "required": ["status", "data"]
}

all_expenses ={
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": ["ok"]
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "carId": {
            "type": "integer"
          },
          "reportedAt": {
            "type": "string",
            "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
          },
          "mileage": {
            "type": "integer"
          },
          "liters": {
            "type": "integer"
          },
          "totalCost": {
            "type": "integer"
          }
        },
        "required": ["id", "carId", "reportedAt", "mileage", "liters", "totalCost"]
      }
    },
    "currentPage": {
      "type": "integer"
    },
    "totalItems": {
      "type": "integer"
    }
  },
  "required": ["status", "data", "currentPage", "totalItems"]
}