```mermaid
gantt
    title Crime Reporting App - Development Schedule
    dateFormat  YYYY-MM-DD
    axisFormat  Week %W

    %% Week 1 starts on 2024-12-27 for timeline purposes

    section Backend & Database
    Backend Setup                  :t1, 2024-12-27, 7d
    Database Setup                 :t2, 2024-12-27, 7d

    section Core Backend Features
    Crime Reporting (API + DB)     :t3, 2025-01-03, 7d

    section Notifications
    Notification System (FCM)      :t4, 2025-01-10, 7d

    section Frontend
    Frontend Setup (RN Project)    :t5, 2025-01-10, 7d

    section Maps & Hotspots
    Map Integration (Google Maps)  :t6, 2025-01-17, 7d
    Hotspot Visualisation          :t7, 2025-01-24, 7d

    section Integration
    System Integration             :t8, 2025-01-31, 7d

    section Testing
    Testing & Bug Fixing           :t9, 2025-02-07, 14d

    section Finalisation
    Final Reporting & Demo         :t10, 2025-02-21, 7d

