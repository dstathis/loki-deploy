#!/usr/bin/env python3

import json
import time
from locust import HttpUser, TaskSet, task
from locust.contrib.fasthttp import FastHttpUser


HEADERS = {
    'Content-Type': 'application/json',
}

class LokiTest1(FastHttpUser):

    @task
    def logfile1(self):
        current_time = time.time_ns()
        data = {
            "streams": [
                {
                    "stream": {"filename": "/var/log/pepetest"},
                    "values": [
                        [str(current_time), "This is a fake pepetest log since we are evaluating Loki" ]
                    ]
                }
            ]
        }

        self.client.post('/loki/api/v1/push',
                         data=json.dumps(data),
                         headers=HEADERS)

    @task
    def logfile2(self):
        current_time = time.time_ns()
        data = {
            "streams": [
                {
                    "stream": {"filename": "/var/log/josetest"},
                    "values": [
                        [str(current_time), "This is a fake josetest log since we are evaluating Loki" ]
                    ]
                }
            ]
        }

        self.client.post('/loki/api/v1/push',
                         data=json.dumps(data),
                         headers=HEADERS)

    @task
    def logfile3(self):
        current_time = time.time_ns()
        data = {
            "streams": [
                {
                    "stream": {"filename": "/var/log/diegotest"},
                    "values": [
                        [str(current_time), "This is a fake diegotest log since we are evaluating Loki" ]
                    ]
                }
            ]
        }

        self.client.post('/loki/api/v1/push',
                         data=json.dumps(data),
                         headers=HEADERS)
