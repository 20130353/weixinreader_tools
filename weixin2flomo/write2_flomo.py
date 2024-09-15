def main():
    filename = "write2flomo_res.txt"
    with open(filename, 'r') as f:
        data = f.readlines()
        i = 0
        while i < len(data):
            j = i + 1
            if j > len(data):
                break
            while data[j].strip() != "结束":
                j += 1
            temp_data = data[i:j]
            tag = temp_data[0]
            content = "".join(temp_data[1:])
            send_post_request(tag, content)
            print(tag, content)
            i = j + 1


def send_post_request(tag, content):
    api_url = "https://flomoapp.com/iwh/ODQ1MDQw/8aefdabb257f52f28c2d1cd5c3481f21/"
    headers = {"Content-Type": "application/json"}
    data = {"content": f"{tag}{content}"}

    try:
        import requests
        import json
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # 如果响应状态码不是 200，将引发异常
        print(f"POST request successful for content. Status code: {response.status_code}")
        print(f"Response: {response.text}\n")
    except requests.RequestException as e:
        print(f"Error sending POST request: {e}\n")


if __name__ == '__main__':
    main()
