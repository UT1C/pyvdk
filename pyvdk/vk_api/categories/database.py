# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Database(Category):

    def get_chairs(
        self,
        faculty_id: int = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getChairs", locals())

    def get_cities(
        self,
        country_id: int = None,
        region_id: Optional[int] = None,
        q: Optional[str] = None,
        need_all: Optional[bool] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getCities", locals())

    def get_cities_by_id(
        self,
        city_ids: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getCitiesById", locals())

    def get_countries(
        self,
        need_all: Optional[bool] = None,
        code: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getCountries", locals())

    def get_countries_by_id(
        self,
        country_ids: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getCountriesById", locals())

    def get_faculties(
        self,
        university_id: int = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getFaculties", locals())

    def get_metro_stations(
        self,
        city_id: int = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getMetroStations", locals())

    def get_metro_stations_by_id(
        self,
        station_ids: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getMetroStationsById", locals())

    def get_regions(
        self,
        country_id: int = None,
        q: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getRegions", locals())

    def get_school_classes(
        self,
        country_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getSchoolClasses", locals())

    def get_schools(
        self,
        q: Optional[str] = None,
        city_id: int = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getSchools", locals())

    def get_universities(
        self,
        q: Optional[str] = None,
        country_id: Optional[int] = None,
        city_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getUniversities", locals())
