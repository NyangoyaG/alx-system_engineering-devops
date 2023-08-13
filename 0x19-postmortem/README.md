### Web Stack Debugging Project Outage Postmortem
#### Issue Summary

##### Between 0945 am and 1140 am on 11 Aug 2023 EAT, 100% users were experiencing error 503 on the browser indicating service unavailable which is caused by Nginx web server causing disruptions to website or web application. The route cause of this outage was a faulty firewall configuration that caused the firewall to deem requests from a content delivery.

#### Timeline
##### 09:45 AM: The website goes down.
##### 10:05 AM: A monitoring alert is triggered, notifying the engineering team of the outage.
##### 10:10 AM: Developers team investigates the issue and determines that the website is not starting because of  faulty configuration in the Nginx.
##### 10:30 AM: The developers team fixed the faulty configurations and restarted the Nginx server.
##### 11:45 AM: 100% of traffic back online
#### Route Cause and Resolution
##### The root cause of the issue was a faulty configuration in the Nginx configuration file. Faulty firewall configuration caused the firewall to deem requests from a content delivery network as an attack on the server and reject them, resulting in a 503 Service Unavailable Error.
##### The issue was resolved by locating the faulty code, correcting it, saving the configuration and restarting the Nginx server.

#### Corrective and Preventative Measures
##### Improve server configuration management to ensure that all necessary ports are open and services are configured correctly.
##### Implement monitoring on the server to alert on any changes to the Nginx configuration and its status.
##### Conduct regular check to ensure that the server is working properly 
##### Develop better mechanisms for quickly delivering status notifications during incidents.

