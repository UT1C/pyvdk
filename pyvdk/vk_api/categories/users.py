from ..category import Category


class Users(Category):
    def get(
        self,
        user_ids: list = None,
        fields: list = None,
        name_case: str = None,
    ) -> dict:
        """
        Returns detailed information on users.
        """
        return self._request("get", locals())

    def get_followers(
        self,
        user_id: int = None,
        offset: int = None,
        count: int = None,
        # ? <= count <= 1000
        fields: list = None,
        name_case: str = None,
    ) -> dict:
        """
        Returns a list of IDs of followers of the user in question, sorted by date added, most recent first.
        """
        return self._request("getFollowers", locals())

    def get_subscriptions(
        self,
        user_id: int = None,
        extended: bool = None,
        offset: int = None,
        count: int = None,
        # ? <= count <= 200
        fields: list = None,
    ) -> dict:
        """
        Returns a list of IDs of users and communities followed by the user.
        """
        return self._request("getSubscriptions", locals())

    def report(
        self,
        user_id: int = None,
        type: str = None,
        comment: str = None,
    ) -> dict:
        """
        Reports (submits a complain about) a user.
        """
        return self._request("report", locals())

    def search(
        self,
        q: str = None,
        sort: int = None,
        offset: int = None,
        count: int = None,
        # ? <= count <= 1000
        fields: list = None,
        city: int = None,
        country: int = None,
        hometown: str = None,
        university_country: int = None,
        university: int = None,
        university_year: int = None,
        university_faculty: int = None,
        university_chair: int = None,
        sex: int = None,
        status: int = None,
        age_from: int = None,
        age_to: int = None,
        birth_day: int = None,
        birth_month: int = None,
        birth_year: int = None,
        # 1900 <= birth_year <= 2100
        online: bool = None,
        has_photo: bool = None,
        school_country: int = None,
        school_city: int = None,
        school_class: int = None,
        school: int = None,
        school_year: int = None,
        religion: str = None,
        company: str = None,
        position: str = None,
        group_id: int = None,
        from_list: list = None,
    ) -> dict:
        """
        Returns a list of users matching the search criteria.
        """
        return self._request("search", locals())


# generated at 2020.11.08 08:32:23
