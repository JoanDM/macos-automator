import json

from automator_class import Automator

# Example implementation of

# fetch('https://jsonplaceholder.typicode.com/posts', {
#   method: 'POST',
#   body: JSON.stringify({
#     title: 'foo',
#     body: 'bar',
#     userId: 1
#   }),
#   headers: {
#     'Content-type': 'application/json; charset=UTF-8'
#   }
# })
# .then(res => res.json())
# .then(console.log)

# A handy trick to know the Post command structure is to open chrome dev tools and
# copy the target Post request as cURL


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    json_payload = {"title": "foo", "body": "bar", "userId": 1}
    headers = {"Content-type": "application/json; charset=UTF-8"}
    timeout_sec = 5
    res_status_code = 201

    automator = Automator()
    automator.start_html_session()

    res = automator.send_html_post_request(
        url=url,
        json_payload=json_payload,
        headers=headers,
        timeout=timeout_sec,
        res_status_code=res_status_code,
    )

    readable_response = json.loads(res.content.decode("unicode_escape"), strict=False)

    print(
        "\nExpected response: {'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}"
    )
    print(f"Actual response:   {readable_response}")

    automator.close_html_session()
