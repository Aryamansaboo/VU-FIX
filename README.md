# VUFIX — Hostel Maintenance & Complaint Management System

**VUFIX** is a responsive Single-Page Web Application (SPA) designed to fix the transparency gap in hostel maintenance complaint handling for Vijaybhoomi University.

Live Link / GitHub Pages: **https://aryamansaboo.github.io/ui-ux-mid-term/**

---

## 🚀 Key Features & User Portals

### 1. Fretbox-Inspired Tabbed Authentication & One-Click Demo Presets
- 3 Interactive Tabs: `Student Login`, `Student Sign Up`, and `Warden / Admin Login`.
- **Quick Fill Demo Presets**:
  - ⚡ **Aryaman Saboo** (`ST20230042`, Hostel A, Block B3, Room B3-304)
  - 🛡️ **Rinu Babu** (`ADM-WARDEN-01`, Hostel Warden)
  - 👤 **Parth Pawar** (`ST20230088`, Room A1-101)

### 2. Student Maintenance Portal
- Personalized header greeting with Roll Number, Hostel Room, and Email badges.
- Overview Stat Cards (Active Requests, Resolved Issues, Escalated Tickets, Avg Response Time).
- **Guided 3-Step Complaint Submission Wizard**: Select Category -> Enter Details & Preferred Visit Slot -> Review & Submit.
- **My Complaints List**: Filter pills (*All*, *Pending*, *In Progress*, *🚨 Escalated*, *Resolved*) and search bar.
- **Live Stepper Timeline Modal**: Tracks full history from submission to resolution, displaying assigned technician details (Ramesh Kumar, Suresh Sharma, Vikas Patil, Sunita Devi), contact links, ETA countdowns, and Warden notes.
- **Escalate to Warden Trigger**: Allows students to flag delayed or urgent tickets to the Warden.
- **Resolution Verification Prompt**: Prompts student to confirm repair (*"Yes, It's Fixed!"* with 5-star rating or *"No, Still Broken"* to reopen ticket).

### 3. Hostel Warden Management Portal
- Admin Overview Dashboard displaying total, pending, in-progress, urgent escalations, and resolved metrics.
- **Urgent Escalation Banner**: High-visibility banner highlighting student-escalated complaints with 1-click action buttons.
- Filter bar (status, category, hostel block) and search.
- **Interactive Ticket Control Center Modal**: Update status, assign staff technician from roster, set/extend target resolution ETA, and add maintenance notes that stream into the student's live timeline.

---

## 🛠️ Architecture & Tech Stack

- **Core**: Vanilla HTML5, JavaScript (ES6+), Vanilla CSS3.
- **Data & State**: LocalStorage persistent reactive state store (`store.js`). Zero external framework dependencies.
- **Design System**: Dark indigo & HSL palette, glassmorphism card elevation, FontAwesome 6 icons, smooth CSS micro-animations.

---

## 📁 Repository Structure

```
index.html               Single Page Web Application entry point
style.css                Custom CSS Design System & glassmorphism theme
store.js                 LocalStorage persistent reactive state store & mock seed data
app.js                   SPA controller, tab routing, modals, and handlers
.gitignore               Git ignore configuration
```
