import socket
import ssl
import datetime

#add domain url below
domains_url = ["metrics.solana.com","internal-metrics.solana.com","api.internal.testnet.solana.com","api.internal.devnet.solana.com","api.internal.mainnet-beta.solana.com"]

def ssl_expiry_datetime(hostname):
    ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    context.check_hostname = False

    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    # 5 second timeout
    conn.settimeout(5.0)

    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    # Python datetime object
    return datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)
ssl_cert_details=" "
ssl_cert_in_1_day=" "
if __name__ == "__main__":
    for value in domains_url:
        now = datetime.datetime.now()
        try:
            expire = ssl_expiry_datetime(value)
            diff = expire - now
            if diff <= datetime.timedelta(days=2):
                 ssl_cert_in_1_day=ssl_cert_in_1_day+str("\n")+str("Domain ") + value + str(" SSL certificate is about to expire in 24 hours")
            ssl_cert_details=ssl_cert_details + str("\n") + "Domain name: {} Expiry Date: {} Expire in: {} ".format(value,expire.strftime("%Y-%m-%d"),diff.days)+("Days")
            print(ssl_cert_details)
        except Exception as e:
            print (e)
            
#check if domains  ssl cert will expire in 1 day and notify on slack

Result_Detail= str("```") + str(ssl_cert_details) + str("```")
Result_Detail2= str("```") + str(ssl_cert_in_1_day) + str("```")
# adding the python-slack client
import logging
logging.basicConfig(level=logging.DEBUG)
import os
os.system('pip install slackclient')
from slack import WebClient
from slack.errors import SlackApiError
#change slack token below with yours 
client = WebClient(token="xoxb-3038346022900-3036090599603-JRp5QGPA0bO9B5dKdAfztwG6")
try:
    response = client.chat_postMessage(
            #change channel below with your's, to get daily update regarding ssl certificate
            channel="C031248E3EF",
            blocks=[{
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": Result_Detail
                    }
                }

            ]
      ) 
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["error"]


if len(ssl_cert_in_1_day)>1:
    import logging
    logging.basicConfig(level=logging.DEBUG)
    import os
    os.system('pip install slackclient')
    from slack import WebClient
    from slack.errors import SlackApiError
    #change slack token below with yours 
    client = WebClient(token="xoxb-3038346022900-3036090599603-JRp5QGPA0bO9B5dKdAfztwG6")
    try:
        response = client.chat_postMessage(
                #change channel below, where you will get notified 1 day before the expiry of the SSL certificate
                channel="C030VB2A6GN",
                blocks=[{
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": Result_Detail2
                        }
                    }
                ]
          ) 
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]
