from tests.api.pages.user_api import PostCreateUser


def test_post_create_user_success(api_url,headers):

    post_create_user = PostCreateUser()

    method = 'POST'
    endpoint = '/v2/user/'

    response = post_create_user.post_request_body(
        api_url=api_url,
        headers=headers,
        method=method,
        endpoint=endpoint)

    assert response.status_code == 200

    post_create_user.validate_response_body()



