import json

from automator_class import Automator

# fetch('https://jsonplaceholder.typicode.com/posts/1')
#   .then(res => res.json())
#   .then(console.log)


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    automator = Automator()
    automator.start_html_session()
    res_status_code = 200
    res = automator.send_get_html_request(url=url, res_status_code=res_status_code)

    # use strict=false if response contains backslashes
    readable_response = json.loads(res.content.decode("unicode_escape"), strict=False)

    print(f"Response:  {readable_response}")

    automator.close_html_session()
