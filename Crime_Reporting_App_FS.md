

Functional Specification

for

Crime Reporting App

Prepared by Luke Robinson and Abdalla Ibrahim



Table of Contents











Introduction

Overview

The Crime Reporting App is a mobile application that will be designed to allow users to submit real time crime reports from their phones. The system addresses a need for community focused safety tools that help people stay aware of crimes that take place near their location. Users will be able to record details of the crime they witnessed, such as the type of crime, a short description, and also their location.



Once a report is submitted, the application will notify nearby users within a certain radius through a push notification. This allows users to make safer decisions, such as avoiding certain routes, and/or staying alert when travelling. All reported incidents will be stored in a database, which the app will then use to generate crime hotspots through heat maps, and will be able to filter through types of crimes, or locations with recurring criminal activity.



The application will be a full stack system, using React Native, , MySQL, Google Maps, and Firebase Cloud Messaging.



Business Context

While the system is being developed for our 3rd Year Project, it is based on real world safety needs for citizens. Community awareness and access to information can significantly help users to avoid certain areas, and stay informed if travelling through an area they are not familiar with.



These are a few possible business contexts where the system could be used:



Community Safety: Neighborhood watch groups could use this app to track suspicious activities occurring in the neighbourhood, and keep neighborhoods informed if a crime takes place eg robbery.

Public Safety Awareness: Councils could use this application to monitor trends of growing crimes, location of crimes, etc

Future Integrations: The system could eventually be integrated with emergency services and/or An Garda Siochana



Glossary





Overall Description

Product / System Functions

The primary system functions include:



Crime Reporting: Users can submit a crime or suspicious activity they witness. This includes the type of crime, the ability to add a small description, and automatically attaches their location. 

Real Time Notifications: When a report is submitted, the system will send a push notifications to nearby users within a certain radius, alerting the user and allows them to take precautionary measures.

Location: The application will use Google Maps API to pinpoint the users location, and will attach said location to the crime they have reported.

Crime Hotspots: The system will store reported crimes, and visualize areas where crimes take place the most.

Account Management: Users can register, log in, and manage their account. Authentication will ensure that reports are linked to real users accounts.

User Characteristics and Objectives

The primary users of the Crime Reporting App will be members of the general public who want to stay informed about crimes happening in their area. The app will be designed in a way that will be accessible to users with little to no technical experience. The expected user characteristics are as follows:



Basic phone literacy such as users should be comfortable navigating apps, using maps, and enabling location permissions.

The interface will be designed in a clear and intuitive way to accommodate to a wide range of ages



From the users perspective, the main objectives will include:



Users who want to avoid areas with a high crime rate, receiving real time alerts to support this goal.

The app will allow users to submit a report, which will take only a couple of seconds, without having to make phone calls or just keeping it to yourself

The hotspots feature will help users to understand crime patterns happening around them.

Operational Scenarios

This section will outline a few scenarios on how different users will interact with the system, and will demonstrate how the app will behave in certain situations.



Registering and Downloading

The user will download the app and select “Register”.

They enter both their email, and choose a password.

After creating an account, they can log in and have access to the application.



Submitting a Crime Report

A user witnesses a crime/suspicious activity.

The user opens the Crime Reporting App and selects “Report Crime”.

The user selects the type of incident and enters an optional description.

The app will automatically detect their GPS location.

Nearby users will then receive a push notification, alerting them of a recent report.

After submitting, the data will be sent to the server and stored in the database.



Receiving a Push Notification

A user within the notification range of a newly submitted report.

The user will receive a push notification detailing the crime type and location.

The user will then be able to open the app to view details regarding the report.

The user is then able to make better informed decisions eg avoiding the area.



Viewing Crime Hotspots

A user plans a route home and night and wants to check if the area is safe.

The user opens the hotspot map

The system retrieves stored crime data within a certain time frame, and highlights risky areas.

The user can then adjust their route accordingly.

Constraints

There will be several design and implementation constraints through the development of our application.



Google Maps API Integration

Neither team members have experience with integrating Google Maps into a mobile application. Implementing this may require more time to learn and become familiar with the platform.

Firebase Cloud Messaging

Similarly to the Google Maps integration, neither team members have experience using Firebase Cloud Messaging for the integration of our push notifications. As this will be our first time using this, it may lead to increased development time.

Full Stack Integration

One of the biggest constraints is connecting the frontend, backend and database. The project will use React Native as the frontend,  backend, and a MySQL database. While both members have some experience with this integration, there are issues which may follow.

REST API design and validation.

Asynchronous communication between frontend, backend, and database.

Ensuring push notification trigger correctly after the database is updated with new information.

Avoiding general inconsistencies between the frontend and backend.

Assumptions

For a user to use the Crime Reporting App, there are several assumptions that are made regarding the user, their environment, etc. These assumptions are made to help with both the design of the application, as well as the expected behavior of the system.



User Assumptions



Users will have a stable internet connection when using the app.

Users will allow the application to access their location services.

Users will allow the application to send push notification to their device.

Users are reporting accurate crime reports.



Device Assumptions



The device used will return the users accurate GPS location.

The users device will be running on a version that is compatible with libraries used.



System Assumptions



The MySQL database will be able to handle the volume of expected read/write operations during our testing phase.

API communication between the frontend and backend will remain consistent throughout the project.



Functional Requirements

This section will outline all the major functional requirements of the application. Each requirement will be described in terms of what it will do, why it is important, and what challenges may arise.

User Registration

Description

This function will allow users to create an account. Users will register using an email and password. The system will then store this information securely in the database, and creates a new user profile.



Criticality

High. This feature is essential for the app. Without the user registering an account, the user will not be able to report crimes, receive notifications, or access any other feature the app offers.



Technical Issues

Must securely store the users credentials.

Validation is needed to prevent multiple accounts from the same user.

Registration must communicate correctly with the backend to create a new record in the database.



Dependencies

Depends on both the backend API and database being up and working correctly.

User Login

Description

Users enter both their email and password to log into their account. Once login is successful, the user can then submit reports, receive notifications, and other features of the app.



Criticality

High. User login is required to ensure accountability for interactions with the app, and prevent anonymous misuse of the app.



Technical Issues

Secure authentication on the backend.

Maintaining session on the frontend.

Handling incorrect credentials in a proper manner.



Dependencies

Requires user registration to be used prior to login (3.1).



Crime Reporting

Description

This function allows the user to submit a crime report. The user will be prompted to select the type of crime, and an optional description. The system will then automatically pinpoint their location and attach it to the report. The report is then stored in the database.



Criticality

High. This feature is the core function of the app.



Technical Issues

Integrating GPS services to fetch accurate location.

Ensuring that the report is properly formatted before sending to the backend.

Edge cases such as submitting a blank report etc.



Dependencies

Requires user to be logged in (3.2).

Requires location services to be enabled.

Push Notifications

Description

After a crime is submitted on the application, the system sends a push notification to nearby users. The notification includes the type of crime and location.



Criticality

Medium - High. Real time push notifications are a major part of the system, which allow users to stay informed and make better informed decisions. While not completely necessary for the user to use, it is a major function of the system.



Technical Issues

Implementation of Firebase Cloud Messaging.

Determining which users are within the specific radius to receive a notification.

Ensuring notifications are triggered within a short time span after a report is submitted.

Dependencies

Requires the successful submission of a crime report (3.3), as well as correct implementation of Firebase Cloud Messaging.



Location Services



Description

The app will attach the users location to a submitted crime report, and also send push notifications based on the users location.



Criticality

High. Location services are essential for users submitting reports, as well as for section 3.6. 



Technical Issues

Unfamiliar with integration of Google Maps API.

Inaccurate locations being attached to reports, or for notifications.

Ensuring the map loads correctly on all devices.



Dependencies

Requires a stable internet connection, location services to be enabled on the users device, as well as backend crime data to be fetched.





Hotspot Visualisation



Description

The system analyses stored crime data, and will highlight areas with a high frequency of reports. 



Criticality

Medium. This visualisation allows for users to make informed decisions.



Technical Issues

Calculation of hotspot thresholds, such as the number of reports per area.

Fetching and retrieving data from the MySQL database.

Using heatmaps from Google Maps API



Dependencies

Requires processing of crime data, and location functionality.



Account Management



Description

Users will be able to update their account details such as their password.



Criticality

Low. This feature is not essential for the functioning of the app, but also important for users who like to regularly change their passwords.



Technical Issues

Updating user data in the database.



Dependencies

Depends on registration (3.1) and login (3.2).



Logout



Description

Allows users to log out of their account.



Criticality

Low - Medium. Prevents the misuse of using multiple accounts.



Technical Issues

Redirecting user back to the login screen



Dependecies

Depends on login (3.2).

System Architecture

The Crime Reporting App will follow a full stack architecture that combines a mobile frontend, a backend REST API, and a database. 

Architecture Overview

The system will be made up of three main parts as follows:



Frontend (React Native)

Handles all user interaction.

Displays maps, reports, and hotspots

Sends the users actions/inputs through API requests.

Backend ( / Express API)

Processes the requests from the app.

Manages the authentication, reporting, and notification logic.

Connects to the database, Google Maps API, and Firebase Cloud Messaging.

Database (MySQL)

Stores user details, crime reports, timestamps, and location details.

Provides data for hotspot generation.

Architecture Diagram





Frontend (React Native)



The frontend of the application will be built using React Native. The frontend will interact through HTTP requests and will not directly connect to the database. Its responsibilities will include:



Displaying the user interface.

Collecting user inputs.

Handles registration, login, and logout.

Sending crime reports to the backend.

Receiving push notification.



Backend API ( / Express API)



The backend of the application will be built using  and Express API. The backend will allow the frontend to:



Register and authenticate new users.

Submit new crime reports.

Retrieve existing reports used for visualisation.

Trigger push notifications to nearby users.



The backend will also handle:



Input validation.

Filtering of crimes by location and data.

Determining which users receive push notifications.

Communication with both the database and Firebase.



Database (MySQL)



The database will be used to store all relevant data, including:



Users accounts.

Crime reports (type, description, timestamp, location).



External Services



Google Maps API:

Displays the map UI, used for hotspot visualization 



Firebase Cloud Messaging

Sending push notifications to users to notify them of a nearby crime.

Other Nonfunctional Requirements

Performance Requirements

The system needs to provide fast performance and be reliable to make it easier for users to act on crime-related information in real In order to do this the following things are required:

Push Notification Speed: Notifications about newly submitted crimes should be submitted to users who are nearby within 5-10 seconds of the report being stored in the database.

Map Rendering: Google Maps views (including crime hotspots) should load within 3 seconds on a stable internet connection.

Database Response Times:API requests to the  backend should return results within 500 ms assuming the testing phase load is as described in the project assumptions.

Concurrent Requests: The backend must support simultaneous read/write operations from multiple users without data corruption, especially for hotspot generation and crime reports.

Safety Requirements

The app must not encourage users to intervene or respond in the case of active crimes.

The system should have safety messaging to indicate that the app is not a replacement for emergency services and that users should dial emergency services in cases of immediate danger.

Sensitive user actions such as report submission must not cause the user to physically approach dangerous areas.

Location access must not expose the users real-time location to other users to avoid safety risks like stalking.

Security Requirements

As this application handles sensitive data like location, it requires strong security:

User Authentication:Must use secure encrypted communication with the backend and secure password handling.

Data Storage Protection:

Software Quality Attributes

Business Rules

<List any operating principles about the product, such as which individuals or roles can perform which functions under specific circumstances. These are not functional requirements in themselves, but they may imply certain functional requirements to enforce the rules.>

Other Requirements

<Define any other requirements not covered elsewhere in the SRS. This might include database requirements, internationalization requirements, legal requirements, reuse objectives for the project, and so on. Add any new sections that are pertinent to the project.>

Appendix A: Glossary

<Define all the terms necessary to properly interpret the SRS, including acronyms and abbreviations. You may wish to build a separate glossary that spans multiple projects or the entire organization, and just include terms specific to a single project in each SRS.>

Appendix B: Analysis Models

<Optionally, include any pertinent analysis models, such as data flow diagrams, class diagrams, state-transition diagrams, or entity-relationship diagrams.>

Appendix C: To Be Determined List

<Collect a numbered list of the TBD (to be determined) references that remain in the SRS so they can be tracked to closure.>