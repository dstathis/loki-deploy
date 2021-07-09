#!/usr/bin/env python3

import argparse
from datetime import datetime
from random import choice
from time import sleep


HEADERS = {
    'Content-Type': 'application/json',
}
LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]
LOG_PATTERN = "{date_time} - [{level}] - [{num}]: {random_text}"
RAND_TEXTS = [
    "Query Execution Time:0.0022099018096924",
    "Configuration variable date.timezone is not set, guessed timezone America/Argentina/Buenos Aires. Please set date.timezone='America/Argentina/Buenos Aires in php.ini!",
    "Query:SELECT users.* FROM users WHERE users.id = '99bcc163-034c-ab4f-f1f3-5f7362bd45de' AND users.deleted=0 LIMIT 0,1",
    "SugarBean constructor error: Object has not fields in dictionary. Object name was: Audit",
    "Query:SELECT u1.first_name, u1.last_name from users u1, users u2 where u1.id = u2.reports_to_id AND u2.id = '99bcc163-034c-ab4f-f1f3-5f7362bd45de' and u1.deleted=0",
    "Query:SELECT gcoop_salesopportunity.* FROM gcoop_salesopportunity WHERE gcoop_salesopportunity.id = '35063c55-1c51-ff9a-473f-5f7610e7ea10' AND gcoop_salesopportunity.deleted=0 LIMIT 0,1",
    "SMTP server settings required first."
    "Query:SHOW INDEX FROM aow_workflow",
    "Query:SHOW TABLES LIKE 'aow_processed'",
    "You're using 'root' as the web-server user. This should be avoided for security reasons. Review allowed_cron_users configuration in config.php.",
]

def generate_log_lines(num):
    return [generate_log_text(num) for _ in range(num)]


def generate_log_text(number):
    date_time = datetime.now().isoformat()
    return LOG_PATTERN.format(date_time=date_time, level=choice(LEVELS), num=number, random_text=choice(RAND_TEXTS))

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', action='store', dest='num',
                        help='Number of lines per second', default=30000, type=int)

    return parser.parse_args()

def main():
    args = parse_args()
    print(f"Lines per second: {args.num}")

    with open('/tmp/loki_load_test.log', mode='at', encoding='utf-8') as f:
        while True:
            f.write('\n'.join(generate_log_lines(args.num)))
            sleep(1)


if __name__ == '__main__':g
    main()
