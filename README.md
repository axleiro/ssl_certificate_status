# ssl_certificate_status

The **ssl_cert.py** Script will check all the given domains SSL certificate and send slack notification daily on the given slack channel

**ssl_cert.py** will also check daily if any of the give domain are about to expire in next 24 hours, and if it found out any such domain it will trigger the slack command which will send an notification over given slack channel


**Prerequisites:**

python-3 and above 


## Steps To Be followed before Running the Script (.py):

1. Add all the domains in the **domains_url** list

2. Change slack token on line 52 and 80

3. Change Slack channel as there are 2 channels in the script. so, in the first channel we need to add a channel where we want to get status of the SSL certificates daily and another channel where we want to get the notification if any of the give domain are about to expire in next 24 hours.

4. As to get notification daily we need this script to run automatically daily on the server so, we need to add a crone Job

**To add Crone Job follow these steps**

1. change user to root 
```bash
 sudo su
```
crontab -e 
