from sources.base_model_request import BaseModelRequest, RequestContext
import allure


class User_Api(BaseModelRequest):

    @allure.step("sign_up endpoint={endpoint} method={method} body={body}")
    def test_post_crate_user(self,  endpoint="/auth/signup", method="post", **kwargs):
        context = RequestContext(endpoint=endpoint,  method=method, **kwargs)
        return self.create_request(context)

    @allure.step("auntificated_user_data endpoint={endpoint} method={method} headers={headers}")
    def test_get_auntificated_user_data(self, headers, endpoint='/users/current', method="get", **kwargs):
        context = RequestContext(headers=headers, endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)

    @allure.step("auntificated_user_profile endpoint={endpoint} method={method} headers={headers}")
    def test_get_auntificated_user_profile(self, headers, endpoint='/users/profile', method="get", **kwargs):
        context = RequestContext(headers=headers, endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)

    @allure.step("auntificated_user_settings endpoint={endpoint} method={method} headers={headers}")
    def test_get_auntificated_user_settings(self, headers, endpoint='/users/settings', method="get", **kwargs):
        context = RequestContext(headers=headers, endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)

    @allure.step("edits_edits_user_settings endpoint={endpoint} method={method} body={body}")
    def test_put_edits_user_profile(self, body, endpoint="/users/profile", method="put", **kwargs):
        context = RequestContext(endpoint=endpoint, method=method, body=body, **kwargs)
        return self.create_request(context)

    @allure.step("edits_user_settings endpoint={endpoint} method={method} body={body}")
    def test_put_edits_user_settings(self, body, endpoint="/users/settings", method="put", **kwargs):
        context = RequestContext(endpoint=endpoint, method=method, body=body, **kwargs)
        return self.create_request(context)

    @allure.step("edits_user_email endpoint={endpoint} method={method} body={body}")
    def test_put_edits_user_email(self, body, endpoint="/users/email", method="put", **kwargs):
        context = RequestContext(endpoint=endpoint, method=method, body=body, **kwargs)
        return self.create_request(context)

    @allure.step("edits_user_password endpoint={endpoint} method={method} body={body}")
    def test_put_edits_user_password(self, body, endpoint="/users/password", method="put", **kwargs):
        context = RequestContext(endpoint=endpoint, method=method, body=body, **kwargs)
        return self.create_request(context)


class Cars(BaseModelRequest):

    @allure.step("test_post_create_a_new_car endpoint={endpoint} method={method} body={body}")
    def test_post_create_a_new_car(self, endpoint='/cars', method='post', **kwargs):
        context = RequestContext(endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)

    @allure.step("test_get_car_brend endpoint={endpoint} method={method} headers={headers}")
    def test_get_car_brend(self, endpoint='/cars/brands', method="get", **kwargs):
        context = RequestContext(endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)

    @allure.step("test_get_car_brend_by_id endpoint={endpoint} method={method} headers={headers}")
    def test_get_car_brend_by_id(self, endpoint='/cars/brands/', method="get", ids=None, **kwargs):
        endpoint = f"{endpoint}{ids}"
        context = RequestContext(endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)

    @allure.step("test_get_car_model endpoint={endpoint} method={method} headers={headers}")
    def test_get_car_model(self, endpoint='/cars/brands', method="get", **kwargs):
        context = RequestContext(endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)

    @allure.step("test_get_car_brend_by_id endpoint={endpoint} method={method} headers={headers}")
    def test_get_car_model_by_id(self, endpoint='/cars/brands/', method="get", ids=None, **kwargs):
        endpoint = f"{endpoint}{ids}"
        context = RequestContext(endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)

    @allure.step("test_put_edits_existin_car endpoint={endpoint} method={method} body={body}")
    def test_put_edits_existin_car(self, endpoint="/cars/", method="put", ids=None, **kwargs):
        endpoint = f"{endpoint}{ids}"
        context = RequestContext(endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)


class Expension(BaseModelRequest):

    @allure.step("test_post_create_a_expenses endpoint={endpoint} method={method}")
    def test_post_create_a_expenses(self, endpoint='/expenses', method='post', **kwargs):
        context = RequestContext(endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)

    @allure.step("test_get_all_expenses endpoint={endpoint} method={method} headers={headers}")
    def test_get_all_expenses(self, endpoint='/expenses', method="get", **kwargs):
        context = RequestContext(endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)

    @allure.step("test_get_expenses_an_id endpoint={endpoint} method={method} headers={headers}")
    def test_get_expenses_an_id(self, endpoint='/expenses/', method="get", ids=None, **kwargs):
        endpoint = f"{endpoint}{ids}"
        context = RequestContext(endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)

    @allure.step("test_put_edit_expenses_an_id endpoint={endpoint} method={method} headers={headers}")
    def test_put_edit_expenses_an_id(self, endpoint='/expenses/', method="put", ids=None, **kwargs):
        endpoint = f"{endpoint}{ids}"
        context = RequestContext(endpoint=endpoint, method=method, **kwargs)
        return self.create_request(context)
