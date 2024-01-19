from pydantic import BaseModel, Field, ValidationError, field_validator


class UserData_setings(BaseModel):
    userId: int
    photoFilename: str
    name: str
    lastName: str
    dateBirth: str
    country: str


class UserData_profile(BaseModel):
    distanceUnits: str
    currency: str


class ApiResponse(BaseModel):
    status: str
    data: UserData_setings

    @field_validator("status")
    def check_status(cls, status):
        if status != "ok":
            raise ValueError("Не тот статус")


class ApiResponse_setings(ApiResponse):
    data: UserData_profile


class ApiResponseCar(BaseModel):
    status: str
    message: str

    @field_validator("status")
    def check_status(cls, status):
        if status != "error":
            raise ValueError("Не тот статус")



class Bodeyexpenses(BaseModel):
    carId: int
    reportedAt: str
    liters: int
    id: int
    mileage: int
    totalCost: int


class ApiResponseExpenses(BaseModel):
    status: str
    data: Bodeyexpenses

    @field_validator("status")
    def check_status(cls, status):
        if status != "ok":
            raise ValueError("Не тот статус")