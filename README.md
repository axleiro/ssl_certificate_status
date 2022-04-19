# ssl_certificate_status

The **ssl_cert.py** Script will check all the given domains SSL certificate and send slack notification daily on the given slack channel

**ssl_cert.py** will also check daily if any of the give domain are about to expire in next 24 hours, and if it found out any such domain it will trigger the slack command which will send an notification over given slack channel


**Prerequisites:**

python-3 and above 


## Steps To Be followed before Running the Script (.py):

1. Add all the domains in the **domains_url** list

2. Change slack token 

 ```bash
client = WebClient(token="YOUR_SLACK_TOKEN")

try:
    response = client.chat_postMessage(
            channel="YOUR_SLACK_CHANNEL", 
            )     

 ```

3. Change Slack channel as there are 2 channels in the script. so, in the first channel we need to add a channel where we want to get status of the SSL certificates daily and another channel where we want to get the notification if any of the give domain are about to expire in next 24 hours.

4. As to get notification daily we need this script to run automatically daily on the server so, we need to add a crone Job

**To add Crone Job follow these steps**

1. Become a root user
```bash
sudo su
```
2. Run below command to open crontab config file 
```bash
crontab -e
```
3. Add Cron Job- when you want to run the job, location of the interpreter and location of the .py script
```bash 
0 0 * * * /usr/bin/python3 /home/joe/ssl_cert_script/ssl_cert.py
```
