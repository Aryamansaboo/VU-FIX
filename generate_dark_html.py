html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VUFIX — Obsidian Edition</title>
  
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="style.css">
  
  <style>
    .hidden { display: none !important; }
    .sidebar-nav-list { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }
    .view-container { display: none; }
    .view-container.active { display: flex; flex-direction: column; }
    
    #view-student, #view-warden, #view-wizard { width: 100%; height: 100vh; overflow: hidden; display: none; }
  </style>
</head>
<body>
  
<div id="toast-container"></div>

<div id="app">

  <!-- ================= AUTH VIEW ================= -->
  <div id="view-auth" class="auth-wrapper active">
    <div class="auth-card">
      <div class="auth-header">
        <div class="auth-logo"><i class="fa-solid fa-bolt"></i></div>
        <h1>VUFIX OBSIDIAN</h1>
        <p>Advanced Hostel Maintenance System</p>
      </div>
      
      <div class="auth-tabs">
        <button class="auth-tab-btn active" data-tab="student-login">Resident</button>
        <button class="auth-tab-btn" data-tab="student-signup">Register</button>
        <button class="auth-tab-btn" data-tab="warden-login">Administrator</button>
      </div>
      
      <form id="form-student-login" class="auth-form">
        <div class="form-group">
          <label for="login-email">Email or Registration ID</label>
          <input type="text" id="login-email" class="form-control" placeholder="Resident ID" required value="aryaman.saboo@vijaybhoomi.edu.in">
        </div>
        <div class="form-group">
          <label for="login-password">Access Code</label>
          <input type="password" id="login-password" class="form-control" placeholder="••••••••" required value="password123">
        </div>
        <button type="submit" class="btn-primary">
          Authenticate as Resident <i class="fa-solid fa-arrow-right"></i>
        </button>
      </form>
      
      <form id="form-student-signup" class="auth-form hidden">
        <div class="form-group"><label>Full Name</label><input type="text" id="signup-name" class="form-control"></div>
        <div class="form-group"><label>Roll Number</label><input type="text" id="signup-roll" class="form-control"></div>
        <div class="form-group"><label>Email</label><input type="email" id="signup-email" class="form-control"></div>
        <div class="form-group"><label>Hostel Block</label><select id="signup-hostel" class="form-control"><option>Hostel A</option></select></div>
        <div class="form-group"><label>Room Number</label><input type="text" id="signup-room" class="form-control"></div>
        <div class="form-group"><label>Create Access Code</label><input type="password" id="signup-password" class="form-control"></div>
        <button type="submit" class="btn-primary">Register Resident</button>
      </form>
      
      <form id="form-warden-login" class="auth-form hidden">
        <div class="form-group"><label>Administrator ID</label><input type="text" id="warden-admin-id" class="form-control" value="ADM-WARDEN-01"></div>
        <div class="form-group"><label>Secure Access Code</label><input type="password" id="warden-password" class="form-control" value="admin123"></div>
        <button type="submit" class="btn-primary"><i class="fa-solid fa-shield-halved"></i> Login to Admin Console</button>
      </form>
      
      <div class="demo-presets">
        <div style="font-size:0.75rem; color:var(--text-gray); text-transform:uppercase; margin-bottom:1rem; letter-spacing:0.05em;"><i class="fa-solid fa-flask"></i> Test Environment Access</div>
        <div class="preset-list">
          <button class="preset-btn btn-preset-quick" data-demo="usr_aryaman">
            <div class="preset-icon" style="background: rgba(14,165,233,0.1); color:#0ea5e9;"><i class="fa-solid fa-user"></i></div>
            <div>
              <strong style="display:block; font-size:0.875rem;">Resident Demo</strong>
              <span style="font-size:0.75rem; color:var(--text-gray);">Aryaman Saboo (2024VUGP0039)</span>
            </div>
          </button>
          <button class="preset-btn btn-preset-quick" data-demo="usr_rinu" style="border-color: rgba(16,185,129,0.3);">
            <div class="preset-icon" style="background: rgba(16,185,129,0.1); color:#10b981;"><i class="fa-solid fa-user-shield"></i></div>
            <div>
              <strong style="display:block; font-size:0.875rem;">Administrator Console</strong>
              <span style="font-size:0.75rem; color:var(--text-gray);">Warden Rinu Babu</span>
            </div>
          </button>
          <button class="preset-btn btn-preset-quick" data-demo="usr_parth">
            <div class="preset-icon" style="background: rgba(161,161,170,0.1); color:#a1a1aa;"><i class="fa-solid fa-user"></i></div>
            <div>
              <strong style="display:block; font-size:0.875rem;">Resident Demo 2</strong>
              <span style="font-size:0.75rem; color:var(--text-gray);">Parth Pawar (2024VUGP0021)</span>
            </div>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Required DOM Hooks hidden -->
  <div style="display:none;">
    <button id="btn-brand-home"></button>
    <button id="btn-user-dropdown"></button>
    <div id="nav-user-avatar"></div>
    <div id="nav-user-name"></div>
    <div id="user-preset-menu"></div>
    <button id="btn-notifications"></button>
    <div id="notif-unread-dot"></div>
    <button id="btn-toggle-research"></button>
  </div>

  <!-- ================= STUDENT VIEW ================= -->
  <div id="view-student">
    <div class="app-layout">
      <aside class="sidebar">
        <div class="sidebar-brand">
          <i class="fa-solid fa-bolt" style="color:var(--primary); font-size:1.5rem;"></i>
          <h2>VUFIX</h2>
        </div>
        <ul class="sidebar-nav-list" style="margin-top:2rem;">
          <li><a href="#" class="nav-item active"><i class="fa-solid fa-layer-group"></i> Command Center</a></li>
          <li><a href="#" class="nav-item" id="btn-open-complaint-wizard"><i class="fa-solid fa-satellite-dish"></i> Dispatch Request</a></li>
          <li><a href="#" class="nav-item"><i class="fa-solid fa-list-check"></i> System Logs</a></li>
        </ul>
        <div style="margin-top: auto;">
          <button id="btn-header-logout" class="preset-btn" style="width:100%; justify-content:center; color:var(--danger); border-color:var(--danger-bg);"><i class="fa-solid fa-power-off"></i> Terminate Session</button>
        </div>
      </aside>
      
      <main class="main-content">
        <div class="top-bar">
          <div>
            <div class="user-greeting" id="student-display-name">Welcome back, Aryaman 👋</div>
            <div class="user-tags">
              <span class="user-tag"><i class="fa-solid fa-fingerprint"></i> ID: <span id="student-badge-roll"></span></span>
              <span class="user-tag" style="border-color:rgba(14,165,233,0.3); color:#0ea5e9;"><i class="fa-solid fa-location-dot"></i> <span id="student-badge-room"></span></span>
              <span class="user-tag"><i class="fa-solid fa-at"></i> <span id="student-badge-email"></span></span>
            </div>
          </div>
          <div>
            <button class="btn-primary" onclick="document.getElementById('btn-open-complaint-wizard').click()"><i class="fa-solid fa-satellite-dish"></i> Dispatch New Request</button>
          </div>
        </div>
        
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon" style="background:rgba(14,165,233,0.1); color:#0ea5e9;"><i class="fa-solid fa-signal"></i></div>
            <div class="stat-info"><h3>Active Dispatches</h3><p id="stat-student-active">0</p></div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" style="background:var(--success-bg); color:var(--success);"><i class="fa-solid fa-check-double"></i></div>
            <div class="stat-info"><h3>Resolved</h3><p id="stat-student-resolved">0</p></div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" style="background:var(--danger-bg); color:var(--danger);"><i class="fa-solid fa-radiation"></i></div>
            <div class="stat-info"><h3>Critical Escalations</h3><p id="stat-student-escalated">0</p></div>
          </div>
        </div>
        
        <div style="display:flex; justify-content:space-between; margin-bottom:1.5rem;">
          <h2 style="font-size:1.25rem;">Live Active Feed</h2>
          <span style="font-size:0.875rem; color:var(--primary);">View Directory (<span id="student-complaints-list-count">4</span>)</span>
        </div>
        <div id="student-filter-pills" style="display:none;"></div>
        <input type="text" id="search-student-complaints" style="display:none;">
        <div id="student-complaints-list" style="display:none;"></div>
        <div class="complaints-grid" id="student-tickets-grid">
          <!-- Populated by JS -->
        </div>
      </main>
    </div>
  </div>

  <!-- ================= WIZARD VIEW ================= -->
  <div id="view-wizard">
    <div class="app-layout">
      <main class="main-content" style="align-items:center;">
        <div style="width:100%; max-width:800px; margin-bottom:2rem;">
          <button class="btn-secondary" id="btn-wiz-prev-top" style="border:none; padding-left:0;"><i class="fa-solid fa-arrow-left"></i> Return to Command Center</button>
        </div>
        
        <div class="wizard-container" id="modal-complaint-wizard" style="width:100%;">
          <div class="wizard-stepper">
            <div class="wizard-step active" id="node-step-1">
              <div class="step-circle">1</div>
            </div>
            <div class="wizard-step" id="node-step-2">
              <div class="step-circle">2</div>
            </div>
            <div class="wizard-step" id="node-step-3">
              <div class="step-circle">3</div>
            </div>
          </div>
          
          <div id="wizard-step-1-content">
            <h3 style="font-size:1.5rem; text-align:center; margin-bottom:2rem;">Select Anomaly Category</h3>
            <div class="category-grid" id="category-grid">
              <div class="cat-card selected" data-cat="Electrical">
                <i class="fa-solid fa-bolt" style="font-size:2rem; color:var(--primary); margin-bottom:1rem;"></i>
                <strong style="display:block;">Electrical Grid</strong>
              </div>
              <div class="cat-card" data-cat="Plumbing">
                <i class="fa-solid fa-faucet-drip" style="font-size:2rem; color:var(--primary); margin-bottom:1rem;"></i>
                <strong style="display:block;">Plumbing System</strong>
              </div>
              <div class="cat-card" data-cat="Furniture">
                <i class="fa-solid fa-chair" style="font-size:2rem; color:var(--primary); margin-bottom:1rem;"></i>
                <strong style="display:block;">Hardware/Furniture</strong>
              </div>
              <div class="cat-card" data-cat="IT/Network">
                <i class="fa-solid fa-wifi" style="font-size:2rem; color:var(--primary); margin-bottom:1rem;"></i>
                <strong style="display:block;">Network Infrastructure</strong>
              </div>
              <div class="cat-card" data-cat="Housekeeping">
                <i class="fa-solid fa-broom" style="font-size:2rem; color:var(--primary); margin-bottom:1rem;"></i>
                <strong style="display:block;">Sanitation Unit</strong>
              </div>
            </div>
          </div>
          
          <div id="wizard-step-2-content" class="hidden">
            <div class="form-group">
              <label>Anomaly Subject</label>
              <input type="text" id="in-issue-title" class="form-control" placeholder="Identify the core issue">
            </div>
            <div class="form-group">
              <label>Detailed Diagnostics</label>
              <textarea id="in-issue-desc" class="form-control" rows="4" placeholder="Log the anomaly diagnostics here..."></textarea>
            </div>
            <div class="form-group">
              <label>Threat Level / Priority</label>
              <select id="in-issue-priority" class="form-control">
                <option value="Low">Low Priority</option>
                <option value="Medium" selected>Standard Priority</option>
                <option value="High">Critical Priority</option>
              </select>
            </div>
          </div>
          
          <div id="wizard-step-3-content" class="hidden">
            <div class="form-group">
              <label>Technician Authorization Slot</label>
              <select id="in-pref-slot" class="form-control">
                <option>Anytime</option>
                <option>Morning Shift (0900 - 1200)</option>
                <option>Afternoon Shift (1200 - 1600)</option>
                <option>Evening Shift (1600 - 1900)</option>
              </select>
            </div>
            <div style="background:var(--bg-main); padding:2rem; border-radius:var(--radius-md); margin-top:2rem;">
              <h4 style="margin-bottom:1rem; color:var(--primary);">Dispatch Transmission Summary</h4>
              <p style="margin-bottom:0.5rem; color:var(--text-gray);"><strong>Subject:</strong> <span id="summary-title" style="color:white;"></span></p>
              <p style="margin-bottom:0.5rem; color:var(--text-gray);"><strong>System:</strong> <span id="summary-category" style="color:white;"></span></p>
              <p style="margin-bottom:0.5rem; color:var(--text-gray);"><strong>Node:</strong> <span id="summary-location" style="color:white;"></span></p>
              <p style="margin-bottom:0.5rem; color:var(--text-gray);"><strong>Threat Level:</strong> <span id="summary-priority" style="color:white;"></span></p>
              <p style="margin-bottom:0.5rem; color:var(--text-gray);"><strong>Auth Slot:</strong> <span id="summary-slot" style="color:white;"></span></p>
              <div style="display:none;">
                <span id="wiz-title"></span>
                <span id="wiz-description"></span>
                <span id="wiz-slot"></span>
                <span id="wiz-room-display"></span>
              </div>
            </div>
          </div>
          
          <div style="display:flex; justify-content:flex-end; gap:1rem; margin-top:3rem;">
            <button class="btn-secondary hidden" id="btn-wiz-prev">Retract</button>
            <button class="btn-primary" id="btn-wiz-next" style="width:auto;">Proceed <i class="fa-solid fa-arrow-right"></i></button>
            <button class="btn-primary hidden" id="btn-wizard-submit" style="width:auto; background:linear-gradient(135deg, #10b981, #059669);"><i class="fa-solid fa-satellite-dish"></i> Execute Dispatch</button>
          </div>
        </div>
      </main>
    </div>
  </div>

  <!-- ================= WARDEN VIEW ================= -->
  <div id="view-warden">
    <div class="app-layout">
      <aside class="sidebar">
        <div class="sidebar-brand">
          <i class="fa-solid fa-shield-halved" style="color:var(--success); font-size:1.5rem;"></i>
          <h2>ADMIN CORE</h2>
        </div>
        <ul class="sidebar-nav-list" style="margin-top:2rem;">
          <li><a href="#" class="nav-item active"><i class="fa-solid fa-satellite-dish"></i> Central Dashboard</a></li>
          <li><a href="#" class="nav-item"><i class="fa-solid fa-radiation"></i> Critical Alerts</a></li>
          <li><a href="#" class="nav-item"><i class="fa-solid fa-users-gear"></i> Technician Matrix</a></li>
        </ul>
        <div style="margin-top: auto;">
          <button id="btn-reset-data-warden" class="preset-btn" style="width:100%; justify-content:center; margin-bottom:1rem;"><i class="fa-solid fa-rotate-left"></i> Purge Data</button>
          
          <!-- Warden Logout mapped to btn-nav-logout which is wired in app.js -->
          <button id="btn-nav-logout" class="preset-btn" style="width:100%; justify-content:center; color:var(--danger); border-color:var(--danger-bg);"><i class="fa-solid fa-power-off"></i> Terminate Session</button>
        </div>
      </aside>
      
      <main class="main-content">
        <div class="top-bar">
          <div>
            <div class="user-greeting">Warden Control Terminal</div>
            <p style="color:var(--text-gray);">Authorized: Warden Rinu Babu [ADM-WARDEN-01]</p>
          </div>
        </div>
        
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon" style="background:rgba(255,255,255,0.1);"><i class="fa-solid fa-list-ul"></i></div>
            <div class="stat-info"><h3>Total Logs</h3><p id="stat-warden-total">0</p></div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" style="background:var(--warning-bg); color:var(--warning);"><i class="fa-solid fa-hourglass-half"></i></div>
            <div class="stat-info"><h3>Pending Triage</h3><p id="stat-warden-pending">0</p></div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" style="background:var(--info-bg); color:var(--info);"><i class="fa-solid fa-gears"></i></div>
            <div class="stat-info"><h3>Active Processing</h3><p id="stat-warden-progress">0</p></div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" style="background:var(--danger-bg); color:var(--danger);"><i class="fa-solid fa-radiation"></i></div>
            <div class="stat-info"><h3>Critical Escalations</h3><p id="stat-warden-escalated">0</p></div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" style="background:var(--success-bg); color:var(--success);"><i class="fa-solid fa-check-double"></i></div>
            <div class="stat-info"><h3>Resolved</h3><p id="stat-warden-resolved">0</p></div>
          </div>
        </div>
        
        <div id="urgent-escalations-banner" style="background:var(--danger-bg); border:1px solid rgba(239,68,68,0.3); border-radius:var(--radius-md); padding:1.5rem; margin-bottom:2rem; display:none; align-items:center; justify-content:space-between;">
          <div style="display:flex; align-items:center; gap:1rem;">
            <i class="fa-solid fa-triangle-exclamation" style="color:var(--danger); font-size:1.5rem;"></i>
            <div>
              <strong style="color:var(--danger); display:block; margin-bottom:0.25rem;">CRITICAL BREACH: Unattended Escalations</strong>
              <span style="font-size:0.875rem; color:#fca5a5;">Immediate warden intervention required on flagged systems.</span>
            </div>
          </div>
          <button style="background:var(--danger); border:none; color:white; padding:0.75rem 1.25rem; border-radius:8px; font-weight:600; cursor:pointer;">Initiate Triage</button>
        </div>
        <div id="urgent-tickets-list-container" style="display:none;"></div>
        
        <div class="table-container">
          <div class="table-header-actions">
            <div class="table-tabs" id="warden-filter-pills">
              <button class="table-tab active" data-filter="All">Global Logs</button>
              <button class="table-tab" data-filter="Pending">Unassigned</button>
              <button class="table-tab" data-filter="In Progress">In Field</button>
              <button class="table-tab" data-filter="Escalated" style="color:var(--danger);">Critical</button>
              <button class="table-tab" data-filter="Resolved">Secured</button>
            </div>
            <div style="display:flex; gap:1rem; align-items:center;">
              <select id="filter-warden-category" style="background:#09090b; color:white; border:1px solid var(--border); padding:0.5rem 1rem; border-radius:8px; outline:none;">
                <option value="All">All Systems</option>
                <option value="Electrical">Electrical</option>
                <option value="Plumbing">Plumbing</option>
                <option value="Furniture">Hardware</option>
              </select>
              <select id="filter-warden-hostel" class="hidden"><option value="All">All</option></select>
              <input type="text" id="search-warden-complaints" class="hidden">
            </div>
          </div>
          
          <table>
            <thead>
              <tr>
                <th>Log ID</th>
                <th>Target Node</th>
                <th>System & Subject</th>
                <th>Threat Lvl</th>
                <th>Field Technician</th>
                <th>Status</th>
                <th>Directive</th>
              </tr>
            </thead>
            <tbody id="warden-table-body">
              <!-- JS Injects Here -->
            </tbody>
          </table>
        </div>
      </main>
    </div>
  </div>

  <!-- ================= MODALS ================= -->
  
  <!-- Manage Ticket (Warden) -->
  <div class="modal-overlay" id="modal-warden-manage">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">
          <h2>Triage Directive <span id="warden-manage-ticket-id" style="color:var(--primary);">#CF-099</span></h2>
          <p>Target: <span id="wm-student-name"></span> — Node <span id="wm-student-room"></span></p>
          <span id="wm-issue-title" class="hidden"></span>
        </div>
        <button class="btn-close btn-secondary" id="close-warden-manage" style="padding:0.5rem 1rem;"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body" style="display:flex; flex-direction:column; gap:1.25rem;">
        <div class="form-group">
          <label>Override Status Code</label>
          <select id="wm-status-select" class="form-control">
            <option value="Submitted">Logged</option>
            <option value="Under Review">Triaging</option>
            <option value="Assigned">Technician Dispatched</option>
            <option value="In Progress">Field Work Active</option>
            <option value="Escalated">Critical Alert</option>
            <option value="On Hold">Suspended</option>
            <option value="Resolved">Secured</option>
            <option value="Closed">Archived</option>
          </select>
        </div>
        <div class="form-group">
          <label>Assign Field Agent</label>
          <select id="wm-tech-select" class="form-control">
            <option value="">-- Unassigned --</option>
          </select>
        </div>
        <div class="form-group">
          <label>Projected Clearance (ETA)</label>
          <input type="datetime-local" id="wm-eta-input" class="form-control">
        </div>
        <div class="form-group">
          <label>Command Override Log</label>
          <textarea id="wm-note-input" class="form-control" rows="3" placeholder="Append directive notes..."></textarea>
        </div>
      </div>
      <div style="display:flex; justify-content:space-between; margin-top:2rem;">
        <button class="btn-secondary" id="btn-warden-cancel">Abort</button>
        <button class="btn-primary" id="btn-warden-save-ticket" style="width:auto;"><i class="fa-solid fa-terminal"></i> Execute Directive</button>
      </div>
    </div>
  </div>

  <!-- Timeline Modal -->
  <div class="modal-overlay" id="modal-timeline">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">
          <h2>Log History: <span id="timeline-ticket-id" style="color:var(--primary);"></span></h2>
          <p id="timeline-ticket-title"></p>
        </div>
        <button class="btn-close btn-secondary" id="close-timeline" style="padding:0.5rem 1rem;"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem;">
          <span class="badge info" id="timeline-status-badge"></span>
          <span style="font-size:0.75rem; color:var(--text-gray);" id="timeline-eta-text"></span>
        </div>
        
        <div id="timeline-tech-box" style="display:flex; gap:1rem; padding:1.25rem; background:rgba(255,255,255,0.02); border:1px solid var(--border); border-radius:var(--radius-md); margin-bottom:1.5rem; align-items:center;">
          <div id="timeline-tech-avatar" style="width:48px; height:48px; background:var(--bg-main); border:1px solid var(--border); border-radius:50%; display:flex; align-items:center; justify-content:center; color:var(--primary); font-weight:700;">TK</div>
          <div>
            <strong id="timeline-tech-name" style="display:block; font-size:1rem; color:var(--text-dark);"></strong>
            <span id="timeline-tech-specialty" style="font-size:0.75rem; color:var(--text-gray);"></span>
          </div>
          <a href="#" id="timeline-tech-phone" class="btn-secondary" style="margin-left:auto; padding:0.5rem 1rem; text-decoration:none;"><i class="fa-solid fa-phone"></i> Comm</a>
        </div>
        
        <div id="stepper-timeline-container" style="display:flex; flex-direction:column; gap:1.5rem; padding-left:1.5rem; border-left:2px dashed var(--border); margin-left:1rem;">
        </div>
      </div>
      <div style="margin-top:2rem; text-align:right;">
        <button class="btn-secondary" id="btn-timeline-close">Close Log</button>
      </div>
    </div>
  </div>
  
  <!-- Escalate Modal -->
  <div class="modal-overlay" id="modal-escalate">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">
          <h2 style="color:var(--danger);"><i class="fa-solid fa-radiation"></i> Execute Escalation Protocol</h2>
          <p>Log ID <span id="escalate-ticket-id"></span></p>
        </div>
        <button class="btn-close btn-secondary" id="close-escalate" style="padding:0.5rem 1rem;"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body" style="margin-bottom:2rem;">
        <p style="font-size:0.875rem; margin-bottom:1rem;">Warning: You are bypassing standard operational procedures to force an immediate alert to Command.</p>
        <textarea id="escalate-custom-text" class="form-control" rows="3" placeholder="Provide justification for override..."></textarea>
      </div>
      <div style="display:flex; justify-content:space-between;">
        <button class="btn-secondary" id="btn-cancel-escalate">Abort</button>
        <button class="btn-primary" id="btn-submit-escalate" style="background:linear-gradient(135deg, #ef4444, #b91c1c); width:auto;">Authorize Escalation</button>
      </div>
    </div>
  </div>

  <!-- Confirm Resolution Modal -->
  <div class="modal-overlay" id="modal-confirm-resolution">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">
          <h2>Verify Security Clearance <span id="confirm-ticket-id" style="color:var(--primary);"></span></h2>
        </div>
        <button class="btn-close btn-secondary" id="close-confirm-res" style="padding:0.5rem 1rem;"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body" style="margin-bottom:2rem;">
        <p style="font-size:0.875rem; margin-bottom:1rem;">Has the structural/system anomaly been fully neutralized?</p>
        <div id="rating-feedback-box" class="hidden">
          <textarea id="res-feedback-text" class="form-control" rows="3" placeholder="Append final debriefing log..."></textarea>
        </div>
      </div>
      <div style="display:flex; gap:1rem;">
        <button class="btn-secondary" id="btn-res-no" style="flex:1; border-color:var(--danger); color:var(--danger);">Negative, Still Active</button>
        <button class="btn-primary" id="btn-res-yes" style="flex:1; background:linear-gradient(135deg, #10b981, #059669);">Affirmative, Secured</button>
      </div>
    </div>
  </div>
  
  <!-- Research Modal -->
  <div class="modal-overlay" id="modal-research">
    <div class="modal-content"><button class="btn-close" id="close-research"></button></div>
  </div>

</div>

<!-- Scripts -->
<script src="store.js"></script>
<script src="app.js"></script>
<script>
  document.getElementById('btn-wiz-prev-top').addEventListener('click', () => {
    document.getElementById('btn-wiz-prev').click();
  });
</script>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("index.html written successfully.")
