from typing import Optional, List, Union

from ..objects import (
    DatabaseUniversity,
    BaseObject,
    DatabaseSchool,
    BaseCountry,
    DatabaseCity,
    DatabaseFaculty,
    DatabaseStation,
    DatabaseRegion,
)
from ..abc import Model


class GetChairsResponse(Model):
    response: Optional["GetChairsResponseModel"] = None


class GetCitiesByIdResponse(Model):
    response: Optional["GetCitiesByIdResponseModel"] = None


class GetCitiesResponse(Model):
    response: Optional["GetCitiesResponseModel"] = None


class GetCountriesByIdResponse(Model):
    response: Optional["GetCountriesByIdResponseModel"] = None


class GetCountriesResponse(Model):
    response: Optional["GetCountriesResponseModel"] = None


class GetFacultiesResponse(Model):
    response: Optional["GetFacultiesResponseModel"] = None


class GetMetroStationsByIdResponse(Model):
    response: Optional["GetMetroStationsByIdResponseModel"] = None


class GetMetroStationsResponse(Model):
    response: Optional["GetMetroStationsResponseModel"] = None


class GetRegionsResponse(Model):
    response: Optional["GetRegionsResponseModel"] = None


class GetSchoolClassesResponse(Model):
    response: Optional["GetSchoolClassesResponseModel"] = None


class GetSchoolsResponse(Model):
    response: Optional["GetSchoolsResponseModel"] = None


class GetUniversitiesResponse(Model):
    response: Optional["GetUniversitiesResponseModel"] = None


class GetChairsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["BaseObject"]] = None


GetCitiesByIdResponseModel = List[BaseObject]


class GetCitiesResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["DatabaseCity"]] = None


GetCountriesByIdResponseModel = List[BaseCountry]


class GetCountriesResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["BaseCountry"]] = None


class GetFacultiesResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["DatabaseFaculty"]] = None


GetMetroStationsByIdResponseModel = List[DatabaseStation]


class GetMetroStationsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["DatabaseStation"]] = None


class GetRegionsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["DatabaseRegion"]] = None


GetSchoolClassesResponseModel = List[List[Union[str, int]]]


class GetSchoolsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["DatabaseSchool"]] = None


class GetUniversitiesResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["DatabaseUniversity"]] = None


GetChairsResponse.update_forward_refs()
GetCitiesByIdResponse.update_forward_refs()
GetCitiesResponse.update_forward_refs()
GetCountriesByIdResponse.update_forward_refs()
GetCountriesResponse.update_forward_refs()
GetFacultiesResponse.update_forward_refs()
GetMetroStationsByIdResponse.update_forward_refs()
GetMetroStationsResponse.update_forward_refs()
GetRegionsResponse.update_forward_refs()
GetSchoolClassesResponse.update_forward_refs()
GetSchoolsResponse.update_forward_refs()
GetUniversitiesResponse.update_forward_refs()
