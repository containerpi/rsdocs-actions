import time
import hmac
import hashlib
import base64
import urllib
import requests
import os


def dingtalk_send(token, secret, json_data=""):
    url = "https://oapi.dingtalk.com/robot/send"
    ts = int(round(time.time() * 1000))
    str = '{}\n{}'.format(ts, secret)
    hmc = hmac.new(secret.encode('utf-8'), str.encode('utf-8'), digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmc))
    endpoint = '{}?access_token={}&timestamp={}&sign={}'.format(url, token, ts, sign)
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(url=endpoint, headers=headers, json=json_data)
    print(resp.text)


if __name__ == '__main__':
    token = os.getenv('DINGTALK_ACCESS_TOKEN')
    secret = os.getenv('DINGTALK_SECRET')
    job_status = os.getenv('JOB_STATE')
    github_ref = os.getenv('GITHUB_REF')
    github_run_id = os.getenv('GITHUB_RUN_ID')
    runner_os = os.getenv('RUNNER_OS')
    github_repository = os.getenv('GITHUB_REPOSITORY')
    if job_status == 'success':
        color = "#1ce43f"
    elif job_status == 'cancelled':
        color = "#c1c1c1"
    else:
        color = "#ff4a83"
    message = {
        "msgtype": "markdown",
        "markdown": {
            "title": "Project Build Info",
            "text": "### Project Build Info #" + github_run_id + "\n\n> status: **<font color=" + color + ">" + str(job_status).upper() + "</font>** \n\n> head ref: **" + github_ref + "** \n\n> runner os: **" + runner_os + "** \n\n> actions url: [" + github_repository + "](https://github.com/" + github_repository + "/actions)\n\n"
        }
    }
    dingtalk_send(token, secret, json_data=message)
