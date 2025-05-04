import datetime
import json
from pprint import pprint
from typing import Dict, List

from pydantic import BaseModel


# class PropertyHistory_home(BaseModel):
#     home: Dict[str, Dict[Any, Any]]

class Listing(BaseModel):
    last_status_change_date: datetime.datetime | None
    last_update_date: datetime.datetime | None
    list_date: datetime.datetime | None
    list_price: int | None
    listing_id: str | None
    status: str | None


class PropertyHistory(BaseModel):
    date: datetime.datetime
    event_name: str
    listing: Listing | None

    price: int | None
    source_listing_id: int | None
    source_name: str | None

    price_change: int | None
    price_sqft: float | None

class AssessmentTax(BaseModel):
    building: int | None
    land: int | None
    total: int | None


class MarketTax(BaseModel):
    building: int | None
    land: int | None
    total: int | None


class TaxHistory(BaseModel):
    assessment: AssessmentTax | None
    market: MarketTax | None

    tax: int | None
    year: int | None


class PropertyTaxHistory(BaseModel):
    property_history: List[PropertyHistory]
    tax_history: List[TaxHistory]


class PropertyHistory_home(BaseModel):
    home: PropertyTaxHistory


class PropertyHistory_data(BaseModel):
    data: PropertyHistory_home


if __name__ == '__main__':
    with open('PropertyHistories', 'r') as file:
        property = json.loads(file.read())

    # print(property)

    values = PropertyHistory_data(**property)

    # print(values)
    print(values.data.home.property_history[0])
    print(values.data.home.tax_history[0])
