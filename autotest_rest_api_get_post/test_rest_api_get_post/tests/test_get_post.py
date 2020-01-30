import pytest
from framework.utils.api_utils import APIUtils
from test_rest_api_get_post.resourses.api.urls import Urls
from framework.constants import status_code as SC
from framework.constants import extension as EX
from test_rest_api_get_post.utils.test_helper import TestHelper
from test_rest_api_get_post.tests.user_stand import UserStand
from test_rest_api_get_post.resourses.test_settings import TestSettings
import allure
from hamcrest import assert_that, equal_to, contains_string, is_not, empty


@allure.story("Тестирование rest api")
class TestGetPost:
    EXP_TITLE = TestHelper.get_string(10)
    EXP_STRING = TestHelper.get_string(20)

    @allure.feature("Тестирование запроса get для всех постов")
    def test_rest_api_get_all_posts(self):

        with allure.step("Шаг 1. Проверка статус кода при запросе GET /posts"):

            api = APIUtils(Urls.TEST_STAND_URL)
            response = api.get(Urls.ALL_POSTS)
            assert_that(api.get_status_code(), equal_to(SC.STATUS_CODE_OK),
                        f"Статус код отличается от {SC.STATUS_CODE_OK}")

        with allure.step("Шаг 2. Проверка расширения файла"):
            posts_content = api.get_content_json()
            assert_that(TestHelper.check_json(posts_content), equal_to(True),
                        f"Расширение файла не {EX.JSON}")

        with allure.step("Шаг 3. Проверк, что json файл отсортирован по id"):
            posts_models = TestHelper.add_post_instance(posts_content)
            assert_that(TestHelper.check_posts(posts_models), equal_to(True), "Список не отсортирован")

    @allure.feature("Тестирование запроса get для одного поста")
    def test_rest_api_get_one_post(self):
        with allure.step("Шаг 1. Проверка статуса кода при запросе GET /posts/99"):
            api = APIUtils(Urls.TEST_STAND_URL)
            api.get(Urls.POST.format(id='99'))
            assert_that(api.get_status_code(), equal_to(SC.STATUS_CODE_OK),
                        f"Статус код отличается от {SC.STATUS_CODE_OK}")

        with allure.step("Шаг 2. Проверка userId"):
            post_99_content = api.get_content_json()
            post_99_model = TestHelper.add_post_instance(post_99_content)
            assert_that(post_99_content['userId'], equal_to(post_99_model.get_userId()), "userId не совпадают")

        with allure.step("Шаг 3. Проверка id"):
            assert_that(post_99_content['id'], equal_to(post_99_model.get_id()), "id не совпадают")

        with allure.step("Шаг 4. Проверка, что title и body не пустые"):
            assert_that(post_99_model.get_title(),  is_not(empty()), "title не пуст")
            assert_that(post_99_model.get_body(), is_not(empty()), "body не пуст")

    @allure.feature("Тестирование запроса get для одного поста")
    @pytest.mark.xfail
    def test_rest_api_get_one_post_fail(self):
        with allure.step("Шаг 1. Проверка статус кода при запросе GET /posts/150"):
            api = APIUtils(Urls.TEST_STAND_URL)
            api.get(Urls.POST.format(id='150'))
            assert_that(api.get_status_code(), equal_to(SC.STATUS_CODE_OK),
                        f"Статус код отличается от {SC.STATUS_CODE_OK}")

        with allure.step("Шаг 2. Проверка, что тело ответа пустое"):
            post_150_content = api.get_content_json()
            assert_that(post_150_content, empty(), "Тело запроса не пустое")

    @allure.feature("Тестирование запроса post для всех постов")
    def test_rest_api_post_all_posts(self):
        with allure.step("Шаг 1. Проверка статус кода при запросе POST /posts"):
            api = APIUtils(Urls.TEST_STAND_URL)
            data = {"title": self.EXP_TITLE, "body": self.EXP_STRING, "userId": Urls.USER_ID}
            api.post(Urls.ALL_POSTS, data)
            assert_that(api.get_status_code(), equal_to(SC.STATUS_CODE_CREATED),
                        f"Статус код отличается от {SC.STATUS_CODE_CREATED}")

        with allure.step("Шаг 2. Проверка отправленных данных методом POST"):
            post_content = api.get_content_json()
            post_model = TestHelper.add_post_instance(post_content)
            assert_that(data['title'], equal_to(post_model.get_title()), "title не соответствует переданным данным")
            assert_that(data['body'], equal_to(post_model.get_body()), "body не соответствует переданным данным")
            assert_that(data['userId'], equal_to(post_model.get_userId()), "userId не соответствует переданным данным")
            assert_that(post_model.get_id(), is_not(empty()), "id пуст")

    @allure.feature("Тестирование запроса get для всех пользователей")
    def test_rest_api_get_all_users(self):
        with allure.step("Шаг 1. Проверка статус кода при запросе GET /users"):
            api = APIUtils(Urls.TEST_STAND_URL)
            response = api.get(Urls.ALL_USERS)
            assert_that(api.get_status_code(), equal_to(SC.STATUS_CODE_OK),
                        f"Статус код отличается от {SC.STATUS_CODE_OK}")

        with allure.step("Шаг 2. Проверка расширения файла"):
            assert_that(api.get_headers(response, TestSettings.HEADER),
                        contains_string(EX.JSON),
                        f"Расширение файла не {EX.JSON}")

        with allure.step(f"Шаг 3. Проверка, что пользователь с id{TestSettings.USER_CHELSEY_DIETRICH['id']} существует"):
            users = api.get_content_json()
            users_models = TestHelper.add_user_instance(users)
            user = TestHelper.add_user_instance(TestSettings.USER_CHELSEY_DIETRICH)
            UserStand.USER = user
            assert_that(users_models[int(TestSettings.USER_CHELSEY_DIETRICH['id']) - 1], equal_to(user),
                        f"Пользователь с id{TestSettings.USER_CHELSEY_DIETRICH['id']} имеет другие данные")

    @allure.feature("Тестирование запроса get для одного пользователя")
    def test_rest_api_get_one_user(self):
        with allure.step("Шаг 1. Проверка статус кода при запросе GET /users/5"):
            api = APIUtils(Urls.TEST_STAND_URL)
            response = api.get(Urls.USERS.format(id='5'))
            assert_that(api.get_status_code(), equal_to(SC.STATUS_CODE_OK),
                        f"Статус код отличается от {SC.STATUS_CODE_OK}")

        with allure.step("Шаг 2. Проверка, что данные полученные на прошлом шаге соотвествуют данным с запросом GET /users/5"):
            another_user_content = api.get_content_json()
            another_user_model = TestHelper.add_user_instance(another_user_content)
            assert_that(another_user_model, equal_to(UserStand.USER),
                        "Данные пользователя не соответствуют данным полученным на прошлом шаге")
