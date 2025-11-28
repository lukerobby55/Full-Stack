# Crime Reporting App – Functional Specification
Prepared by **Luke Robinson** & **Abdalla Ibrahim**

## Table of Contents
1. [Introduction](#1-introduction)
   - [1.1 Overview](#11-overview)
   - [1.2 Purpose](#12-purpose)
   - [1.3 Business Context](#13-business-context)
   - [1.4 Intended Audience](#14-intended-audience)
   - [1.5 Document Conventions](#15-document-conventions)
   - [1.6 Glossary](#16-glossary)

2. [Overall Description](#2-overall-description)
   - [2.1 Product / System Functions](#21-product--system-functions)
   - [2.2 User Characteristics and Objectives](#22-user-characteristics-and-objectives)
   - [2.3 Operational Scenarios](#23-operational-scenarios)
   - [2.4 Constraints](#24-constraints)
   - [2.5 Assumptions](#25-assumptions)

3. [Functional Requirements](#3-functional-requirements)
   - [3.1 User Registration](#31-user-registration)
   - [3.2 User Login](#32-user-login)
   - [3.3 Crime Reporting](#33-crime-reporting)
   - [3.4 Push Notifications](#34-push-notifications)
   - [3.5 Location Services](#35-location-services)
   - [3.6 Hotspot Visualisation](#36-hotspot-visualisation)
   - [3.7 Crime History](#37-crime-history)
   - [3.8 Account Management](#38-account-management)
   - [3.9 Logout](#39-logout)

4. [System Architecture](#4-system-architecture)
   - [4.1 Architecture Overview](#41-architecture-overview)
   - [4.2 Architecture Diagram](#42-architecture-diagram)
   - [4.3 Frontend (React Native)](#43-frontend-react-native)
   - [4.4 Backend (Nodejs--Express)](#44-backend-nodejs--express)
   - [4.5 Database (MySQL)](#45-database-mysql)
   - [4.6 External Services](#46-external-services)
   - [4.7 Data Flow Summary](#47-data-flow-summary)

5. [High-Level Design](#5-high-level-design)
   - [5.1 System Workflow](#51-system-workflow)
   - [5.2 Data Flow Diagram (DFD)](#52-data-flow-diagram-dfd)
   - [5.3 Sequence Diagram](#53-sequence-diagram)

6. [Preliminary Schedule](#6-preliminary-schedule)

7. [Appendices](#7-appendices)


# 1. Introduction

## 1.1 Overview
The Crime Reporting App is a mobile application designed to allow users to submit real-time crime or suspicious activity reports. Reports include the crime type, an optional description, and the user’s GPS-based location.

After submission, the system automatically notifies nearby users through push notifications, helping people avoid potentially unsafe areas. All reports are stored and used to generate crime hotspots and visualise trends over time.

The system is built using: React Native, Node.js, Express, MySQL, Google Maps API, and Firebase Cloud Messaging.

## 1.2 Purpose
This document outlines the full Functional Specification of the Crime Reporting App.

## 1.3 Business Context
The system is developed as part of a CA326 third-year project. Although academic in nature, it mimics real-world safety tools.

## 1.4 Intended Audience
- CA326 supervisor and graders  
- Developers  
- Reviewers and testers  

## 1.5 Document Conventions
- Requirements labeled REQ-X  
- JSON used for data transfer  
- Technical terms defined in Glossary  

## 1.6 Glossary
| Term | Meaning |
|------|---------|
| GPS | Device location service |
| Hotspot | High-frequency crime area |
| FCM | Firebase Cloud Messaging |


# 2. Overall Description

## 2.1 Product / System Functions
- Crime reporting  
- Push notifications  
- Map display  
- Hotspot analysis  
- Account management  

## 2.2 User Characteristics and Objectives
Users: general public with basic mobile literacy.  
Objectives: stay safe, report incidents, view hotspots.

## 2.3 Operational Scenarios
- Register  
- Submit report  
- Receive notification  
- View hotspots  

## 2.4 Constraints
- Limited Maps API experience  
- First-time Firebase use  
- Full-stack complexity  
- Internet required  

## 2.5 Assumptions
- Users allow GPS + notifications  
- Devices are Android  
- Stable internet available  


# 3. Functional Requirements

## 3.1 User Registration (REQ-1)
Essential for identity and accountability.

## 3.2 User Login (REQ-2)
Authenticates users.

## 3.3 Crime Reporting (REQ-3)
Core feature: submit crime + GPS.

## 3.4 Push Notifications (REQ-4)
Alerts nearby users.

## 3.5 Location Services (REQ-5)
Retrieves GPS accurately.

## 3.6 Hotspot Visualisation (REQ-6)
Displays heatmap of crime activity.

## 3.7 Crime History (REQ-7)
Allows browsing past reports.

## 3.8 Account Management (REQ-8)
Modify user details.

## 3.9 Logout (REQ-9)
Ends session.


# 4. System Architecture

## 4.1 Architecture Overview
Full-stack system using mobile app, backend API, database, external APIs.

## 4.2 Architecture Diagram
```
           +------------------------------+
           |       React Native App       |
           |        (Frontend / Mobile)   |
           +------------------------------+
                 |                  ^  
                 |  JSON Responses  |  
   API Calls     v                  |
      ------------------------------------------------
      |        Node.js / Express Backend API         |
      |      (Authentication, Crime Logic, API)      |
      ------------------------------------------------
            |                          |
     SQL Queries                 Trigger Push Notification
            |                          |
            v                          v
     +----------------+        +-----------------------------+
     |   MySQL DB     |        | Firebase Cloud Messaging    |
     | (Users, Crimes)|        |   (Push Notifications)      |
     +----------------+        +-----------------------------+
                 ^
                 |
  Request Map Tiles, Markers, Routes, Hotspot Overlays
                 |
      +--------------------------+
      |     Google Maps API      |
      +--------------------------+
```

## 4.3 Frontend (React Native)
Handles UI, map display, GPS, notifications.

## 4.4 Backend (Node.js + Express)
Handles authentication, data storage, notification triggers.

## 4.5 Database (MySQL)
Stores crime data + users.

## 4.6 External Services
- Firebase Cloud Messaging  
- Google Maps API  

## 4.7 Data Flow Summary
1. User submits report  
2. Backend stores data  
3. Backend triggers FCM  
4. Notifications delivered  


# 5. High-Level Design

## 5.1 System Workflow
1. User opens app  
2. GPS retrieved  
3. Report submitted  
4. Data stored  
5. Notifications sent  

## 5.2 Data Flow Diagram (DFD)
```
User → App → Backend → Database  
Backend → Firebase → Other Users  
Maps API → App → User
```

## 5.3 Sequence Diagram
```
User -> App: Submit Report  
App -> Backend: POST /report  
Backend -> DB: Insert  
Backend -> FCM: Send notification  
FCM -> Devices: Notify users  
```


# 6. Preliminary Schedule
To be completed (Gantt chart).


# 7. Appendices
- Glossary  
- UML Diagrams  
- TBD Items  
